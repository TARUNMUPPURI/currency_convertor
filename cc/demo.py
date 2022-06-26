import requests
import json

import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
currency1="INR"
currency2="USD"
amount=52000

querystring = {"from":currency1,"to":currency2,"amount":amount}

headers = {
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
	"X-RapidAPI-Key": "b022c4fd5amsh73faf2ccf34da4cp191936jsn646f45722843"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#print(response.text)
data=json.loads(response.text)
converted_amount=data["result"]["convertedAmount"]
formatted="{:,.2f}".format(converted_amount)
print(formatted)
