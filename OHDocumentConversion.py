# coding=utf-8
import json
from watson_developer_cloud import DocumentConversionV1
from config import *
import subprocess
import requests

class OHDocumentConversion:
  def __init__(self, filename):
    document_conversion = DocumentConversionV1(
      username = RR_SA_USERNAME,
      password = RR_SA_PASSWORD,
      version = RR_API_VERSION)
    with open(filename, 'rb') as document:
      config = {'conversion_target': DocumentConversionV1.ANSWER_UNITS}
      answer_units = document_conversion.convert_document(document=document, config=config)['answer_units']
      
      entries = []
      commit = {}
      
      for answer_unit in answer_units:
        doc = {}
        entry = {}
        entry['title'] = answer_unit['title']
        entry['id'] = answer_unit['id']
        entry['body'] = answer_unit['content'][0]['text']
        doc['doc'] = entry
        
        # Skip probably useless entries
        if len(entry['title']) < MINIMUM_CONTENT_LENGTH:
          continue
        if len(entry['body']) < MINIMUM_CONTENT_LENGTH:
          continue
        # Add the new entry
        entries.append(('add', doc))
      
      entries.append(('commit', commit))
      
    #Final output JSON ready to load into Solr
    output = '{%s}' % ',\n'.join(['"{}": {}'.format(action, json.dumps(dictionary)) for action, dictionary in entries])
    print output
    
    with open("output.json", "w") as outputFile:
      outputFile.write("%s" % output)
      
    data = open('output.json', 'rb').read()
    r = requests.post(url='https://<RR_SA_USERID>:<RR_SA_PASSWORD>@gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/<SOLR_CLUSTER_ID>/solr/officehours_demo_collection/update',
                    data=data,
                    headers={'Content-Type': 'application/json'})
    print r.text
    # subprocess.call([
    #   'curl',
    #   '-X',
    #   'POST',
    #   '-H',
    #   'Content-Type: application/json',
    #   '-u',
    #   '<RR_SA_USERID>:<RR_SA_PASSWORD>',
    #   'https://gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/<SOLR_CLUSTER_ID>/solr/officehours_demo_collection/update',
    #   '--data-binary',
    #   '@output.json'
    # ])





