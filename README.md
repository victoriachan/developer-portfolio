# 🚀 Victoria Chan's developer portfolio website

This project has been created using the amazing [Wagtail CMS](https://github.com/wagtail/wagtail).

This project is meant to be a minimalistic Wagtail site for showcasing a freelance developer's portfolio and details. 
I'm hoping to keep the dependencies light so that this website can be cheaply (if not freely) hosted using minimal 
resources.

## Local Development

### Setup with locally using Docker

#### Dependencies

- [Docker](https://docs.docker.com/engine/installation/)
- [Docker Compose](https://docs.docker.com/compose/install/)

#### Installation

##### To build the container:

```bash
git clone https://github.com/victoriachan/developer-portfolio.git --config core.autocrlf=input
cd developer-portfolio
docker-compose build
```

##### To start the container and gunicorn, run:

```bash
docker-compose up -d
```

The local site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the Wagtail admin
interface at [http://localhost:8000/admin/](http://localhost:8000/admin/).

##### To run bash on the container:

```bash
docker-compose exec web bash
```

You can then run the usual Wagtail commands:

```bash
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser
```

##### To stop the container:

```bash
docker-compose stop
```

**Important:** This `docker-compose.yml` is configured for local testing only, and is _not_ intended for production use.

##### Debugging

To tail the logs from the Docker containers in realtime, run:

```bash
docker-compose logs -f
```

### Add packages

To update pip packages, edit `requirements.in`, and then run:

```bash
pip-compile --allow-unsafe --generate-hashes
pip install -r requirements.txt
```

### Frontend

Frontend css and js src files are in `static_src/` directory, and are compiled into `static_compiled/`.

#### To install frontend tooling:

```bash
npm install
```

#### To create a production build:

```bash
npm run build-prod
```

#### To create a development build:

```bash
npm run build-dev
```