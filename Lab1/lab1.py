#CSCD 388 - Lab 1
#Matthew Teears

#Declare Imports
import statistics


#Define the list
list = [1,2,3,4,5,6,7,8,9,10]

#Define zeroed variables
nobj = 0
sum = 0
index = 0
var_sum = 0
diff = []
std_dev = 0;
#Print initial list
print("The list consists of : ", list)

#Count the number of objects in the list
for x in list:
    nobj = nobj + 1
#Print the number of objects in the list
print("nobj : ",nobj)

#Sum up the list
for x in list:
    sum = sum + x
#Print the sum of the list
print("sum  : ", sum)

#Compute the average
avg = sum/nobj
#print the average
print("avg  : ", avg)

#compute the variance using statistics library
var1 = statistics.variance(list)
print("var1 : ", var1)

#compute variance using code
#compute mean difference squared
for x in list:
    diff.append((x - avg)**2)
#sum differenes
for d in diff:
    var_sum = var_sum + d
#divide by n-1 for sample
var2 = var_sum/(nobj-1)
#print variance
print("var2 : ",var2)

#compute standard deviation
std_dev = var2**(1/2)
#print std deviation
print("std  : ",std_dev)

#find minimum values
min = min(list)
#print minimum
print("min  : ",min)

#find maximum values
max = max(list)
#print max
print("max  : ",max)

#find range of data
range = max - min
#print range
print("rng  : ",range)

#find confidence interval
conf_low = avg - 1.96*std_dev
conf_high = avg + 1.96*std_dev
print("( {0} , {1} ) Should contain about 95% of the data.".format(conf_low, conf_high))