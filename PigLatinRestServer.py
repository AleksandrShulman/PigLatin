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
        #TODO: Adding logging framework to log bad requests
        return "Bad request: {0}".format(e.message), 400
    return "{0}\n".format(result), 200

if __name__ == '__main__':
    # TODO: Add arguments for running in production mode vs. running in test mode.
    # test/debug mode will have debug enabled and run on a non-restricted port
    # toggle between localhost and 0.0.0.0 for testing and production, respectively
    app.run(host="0.0.0.0", port=80, debug=False)