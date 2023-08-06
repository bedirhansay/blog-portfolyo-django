const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");
const webpack = require("webpack");

const mode = process.env.NODE_ENV || "development";
const target = mode === "production" ? "browserslist" : "web";

module.exports = {
  mode: mode,

  entry: "./index.js",
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "js/bundle.js",
    publicPath: "/templates/build/",
  },
  target: 'web',
  watch: mode === "development",
  watchOptions: {
    ignored: /node_modules/,
  },
  devServer: {
    port:8000,
    compress: true,
    liveReload: true,
    static: {
      directory: path.resolve(__dirname, "bundle"),
    },
    historyApiFallback: true,
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        test: /\.(scss|css)$/,
        exclude: /node_modules/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'postcss-loader',
          'sass-loader',
        ],
      },
    ],
  },

  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css",
    }),
  ],

  optimization: {
    minimize: mode === "production",
    minimizer: [
      new CssMinimizerPlugin({
        minimizerOptions: {
          level: {
            1: {
              roundingPrecision: "all=3,px=5",
            },
          },
        },
      }),
    ],
  },
};
