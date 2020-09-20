# Logger

Automating Public Key Storage using GitHub Web-Hooks.

---

## Setup

> Make an empty directory and clone this repository.
> Initialize a virtual environment and install all the necessary dependencies using 'requirements.txt'
	``` pip install -r requirements.txt ```

> Set environment variables for flask
	```
	export FLASK_APP=logger
	export FLASK_ENV=development
	```

> You can change the FLASK_ENV according to your needs.
> Copy ```config-stencil.yml``` to ```config.yml```.


> Make another GitHub Repository for storing Public Keys. Let's call it "logger-ssh-keys"
	> Goto: Settings / Webhooks
	> Payload URL: The public URL of your server
	> Content type: application/x-www-form-urlencoded
	> Secret: A random secret with high entropy
	> Triggers: Just the push event
	> Active: yes

> Make an empty directory and set remote branch named ```origin``` to the above GitHub repository.

> Now, set the environment variables in ```config.yml``` as follows:
	```
	repo: path/to/the/directory/containing/ssh-keys (The directory containing .git folder alongside another directory called public-keys)
	destination_file: path/to/the/authorized_keys/in/the/.ssh/directory (usually ~/.ssh/authorized_keys
	secret: <The secret that you entered for the GitHub Webhooks
	```

> Run ```flask run``` in the directory containing ```logger.py```

Thats it!

---

## Working

If someone wants access to your ssh server, all he/she has to do is make a PR on "logger-ssh-keys" after uploading his/her Public Key in the "public-keys" folder.

---
#### Happy hacking!
