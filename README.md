# PigLatin
A REST service running on port :80 that will translate english into Pig-Latin. It can accept simple words and phrases,
all the way to full paragraphs.

# Usage
There are two modes of interaction:
- For shorter requests, use the GET verb at the /translate URI, with the string URL-encoded in the variable 'input'
Example:
```
curl -X GET localhost:80/translate?input=$(urlencode "translate this please")
```

- For longer requests (>1024 characters), use the POST verb at the same /translate URI, with the text in the body.
Example:
```
curl -X POST localhost:80/translate -d "translate this please"
```

# Running the Microservice
- You can kick it off using the python script itself. Make sure to run as root as it requires access to port 80:
```
python PigLatinRestServer.py
```
OR
- You can use the included install script that will also install flask. It's idempotent so worries about
running it repeatedly. Make sure to run as root.
```
./install_and_run.sh
```

# Stopping/restarting the microservice
kill -9 the process and start the script again

# Future work
- Logging improvements, both in the app and at the level of running the application
- Improved testing and handling of edge cases in the core logic
- Stop/Restart functionality in the script
