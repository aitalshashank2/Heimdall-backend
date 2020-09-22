from flask import Flask, request
import subprocess
import yaml
import io
import os
import hmac
import hashlib
import requests
import json

with io.open('config.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

repo = data_loaded["repo"]
secret = data_loaded["secret"]

app = Flask(__name__)

@app.route('/', methods=['POST'])

def heimdall():
    headers = request.headers

    encoded_secret = secret.encode()
    payload = request.get_data()
    
    signature = 'sha1=' + hmac.new(encoded_secret, payload, hashlib.sha1).hexdigest()
    if signature != headers['X-Hub-Signature']:
        return "Invalid X-Hub-Signature"


    if headers["X-GitHub-Event"]=="push":
        pull = subprocess.Popen(["git", "pull", "origin", "master"], cwd=repo)
        output, error = pull.communicate()

        servers = os.listdir(repo+"servers/")
        with io.open(repo+"server-mappings.yml", 'r') as stream:
            server_mappings = yaml.safe_load(stream)

        for i in servers:
            dest = server_mappings['servers'][i]
            keys = ""

            auth_users = open(repo+"servers/"+i, 'r')
            for user in auth_users:
                keys += open(repo+"public-keys/"+user.rstrip(), 'r').read()

            # Make a post request to the server at dest
            payload_keys = {'authorized_keys': keys}
            payload_keys = json.dumps(payload_keys)
            r = requests.post(dest, json=payload_keys)

    else:
        return "An error occured."
    return "OK"
