# ClarifaiDemo

A simple demo project to show the power of the Clarifai API

## How to run

- ```pip install -r requirements.txt```
- ```python app.py```


## Pack app for MacOSX

- ```env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install -v 3.6.0```
- ```pyenv local 3.6.0```
- ```pyenv rehash```
- ```cd ./ClarifaiVideoDemo```
- ```python setup.py py2app```
- ```cd ./dist/ClarifaiDemoApp.app/Contents/Resources/lib```
- ```unzip python36.zip -d python36```
- ```rm python36.zip```
- ```mv python36 python36.zip```
