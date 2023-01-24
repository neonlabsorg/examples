const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync = Web3.providers.HttpProvider.prototype.send

const provider = new Web3.providers.HttpProvider("https://devnet.neonevm.org");

// Private keys for test accounts
// NOTE: Replace this private keys by your own and make sure it has non-zero NEON balances
const privateKeys = [
  "0x7efe7d68906dd6fb3487f411aafb8e558863bf1d2f60372a47186d151eae625a",
  "0x09fb68d632c2b227cc6da77696de362fa38cb94e1c62d8a07db82e7d5e754f10"
];

module.exports = {
  networks: {
    neonlabs: {
      provider: () => {
        return new HDWalletProvider(
          privateKeys,
          provider,
        );
      },
      network_id: "*"
    }
  },
  compilers: {
    solc: {
      version: "^0.8.0"
    }
  }
};
