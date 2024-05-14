# 🚀 Wagtail startup website

This project has been created using the amazing [Wagtail CMS](https://github.com/wagtail/wagtail).

This project is meant to be a minimalistic Wagtail site demo, which can be referenced to build a more extensive Wagtail site. This differs from the `wagtail start mysite mysite` site as it contains some of the basics I find I almost always need, such as frontend tooling, CI, pre-commit linting, hosting configuration (e.g. Fly.io), etc.

For this stack, I'm aiming to keep the dependencies light so that this website can be cheaply (if not freely) hosted using minimal resources.

Also worth checking out the [Wagtail Bakery demo site](https://github.com/wagtail/bakerydemo) which uses a different stack. The main difference being that this uses SQLite instead of postgres.


**Document contents**

- [Installation](#installation)
- [Backend development](#backend-development)
- [Frontend development](#frontend-development)

## Installation

We use [Docker](https://docs.docker.com/) to set up a local build for development.

### Dependencies

- [Docker](https://docs.docker.com/engine/installation/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### To build the container:

```bash
git clone https://github.com/victoriachan/wagtail-startup-site.git
cd wagtail-startup-site
docker-compose build
```

### To start the container and gunicorn, run:

```bash
docker-compose up -d
```

The local site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the Wagtail admin
interface at [http://localhost:8000/admin/](http://localhost:8000/admin/).


### To run bash on the container:

```bash
docker-compose exec web bash
```

You can then run the usual Wagtail commands:

```bash
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser
```

### Backup and restore

#### Database

This site uses SQLite database. To backup / restore the database, simply copy and replace the `data/db.sqlite3` file. On local builds, this file is mounted as a bind mount, and will persist between docker builds unless explicitly deleted.

#### Media files (images and docs)

Similarly, the `data/media` (Wagtail Image and Document files) directory is mounted as a bind mount, and will persist between docker builds unless explicitly deleted. Likewise, it can be backed up and restored by simply copying and replacing the directory.


### To stop the container:

```bash
docker-compose stop
```

### Debugging

To tail the logs from the Docker containers in realtime, run:

```bash
docker-compose logs -f
```

## Backend development

### Updating backend dependencies

We use [pip-tools](https://pip-tools.readthedocs.io/en/latest/) to manage these.

To update pip packages, edit `requirements.in`, and then run:

```bash
pip-compile --allow-unsafe --generate-hashes
pip install -r requirements.txt
```

## Frontend development

Frontend css and js src files are in `static_src/` directory, and are compiled into `static_compiled/`. By default if not changing any frontend files, the CSS and JS should already be compiled on a fresh docker build.

For working with frontend files, see documentation about [Frontend tooling](https://github.com/victoriachan/wagtail-startup-site/blob/main/docs/frontend_tooling.md).
