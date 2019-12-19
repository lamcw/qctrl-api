# Simple BLACK OPAL API

## Development Set-up
Make sure you have `poetry` installed. And create a database in postgreSQL.

```console
$ ln -sv qctrl/.envs/.env.dev qctrl/.env
$ poetry install
```

Modify project settings as you require in `qctrl/.env`, or override them using
environment variables when calling `manage.py`.

You can then run a development server with
```console
$ poetry run ./manage.py runserver
```
