# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 01:07:53 2023

@author: juLeena
"""
import datetime
import pymongo
import json

def load_db():
    client = pymongo.MongoClient("mongodb://hehehaha:hehehaha14@3.38.118.228:27017")

    db=client.get_database("moodmemo")
    
    return db

def store_data(db):
    prev_time=datetime.datetime(2023, 6, 23)
    pres_time=datetime.datetime.now() - datetime.timedelta(hours=9) #UTC로 변경
    #print(pres_time)
    json_object={
                'daily_stamp_total':{},
                'stamp_time':{},
                'time_daily_stamp_total':{
                                            '00-02':{},
                                            '03-08':{},
                                            '09-10':{},
                                            '11-12':{},
                                            '13-14':{},
                                            '15-18':{},
                                            '19-21':{},
                                            '22-22':{},
                                            '23-23':{}
                                        },
                
                }
    #start storing total daily stamp
    for item in db.stamps.find({"dateTime":{"$gt":prev_time,"$lte":pres_time}}):
        stamp_time=(item['dateTime']+datetime.timedelta(hours=9)).strftime("%y-%m-%d")
        if stamp_time not in json_object['daily_stamp_total']:
            json_object['daily_stamp_total'][stamp_time]=1
        else:
            json_object['daily_stamp_total'][stamp_time]+=1
    #end storing total daily stamp
    
    #start storing total daily stamp
    for item in db.stamps.find({"dateTime":{"$gt":prev_time,"$lte":pres_time}}):
        stamp_time=(item['dateTime']+datetime.timedelta(hours=9)).strftime("%H")
        if stamp_time not in json_object['stamp_time']:
            json_object['stamp_time'][stamp_time]=1
        else:
            json_object['stamp_time'][stamp_time]+=1
    #end storing total daily stamp
    
    #start storing total daily stamp
    L=[['00','02'],['03','08'],['09','10'],['11','12'],['13','14'],['15','18'],['19','21'],['22','22'],['23','23']]
    for i in range(len(L)):
        start=L[i][0]
        end=L[i][1]
        json_object2={'%s'%(prev_time+datetime.timedelta(days=i)).strftime("%y-%m-%d"):0 for i in range((pres_time+datetime.timedelta(hours=9)-prev_time).days+1)}
        for item in db.stamps.find({"dateTime":{"$gt":prev_time,"$lte":pres_time}}):
            stamp_date=(item['dateTime']+datetime.timedelta(hours=9)).strftime("%y-%m-%d")
            stamp_time=(item['dateTime']+datetime.timedelta(hours=9)).strftime("%H")
            if start<=stamp_time<=end:
                json_object2[stamp_date]+=1
        json_object['time_daily_stamp_total'][start+'-'+end]=json_object2
    #end storing total daily stamp
    
    #TODO : 그 외 다른 통계들 추가하기
    
    json_object2 = json.dumps(json_object,sort_keys=True, default=str)
    with open('index.json', 'w') as f:
        json.dump(json_object2, f)