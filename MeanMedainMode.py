import csv
import pandas as pd
import statistics
from collections import Counter

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
     n_num = file_data[i][1]
     new_data.append(float(n_num)) 

n= len(new_data)
total = 0
for x in new_data:
    total+=x

mean = total/n
print("Mean/Average is:"+ str(mean))       

new_median = []
for i in range(len(file_data)):
     n_median = file_data[i][1]
     new_median.append(float(n_median)) 

median = len(n_num)
n_median.sort()
  
if n % 2 == 0:
    median1 = n_median[n//2]
    median2 = n_median[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_median[n//2]
print("Median is: " + str(median))

new_mode = []

for i in range(len(file_data)):
     n_mode = file_data[i][1]
     new_mode.append(float(n_mode))
mode = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)