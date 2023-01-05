require("@nomiclabs/hardhat-waffle");

const proxy_url = "https://devnet.neonevm.org";
const network_id = 245022926;

// Private keys for test accounts
// NOTE: Replace this private keys by your own and make sure it has non-zero NEON balances
const privateKeys = [
  "0x8aa061f89a54f4374d7de4f6cc06120c06db9af3e9fcbfb997458d9f55ab844a",
  "0x8bfafc75212e9bf00c1380c15efa808f30c6d3f17219feddaae9c5048ac68061",
];

module.exports = {
  solidity: "0.8.4",
  defaultNetwork: "neonlabs",
  networks: {
    neonlabs: {
      url: proxy_url,
      accounts: privateKeys,
      network_id: network_id,
      chainId: network_id,
      allowUnlimitedContractSize: false,
      timeout: 1000000,
      isFork: true,
    },
  },
};
