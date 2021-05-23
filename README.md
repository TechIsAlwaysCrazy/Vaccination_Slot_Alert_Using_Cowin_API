### Vaccination slot Alert based on District IDs
-------------------------------------------------------------------------------------


- Works with Python 3.6 and above.

```
 $ pip install requests argparse colorama
 $ python cowin_scripts.py --id id1,id2 (Using distric id or multiple ids)
```
- Arguments and Optional arguments.
```
 $ python cowin_scripts.py --id id1,id2 (Using distric id or multiple ids)
 $ python cowin_scripts.py --id id1,id2 -a min_age(it can be 18 or 45) & default is 18.
 $ python cowin_scripts.py --id id1,id2 -s sleep_time (Default is 10 second)
 $ python cowin_scripts.py --id id1 -d <customer start date dd-mm-yyyy/default is todays date) 
 $ python cowin_scripts.py --id 305,307 -s 15 -a 45 -d 24-05-2021 (Filtering data for 45 age groups with a duration of 15 and a default starting date)
 
```
- All argeuments except --id /-i are optional.
- Distric IDs can be fetch from cowin sites.
- It will beep if it identifies a slot & change the color of display (BLUE <10 and Green >10 capacities).
- This can be alter based on pin number as well ,refer cowin.py file here for clue .
- It will be usefull while you are working and dont need to watch your phone for alerts too.
  
 - It wont make any booking as obevious.
 - All credit and data accuracy goes to COWIN APIs.
