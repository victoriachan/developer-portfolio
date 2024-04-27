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

Run the following commands:

```bash
git clone https://github.com/victoriachan/developer-portfolio.git --config core.autocrlf=input
cd developer-portfolio
docker-compose up -d
```

To run bash on the container, run

```bash
docker-compose exec web bash
```

You can then run the usual Wagtail commands:

```bash
./manage.py collectstatic
./manage.py migrate
./manage.py createsuperuser
```

The local site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the Wagtail admin
interface at [http://localhost:8000/admin/](http://localhost:8000/admin/).


**Important:** This `docker-compose.yml` is configured for local testing only, and is _not_ intended for production use.

### Debugging

To tail the logs from the Docker containers in realtime, run:

```bash
docker-compose logs -f
```

### Add packages

To update pip packages, edit `requirements.in`, and then run:

```
pip-compile --allow-unsafe --generate-hashes
pip install -r requirements.txt
```
