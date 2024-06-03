"""
@author: James Sweetsir
"""

import requests

url = "https://finance.yahoo.com/quote/AAPL/"

response = requests.get(url)

print(response)
print("HTML Status Code is " + str(response.status_code))

if response.status_code == 200:
    text = response.text

    ind = text.find("Previous Close")
    
    if ind != -1:
        start_index = text.find('value="', ind) + len('value="')
        end_index = text.find('"', start_index)
        val = text[start_index:end_index]
        print("Previous Close value is " + val)
    else:
        print("Property not found in the HTML content.")
else:
    print("Failed to retrieve the webpage.")
