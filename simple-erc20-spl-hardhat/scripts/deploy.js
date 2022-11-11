const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);
  const ERC20 = await hre.ethers.getContractFactory("ERC20ForSplMintable");
  const erc20_for_spl = await ERC20.deploy(
    "Test token",
    "TPL",
    9,
    deployer.address
  );

  await erc20_for_spl.deployed();
  console.log("Contract address is: ", erc20_for_spl.address);

  const amount = 100 * 10 ** 9;
  console.log("Minting ", amount, " tokens...");
  await erc20_for_spl.mint(deployer.address, amount);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
