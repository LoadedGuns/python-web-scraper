"""
@author: James Sweetsir
"""

import requests

url = "https://finance.yahoo.com/quote/AAPL/"

prop = "Previous Close"

response = requests.get(url)

print(response)
print("HTML Status Code is " + str(response.status_code))
text = response.text

ind = text.index("Previous Close")

redText = text[ind:].split("</span>")[1]
val = redText.split(">")[-1]
print(val)