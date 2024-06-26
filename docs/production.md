# Production site


## Fly.io

The production site is hosted on [Fly.io](https://fly.io/), a platform as a service (PaaS) provider. We use Docker rather than fly.io buildpacks for portability. 

As we use SQlite database, we cannot host this on Heroku (see [why](https://devcenter.heroku.com/articles/sqlite3)). We don't want to use postgres as that will cost another $5/mth/app.

### Useful fly commands

To SSH

```bash
fly ssh console
```

### Set up a new Fly.io app

You'll need to [install flyctl](https://fly.io/docs/hands-on/install-flyctl/), if not already.

- Create a Fly.io app (using `flyctl launch` or admin dashboard).
- Create a Fly.io volume: `fly volumes create <volume name> -r <region code>`.
- Make sure app name, volume name (in mount source) matches those in `fly.toml`.
- Set [environment variables](#environment-variables-required) as stated below.
- Run `flyctl deploy`

#### Environment variables (aka Secrets) required

- **`WAGTAIL_SITE_NAME`**: This is displayed on Wagtail CMS admin.
- **`WAGTAILADMIN_BASE_URL`**: e.g. `http://example.com`
- **`ALLOWED_HOSTS`**: Security measure to prevent HTTP Host header attacks. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)
- **`CSRF_TRUSTED_ORIGINS`**: List of trusted origins for post requests. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#csrf-trusted-origins)
- **`SECRET_KEY`**: Django secret key. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key). Generate by running `python -c "import secrets; print(secrets.token_urlsafe())"
`
- **`SENTRY_DSN`**: For error monitoring. See https://docs.sentry.io/platforms/python/integrations/django/#configure
- **`SENTRY_ENVIRONMENT`**: Optional. Can be set as 'production' or 'staging' to make it easier to filter errors on Sentry.
- **`MEDIA_ROOT`**: For Fly.io, this should be `/data/media`. 
- **`SQLITE_DATABASE_NAME`**: For Fly.io, this should be `/data/db.sqlite3`.
- **`FLY_API_TOKEN`**: For Fly.io deployment, see https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/

### Backup

Fly.io takes daily block-level snapshots of volumes (i.e. the SQLite database). They keep snapshots for five days. See https://fly.io/docs/reference/volumes/#volume-snapshots

### References:

- https://usher.dev/posts/wagtail-on-flyio/part-1/
- https://programmingmylife.com/2023-11-06-using-sqlite-for-a-django-application-on-flyio.html
- https://community.fly.io/t/using-sqlite-from-persistent-volume-for-django-application/16206/5


## Sentry: Error Monitoring

[Sentry.io](https://docs.sentry.io/) is used for error monitoring.