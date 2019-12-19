# Simple BLACK OPAL API

Implementation of [Q-CTRL back-end engineering challenge](https://github.com/qctrl/back-end-challenge/) in Django.

## Development Set-up
Make sure you have [Poetry](https://python-poetry.org/) installed. And create a
fresh database in postgreSQL.

```console
$ ln -sv .envs/.env.dev qctrl/.env
$ poetry install
```

Modify project settings as you require in `qctrl/.env`, or override them using
environment variables when calling `manage.py`.

You can then run a development server with
```console
$ poetry run ./manage.py makemigrations api
$ poetry run ./manage.py migrate
$ poetry run ./manage.py runserver
```

## Usage
The API root is available at `api/`. HTTP request bodies should be in JSON,
unless otherwise specified.

### Controls
The API allows for

1. [Create a new control](#create-a-new-control)
1. [List all controls (five per page)](#list-all-controls)
1. [Get a specific control](#list-one-control)
1. [Update a specific control](#update-one-specific-control)
1. [Delete a specific control](#delete-one-control)
1. [Bulk upload controls in CSV format](#bulk-upload-controls-in-csv)
1. [Download controls in CSV format](#download-controls-in-csv)

#### Create a new control
```
POST /controls/
```

##### Input
Name | Type | Description
---- | ---- | -----------
`name` | `string` | **Required** Name of the control
`type` | `string` | **Required** One of: Primitive, CORPSE, Gaussian, CinBB, CinSK
`maximum_rabi_rate` | `float` | **Required** The maximum achievable angular frequency of the Rabi cycle for a driven quantum transition. This is a number between 0 and 100.
`polar_angle` | `float` | **Required** An angle measured from the z-axis on the Bloch sphere. This is a number between 0 and 1 (units of pi).

#### List all controls
```
GET /controls/
```

#### List one control
```
GET /controls/:id
```

#### Update one specific control
```
PUT /controls/:id
```

##### Input
Name | Type | Description
---- | ---- | -----------
`name` | `string` | **Required** Name of the control
`type` | `string` | **Required** One of: Primitive, CORPSE, Gaussian, CinBB, CinSK
`maximum_rabi_rate` | `float` | **Required** The maximum achievable angular frequency of the Rabi cycle for a driven quantum transition. This is a number between 0 and 100.
`polar_angle` | `float` | **Required** An angle measured from the z-axis on the Bloch sphere. This is a number between 0 and 1 (units of pi).

#### Delete one control
```
DELETE /controls/:id
```

#### Bulk upload controls in CSV
```
POST /controls/upload
```

##### Input
Name | Type | Description
-----|------|------------
`data` | `binary` | CSV file in binary format

For example,
```
curl -X POST -i
--data-binary @dir/to/foo.csv
-H 'Content-Type: text/csv'
-H 'Accept: text/csv' http://domain.name/api/controls/upload/
```

#### Download controls in CSV
```
GET /controls/download
```

## Testing
You can easily invoke tests with
```console
$ poetry run ./manage.py test
```

## Future Improvements
1. CI/CD (with GitHub actions)
1. Authentication to limit scope of API
1. API versioning
1. Rate limiting
1. User-Agent detection
