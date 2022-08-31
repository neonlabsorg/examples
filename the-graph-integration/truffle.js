const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync = Web3.providers.HttpProvider.prototype.send

const provider = new Web3.providers.HttpProvider("http://127.0.0.1:9090");

const privateKeys = [
  '0xf5c746b15e3bdd6bf8c516031a15de16ea161ce10552635abb27c9bd16e0a04a',
  '0xf5cc5e36108264bc26e33616287a34eeaab06bffc6890e7db40d53e7821b382a',
  '0xd482434a14e3c2418afe25a29c18e685fdc86c26a3402c0ace449f3e5c5df6e5',
];

module.exports = {
  networks: {
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(
          privateKeys,
          provider
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
