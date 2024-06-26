## URL AWS 
http://flaskchulanlpbpmnv1-env.eba-hiwuhfgp.us-east-2.elasticbeanstalk.com/

## Install Python
version | detail | reference
--- | --- | ---
3.9.1 | Install for M1 and active (macOS 64-bit universal2 installer) | https://www.python.org/downloads/release/python-391/
3.7.0 | Recommend for NeuralCoref | https://www.python.org/downloads/release/python-370/

## Step Install
detail | command
--- | ---
Environtment | $ python3 -m venv venv
Activate Environtment | $ source venv/bin/activate
pip list | $ pip list
Upgrade pip | $ pip install --upgrade pip
setuptools | $ pip install -U pip setuptools wheel
Spacy | $ pip install spacy==2.1.0
Download spacy model | $ python -m spacy download en_core_web_sm
Flask | $ pip install flask
Neuralcoref | $ pip install neuralcoref
pip freeze | $ pip freeze > requirements.txt
pip install requirement | $ pip3 install -r requirements.txt

## Activate Environtment
- $ python3 -m venv venv && source venv/bin/activate
- $ pip install -r requirement.txt

## Flask Run
- $ export FLASK_APP="application.py"
- $ flask run

## Git 
detail | command
--- | ---
Add | $ git add .
Commit | $ git commit -m "test"
Push | $ git push origin main

## AWS Elastic Beanstalk
step | detail
--- | ---
1 | login : https://aws.amazon.com/
2 | elastic beanstalk : https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/environments
3 | Create new environtment : https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/newEnvironment
4 | Create application name : flask-chula-nlp-bpmn-v1
5 | Environment name : Flaskchulanlpbpmnv1-env
6 | Platform : python 3.7
7 | Create sample application
8 | URL : Flaskchulanlpbpmnv1-env.eba-hiwuhfgp.us-east-2.elasticbeanstalk.com

## Code Commit CI/CD : goto code pipeline
step | detail
--- | ---
1 | Create pipeline name : flask-chula-nlp-bpmn-v1
2 | Role name : AWSCodePipelineServiceRole-us-east-2-flask-chula-nlp-bpmn-v1
3 | Select Github (Version 2)
4 | Select connect with github
5 | Authorize Github with AWS
6 | Enter Github apps by github account

## Success and back to project to commit project
step | detail
--- | ---
1 | $ git 
2 | $ git init
3 | $ git status
- URL : https://github.com/kullawattana/aws_flask_chula_nlp_bpmn_v1.git

```
.venv/
__pycache__/
application.py
requirements.txt
```

## create .gitignore file 
- copy all and put on this project to ignore deploy
- Ref : https://github.com/github/gitignore/blob/main/Python.gitignore

## back to terminal on this project
- $ git status

```
.gitignore
application.py
requirements.txt
```

## Commit to Git
step | detail
--- | ---
1 | $ git add .
2 | $ git commit -m "init"
3 | $ git push origin main

```
[main (root-commit) aec1f9b] init
3 files changed, 176 insertions(+)
create mode 100644 .gitignore
create mode 100644 application.py
create mode 100644 requirements.txt
```

## Step by Step of AWS pipeline
step | detail
--- | ---
1 | select: flask-chula-nlp-bpmn-v1
2 | select: main branch
3 | Press "next" button
4 | Add build stage : skip build state
5 | Add deploy stage : 
6 | Deploy Provider : AWS Elastic Beanstalk
7 | Region : US East (Ohio)
8 | Application name : flask-chula-nlp-bpmn-v1
9 | Environtment name : flaskchulanlpbpmnv1-env
10 | Press next
11 | create pipeline
12 | Deploy Success

back to AWS elastic beanstalk
https://us-east-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-east-2#/application/overview?applicationName=flask-example

Other have issue deploy 
https://stackoverflow.com/questions/53683358/flask-app-no-module-named-flask-error-in-elasticbeanstalk-after-confirming-flask

<img src="https://github.com/kullawattana/aws_flask_chula_nlp_bpmn_v1/blob/main/screenshot/code_pipeline_cicd.png" width="1024" height="430" />

<img src="https://github.com/kullawattana/aws_flask_chula_nlp_bpmn_v1/blob/main/screenshot/deployment.png" width="1024" height="430" />
