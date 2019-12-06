# Python Notes

## Make Python 3 Default
We don't have to delete Python 2.7.4 because some system files might still be using it so instead we will just alias 
python 3 as python.

### Create alias in ~/.bashrc
```
alias python=python3
```

## Virtual Environment
A virtual environment creates an isolated environment to contain all the dependencies for a project.

### Install Virtual Env
```
pip install virtualenv
```

### Make a directory to store environments
```
mkdir ~/environments
```

### Create a new virtual environment
```
python -m venv ~/environments/tutorial-env
```

### Activate the virtual environment
```
source ~/environments/tutorial-env/bin/activate
```

### Deactivate the virtual environment
```
deactivate
```