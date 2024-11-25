import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

# Defining the credentials
class Credentials:
    consumer_key = 'rFKrBKqIDaxgSQXLG9AICb4HqY1ay8nNISfxzUgLPcE9pHpu'
    consumer_secret = 'B3oejElg4hqmIA1vcKDsnxOJrnpXlGkzAcL5q8R5pQqHLAFBjBqXg51Tiommh6LB'
    apiurl = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

# Generating the token
class AccessToken:
    request = requests.get(Credentials.apiurl, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    access_token = json.loads(request.text)['access_token']

# Handling password
class Password:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = '174379'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    to_encode = shortcode + passkey + timestamp
    encoded_password = base64.b64encode(to_encode.encode())
    decoded_password = encoded_password.decode('utf-8')