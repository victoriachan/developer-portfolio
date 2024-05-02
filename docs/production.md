# Production site

## Environment variables required

- **WAGTAIL_SITE_NAME**: e.g. `My Portfolio` - This is displayed on Wagtail CMS admin.
- **WAGTAILADMIN_BASE_URL**: e.g. `http://example.com`
- **ALLOWED_HOSTS**: Security measure to prevent HTTP Host header attacks. See [Django documentation](https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts)


## Production hosting

The hosting solution of choice for this site is a PaaS provider such as [Heroku](https://heroku.com/) and [Fly.io](https://fly.io/) for ease of use. 

As the default setup here uses SQlite database, it would be cheaper for hosting since most providers charge extra for Postgres.

### Heroku

Requires [Eco dynos plan](https://devcenter.heroku.com/articles/eco-dyno-hours) subscription or higher.

Using Heroku CLI on host machine, run the following to create the app:

```bash
heroku login
heroku create -a example-app
```

Deploy the application (`main` branch) to Heroku:

```bash
git push heroku main
```

Once the application is deployed. Ensure that at least one instance of the app is running:

```bash
heroku ps:scale web=1
```

Visit the app at the URL shown in the deploy output. As a handy shortcut, you can also open the website as follows:

```bash
heroku open
```

Source: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#create-and-deploy-the-app)
