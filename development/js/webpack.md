# Webpack

# Module bunder(Webpack)
Alternative
- rool up
- parcel
- snowpack
https://www.youtube.com/watch?v=lFjinlwpcHY&ab_channel=uidotdev

## Webpack Modules
> Loader works in file level

- bundle-loader
- babel-loader
- file-loader
- style-loader, css-loader, postcss-loader, resolve-url-loader, sass-loader


> plugin works in other levels (Ex: bundle)
- HotModuleReplacementPlugin
- CleanWebpackPlugin
- SplitChuncksPlugin
- HtmlWebpackPlugin


### Styles
- `node-sass` provides binding for Node.js to LibSass, a Sass compiler.
- `sass-loader` is a loader for Webpack for compiling SCSS/Sass files.
- `style-loader` injects our styles into our DOM.
- `css-loader` interprets @import and @url() and resolves them.
- `mini-css-extract-plugin` extracts our CSS out of the JavaScript bundle into a separate file, essential for production builds.

### JS
`babel` - es6
`polyfill` - browser compability

### webpack.config.js
https://webpack.js.org/configuration/resolve/
> sourceMap `bundle.js.map` links compiled code to source line
```
const webpack = require('webpack');
const path = require('path');
// const merge = require('webpack-merge');
// process.env.npm_lifecycle_event

module.exports = {
  context: path.join(__dirname, 'xyz/'),
  entry: {
    /* multi entry will code splitting */
  },
  output: {},
  module: {
    rules: [
      {
        test: /* regx find target files */,
        use: [/* loaders */]
      }
    ]
  },
  // devtool: 'cheap-eval-source-map',
  plugins: [
    new CleanWebpackPlugin(),
    new webpack.HashedModuleIdsPlugin(),
    new webpack.optimize.SplitChunksPlugin(),
    new HtmlWebpackPlugin({
      filename: 'views/index.html',
      title: 'Terry',
      template: 'views/base.ejs',
    }),
    // Example inject variable into front end
    new webpack.DefinePlugin({
      AUTHOR: 'Terry',
      ANOTHER_ENV: '123',
    }),
  ],
  resolve: {
    alias: {}
  },
}
```
