# Production site


## Fly.io

The production site is hosted on [Fly.io](https://fly.io/), a platform as a service (PaaS) provider. We use Docker rather than fly.io buildpacks for portability. 

As we use SQlite database, we cannot host this on Heroku (see [why](https://devcenter.heroku.com/articles/sqlite3)). We don't want to use postgres as that will cost another $5/mth/app.


### Set up a new Fly.io app

You'll need to [install flyctl](https://fly.io/docs/hands-on/install-flyctl/), if not already.

- Create a Fly.io app (using `flyctl launch` or admin dashboard).
- Create a Fly.io volume: `fly volumes create <volume name> -r <region code>`.
- Make sure app name, volume name (in mount source) matches those in `fly.toml`.
- Set [environment variables](#environment-variables-required) as stated below.
- Run `flyctl deploy`

### Environment variables required

- **`WAGTAIL_SITE_NAME`**: This is displayed on Wagtail CMS admin.
- **`WAGTAILADMIN_BASE_URL`**: e.g. `http://example.com`
- **`ALLOWED_HOSTS`**: Security measure to prevent HTTP Host header attacks. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)
- **`SECRET_KEY`**: Django secret key. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key). Generate by running `python -c "import secrets; print(secrets.token_urlsafe())"
`
- **`SENTRY_DSN`**: For error monitoring. See https://docs.sentry.io/platforms/python/integrations/django/#configure
- **`SENTRY_ENVIRONMENT`**: Optional. Can be set as 'production' or 'staging' to make it easier to filter errors on Sentry.

#### Fly.io only

- **`MEDIA_DIR`**: For Fly.io, this should be `/app/data/media`. 
- **`SQLITE_FILEPATH`**: For Fly.io, this should be `/app/data/db.sqlite3`.


### References:

- https://usher.dev/posts/wagtail-on-flyio/part-1/
- https://programmingmylife.com/2023-11-06-using-sqlite-for-a-django-application-on-flyio.html
- https://community.fly.io/t/using-sqlite-from-persistent-volume-for-django-application/16206/5




## Sentry: Error Monitoring

[Sentry.io](https://docs.sentry.io/) is used for error monitoring.
