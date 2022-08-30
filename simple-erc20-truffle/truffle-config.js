const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync = Web3.providers.HttpProvider.prototype.send

const provider = new Web3.providers.HttpProvider("https://devnet.neonevm.org");

const privateKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"; // Specify your private key here

module.exports = {
  networks: {
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(
          [ privateKey ],
          provider,
        );
      },
      network_id: "*"
    }
  }
};
