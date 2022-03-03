const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  const ERC20 = await hre.ethers.getContractFactory("ERC20");
  const erc20 = await ERC20.deploy();

  await erc20.deployed();
  console.log("Contract address is: ", erc20.address);

  const amount = 100 * 10 ** 9;
  console.log("Minting ", amount, " tokens...");
  await erc20.mint(100 * 10 ** 9);
  console.log("Balance of deployer is: ", await erc20.balanceOf(deployer.address));
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
