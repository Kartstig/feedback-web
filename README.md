# smart_container

## Setup (Debian/Ubuntu)

```
$ sudo apt-get install libzmq3 libevent-dev python-dev tcl8.5 build-essential python-pip
```

### Virtual Environment
```
$ pip install virtualenvwrapper

# Add the following to your .bashrc:
export WORKON_HOME="/opt/virtual_env/"
source "/opt/virtual_env/bin/virtualenvwrapper_bashrc"

# Now you should be able to run the mkvirtualenv command:
$ mkvirtualenv feedback
$ pip install -r requirements.txt
```

### Set Configs
Copy Config.py.sample to Config.py
See [Flask Config](http://flask.pocoo.org/docs/0.10/config/)

### Workbench

```
$ python -i workbench.py
```

### Run Server
```
$ python run.py
```

 OR

```
$ circusd dev.ini
```
Circus is used as a process manager to run the app in production