#!/usr/bin/env bash
set +x
set -e

usage_string="""This will install the requirements for the Translation Microservice.
                Usage: Run without arguments as the root user
                Assumptions:
                - Python installed, version 2.6+
                - Pip installed"""

echo "${usage_string}"

set +e

# Check if python is installed
which python
if [[ "$?" != "0" ]]; then
  echo "python is a requirement. Please install it."
  exit 1;
fi

# Check if pip is installed
which pip
if [[ "$?" != "0" ]]; then
  echo "Pip is a requirement. Please install it first using these instructions: https://pip.pypa.io/en/latest/installing/"
  exit 1;
fi

# Check if flask is installed
which flask
if [[ "$?" != "0" ]]; then
  echo "Flask is not yet installed. Installing now. http://flask.pocoo.org/docs/0.12/"
  sudo easy_install flask
fi

set -e
# Verify that flask is on the path
which flask

# Start the server with a basic sleep!
nohup python /Users/aleks/PycharmProjects/PigLatin/PigLatinRestServer.py &
# TODO: Implement this more elegantly
echo "Waiting for server to start....please standby."
sleep 15

# Simple bootstrapping test to make sure it's up and working
# This method was taken from this thread:
# http://stackoverflow.com/questions/37309551/how-to-urlencode-data-into-a-url-with-bash-or-curl
urlencode() {
  python -c 'import urllib, sys; print urllib.quote(sys.argv[1], sys.argv[2])' "$1" "$urlencode_safe"
}

result=$(curl -X GET localhost:80/translate?input=$(urlencode "translate this please"))
echo "result is: ${result}"
expectedResponse="anslatetray isthay easeplay"

# The server has failed a very basic test
if [[ "${result}" != "${expectedResponse}" ]]; then
  echo "Server is not running correctly or has been misconfigured. Please fix issues and try again."
  exit 1
fi

# Up and ready!
echo "The server is up and running. Please enjoy!"