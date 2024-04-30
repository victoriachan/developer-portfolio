# Frontend tooling

This project uses Webpack to 'compile' frontend assets from `static_src` into `static_compiled`.

## To run locally

### Run npm in docker container

By default, for local dev npm is run in the host container. The docker build will already have compiled the CSS and JS. But if there are changes to `static_src`, you can run npm in the container to rebuild the files.

Run this to get into the container shell:

```bash
docker-compose exec web bash
```

Then run npm as needed, e.g. `npm run build-prod`, in the `/app` directory. 

### Run npm on host machine (not in Docker). 

To run npm on host machine instead, update `docker-compose.yml` then restart the docker container:

- Uncomment `- ./static_compiled:/app/static_compiled`, 
- Change `target: dev` to `target: production`, 

Then run the following on your host machine:

```bash
npm install
npm run build-prod
```


## Webpack and plugins for basic operations

Specified on `package.json` as dependencies. See also `webpack.config.js` for Webpack config for the plugins.

- **webpack** (`webpack`, `webpack-cli`): For bundling, minification, etc.
- **clean-webpack-plugin**: Clean up unused webpack assets on build
- **copy-webpack-plugin**: Used to sync images from static_src to static_compiled
- **css-loader** (`css-loader`, `style-loader`): Basic css support for Webpack
- **css-minimizer-webpack-plugin**: CSS minimizer
