# googles-hash-code-2020

## Install

Required: a virtual environment such as virtual env

### Dependencies On MacOS
```bash
# if you don't have brew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# if you don't have python 3
brew install python
# if you don't have virtualenv
sudo /usr/bin/easy_install virtualenv
````

#### Setup the project
```bash
virtualenv venv
source venv/bin/activate
pip install --requirement requirements.txt
```

## Developing

### Format the code

```bash
black .
```

### Lint the code

```
flake8 .
```
