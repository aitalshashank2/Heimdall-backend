from flask import Flask, request
import subprocess
import yaml
import io
import os
import hmac
import hashlib

with io.open('config.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

repo = data_loaded["repo"]
destination_file = data_loaded["destination_file"]
secret = data_loaded["secret"]

app = Flask(__name__)

@app.route('/', methods=['POST'])

def logger():
    headers = request.headers

    encoded_secret = secret.encode()
    payload = request.get_data()
    
    signature = 'sha1=' + hmac.new(encoded_secret, payload, hashlib.sha1).hexdigest()
    if signature != headers['X-Hub-Signature']:
        return "Invalid X-Hub-Signature"


    if headers["X-GitHub-Event"]=="push":
        pull = subprocess.Popen(["git", "pull", "origin", "master"], cwd=repo)
        output, error = pull.communicate()

        public_keys = os.listdir(repo+"public-keys/")

        f = open(destination_file, "w")
        for i in public_keys:
            if i=="instructions.md":
                continue
            with open(os.path.join(repo+"public-keys", i), 'r') as tf:
                f.write(tf.read())

    else:
        return "An error occured."
    return "OK"
