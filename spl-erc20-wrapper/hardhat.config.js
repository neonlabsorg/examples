require("@nomiclabs/hardhat-waffle");

const proxy_url = 'https://proxy.devnet.neonlabs.org/solana';
const network_id = 245022926;
const deployerPrivateKey = '0x42679bb84732ca108204abdd4841a716ba43593cba16a61f3289c0842e2f5e42';

module.exports = {
  solidity: "0.8.4",
  defaultNetwork: 'neonlabs',
  networks: {
    neonlabs: {
      url: proxy_url,
      accounts: [deployerPrivateKey],
      network_id: network_id,
      chainId: network_id,
      gas: 3000000,
      gasPrice: 600000000000,
      blockGasLimit: 10000000,
      allowUnlimitedContractSize: false,
      timeout: 1000000,
      isFork: true
    }
  }
};
