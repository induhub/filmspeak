from elasticsearch import Elasticsearch
from flask import Flask
from flask import render_template
from flask import request

es = Elasticsearch([
    {'host': '54.172.245.221'}
])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        myvar = request.args.get("q")
        res = es.search(index="top_250", body={"query": {"query_string": {"query": myvar}}})
        hits = res['hits']['total']
        items=res['hits']['hits']
        result = ''
        for each in items:
            result = result+str(each['_source']['dialogue'])+'<br>'
        return result
	


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
