import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

headers = {
    'User-Agent': user_agent
}


api_key = 'AVAILABLE_IN_THE_CHAT'
secret  = 'AVAILABLE_IN_THE_CHAT'

url = 'https://api.guesty.com/api/v2/reservations';

data={
"filters":[{"field":"status", "operator":"$in", "value":["canceled"]}],
"limit":26
}

response = requests.get(url, headers=headers, 
                        auth=(api_key, secret),
                        json= data )

print(response, response.text )