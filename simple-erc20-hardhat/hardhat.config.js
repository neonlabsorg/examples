require("@nomiclabs/hardhat-waffle");

const proxy_url = 'https://devnet.neonevm.org';
const network_id = 245022926;
const deployerPrivateKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"; // Specify your private key here

module.exports = {
  solidity: "0.8.4",
  defaultNetwork: 'neonlabs',
  networks: {
    neonlabs: {
      url: proxy_url,
      accounts: [deployerPrivateKey],
      network_id: network_id,
      chainId: network_id,
      allowUnlimitedContractSize: false,
      timeout: 1000000,
      isFork: true
    }
  }
};
