import requests
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date='19-05-2021'
url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=673016&date={date}'
response = requests.get(url, headers=headers)
print(response.text)