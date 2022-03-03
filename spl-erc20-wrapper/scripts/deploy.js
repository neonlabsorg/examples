const { base58_to_binary } = require('base58-js');
const hre = require("hardhat");

async function main() {
  let token_mint = process.env.AWESOME_TOKEN_ADDRESS;
  if (token_mint == null) {
    console.log(`One must specify address of SPL token mint as environment variable AWESOME_TOKEN_ADDRESS`);
    return;
  }

  token_mint = base58_to_binary(token_mint);

  const Wrapper = await hre.ethers.getContractFactory("NeonERC20Wrapper");
  const wrapper = await Wrapper.deploy(token_mint);

  await wrapper.deployed();

  console.log(wrapper.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
