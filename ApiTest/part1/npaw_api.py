import time
import requests
import urllib.parse
from hashlib import md5
from datetime import datetime, timedelta

# API Configuration
account_code = "/powerce"  # Do not remove the leading "/"
api_key = "AzZ7mGCbLTxprItPsExOmijMalOx9PxEovbQ9asP47baO2JRCEGZLQ34s4PbZB9E"
host = "https://api.npaw.com"

# Set TTL for token (1 year in milliseconds)
ttl_ms = 31536000000
expiration_time = int(round(time.time() * 1000)) + ttl_ms
dateToken = ('&dateToken=' + str(expiration_time))

# Calculate time range (last 6 hours)
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=6)

# Format timestamps for the API
start_date = start_time.strftime('%Y-%m-%d %H:%M:%S')
end_date = end_time.strftime('%Y-%m-%d %H:%M:%S')

# API Call Parameters
call_type = '/data?'  # This example is specific for /data?
fromDate = ('fromDate=' + str(urllib.parse.quote_plus(start_date)))  # First parameter must not have "&"
toDate = ('&toDate=' + str(urllib.parse.quote_plus(end_date)))
metrics = "&metrics=plays"  # Format: "&metrics=metric_code1,metric_code2,metric_code3..."
dimensions = "&dimensions=ip"
granularity = "&granularity=minute"  # Using minute granularity for 6-hour range

# Building the pre-final URL
pre_url = call_type + str(fromDate) + str(toDate) + metrics + dimensions + granularity + dateToken

# Token Generation
token_encrypt = md5(f"{account_code}{pre_url}{api_key}".encode('utf-8'))
token = token_encrypt.hexdigest()

# Building Final URL
final_url = f"{host}{account_code}{pre_url}&token={token}"

print(f"Request URL: {final_url}")  # Debug print

try:
    response = requests.get(final_url)
    print(f"Response status: {response.status_code}")  # Debug print
    print(f"Response content: {response.text[:500]}")  # Debug print (first 500 chars)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}") 