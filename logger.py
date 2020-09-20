from flask import Flask, request
import subprocess
import yaml
import io
import os

with io.open('config.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

repo = data_loaded["repo"]
destination_file = data_loaded["destination_file"]

app = Flask(__name__)

@app.route('/', methods=['POST'])

def logger():
    headers = request.headers
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
        print("An error occured.")
        return "An error occured."
    return "OK"
