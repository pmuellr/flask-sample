#!/usr/bin/env python
import os
import json
from dataHandler import DataHandler

from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

www          = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")
www_css      = os.path.join(www, "css")
www_images   = os.path.join(www, "images")
www_scripts  = os.path.join(www, "scripts")

dh = DataHandler(max=20)

#-------------------------------------------------------------------------------
# test the data APIs with curl:
#
#   post data:
#     curl -d "datum=321" http://localhost:5000/api/data 
#
#   get data:
#     curl http://localhost:5000/api/data
#
#-------------------------------------------------------------------------------
@app.route('/api/data', methods=['POST'])
def api_data_post():
    datum = request.form['datum']

    try:
        json.loads(datum)
    except:
        print "error parsing json: ", datum
        return jsonify(status="ERROR-JSON")

    dh.put(datum)

    return jsonify(status="OK")

#-------------------------------------------------------------------------------
@app.route('/api/data', methods=['GET'])
def api_data_get():
    data = dh.get()

    return jsonify(status="OK", data=data)

#-------------------------------------------------------------------------------
@app.route('/', methods=['GET'])
def www_index(): return send_from_directory(www, 'index.html')

#-------------------------------------------------------------------------------
@app.route('/css/<path:path>', methods=['GET'])
def www_css(path): return send_from_directory(www_css, path)

#-------------------------------------------------------------------------------
@app.route('/scripts/<path:path>', methods=['GET'])
def www_scripts(path): return send_from_directory(www_scripts, path)

#-------------------------------------------------------------------------------
@app.route('/images/<path:path>', methods=['GET'])
def www_images(path): return send_from_directory(www_images, path)

#-------------------------------------------------------------------------------
def main():
    onCF         = None is not os.getenv('VCAP_APPLICATION')
    port         = os.getenv('VCAP_APP_PORT', '5000')
    use_debugger = True
    debug        = True

    if onCF:
        host = '0.0.0.0'

        vcap_app = json.loads(os.getenv('VCAP_APPLICATION'))
        url      = 'https://%s' % vcap_app['application_uris'][0]

    else:
        host = 'localhost'
        url  = 'http://localhost:%s' % port

    print 'starting server on %s' % url
    app.run(
        host         = host,
        port         = int(port),
        use_debugger = use_debugger,
        debug        = debug
    )

#-------------------------------------------------------------------------------
if __name__ == "__main__": main()
