const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync = Web3.providers.HttpProvider.prototype.send

const provider = new Web3.providers.HttpProvider("https://proxy.devnet.neonlabs.org/solana");

const privateKey = "0x42679bb84732ca108204abdd4841a716ba43593cba16a61f3289c0842e2f5e42"; // Specify your private key here

module.exports = {
  networks: {
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(
          privateKey,
          provider,
        );
      },
      from: "0xcB31Ce6E4Ff9E2C8f6CbB7044dd9529263a846De",
      network_id: "*",
      gas: 300000000,
      gasPrice: 443065000000,
    }
  },
  
  compilers: {
    solc: {
      version: "^0.8.0"
    }
  }
};
