import requests
import datetime
import winsound

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date='19-05-2021'
url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=673016&date={date}'
response = requests.get(url, headers=headers)
output=response.json()
age=output['centers'][0]['sessions'][1]['min_age_limit']
capacity=output['centers'][0]['sessions'][1]['available_capacity']
date=datetime.datetime.now() 

if int(capacity) > 0:
  winsound.Beep(500, 1000) #it will make a beep
print(f'{date}=> AGE:{age},capacity:{capacity}')