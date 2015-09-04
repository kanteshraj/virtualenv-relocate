# Virtualenv-relocate  
virtualenv-relocate help in relocating no-relocatable virtualenv from build server to multiple production server.  
script is based on [virtualenv-clone](https://github.com/edwardgeorge/virtualenv-clone/)

### Installation:  
```sh
$ pip install git+https://github.com/kanteshraj/virtualenv-relocate.git
````  

### Usage:
```sh
$ virtualenv-relocate -s <virtualenv_path>
```
copy virtualenv to other server and run following commands  
```sh
$ virtualenv-relocate -d <virtualenv_path>
```