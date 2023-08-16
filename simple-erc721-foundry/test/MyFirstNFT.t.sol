// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.21;

import {Test, console2} from "forge-std/Test.sol";
import {MyFirstNFT} from "../src/MyFirstNFT.sol";

contract MyFirstNFTTest is Test {
    MyFirstNFT token;

    address alice = vm.addr(0x1);

    function setUp() public {
        token = new MyFirstNFT();
    }

    function testName() external {
        assertEq("MyFirstNFT", token.name());
    }

    function testSymbol() external {
        assertEq("FNFT", token.symbol());
    }

    function testMint() public {
        token.safeMint(alice, "https://apricot-official-sailfish-923.mypinata.cloud/ipfs/QmRsP8VDyPZ54xC3FXJqAtZpBTW8CXQmHUsvJEbc5q7vKG");
        assertEq("https://apricot-official-sailfish-923.mypinata.cloud/ipfs/QmRsP8VDyPZ54xC3FXJqAtZpBTW8CXQmHUsvJEbc5q7vKG", token.tokenURI(0));
    }
}
