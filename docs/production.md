# Production site

## Environment variables required

- **`WAGTAIL_SITE_NAME`**: This is displayed on Wagtail CMS admin.
- **`WAGTAILADMIN_BASE_URL`**: e.g. `http://example.com`
- **`ALLOWED_HOSTS`**: Security measure to prevent HTTP Host header attacks. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)
- **`SECRET_KEY`**: Django secret key. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key)
- **`SENTRY_DSN`**: For error monitoring. See https://docs.sentry.io/platforms/python/integrations/django/#configure
- **`SENTRY_ENVIRONMENT`**: Optional. Can be set as 'production' or 'staging' to make it easier to filter errors on Sentry.

## Production hosting

The hosting solution of choice for this site is a PaaS provider such as [Heroku](https://heroku.com/) and [Fly.io](https://fly.io/) for ease of use.

As the default setup here uses SQlite database, it would be cheaper for hosting since most providers charge extra for Postgres.

### Fly.io

Coming soon..

References:

- https://programmingmylife.com/2023-11-06-using-sqlite-for-a-django-application-on-flyio.html
- https://community.fly.io/t/using-sqlite-from-persistent-volume-for-django-application/16206/5

### Heroku

**IMPORTANT:** Sqlite database does not work on Heroku (see [why](https://devcenter.heroku.com/articles/sqlite3)). So the settings will need to be changed to use postgres, and this would mean extra hosting cost.

Requires [Eco dynos plan](https://devcenter.heroku.com/articles/eco-dyno-hours) subscription or higher.

Using Heroku CLI on host machine, run the following to create the app:

```bash
heroku login
heroku create -a example-app --region=eu --stack=container
```

We are using the 'container' (Docker) stack here instead of a Python buildpack. This makes our config more portable (e.g. switching between Fly.io and Heroku), and also we can use the same container for local development.


Deploy the application (`main` branch) to Heroku:

```bash
git push heroku main
```

Once the application is deployed. Ensure that at least one instance of the app is running:

```bash
heroku ps:scale web=1
```

Also don't forget to set [environment variables](#environment-variables-required) as stated above.

Visit the app at the URL shown in the deploy output. As a handy shortcut, you can also open the website as follows:

```bash
heroku open
```

To get on production shell, 

```bash
heroku run bash
```


#### Recommended Heroku addons

- Papertrail (free): For logging. Useful for debugging problems.
- Heroku Scheduler (free): For cron tasks such as `python manage.py update_index`/

Source: 

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#create-and-deploy-the-app)
- [Building Docker Images with heroku.yml](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

## Sentry: Error Monitoring

[Sentry.io](https://docs.sentry.io/) is used for error monitoring.
