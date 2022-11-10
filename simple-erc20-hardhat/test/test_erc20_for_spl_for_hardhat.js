const axios = require("axios");
const { ethers, waffle } = require("hardhat");
const provider = waffle.provider;
const { waitUntil } = require("async-wait-until");

let chai = require("chai");

var assert = chai.assert;
var expect = chai.expect;
const NEON_FAUCET_URL = "https://api.neonfaucet.org/request_neon";

describe("Testing erc20_for_SPL contract", function () {
  let erc20Instance;
  let accountOne;
  let accountTwo;

  before(async function () {
    [accountOne, accountTwo] = await ethers.getSigners();
    amount = 100;
    await request_neon(100, accountOne.address);
    await waitUntil(
      async () =>
        ethers.utils.formatEther(
          await provider.getBalance(accountOne.address)
        ) >= amount,
      {
        timeout: 15 * 60,
      }
    );
  });

  beforeEach(async function () {
    let erc20Factory = await ethers.getContractFactory("ERC20ForSplMintable");
    erc20Instance = await erc20Factory.deploy(
      "Test token",
      "TPL",
      9,
      accountOne.address
    );
  });

  async function request_neon(amount, address) {
    let res = axios
      .post(NEON_FAUCET_URL, { amount: amount, wallet: address })
      .catch(function (error) {
        console.log(error);
      });

    if (res.ok) {
      let ret = await res.json();
      return JSON.parse(ret.data);
    } else {
      return `HTTP error: ${res}`;
    }
  }

  it("should return token symbol", async () => {
    let symbol = await erc20Instance.symbol();
    assert.equal(symbol, "TPL");
  });

  it("should successfully mint 10000 ERC20 in the first account", async () => {
    const mintAmount = 10000;
    const balanceBefore = await erc20Instance.balanceOf(accountOne.address);

    await expect(erc20Instance.mint(accountOne.address, mintAmount)).to.emit(
      erc20Instance,
      "Transfer"
    );
    const balanceAfter = await erc20Instance.balanceOf(accountOne.address);
    assert.equal(
      balanceAfter - balanceBefore,
      mintAmount,
      "Mint was not successed"
    );
  });

  it("should transfer tokens correctly", async () => {
    const mintAmount = 10000;
    const transferAmount = 1234;

    await expect(erc20Instance.mint(accountOne.address, mintAmount)).to.emit(
      erc20Instance,
      "Transfer"
    );

    const balanceOneBefore = await erc20Instance.balanceOf(accountOne.address);
    const balanceTwoBefore = parseInt(
      await erc20Instance.balanceOf(accountTwo.address)
    );

    await expect(
      erc20Instance.transfer(accountTwo.address, transferAmount)
    ).to.emit(erc20Instance, "Transfer");

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

  it("should burn tokens correctly", async () => {
    const mintAmount = 10000;
    const balanceBefore = await erc20Instance.balanceOf(accountOne.address);

    await expect(erc20Instance.mint(accountOne.address, mintAmount)).to.emit(
      erc20Instance,
      "Transfer"
    );
    const burnAmount = 5000;
    await expect(erc20Instance.burn(burnAmount)).to.emit(
      erc20Instance,
      "Transfer"
    );
    const balanceAfter = await erc20Instance.balanceOf(accountOne.address);
    assert.equal(
      balanceAfter,
      balanceBefore + mintAmount - burnAmount,
      "Burn was not successed"
    );
  });

  it("should return total supply correctly", async () => {
    const mintAmount = 10000;

    await expect(erc20Instance.mint(accountOne.address, mintAmount)).to.emit(
      erc20Instance,
      "Transfer"
    );
    const totalSupply = await erc20Instance.totalSupply();

    assert.equal(totalSupply, mintAmount);
  });
});
