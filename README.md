1. Install Brownie

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip
```bash
pip install eth-brownie
```

2. Clone this
```bash
git clone https://github.com/PatrickAlphaC/brownie_simple_storage
cd brownie_simple_storage
```
3. Add your metamask to the brownie accounts at the `0` index

```bash
brownie accounts new 0
```
You'll be prompted to add your private key:
`0xa5555555555555a09215803a6b540f1e054797eeda2eec6d49076760d48e7589`
And a password, and you can see your new added account with `brownie accounts list`

Or, export your `PRIVATE_KEY` as an environment variable, and uncomment the line:
```python
# account = accounts.add(config["wallets"]["from_key"])
```
and comment the line:
```python
account = accounts[0]
```

4. Testing

```bash
brownie run test
```

5. Running scripts

```bash
brownie run scripts/deploy.py
```

6. Deploy to a testnet

Add your `WEB3_INFURA_PROJECT_ID` from [Infura](https://infura.io/) to your `.env` and run 
```bash
source .env
``` 
To set your environment variable. You can check you've done it correctly with:
```bash
echo $WEB3_INFURA_PROJECT_ID
```
Change the `deploy_simple_storage` function in `deploy.py` to look like:
```
account = accounts.add(config["wallets"]["from_key"])
# account = accounts.load("id")
# account = accounts[0]
```

Then run:
```
brownie run scripts/deploy.py --network rinkeby
```

Make sure you have some testnet ETH. You can find faucets in the [Chainlink Documenatation](https://docs.chain.link/docs/link-token-contracts/)


