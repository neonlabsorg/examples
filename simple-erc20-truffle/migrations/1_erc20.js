var SimpleERC20 = artifacts.require("ERC20");

module.exports = function(deployer) {
  // deployment steps
  deployer.deploy(SimpleERC20);
};
