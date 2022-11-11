require("@nomiclabs/hardhat-waffle");

const proxy_url = 'https://devnet.neonevm.org';
const network_id = 245022926;

// Private keys for test accounts
// NOTE: Replace this private keys by your own and make sure it has non-zero NEON balances
const privateKeys = [
  "0xb639c3b4485c5f067c1e86d63f6f31afd0c4c8fb5227d24c431e3a172c830513",
  "0x41ac2becab52d55cb204c65366c3475189064d1d612cc2552103b96de0909ec4"
];

module.exports = {
  solidity: "0.8.4",
  defaultNetwork: 'neonlabs',
  networks: {
    neonlabs: {
      url: proxy_url,
      accounts: privateKeys,
      network_id: network_id,
      chainId: network_id,
      allowUnlimitedContractSize: false,
      timeout: 1000000,
      isFork: true
    }
  }
};
