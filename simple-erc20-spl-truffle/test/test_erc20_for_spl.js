const ERC20ForSplMintable = artifacts.require("ERC20ForSplMintable");

contract("ERC20ForSplMintable", (accounts) => {
  let erc20SplInstance;

  beforeEach(async function () {
    erc20SplInstance = await ERC20ForSplMintable.deployed();
  });

  it("should mint 10000 ERC20", async () => {
    const mintAmount = 10000
    const balanceBefore = await erc20SplInstance.balanceOf.call(accounts[0]);

    await erc20SplInstance.mint(accounts[0], mintAmount)

    const balanceAfter = await erc20SplInstance.balanceOf.call(accounts[0]);
    assert.equal(
      balanceAfter.valueOf() - balanceBefore.valueOf(),
      mintAmount,
      "Minting was not successful"
    );
  });

  it("should check name", async () => {
    const name = await erc20SplInstance.name.call();

    assert.equal(
      name,
      "Test token",
      "Name does not match"
    );
  });

  it("should check symbol", async () => {
    const symbol = await erc20SplInstance.symbol.call();

    assert.equal(
      symbol,
      "TTL",
      "Symbol does not match"
    );
  });

  it("should check decimals", async () => {
    const decimals = await erc20SplInstance.decimals.call();

    assert.equal(
      decimals,
      9,
      "Decimals do not match"
    );
  });

  it("should check total supply", async () => {
    const mintAmount = 20000
    const b = await erc20SplInstance.mint(accounts[0], mintAmount)
    console.log("mint: ", JSON.stringify(b))

    const totalSupply = await erc20SplInstance.totalSupply.call();
    console.log("totalSupply: ", JSON.stringify(totalSupply))

    assert.equal(
      mintAmount,
      totalSupply.valueOf(),
      "Total supply does not match"
    );
  });

  it("should burn 100 ERC20", async () => {
    const mintAmount = 15000
    const burnAmount = 100

    await erc20SplInstance.mint(accounts[0], mintAmount)

    const balanceBefore = await erc20SplInstance.balanceOf.call(accounts[0]);

    await erc20SplInstance.burn(burnAmount)

    const balanceAfter = await erc20SplInstance.balanceOf.call(accounts[0]);

    assert.equal(
      balanceBefore.valueOf() - balanceAfter.valueOf(),
      burnAmount,
      "Burning was not successful"
    );
  });

  it("should transfer token correctly", async () => {
    const mintAmount = 17000;
    const transferAmount = 1200;

    await erc20SplInstance.mint(accounts[0], mintAmount);

    const balanceOneBefore = await erc20SplInstance.balanceOf.call(accounts[0]);
    const balanceTwoBefore = await erc20SplInstance.balanceOf.call(accounts[1]);

    await erc20SplInstance.transfer(accounts[1], transferAmount, { from: accounts[0] });

    const balanceOneAfter = await erc20SplInstance.balanceOf.call(accounts[0]);
    const balanceTwoAfter = await erc20SplInstance.balanceOf.call(accounts[1]);

    assert.equal(
      balanceOneAfter.valueOf(),
      balanceOneBefore.valueOf() - transferAmount,
      "Source balance should decrease by transferAmount"
    );

    assert.equal(
      balanceTwoAfter.valueOf(),
      balanceTwoBefore.valueOf() + transferAmount,
      "Traget balance should increase by transferAmount"
    );
  });
});
