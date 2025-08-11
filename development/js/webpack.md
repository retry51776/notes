# Module Bundler

> Think of a modern website as a puzzle presented to the user.  
> The module bundler (e.g., Webpack) is the process that assembles the pieces in the puzzle factory.

## Alternatives

- Rollup  
- Parcel  
- Snowpack  

[Watch this video for an overview](https://www.youtube.com/watch?v=lFjinlwpcHY&ab_channel=uidotdev)

## Webpack Modules

> Loaders operate at the file level.

- `bundle-loader`
- `babel-loader`
- `file-loader`
- `style-loader`, `css-loader`, `postcss-loader`, `resolve-url-loader`, `sass-loader`

> Plugins work at higher levels (e.g., on bundles).

- `HotModuleReplacementPlugin`
- `CleanWebpackPlugin`
- `SplitChunksPlugin`
- `HtmlWebpackPlugin`

### Styles

- `node-sass` provides bindings for Node.js to **LibSass**, a Sass compiler.  
- `sass-loader` compiles SCSS/Sass files for Webpack.  
- `style-loader` injects styles into the DOM at runtime.  
- `css-loader` interprets `@import` and `url()` statements and resolves them.  
- `mini-css-extract-plugin` extracts CSS from the JavaScript bundle into a separate file, which is essential for production builds.

### JavaScript

- `babel` – transpiles modern ES6+ syntax.  
- `polyfill` – adds browser compatibility for missing features.

### webpack.config.js

For full configuration options see the [Webpack documentation](https://webpack.js.org/configuration/resolve/).

> Source maps (e.g., `bundle.js.map`) link compiled code back to the original source lines, making debugging easier.

```js
const webpack = require('webpack');
const path = require('path');
// const merge = require('webpack-merge');
// process.env.npm_lifecycle_event

module.exports = {
  context: path.join(__dirname, 'xyz/'),
  entry: {
    /* Multi‑entry will enable code splitting */
  },
  output: {},
  module: {
    rules: [
      {
        test: /* regex to find target files */,
        use: [/* loaders */],
      },
    ],
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
    // Example of injecting variables into the front end
    new webpack.DefinePlugin({
      AUTHOR: 'Terry',
      ANOTHER_ENV: '123',
    }),
  ],
  resolve: {
    alias: {},
  },
};
```
```​```