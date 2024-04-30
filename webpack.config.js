const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

const projectRoot = 'portfolio';

module.exports = {
  entry: {
    'main': `./${projectRoot}/static_src/js/main.js`,
    'styles': `./${projectRoot}/static_src/css/styles.css`
  },
  output: {
    path: path.resolve(`./${projectRoot}/static_compiled/`),
    // based on entry name, e.g. main.js
    filename: 'js/[name].js', // based on entry name, e.g. main.js
  },
  plugins: [
    new CopyPlugin({
        patterns: [
            {
                // Copy images to be referenced directly by Django to the "images" subfolder in static files.
                from: 'images',
                context: path.resolve(`./${projectRoot}/static_src/`),
                to: path.resolve(`./${projectRoot}/static_compiled/images`),
            },
        ],
    }),
    new MiniCssExtractPlugin({
      filename: 'css/[name].css',
    }),
    //  Automatically remove all unused webpack assets on rebuild
    new CleanWebpackPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        type: 'asset/resource',
      },
    ],
  },
  optimization: {
    minimizer: [
      // For webpack@5 you can use the `...` syntax to extend existing minimizers (i.e. `terser-webpack-plugin`), uncomment the next line
      // `...`,
      new CssMinimizerPlugin(),
    ],
  },
};
