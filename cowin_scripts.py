import requests
import datetime
import winsound
import argparse

def action(date,dist_id):
  try:
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={dist_id}&date={date}'
    response = requests.get(url, headers=headers)
    output=response.json()
    date_ref=datetime.datetime.now()
    for centers in output['centers']:
      center_name=centers['name']
      center_address=centers['address']
      for session in centers['sessions']:
        min_age_limit=session['min_age_limit']
        available_capacity=session['available_capacity']
        if int(min_age_limit) == 18:
          if int(available_capacity) > 0:
            winsound.Beep(400, 1000) #it will make a beep
          print(f'{date_ref}=> Range From :{date},distric_id:{dist_id} Center:{center_name} ,Age:{min_age_limit},Capacity:{available_capacity},Address:{center_address}')
  except Exception as e:
    print("Exception " + str(e))

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date= datetime.date.today().strftime("%d-%m-%Y")
parser = argparse.ArgumentParser()
parser.add_argument('-i','--id',type=int, help='Dsitrict ID', required=True)
args = parser.parse_args()
action(date,args.id)



