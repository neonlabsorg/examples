let chai = require("chai");
const axios = require("axios");
const { ethers, waffle } = require("hardhat");
const provider = waffle.provider;
const { waitUntil } = require("async-wait-until");

var assert = chai.assert;
var expect = chai.expect;
const NEON_FAUCET_URL = "https://api.neonfaucet.org/request_neon";

describe("Testing ERC721 contract", function () {
  let erc721Instance;
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
        timeout: 15 * 60 * 60,
      }
    );
  });

  beforeEach(async function () {
    [accountOne, accountTwo] = await ethers.getSigners();
    let erc721Factory = await ethers.getContractFactory("ERC721ForMetaplex");

    erc721Instance = await erc721Factory.deploy();
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
      return `HTTP error:   ${res}`;
    }
  }

  it("should successfully mint in the first account", async () => {
    const seed = ethers.utils.randomBytes(32);
    const uri = Math.random().toString(36).substring(7);

    await expect(
      erc721Instance.connect(accountOne).mint(seed, accountOne.address, uri)
    ).to.emit(erc721Instance, "Transfer");
    const balanceAfter = await erc721Instance.balanceOf(accountOne.address);

    assert.equal(balanceAfter, 1, "Mint was not successed");
  });

  it("should transfer token correctly", async () => {
    const seed = ethers.utils.randomBytes(32);
    const uri = Math.random().toString(36).substring(7);
    let transferEvent = {};
    erc721Instance.on("Transfer", (from, to, tokenId) => {
      transferEvent = {
        from: from,
        to: to,
        tokenId: tokenId,
      };
    });

    await expect(
      erc721Instance.connect(accountOne).mint(seed, accountOne.address, uri)
    ).to.emit(erc721Instance, "Transfer");
    await waitUntil(() => transferEvent.tokenId !== undefined);

    const tokenId = transferEvent.tokenId.toHexString();

    await expect(
      erc721Instance.transferFrom(
        accountOne.address,
        accountTwo.address,
        tokenId
      )
    ).to.emit(erc721Instance, "Transfer");

    const balanceOneAfter = await erc721Instance.balanceOf(accountOne.address);
    const balanceTwoAfter = await erc721Instance.balanceOf(accountTwo.address);

    assert.equal(balanceOneAfter, 0, "Mint was not successed");
    assert.equal(balanceTwoAfter, 1, "Mint was not successed");
  });

  it("should return token symbol", async () => {
    let symbol = await erc721Instance.symbol();
    assert.equal(symbol, "MPL", "Symbol is not correct");
  });

  it("should return token URI", async () => {
    const seed = ethers.utils.randomBytes(32);
    const uri = Math.random().toString(36).substring(7);
    let transferEvent = {};
    erc721Instance.on("Transfer", (from, to, tokenId) => {
      transferEvent = {
        from: from,
        to: to,
        tokenId: tokenId,
      };
    });
    await expect(
      erc721Instance.connect(accountOne).mint(seed, accountOne.address, uri)
    ).to.emit(erc721Instance, "Transfer");
    await waitUntil(() => transferEvent.tokenId !== undefined);
    const tokenId = transferEvent.tokenId.toHexString();
    let actualUri = await erc721Instance.tokenURI(tokenId);
    assert.equal(actualUri, uri, "URI is not correct");
  });
});
