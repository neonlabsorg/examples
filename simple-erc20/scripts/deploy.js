const hre = require("hardhat");

async function main() {
  const ERC20 = await hre.ethers.getContractFactory("ERC20");
  const erc20 = await ERC20.deploy("Example ERC20 token", "EERC");

  await erc20.deployed();
  console.log(erc20.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
