# CUTOUT portal initial setup instruction (General) 

steps: [setup dev environment]

Clone repo
------------
```bash 
$ git clone https://github.com/lhmisho/cutout-portalssss
```

Checkout to latest branch
-----------------------------
```bash
$ git checkout {branch_name}
```

Create `virtualenv` and activate `venv`
---------------------------------------

```bash
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
```

Install dependencies for project
--------------------------------
```bash
$ pip install -r requirements.txt
```

`Note: during the installation  if having any issue with secp256k1 than need to install libsecp256k1-dev`
```
$ sudo apt-get update -y
$ sudo apt-get install -y libsecp256k1-dev
```
 

Copy `example.env` file to `.env`
-------------------------------------------
```bash
|
|--> example.env
|--> .env
```
Migrate, create superuser and run project
-----------------------------------------
```bash
 $ python manage.py migrate
 $ python manage.py createsuperuser
 $ python manage.py runserver
```

## Docker Instruction
[Docker Deployment](DockerDeploy.md)
## Log File Generation
copy the logs folder from project and past into your project
```python
from logs.log import Log

log_text = "API request success"

Log.info(log_text, request)
Log.debug(log_text, request)
Log.critical(log_text, request)
Log.error(log_text, request)

```
A log file will be created with a name which contain current date and log_type message IP and Request url
## :wink: happy coding :wink:

