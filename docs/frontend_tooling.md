# Frontend tooling

This project uses Webpack to 'compile' frontend assets from `portfolio/static_src` into `portfolio/static_compiled`.

## To run locally

On the host machine, in the project directory, run the following to install:

```bash
npm install
```

This will create a `node_modules` directory with the dependencies downloaded. Subsequently, to compile JS and CSS, run:

```bash
npm run build-prod
```

Or for dev:

```bash
npm run build-dev
```

## Webpack and plugins for basic operations

Specified on `package.json` as dependencies. See also `webpack.config.js` for Webpack config for the plugins.

- **webpack** (`webpack`, `webpack-cli`): For bundling, minification, etc.
- **clean-webpack-plugin**: Clean up unused webpack assets on build
- **copy-webpack-plugin**: Used to sync images from static_src to static_compiled
- **css-loader** (`css-loader`, `style-loader`): Basic css support for Webpack
- **css-minimizer-webpack-plugin**: CSS minimizer
