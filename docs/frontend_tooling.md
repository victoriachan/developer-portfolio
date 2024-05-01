# Frontend tooling

This project uses Webpack to 'compile' frontend assets from `static_src` into `static_compiled`. 

By default, for npm is run in the docker container. The docker build stage will already have compiled the CSS and JS, so unless there are changes to `static_src`, it is not necessary to re-run `npm run build-prod`. 


## To run locally

### Run npm in docker container

If there are changes to `static_src`, you can run npm in the **container** to rebuild the files.

To get into the container shell:

```bash
docker-compose exec web bash
```

Then run npm as needed, e.g. `npm run build-prod`. 


### Run npm on host machine (i.e. not in Docker). 

To run npm on host machine instead, update `docker-compose.yml` with the following, then restart the docker container.

- Uncomment `- ./static_compiled:/app/static_compiled`, 
- Change `target: dev` to `target: production`, 
- Make sure you have [NVM](https://github.com/nvm-sh/nvm) installed on your host machine. 


Then run the following on your host machine:

```bash
nvm use
npm install
npm run build-prod
```

## Frontend dependencies

These are specified on `package.json`. See also `webpack.config.js` for Webpack config for the plugins.

We should try to keep dependencies to minimal, and document justification for their uses below. Bloated dependencies can have performance, security and maintenance issues.

- **webpack** (`webpack`, `webpack-cli`): For bundling, minification, etc.
- **clean-webpack-plugin**: Clean up unused webpack assets on build.
- **copy-webpack-plugin**: Used to sync images from static_src to static_compiled.
- **css-loader**: Basic css support for Webpack.
- **css-minimizer-webpack-plugin**: CSS minimizer.
- **mini-css-extract-plugin**: Need this to extract/copy our .css from static_src to static_compiled.
