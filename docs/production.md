# Production site

## Environment variables required

- **WAGTAIL_SITE_NAME**: e.g. `My Portfolio` - This is displayed on Wagtail CMS admin.
- **WAGTAILADMIN_BASE_URL**: e.g. `http://example.com`
- **ALLOWED_HOSTS**: Security measure to prevent HTTP Host header attacks. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)


## Production hosting

The hosting solution of choice for this site is a PaaS provider such as [Heroku](https://heroku.com/) and [Fly.io](https://fly.io/) for ease of use. 

As the default setup here uses SQlite database, it would be cheaper for hosting since most providers charge extra for Postgres.
