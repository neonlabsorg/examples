const GravatarRegistry = artifacts.require("GravatarRegistry");

module.exports = async function(deployer) {
  await deployer.deploy(GravatarRegistry);

  const registry = await GravatarRegistry.deployed();
  console.log("Account address:", registry.address);

  let accounts = await web3.eth.getAccounts();
  console.log("Accounts: ", accounts);

  await registry.createGravatar(
    "Carl",
    "https://thegraph.com/img/team/team_04.png",
    {
      from: accounts[0],
    }
  );

  await registry.createGravatar(
    "Lucas",
    "https://thegraph.com/img/team/bw_Lucas.jpg",
    {
      from: accounts[1],
    }
  );

  await registry.createGravatar(
    "Rob",
    "https://thegraph.com/img/team/bw_Rob.jpg",
    {
      from: accounts[2],
    }
  );
};
