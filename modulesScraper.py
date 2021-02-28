import requests
import subprocess

print("Enter the URL you want to download the HTML for: ")

consInput = input()

url = consInput

r = requests.get(url, allow_redirects=True)

open('drdk.html', 'wb').write(r.content)