require('babel-register')
require('babel-polyfill')
const Web3 = require("web3");
const HDWalletProvider = require('truffle-hdwallet-provider')

let privateKeys = [
  '0xf5c746b15e3bdd6bf8c516031a15de16ea161ce10552635abb27c9bd16e0a04a',
  '0xf5cc5e36108264bc26e33616287a34eeaab06bffc6890e7db40d53e7821b382a',
  '0xd482434a14e3c2418afe25a29c18e685fdc86c26a3402c0ace449f3e5c5df6e5',
];

const provider = 

module.exports = {
  networks: {
    development: {
      host: '127.0.0.1',
      port: 8545,
      network_id: '*',
    },
    ropsten: {
      provider: function() {
        return new HDWalletProvider(
          process.env.MNEMONIC,
          `https://ropsten.infura.io/v3/${process.env.ROPSTEN_INFURA_API_KEY}`
        )
      },
      network_id: '3',
    },
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(
          privateKeys,
          new Web3.providers.HttpProvider("http://127.0.0.1:9090"),
          0, 3
        );
      },
      network_id: "*"
    }
  },
  compilers: {
    solc: {
      version: '0.4.25'    // Fetch exact version from solc-bin (default: truffle's version)
    }
  }
}
