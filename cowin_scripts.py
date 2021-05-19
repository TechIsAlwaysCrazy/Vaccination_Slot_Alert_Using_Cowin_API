import requests
import datetime
import winsound

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date= datetime.date.today().strftime("%d-%m-%Y")
pin='673016'
url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={int(pin)}&date={date}'
response = requests.get(url, headers=headers)
output=response.json()
age=output['centers'][0]['sessions'][1]['min_age_limit'] #limitted to first value .it can be iterated if needed.
capacity=output['centers'][0]['sessions'][1]['available_capacity']
date_ref=datetime.datetime.now() 

if int(capacity) > 0:
  winsound.Beep(500, 1000) #it will make a beep
print(f'{date_ref}=> Range From :{date},Age:{age},capacity:{capacity}')
#while true; do python.exe cowin_scripts.py; sleep 100;done
