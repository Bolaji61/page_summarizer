import pickle as p
# import traceback
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

#@app.before_request
#def exe():
#    summarizer = 'modelfile.pkl'
#    model = p.load(open(summarizer, 'rb'))


@app.route('/api/summarize', methods=['POST', 'GET'])
def get_url():
    if request.method == 'POST':
        url = request.json['theUrl']
        #print(content)
        return jsonify(url), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

