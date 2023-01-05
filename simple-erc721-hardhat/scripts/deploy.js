const hre = require("hardhat");

async function main() {
  const [deployer] = await ethers.getSigners();
  console.log("Deploying contracts with the account:", deployer.address);

  const ERC721 = await hre.ethers.getContractFactory("ERC721ForMetaplex");
  const erc721 = await ERC721.deploy();

  await erc721.deployed();
  console.log("Contract address is: ", erc721.address);

}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
