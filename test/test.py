from datetime import time

x = 0.9166666666666666 # a float
x = int(x * 24 * 3600) # convert to number of seconds
my_time = time(x//3600, (x%3600)//60, x%60) # hours, minutes, seconds

print ("%.2d:%.2d" %(my_time.hour, my_time.minute))