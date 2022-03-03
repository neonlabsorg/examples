// SPDX-License-Identifier: MIT

pragma solidity >=0.5.12;

// Default implementation of NEON's ERC20 wrapper contract
contract NeonERC20Wrapper {
    address constant NeonERC20 = 0xff00000000000000000000000000000000000001;

    string public name;
    string public symbol;
    bytes32 public tokenMint;

    constructor(bytes32 _tokenMint) {
        name = "Awesome Token";
        symbol = "AWST";
        tokenMint = _tokenMint;
    }

    fallback() external {
        bytes memory call_data = abi.encodePacked(tokenMint, msg.data);
        (bool success, bytes memory result) = NeonERC20.delegatecall(call_data);

        require(success, string(result));

        assembly {
            return(add(result, 0x20), mload(result))
        }
    }
}


