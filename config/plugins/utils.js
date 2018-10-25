import webpack from "webpack";
import { StatsWriterPlugin } from "webpack-stats-plugin";

import { NODE_ENV, BANNER } from "../config";

const define = new webpack.DefinePlugin({
  __DEV__: JSON.stringify(NODE_ENV === "development"),
  __PRODUCTION__: JSON.stringify(NODE_ENV === "production")
});

const HMR = new webpack.HotModuleReplacementPlugin();

const hashedModuleIds = new webpack.HashedModuleIdsPlugin();

const banner = new webpack.BannerPlugin({
  banner: BANNER,
  raw: false,
  entryOnly: false
});

const buildInfo = new StatsWriterPlugin({
  filename: "stats.json"
});

export { define, HMR, hashedModuleIds, banner, buildInfo };
