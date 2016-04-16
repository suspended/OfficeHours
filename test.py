import requests

data = open('output.json', 'rb').read()
r = requests.post(url='https://<RR_SA_USERID>:<RR_SA_PASSWORD>@gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/<SOLR_CLUSTER_ID>/solr/officehours_demo_collection/update',
                    data=data,
                    headers={'Content-Type': 'application/json'})
print r.text