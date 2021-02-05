#https://github.com/nic-delhi/AarogyaSetu_Android
#atom


import requests

#contributors_url = 'https://api.github.com/repos/nic-delhi/AarogyaSetu_Android'
#contributors_url = 'https://api.github.com/repos/atom/flight-manual.atom.io'
contributors_url = 'https://api.github.com/nic-delhi/AarogyaSetu_Android/forks'


contributors = requests.get(contributors_url).json()
print (contributors)