# Heimdall

Be warned, I shall uphold my sacred oath to protect this realm as its gatekeeper.

---

## Setup

- Make an empty directory and clone this repository.
- Initialize a virtual environment and install all the necessary dependencies using 'requirements.txt'
	``` pip install -r requirements.txt ```

- Set environment variables for flask
	```
	export FLASK_APP=heimdall
	export FLASK_ENV=development
	```

- You can change the FLASK_ENV according to your needs.
- Copy ```config-stencil.yml``` to ```config.yml```.


- Make another GitHub Repository for storing Public Keys. Let's call it "Heimdall-ssh-keys"
	- Goto: Settings / Webhooks
	- Payload URL: The public URL of your server
	- Content type: application/x-www-form-urlencoded
	- Secret: A random secret with high entropy
	- Triggers: Just the push event
	- Active: yes
	- Repository structure:
		```
		public-keys/
			Stores public keys of all the members of the organization
		server-mappings.yml
		servers/
			Stores with files with the same names as specified in server-mappings.yml
		```
	- ```server-mappings.yml``` maps the files to Heimdall's endpoint on the servers. Structure of ```server-mappings.yml```:
		```
		servers:
			name-of-server1-file-in-servers-directory: endpoint-listening-for-post-request-from-Heimdall
			name-of-server2-file-in-servers-directory: endpoint-listening-for-post-request-from-Heimdall
		```

- Make an empty directory and set remote branch named ```origin``` to the above GitHub repository.

- Now, set the environment variables in ```config.yml``` as follows:
	```
	repo: path/to/the/directory/containing/ssh-keys (The directory containing .git folder alongside another directory called public-keys)
	secret: <The secret that you entered for the GitHub Webhooks
	```

- Run ```flask run``` in the directory containing ```heimdall.py```

Thats it!

---

## Working

If someone wants access to your ssh server, all he/she has to do is make a PR on "Heimdall-ssh-keys" after uploading his/her Public Key in the "public-keys" folder and entering the name of the file containing the Public Key to that corresponding server's file in the ```servers/``` directory.

---
#### Happy hacking!
