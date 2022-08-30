var SimpleERC20 = artifacts.require("ERC20");

module.exports = async function(deployer, network, accounts) {
  // deployment steps
  await deployer.deploy(SimpleERC20);
  let erc20Instance = await SimpleERC20.deployed();
  await erc20Instance.mint(1000000000, { from: accounts[0] });
};
