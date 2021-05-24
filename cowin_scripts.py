import requests
import datetime
import winsound
import argparse
import time
import colorama
from colorama import Fore, Back, Style

def print_details(date,dist_id,center_name,min_age_limit,available_capacity,available_capacity_detailed,center_address,beep):
  if available_capacity == 0:
    print(f'=> Date:{date}|distric_id:{dist_id}|Center:{center_name}|Age:{min_age_limit}|Capacity:{available_capacity}|Dose:{available_capacity_detailed}|Address:{center_address}')
    return None
  elif available_capacity >10:
    if beep == "on":
      winsound.Beep(400, 2000) #it will make a beep
    print(f'{Back.MAGENTA}=> Date:{date}|distric_id:{dist_id}|Center:{center_name}|Age:{min_age_limit}|Capacity:{available_capacity}|Dose:{available_capacity_detailed}|Address:{center_address}{Style.RESET_ALL}')
  else:
    if beep == "on":
      winsound.Beep(600, 2000) #it will make a beep
    print(f'{Back.BLUE}=> Date:{date}|distric_id:{dist_id}|Center:{center_name}|Age:{min_age_limit}|Capacity:{available_capacity}|Dose:{available_capacity_detailed}|Address:{center_address}{Style.RESET_ALL}')
  

def action(date,ids,age,dose,mode,beep):
  try:
    if mode == "districts":
      url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={ids}&date={date}'
    else:
      url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={ids}&date={date}'
    response = requests.get(url, headers=headers,timeout = 5)
    output=response.json()
    
    for centers in output['centers']:
      center_name=centers['name']
      center_address=centers['address']
      for session in centers['sessions']:
        min_age_limit=session['min_age_limit']
        date=session['date']
        if dose == 0:
          available_capacity=session['available_capacity']
          dose1_slots=session['available_capacity_dose1']
          dose2_slots=session['available_capacity_dose2']
          available_capacity_detailed=f"Dose1-{dose1_slots}/Dose2-{dose2_slots}"
        else:
          available_capacity=session[f'available_capacity_dose{dose}']
          available_capacity_detailed=f"Dose{dose}-{available_capacity}"
        if int(min_age_limit) == age:
          print_details(date,ids,center_name,min_age_limit,available_capacity,available_capacity_detailed,center_address,beep)
  except Exception as e:
    
    print("Exception " + str(e))

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
}
date= datetime.date.today().strftime("%d-%m-%Y")
parser = argparse.ArgumentParser()
parser.add_argument('-i','--id',type=str, help='Dsitrict IDs or Pin numbers', required=True)
parser.add_argument('-d','--date',type=str,help='Custom start date',default=date)
parser.add_argument('-a','--age',type=int,help="Minimum age",choices=[18,45],default=18)
parser.add_argument('-s','--sleep',type=int,help="Slpping time/default is 5sec",default=15)
parser.add_argument('-v','--vdose',type=int,help="Vaccine dose 1 or 2",default=0,choices=[0,1,2])
parser.add_argument('-b','--beep',type=str,help="Make Beep on /off",choices=["on","off"],default="on")
parser.add_argument('-m','--mode',type=str,help="Select the mode as pin(default) or district",required=True,choices=["pin","districts"])
args = parser.parse_args()
colorama.init()

try:
  while True:
    for id in args.id.split(","):
      action(args.date,int(id),args.age,args.vdose,args.mode,args.beep)
    date_ref=datetime.datetime.now()
    print(f'-------Current Date - {date_ref}------Slots Starting From - {args.date}----------Beep:{args.beep.upper()}------------Delay:{args.sleep}s-----------------')
    time.sleep(args.sleep)
except KeyboardInterrupt:
    pass

