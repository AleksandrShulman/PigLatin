#!/usr/bin/env bash
set -e

# This a basic test script to run to verify correctness of the server.

urlencode() {
  python -c 'import urllib, sys; print urllib.quote(sys.argv[1], sys.argv[2])' "$1" "$urlencode_safe"
}

stop_server() {
  pid=$(ps aux | grep python | grep PigLatinRestServer.py | awk '{ print $2}')
  echo "Stopping the server running as $pid"
  kill -9 $pid
  echo "Server should be stopped."
}

# Start the server
nohup /Users/aleks/PycharmProjects/PigLatin/PigLatinRestServer.py &
# TODO: Implement this more elegantly
echo "Waiting for server to start....please standby."
sleep 15

# Test inputs and outputs
test_string="translate this please"
expectedResponse="anslatetray isthay easeplay"

# Test GET
result=$(curl -X GET localhost:80/translate?input=$(urlencode "translate this please"))
echo "Received result ${result}"

# The server has failed a very basic test
if [[ "${result}" != "${expectedResponse}" ]]; then
  echo "Server is not running correctly or has been misconfigured. Please fix issues and try again."
  exit 1
else
  echo "Passed /GET test"
fi

# Test POST
unset result
result=$(curl -X POST localhost:80/translate -d "translate this please")
echo "Received result ${result}"

# The server has failed a very basic test
if [[ "${result}" != "${expectedResponse}" ]]; then
  echo "Server is not running correctly or has been misconfigured. Please fix issues and try again."
  exit 1
else
  echo "Server passed /POST test"
fi

stop_server
echo "Done with test"
