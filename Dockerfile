# Install and build front-end dependencies. 
# Make node version matches version in .nvmrc.
FROM node:20 as frontend

COPY . .

RUN npm ci --omit=optional --no-audit --progress=false
RUN npm run build-prod


# Use an official Python runtime based on Debian 12 "bookworm" as a parent image.
FROM python:3.12-slim-bookworm as production

# Install dependencies in a virtualenv
ENV VIRTUAL_ENV=/venv

# Add user that will be used in the container.
# Use --create-home to create a home directory for the user, as we need it for nvm.
RUN useradd wagtail --create-home && mkdir /app $VIRTUAL_ENV && chown -R wagtail /app $VIRTUAL_ENV

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PATH=$VIRTUAL_ENV/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PORT=8000 \
    DJANGO_SETTINGS_MODULE="portfolio.settings.production"

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Install the project requirements.
RUN python -m venv $VIRTUAL_ENV
RUN pip install --no-cache --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf $HOME/.cache

# Copy compiled FE output from the frontend build stage into the container
COPY --chown=wagtail --from=frontend ./static_compiled ./static_compiled

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static. This command will move static files from application
# directories and "static_compiled" folder to the main static directory that
# will be served by the WSGI server.
RUN python manage.py collectstatic --noinput --clear

# Run the WSGI server. It reads GUNICORN_CMD_ARGS, PORT and WEB_CONCURRENCY
# environment variable hence we don't specify a lot options below.
CMD gunicorn portfolio.wsgi:application

# Local config for using npm in the container for local development.
# To use, update target in docker-compose.yml to "dev"
FROM production as dev

# FE tooling so we can use npm in the container. 
USER wagtail

# Copy bash_aliases to the container for the wagtail user.
# This fixes an issue with nvm in the dev container.
COPY ./docker/bash_aliases.sh /home/wagtail/.bash_aliases

# Copy the node_modules from the frontend build stage so we don't have to rebuild them.
COPY --chown=wagtail --from=frontend ./node_modules ./node_modules

# Install nvm and node/npm
COPY --chown=wagtail .nvmrc ./
RUN curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash && \
    bash --login -c "nvm install --no-progress && nvm alias default $(nvm run --silent --version)"

# do nothing forever - exec commands elsewhere
CMD tail -f /dev/null
