import requests
import json
from datetime import datetime


id = '-'*10
country = input('Please enter a continent: ')

city = input("Please enter a city: ")




def call_offset(country,city):
  key ='Your Key Here'
  url = f'http://api.timezonedb.com/v2.1/get-time-zone?key={key}&format=json&by=zone&zone={country}/{city}'
  r = requests.get(url)
  response= r.json()
  print(response)
  tz = response['zoneName']
  gmt_offset = response['gmtOffset']
  return gmt_offset/3600,tz


    
  


offset,tz = call_offset(country,city)
neg = False
if offset<0:
  neg = True
else:
  neg = False




class Time:
  def __init__(self,utc_now):
    
    self.year = int(utc_now[0:3])
    self.month = int(utc_now[5:7])
    self.day = int(utc_now[8:10])
    self.hour = int(utc_now[11:13])
    self.min = int(utc_now[14:16])
    self.sec = round(float(utc_now[17:]))
    print(f'UTC TIME: \nDay: {self.day} Hours: {self.hour} Minutes: {self.min}\n')
    

  def addOffset(self,offset,offset_minutes,neg):
    offset_minutes = int(round(offset_minutes*60))
    print(f'The offset is Hour: {offset} h and {offset_minutes} m\n')
    if offset_minutes == 0:
      if neg == True:
        self.hour = int(self.hour - offset)
      else:
        self.hour = int(self.hour+ offset)
    else:
      if neg == True:
        self.hour = int(self.hour - offset )
        self.min = int(self.min + offset_minutes)
        print(self.hour)
        if self.min >= 60:
          self.min= self.min - 60
          self.hour = self.hour +1
      else:
        self.hour = int(self.hour + offset )
        self.min = int(self.min + offset_minutes)
        if self.min >= 60:
          self.min= self.min - 60
          self.hour = self.hour +1

        
        if self.min >= 60:
          self.min-=60
          self.hour = self.hour +1
    
    if self.hour > 24:
      self.hour -= 24
      self.day = self.day + 1
    else:
      self.day = self.day

"""offset_time = "-11:00"
offset_minutes = int(offset_time[4:6])
offset = int(offset_time[1:3])

if offset_minutes == 0:
  pass
else:
  offset_minutes = round(offset_minutes/60,2)"""
  
  
  
  



offset_minutes = round(offset % 1,2)
offset = int(offset - offset_minutes)


utc_current_time = Time(str(datetime.utcnow()))
utc_current_time.addOffset(offset,offset_minutes,neg)
local_day = utc_current_time.day
local_hour = utc_current_time.hour
local_min = utc_current_time.min


if local_hour >11:
  am_pm = 'pm'
  if local_hour > 12:
    local_hour = local_hour-12
else:
  am_pm = 'am'


if local_hour <0:
  am_pm = 'pm'
  local_day = local_day - 1
  local_hour = local_hour*-1
  

if local_hour == 0:
  local_hour = 12


print(f'Its currently \n\nDate: {local_day} Time: {local_hour}:{local_min} {am_pm} at {city}')
  
