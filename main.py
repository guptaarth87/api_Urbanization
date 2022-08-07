from flask import Flask
from flask import Blueprint
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import linear_model

import numpy as np
import sklearn
import pandas as pd
from data_constants import urbanised_dataset,rural_dataset,development_ratio_list

data_bp = Blueprint('data', __name__)
country_name=Blueprint('country_name',__name__)
urbanData=Blueprint('urbanData',__name__)
ruralData=Blueprint('ruralData',__name__)
developmentRatio=Blueprint('developmentRatio',__name__)
urbanised_dataByYear=Blueprint('urbanised_dataByYear',__name__)
rural_dataByYear=Blueprint('rural_dataByYear',__name__)
data_by_year=Blueprint('data_by_year',__name__)
countrydataBy_date=Blueprint('country_data_by_date',__name__)

predictions=Blueprint('predictions',__name__)

global df1
global df2
global data1,data2,dev_data
data1=urbanised_dataset
data2=rural_dataset
dev_data=development_ratio_list


df1= pd.read_csv("urban-and-rural-population.csv")
df2=df1
df2=df2.to_dict()
df1['Total_Population']=df1['Urban_population']+df1['Rural_population']
df1['Urban_Population_percentage']=(df1['Urban_population']/df1['Total_Population'])*100
df1['Rural_Population_percentage']=(df1['Rural_population']/df1['Total_Population'])*100


@data_bp.route('/data/',methods=['GET','POST'])
def get_data():
    return df2

@country_name.route('/countryNames/',methods=['GET','POST'])
def countyName():
  
    Country_list=df1['Country'].tolist()
    distinct_country_name=[]
    for con in Country_list:
      if con not in distinct_country_name:
        distinct_country_name.append(con)
      else:
        continue
    return {
        "Country_list":distinct_country_name,
        "total_countries":len(distinct_country_name),
        "status":200
    }

@urbanData.route('/UrbanData/',methods=['GET','POST'])
def urbandata():
   return{
    'response':data1,
    'status':200
   }


@ruralData.route('/ruralData/',methods=['GET','POST'])
def ruraldata():
   return{
    'response':data2,
    'status':200
   }


@developmentRatio.route('/developmentRatio/',methods=['GET','POST'])
def devdata():
   return{
    'response':dev_data,
    'status':200
   }

@urbanised_dataByYear.route('/urbanisedDataByYear/<int:year>/',methods=['GET', 'POST'])
def urban_data(year):
  #sorting by decreasing order with urban percentage
  if year<1960:
    year=1960
  year_for=year
  grouped_year=df1.groupby('Year')
  df_grouped_year=grouped_year.get_group(year_for)
  req_list_res=[]
  arranged_decreasingly_df=df_grouped_year.sort_values(by=['Urban_Population_percentage'],ascending=False)
  for row,rowser in arranged_decreasingly_df.iterrows():
     req_list_res.append({rowser['Country']:{'Urban_population':rowser['Urban_population'],'Code':rowser['Code'],'Year':rowser['Year'],'Rural_population':rowser['Rural_population'],'Total_Population':rowser['Total_Population'],'Urban_Population_percentage':rowser['Urban_Population_percentage']}})
  return {
    'sorted_urban_dataset':req_list_res,
    'status':200
  }

@rural_dataByYear.route('/ruralDataByYear/<int:year>/',methods=['GET', 'POST'])
def rural_data(year):
  if year<1960:
    year=1960
  year_for=year
  grouped_year=df1.groupby('Year')
  df_grouped_year=grouped_year.get_group(year_for)
  arranged_decreasingly_rural_df=df_grouped_year.sort_values(by=['Rural_Population_percentage'],ascending=False)
  
  req_list_res=[]
  for row,rowser in arranged_decreasingly_rural_df.iterrows():
     req_list_res.append({rowser['Country']:{'Urban_population':rowser['Urban_population'],'Code':rowser['Code'],'Year':rowser['Year'],'Rural_population':rowser['Rural_population'],'Total_Population':rowser['Total_Population'],'Rural_Population_percentage':rowser['Rural_Population_percentage']}})
  return {
    "sorted_rural_dataset":req_list_res,
    "status":200
    }

@countrydataBy_date.route('/dataByDate/<string:country>/<int:year1>/',methods=['GET', 'POST'])
def country_data_by_date(country,year1):
   country=country[0].capitalize()+country[1:]
   if year1<1960:
    year1=1960
   year_for=year1
   grouped_year=df1.groupby('Year')
   df_grouped_year=grouped_year.get_group(year_for)
   req_res={}
   for(row,row_ser) in df_grouped_year.iloc[:,:].iterrows():
     
      if row_ser['Country']==country:
        for i,k in row_ser.iteritems():
          req_res[i]=k
        
      else:
        continue
   if (req_res):
    return ({
      'response':req_res,
      'status':200
    })

@predictions.route('/predict/<string:country>',methods=['GET','POST'])
def predict_(country):
  country=country[0].capitalize()+country[1:]
  temp_df=df1[df1['Country']==country]
  machine_learning_dict={"Year":temp_df['Year'],"Urban_Population":temp_df['Urban_Population_percentage']}
  machine_learning_df=pd.DataFrame(machine_learning_dict)
  year=pd.DataFrame(machine_learning_df['Year'])
  population=pd.DataFrame(machine_learning_df['Urban_Population'])
  lm=linear_model.LinearRegression()
  model=lm.fit(year.iloc[40:,:],population.iloc[40:,:])
  score_=model.score(year,population)
  #predicting values
  X=([2021,2022,2023,2024,2025,2026,2027])
  X=pd.DataFrame(X)
  Y=model.predict(X)
  Y=pd.DataFrame(Y)
  df=pd.concat([X,Y], axis=1, keys=['YEARS','URBANISED_POP'])
  res=[]
  for i,j in df.iterrows():
     res.append({int(j['YEARS']):j['URBANISED_POP'][0]})
  return {
    'response':res,
    'model_score':score_,
    'status':200
  }



 
   


  




