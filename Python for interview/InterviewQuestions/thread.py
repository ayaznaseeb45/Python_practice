# thread in python without using thread module
import time 

def task(name):
    print(f" {name} started")
    time.sleep(2)
    print(f"{name} completed")

task("task 1")
task("task 2") 
task("task 3") 