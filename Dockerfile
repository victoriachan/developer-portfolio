# Install and build front-end dependencies. 
# Make node version matches nodesource version below.
FROM node:20 as frontend

COPY . .

RUN npm ci --no-optional --no-audit --progress=false
RUN npm run build-prod


# Use an official Python runtime based on Debian 12 "bookworm" as a parent image.
FROM python:3.12-slim-bookworm as production

# Add user that will be used in the container.
# Use -m to create a home directory for the user, as we need it for nvm.
RUN useradd -m wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
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
    && curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Copy compiled FE output from the frontend build stage into the container
COPY --from=frontend ./portfolio/static_compiled ./portfolio/static_compiled

# Use user "wagtail" to run the build commands below and the server itself.
USER wagtail

# Collect static. This command will move static files from application
# directories and "static_compiled" folder to the main static directory that
# will be served by the WSGI server.
RUN python manage.py collectstatic --noinput --clear

# Run the WSGI server. It reads GUNICORN_CMD_ARGS, PORT and WEB_CONCURRENCY
# environment variable hence we don't specify a lot options below.
CMD gunicorn portfolio.wsgi:application


# The below only runs on local development and won't affect production
FROM production as dev

# Install nvm and node/npm
COPY --chown=wagtail .nvmrc ./
RUN curl https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash && \
    bash --login -c "nvm install --no-progress && nvm alias default $(nvm run --silent --version)"

# Copy the node_modules from the frontend build stage so we don't have to rebuild them.
COPY --chown=wagtail --from=frontend ./node_modules ./node_modules
