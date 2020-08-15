 from collections import Counter
 import csv
with open('height-weight.csv', newline='') as f:
	reader = csv.reader(f)
	file_data = list(reader)

	


 file_data.pop(0)
['ï»¿Index', 'Height(Inches)', 'Weight(Pounds)']
 new_data=[]

for i in range(len(file_data)):
	n_num = file_data[i][1]

	new_data.append(float(n_num))

     
 n=len(new_data)
 total=0
 for x in new_data:
	total+=x

	
 mean=total/n
 print("mean = "+str(mean))
mean = 67.99311359679979
 median_data=[]
 for i in range(len(file_data)):
	n_num = file_data[i][1]

	median_data.append(float(n_num))

	
 n=len(median_data)
 median_data.sort()
 if n % 2 ==0:
	i%2 ==0:
    if n % 2 ==0:
	median1 = float(median_data[n//2])
	median2 = float(median_data[n//2 -1])
	median = (median1+median2)/2
else:
	median = median_data[n//2]
	print(n)

	
 print("Median is:" +str(median))
Median is:67.9957
 mode_data = []
 for i in range(len(file_data)):
	n_num = file_data[i][1]

	mode_data.append(float(n_num))

	
 data = Counter(mode_data)
 mode_data_for_range = {}
 mode_data_for_range = {}
mode_data_for_range = {
	                     "50-60":0,
			     "60-70":0,
			     "70-80":0
			     }
 for height,occurrence in data.items():
	if 50<float(height)<60:
		mode_data_for_range["50-60"] += occurrence
	elif 60<float(height)<70:
		mode_data_for_range["60-70"]+= occurrence
	elif 70<float(height)<80:
		mode_data_for_range["70-80"]+= occurrence

 mode_range,mode_occurrence=0,0
 for range,occurrence in mode_data_for_data.item():
	if occurrence > mode_occurrence:
		mode_range,mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence