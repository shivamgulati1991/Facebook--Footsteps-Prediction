import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

#input data from train.csv and test.csv
def inputDataSet():
  train_data = pd.read_csv('train.csv',dtype={'x':np.float32,'y':np.float32,'accuracy':np.int16,'time':np.int,'place_id':np.int},index_col = 0)
  test_data = pd.read_csv('train.csv',dtype={'x':np.float32,'y':np.float32,'accuracy':np.int16,'time':np.int,'place_id':np.int},index_col = 0)
  return train_data, test_data

# processing dataset; removing the place_id that appear less than 3 times in train data to speed up computation and reduce the number of 
# output classes that we have; extracting Hours, Day, weekday, month from time.
def preprocessData(train_data):
  place_count = train_data.place_id.value_counts() 
  mask = place_count[train_data.place_id.values] > 500
  train_data = train_data.loc[mask.values]
  hour = []
  weekday = []
  month = []
  year = []
  day = []
  for i in train_data.time.values:
    hour.append((i/60)%24)
    weekday.append = ((i/(60*24))%7)
    month.append = (i/(60*24*30)) % 12 #month-ish
    year.append = i/(60*24*365)
    day.append = i/(60*24) % 365
  train_data['hour'] = hour
  train_data['weekday'] = weekday
  train_data['month'] = month
  train_data['year'] = year
  train_data['day'] = day
  train_data = train_data.drop('time', 1)
  return train_data

# def areadivision():

def main():
  train_data, test_data = inputDataSet()
  print len(train_data)
  train_data = preprocessData(train_data)
  print len(train_data)
  # train_data_1 = train_data.loc[(train_data['x']>5.0)&(train_data['x']<5.25)&(train_data['y']>5.0)&(train_data['y']<5.25)]
  # place_count = train_data_1.place_id.value_counts() 
  # mask = place_count[train_data_1.place_id.values] > 500
  # train_data_2 = train_data_1.loc[mask.values]
  # print len(train_data_2)



                
if __name__ == '__main__':
  main()