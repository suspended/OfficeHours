import os
from flask import Flask, request, redirect, url_for
from flask import *
from OHDocumentConversion import *
import requests

app = Flask(__name__)
UPLOAD_FOLDER = 'data'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'html'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploaded')
def uploaded():
    return render_template('uploaded.html')

@app.route('/magic', methods=["POST"])
def results():
   file = request.files['file']
   if file and allowed_file(file.filename):
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      newDC = OHDocumentConversion(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
      return render_template('magic.html')

@app.route('/search', methods=["GET"])
def search():
    q = request.args.get('q','')
    r = requests.get("https://<RR_SA_USERID>:<RR_SA_PASSWORD>@gateway.watsonplatform.net/retrieve-and-rank/api/v1/solr_clusters/<SOLR_CLUSTER_ID>/solr/officehours_demo_collection/fcselect?ranker_id=868fedx13-rank-1162&q="+q+"&wt=json&fl=id,title,body")
    return r.text

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('templates/images', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port), debug=True)
