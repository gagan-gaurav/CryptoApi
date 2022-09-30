import json
from django.http import JsonResponse
from django.core import serializers
import requests


def cryptoApi(request):
	url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing"

	querystring = {"start":"1","limit":"1000","sortBy":"market_cap","sortType":"desc","convert":"USD,BTC,ETH","cryptoType":"all","tagType":"all","audited":"false","aux":"ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"}

	payload = ""
	headers = {
		"authority": "api.coinmarketcap.com",
		"accept": "application/json, text/plain, */*",
		"accept-language": "en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,pl;q=0.5",
		"cache-control": "no-cache",
		"dnt": "1",
		"origin": "https://coinmarketcap.com",
		"platform": "web",
		"referer": "https://coinmarketcap.com/",
		"sec-ch-ua": "^\^Chromium^^;v=^\^106^^, ^\^Google"
	}

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
	data = response.json()
	return JsonResponse({'body' : data, 'success' : True})