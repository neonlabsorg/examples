# Example deploying ERC20 to Neonlabs devnet using Truffle

## Cloning repository
Run command
```sh
git clone https://github.com/neonlabsorg/examples.git
```

**NOTE** All the next operations must be performed from the **examples/simple-erc20-truffle** directory

## Installing requirements

1. Install truffle
```sh
npm i truffle
```
2. Install requirements

```sh
npm i
```

## Compiling and deploying contract

1. Compiling contract
```sh
truffle compile
```
3. Deploying contract
```sh
truffle migrate --network neonlabs
```

## ...Try it with your own contract and have fun!
