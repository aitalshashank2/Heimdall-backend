from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])

def logger():
    headers = request.headers
    if(headers["X-GitHub-Event"]=="push"):
        print("Push Event Detected.")
    else:
        print("An error occured.")
    return "Hello World!"
