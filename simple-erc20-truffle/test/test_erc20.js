const TestERC20 = artifacts.require("ERC20");

contract("TestERC20", (accounts) => {
  it("should successfully mint 10000 ERC20 in the first account", async () => {
    const erc20Instance = await TestERC20.deployed();
    const mintAmount = 10000
    const balanceBefore = await erc20Instance.balanceOf.call(accounts[0]);
    await erc20Instance.mint(mintAmount, { from: accounts[0] });
    const balanceAfter = await erc20Instance.balanceOf.call(accounts[0]);

    assert.equal(
       balanceAfter.valueOf() - balanceBefore.valueOf(), 
       mintAmount, 
       "Mint was not successed"
    );
  });

  it("should transfer token correctly", async () => {
    const erc20Instance = await TestERC20.deployed();

    // Setup 2 accounts.
    const accountOne = accounts[0];
    const accountTwo = accounts[1];
    const mintAmount = 10000;
    const transferAmount = 1234;
    
    // mint tokens to first account
    await erc20Instance.mint(mintAmount, { from: accountOne });
    
    const balanceOneBefore = await erc20Instance.balanceOf.call(accountOne);
    const balanceTwoBefore = parseInt(await erc20Instance.balanceOf.call(accountTwo));
    
    await erc20Instance.transfer(accountTwo, transferAmount, { from: accountOne });
    
    const balanceOneAfter = await erc20Instance.balanceOf.call(accountOne);
    const balanceTwoAfter = await erc20Instance.balanceOf.call(accountTwo);
    
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
