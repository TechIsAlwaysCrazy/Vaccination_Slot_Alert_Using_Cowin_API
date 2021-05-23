import requests
import datetime
import winsound
import argparse
import msvcrt
import time
import colorama
from colorama import Fore, Back, Style

def print_details(date_ref,date,dist_id,center_name,min_age_limit,available_capacity,available_capacity_detailed,center_address):
  if available_capacity ==0:
    print(f'{date_ref}=> Range From :{date},distric_id:{dist_id} Center:{center_name} ,Age:{min_age_limit},Capacity:{available_capacity},Dose:{available_capacity_detailed},Address:{center_address}')
  elif available_capacity >10:
    winsound.Beep(400, 2000) #it will make a beep
    print(f'{Back.GREEN}{date_ref}=> Range From :{date},distric_id:{dist_id} Center:{center_name} ,Age:{min_age_limit},Capacity:{available_capacity},Dose:{available_capacity_detailed},Address:{center_address}{Style.RESET_ALL}')
  else:
    winsound.Beep(600, 2000) #it will make a beep
    print(f'{Back.GREEN}{date_ref}=> Range From :{date},distric_id:{dist_id} Center:{center_name} ,Age:{min_age_limit},Capacity:{available_capacity},Dose:{available_capacity_detailed},Address:{center_address}{Style.RESET_ALL}')
  

def action(date,dist_id,age,dose):
  try:
    
    url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={dist_id}&date={date}'
    response = requests.get(url, headers=headers,timeout = 5)
    output=response.json()
    date_ref=datetime.datetime.now()
    for centers in output['centers']:
      center_name=centers['name']
      center_address=centers['address']
      for session in centers['sessions']:
        min_age_limit=session['min_age_limit']
        if dose == 0:
          available_capacity=session['available_capacity']
          dose1_slots=session['available_capacity_dose1']
          dose2_slots=session['available_capacity_dose2']
          available_capacity_detailed=f"Dose1-{dose1_slots}/Dose2-{dose2_slots}"
        else:
          available_capacity=session[f'available_capacity_dose{dose}']
          available_capacity_detailed=f"Dose{dose}-{available_capacity}"
        if int(min_age_limit) == age:
          print_details(date_ref,date,dist_id,center_name,min_age_limit,available_capacity,available_capacity_detailed,center_address)
  except Exception as e:
    
    print("Exception " + str(e))

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date= datetime.date.today().strftime("%d-%m-%Y")
parser = argparse.ArgumentParser()
parser.add_argument('-i','--id',type=str, help='Dsitrict ID', required=True)
parser.add_argument('-d','--date',type=str,help='Custom start date',default=date)
parser.add_argument('-a','--age',type=int,help="Minimum age",choices=[18,45],default=18)
parser.add_argument('-s','--sleep',type=int,help="Slpping time/default is 5sec",default=15)
parser.add_argument('-v','--vdose',type=int,help="Vaccine dose 1 or 2",default=0,choices=[0,1,2])
args = parser.parse_args()
colorama.init()
try:
  while True:
    for id in args.id.split(","):
      action(args.date,int(id),args.age,args.vdose)
    time.sleep(args.sleep)
except KeyboardInterrupt:
    pass



#####USAGE python cowin_scripts.py --id <id of the district or multiple ids seperated by comma> -a <Age/Optional and default is 18> -d <dd-mm-yy/optioanl/default is today's date>.#########
