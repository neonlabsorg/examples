const { ethers } = require("hardhat");
let chai = require('chai');

var assert = chai.assert;
var expect = chai.expect;

describe("Testing TestERC20 contract", function() {
  let erc20Instance;
  let accountOne;
  let accountTwo

  beforeEach(async function() {
    let erc20Factory = await ethers.getContractFactory("ERC20");
    [ accountOne, accountTwo ] = await ethers.getSigners();
    erc20Instance = await erc20Factory.deploy();
  });

  it("should successfully mint 10000 ERC20 in the first account", async () => {
    const mintAmount = 10000
    const balanceBefore = await erc20Instance.balanceOf(accountOne.address);
    await expect(erc20Instance.connect(accountOne).mint(mintAmount))
      .to.emit(erc20Instance, 'Transfer');
    const balanceAfter = await erc20Instance.balanceOf(accountOne.address);

    assert.equal(
       balanceAfter - balanceBefore, 
       mintAmount, 
       "Mint was not successed"
    );
  });

  it("should transfer token correctly", async () => {
    const mintAmount = 10000;
    const transferAmount = 1234;
    
    // mint tokens to first account
    await expect(erc20Instance.connect(accountOne).mint(mintAmount))
      .to.emit(erc20Instance, 'Transfer');
    
    const balanceOneBefore = await erc20Instance.balanceOf(accountOne.address);
    const balanceTwoBefore = parseInt(await erc20Instance.balanceOf(accountTwo.address));
    
    await expect(erc20Instance
                  .connect(accountOne)
                  .transfer(accountTwo.address, transferAmount))
            .to.emit(erc20Instance, 'Transfer');
    
    const balanceOneAfter = await erc20Instance.balanceOf(accountOne.address);
    const balanceTwoAfter = await erc20Instance.balanceOf(accountTwo.address);
    
    assert.equal(
      balanceOneAfter,
      balanceOneBefore - transferAmount, 
      "Source balance should decrease by transferAmount"
    );
    
    assert.equal(
       balanceTwoAfter,
       balanceTwoBefore + transferAmount, 
       "Traget balance should increase by transferAmount"
    );
  });
});
