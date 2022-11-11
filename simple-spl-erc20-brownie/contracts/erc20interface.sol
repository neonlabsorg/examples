// SPDX-License-Identifier: MIT

pragma solidity >=0.4.22 <0.9.0;

interface IERC20ForSpl {
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Approval(address indexed owner, address indexed spender, uint256 amount);
    event ApprovalSolana(address indexed owner, bytes32 indexed spender, uint64 amount);
    event TransferSolana(address indexed from, bytes32 indexed to, uint64 amount);
    function mint(address to, uint256 amount) external;
    function findMintAccount() external pure returns (bytes32);
    function claim(bytes32 from, uint64 amount) external returns (bool);
    function transferSolana(bytes32 to, uint64 amount) external returns (bool);
    function approveSolana(bytes32 spender, uint64 amount) external returns (bool);
    function burnFrom(address from, uint256 amount) external returns (bool);
    function burn(uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function balanceOf(address who) external view returns (uint256);
    function totalSupply() external view returns (uint256);
    function decimals() external view returns (uint8);
    function symbol() external view returns (string memory);
    function name() external view returns (string memory);
    function tokenMint() external view returns (bytes32);
    function claimTo(bytes32 from, address to, uint64 amount) external returns (bool);
}