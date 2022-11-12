# GPXplorer
Djago based app for GPX routes management

# Developer guideline
Create a new virtual environment by running the command below:

```sh
python -m venv .venv
```

Activate it in a Linux enviroment by running:

```sh
source .venv/bin/activate
```

or in a Windows enviroment by running:

```sh
.\.venv\Scripts\activate
```

Install the dependencies by running:

```sh
pip install -r requirements.txt
```

```sh
cd Site
python3 manage.py runserver 
```

# On models changes

```sh
python3 manage.py makemigrations GPXManager
python3 manage.py migrate      
```

# Shell
```sh
python3 manage.py shell 
```