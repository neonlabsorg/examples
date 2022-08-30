const Web3 = require("web3");
const HDWalletProvider = require("@truffle/hdwallet-provider");

Web3.providers.HttpProvider.prototype.sendAsync = Web3.providers.HttpProvider.prototype.send

const provider = new Web3.providers.HttpProvider("https://devnet.neonevm.org");

// Private keys for test accounts
// NOTE: Replace this private keys by your own and make sure it has non-zero NEON balances
const privateKeys = [
  "0xf5c746b15e3bdd6bf8c516031a15de16ea161ce10552635abb27c9bd16e0a04a",
  "0x41ac2becab52d55cb204c65366c3475189064d1d612cc2552103b96de0909ec4"
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
  }
};
