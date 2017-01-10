#!/usr/bin/env python
from flask import Flask, request
from PigLatin import PigLatin
app = Flask(__name__)

@app.route("/translate", methods=['GET'])
def get_translate():
    """
    For simple requests of less than 1024 characters, a simple get request will do.
    Assume that the request is url-encoded and that flask will url-decode it.
    :return: the translated string, and 200 for success
    """
    text_string = request.args.get('input')
    try:
      result = PigLatin.translate(text_string)
    except Exception as e:
        #TODO: Log bad request
        return "Bad request: {0}".format(e.message), 400
    return "{0}\n".format(result), 200

@app.route("/translate", methods=['POST'])
def get_translate():
    """
    For longer requests
    :return: the translated string, and 200 for success
    """
    text_string = request.args.get('input')
    try:
      result = PigLatin.translate(text_string)
    except Exception as e:
        #TODO: Log bad request
        return "Bad request: {0}".format(e.message), 400
    return "{0}\n".format(result), 200

if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)