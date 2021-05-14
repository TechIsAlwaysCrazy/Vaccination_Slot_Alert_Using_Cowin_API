import requests
import argparse
import datetime


class cowin_api:
    def __init__(self):
        self.api_check="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public"
        self.date_formatted=f"{datetime.datetime.now():%d-%m-%Y}"
        
        
    def get_slot_today(self,district_id):
        try:
            url=f'{self.api_check}/findByDistrict?district_id={district_id}&date={self.date_formatted}'
            return url

        except Exception as e:
            print(e)

        return "Today slot"

    def get_weekly_slots(self,district_id):
        url=f'{self.api_check}/calendarByDistrict?district_id={district_id}&date={self.date_formatted}'
        return url
       

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--choice',choices=["today","week"], help='Select one of the option,today for todays slot and week for next seven days', required=True)
    parser.add_argument('-i','--id',type=int, help='District ID', required=True)
    #parser.add_argument('-a','--age',type=int,choices=["18","45"], help='Put an agelimit as minimum age for vaccination')
    args = parser.parse_args()
    api = cowin_api()
    if args.choice == "today":
        result=api.get_slot_today(args.id)
    else:
        result=api.get_weekly_slots(args.id)
    print("-----------OPEN BELOW URL In Your browser and check----------")
    print(result)
    

if __name__=="__main__":
    """A small effort to fetch the API URL
    - enable virtualenv after pip install -r requirements.txt
    - try with various options Eg: python .\cowin.py -c week -i 307
    """

    main()
    
