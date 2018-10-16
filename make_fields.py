# get fields and sav to csv file
import sys
import os.path as op
import csv
#import numpy as np

if len(sys.argv)!=2:
    print('Usage:',sys.argv[0],'<csv filename>')
    sys.exit(2)

# source csv file
sname=sys.argv[1]

# target csv file
fp=op.split(sname)
tname=fp[0]+'/new_'+fp[1]

PU_Time = ('Pickup_date','Pickup_DateTime','pickup_datetime','lpep_pickup_datetime','Trip_Pickup_DateTime','tpep_pickup_datetime')
DO_Time = ('DropOff_datetime','dropoff_datetime','Lpep_dropoff_datetime','lpep_dropoff_datetime','Trip_Dropoff_DateTime','tpep_dropoff_datetime')
Trip_Distance = ('Trip_distance','trip_distance','Trip_Distance')
Rate_Code = ('rate_code','RateCodeID','Rate_Code','RatecodeID')
PU_Lon = ('Pickup_longitude','Start_Lon','pickup_longitude')
PU_Lat = ('Pickup_latitude','Start_Lat','pickup_latitude')
DO_Lon = ('Dropoff_longitude','End_Lon','dropoff_longitude')
DO_Lat = ('Dropoff_latitude','End_Lat','dropoff_latitude')
Fare_Amt = ('Fare_amount','fare_amount','Fare_Amt')
Extra = ('Extra','extra','surcharge')
Tip_Amt = ('Tip_amount','tip_amount','Tip_Amt')
PULocationID = ('PULocationID')
DOLocationID = ('DOLocationID')

cols = [PU_Time,DO_Time,Trip_Distance,Rate_Code,PU_Lon,PU_Lat,DO_Lon,DO_Lat,
        Fare_Amt,Extra,Tip_Amt,PULocationID,DOLocationID]

col_names = ['PU_Time','DO_Time','Trip_Distance','Rate_Code','PU_Lon','PU_Lat','DO_Lon','DO_Lat',
             'Fare_Amt','Extra','Tip_Amt','PULocationID','DOLocationID']

nr=0    # number of records

with open(sname,'r') as sf, open(tname,'w') as tf:
    reader=csv.reader(sf)
    writer=csv.writer(tf)
    
    # read header
    row=next(reader)
    nf=len(row)   # number of fileds
    scols=[]      # keep wanted column index
    scol_names=[] # keep new column names
    
    ncols = len(cols)
    for i in range(0,nf): # get each column name
        for j in range(0,ncols): # get each cols element
            if row[i] in cols[j]: # check if the column has data we want
                scols+=[i]
                scol_names+=[col_names[j]]
                
                # remove element already checked
                del cols[j]
                del col_names[j]
                
                # re-count number of columns
                ncols = len(cols)
                break
    
    writer.writerow(scol_names)
    
    # process data
    for row in reader:
        data=list( row[i] for i in scols)
        writer.writerow(data)
        nr+=1
        not nr%10000 and print('.',end=' ',flush=True)

    print('\n')
    
    