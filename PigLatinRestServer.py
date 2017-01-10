#!/usr/bin/env python
from flask import Flask, request
from PigLatin import PigLatin
app = Flask(__name__)

@app.route("/translate", methods=['GET', 'POST'])
def get_translate():
    """
    For simple requests of less than 1024 characters, a simple get request will do.
    Otherwise, for larger messages, a POST must be used. The message to encode
    will be in the body
    Assume that the request is url-encoded and that flask will url-decode it.
    :return: the translated string, and 200 for success
    """
    if request.method == 'GET':
      text_string = request.args.get('input')
    elif request.method == 'POST':
      text_string = request.get_data()
    try:
      result = PigLatin.translate(text_string)
    except Exception as e:
        #TODO: Log bad request
        return "Bad request: {0}".format(e.message), 400
    return "{0}\n".format(result), 200

if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)