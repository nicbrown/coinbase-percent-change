#! /usr/bin/python
from coinbase.wallet.client import Client
import os
import urllib2
import json

api_key = os.environ['COINBASE_KEY']
api_secret = os.environ['COINBASE_SECRET']

client = Client(api_key, api_secret, api_version='2017-05-19')

accounts = client.get_accounts()

running_buy = 0
running_sell = 0

for account in accounts['data']:

	# Generate the total amount of cash that is currently invested
	account_id = account['id']
	deposits = client.get_buys(account_id)
	withdrawls = client.get_sells(account_id)

	for deposit in deposits['data']:
		running_buy = running_buy + float(deposit['subtotal']['amount'])

	for withdrawl in withdrawls['data']:
		running_sell = running_sell + float(withdrawl['subtotal']['amount'])

	initial_total = running_buy - running_sell
	
	# Calculate how much of each currency currently have

	currency = account['balance']['currency']
	vc_balance = account['balance']['amount']
	#print "Total of cash investments  " + str(initial_total)
	#print "Virutal currency amount " + str(vc_balance) + ' ' + str(currency)

	response = urllib2.urlopen('https://api.coinbase.com/v2/exchange-rates?currency='+ str(currency))
	exchange_rates = json.load(response) 

	market_price = exchange_rates['data']['rates']['GBP']
	#print "market price " +str(market_price)



	current_value = float(market_price) * float(vc_balance)
	#print "current value " + str(current_value)

	precentage_change = 100 * (current_value - initial_total) / initial_total
	if precentage_change < 0:
		colour = 'red'
	else:
		colour = 'green'

	print currency + ' % change ' + str(round(precentage_change,2)) +' | color=' + colour