const path = require('path');
const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
  entry: './assets/index.js',  // path to our input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './static'),  // path to our Django static directory
  },
  resolve: {
    alias: {
      'vue$':'vue/dist/vue.esm.js'
    }
  },
  module: {
    rules: [
        {
            test: /\.vue$/,
            loader: 'vue-loader'
        },
        {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            loader: "babel-loader",
            options: { presets: ["@babel/preset-env"] }
        },
        {
            test: /\.css$/,
            use: [
              'vue-style-loader',
              'css-loader'
            ]
        }
    ]
  },
  plugins: [
      new VueLoaderPlugin()
  ]
};