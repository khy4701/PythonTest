
from _ctypes import Structure
from ctypes import c_long, c_uint8
import ctypes
import json
import pprint
import sched
import threading
import time

from enum import Enum

class PeriodicScheduler(threading.Thread):                                                  
    def __init__(self):    
        super(PeriodicScheduler,self).__init__()
                                                       
        self.scheduler = sched.scheduler(time.time, time.sleep)
           
        INTERVAL = 1 # every second
        self.setup(INTERVAL, periodic_event) # it executes the event just once  
                                                                            
    def setup(self, interval, action, actionargs=()):                             
        action(*actionargs)                                                       
        self.scheduler.enter(interval, 1, self.setup,                             
                        (interval, action, actionargs))                           
                                                                        
    def run(self):                                                                
        self.scheduler.run()


# This is the event to execute every time  

list = ['1','2','3']
def periodic_event():

    print len(list)
    print list    
    list[:] = []
    print len(list)

periodic_scheduler = PeriodicScheduler()
periodic_scheduler.start()

print '22222222222222'

