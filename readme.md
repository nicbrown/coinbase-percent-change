# Coinbase Percentage Change Tracker

This script is designed to query against an active coinbase account with the API enabled. The script will query your account obtaining the amount of each crypto currency that you've bought. This is then compared against the current sell value of the same currency for the amount you have. The percentage change is then outputted.

## Prequisites
* Python2.7
* Coinbase Python Library
	* pip install coinbase OR
	* easy_install coinbase
* Set the following envrionment variables
	* COINBASE_KEY -> coinbase API key
	* COINBASE_SECRET -> coinbase API secret
* Minimum Coinbase API access
	* Wallets that you want to compare (BTC, LTE, ETH)
	* wallet:accounts:read 
	* wallet:buys:read 
	* wallet:checkouts:read 
	* wallet:deposits:read 
	* wallet:sells:read 
	* wallet:withdrawals:read

## How to run it 
```javascript
$ python calculate_change.py

```