# Todo

### psql
```postgresql
CREATE USER user_41 PASSWORD 'user';
CREATE DATABASE db_todo OWNER user_41;
GRANT ALL PRIVILEGES ON DATABASE db_todo TO user_41;
```

### venv
```shell
# Create environment
python3.8 -m venv --copies app/venv
# Activate
source app/venv/bin/activate
# Make sure to use app/venv/bin/pip3.8 
which pip3.8
# Install packages
pip3.8 install -r app/requirements.txt
```


### migrate
```shell
app/todo/manage.py migrate
```


### run server

...