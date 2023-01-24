var ERC20ForSplMintable = artifacts.require("ERC20ForSplMintable");

module.exports = async function (deployer, network, accounts) {
  // deployment steps
  await deployer.deploy(ERC20ForSplMintable, "Test token",
    "TTL",
    9,
    accounts[0]);
};
