# Todo

### psql
```postgresql
CREATE USER custom_user PASSWORD '1qw2er3ty';
CREATE DATABASE todo OWNER custom_user;
GRANT ALL PRIVILEGES ON DATABASE todo TO custom_user;
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

### collect assets 
```shell
app/todo/manage.py collectstatic
```

### run server

...


# Docker


```shell
docker system prune -a
```

```shell
docker-compose build --no-cache
```

```shell
docker-compose up -d --force-recreate
```

```shell
docker-compose exec app ./manage.py migrate
```

```shell
docker-compose exec app ./manage.py createsuperuser
```
