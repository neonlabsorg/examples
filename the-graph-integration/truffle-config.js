require("dotenv").config();
const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync =
  Web3.providers.HttpProvider.prototype.send;

const provider = new Web3.providers.HttpProvider("https://devnet.neonevm.org/");

const privateKeys = [
  process.env.PRIVATE_KEY_1,
  process.env.PRIVATE_KEY_2,
  process.env.PRIVATE_KEY_3,
];

module.exports = {
  networks: {
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(privateKeys, provider);
      },
      network_id: "*",
    },
  },

  // Set default mocha options here, use special reporters, etc.
  mocha: {
    // timeout: 100000
  },

  // Configure your compilers
  compilers: {
    solc: {
      version: "0.7.6", // Fetch exact version from solc-bin (default: truffle's version)
    },
  },
};
