from flask import Flask, request
import subprocess
import yaml
import io

with io.open('config.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

repo = data_loaded["repo"]
repo_file = data_loaded["repo_file"]
destination_file = data_loaded["destination_file"]

app = Flask(__name__)

@app.route('/', methods=['POST'])

def logger():
    headers = request.headers
    if(headers["X-GitHub-Event"]=="push"):
        pull = subprocess.Popen(["git", "pull", "origin", "master"], cwd=repo)
        output, error = pull.communicate()
        copy = subprocess.Popen(["cp", repo+repo_file, destination_file])
        output, error = copy.communicate()
    else:
        print("An error occured.")
    return "OK"
