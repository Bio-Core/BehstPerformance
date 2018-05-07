import webbrowser 
import urllib
import requests
import urllib2
from time import time
import matplotlib.pyplot as plt

def main():
    list_of_times = []
    for i in range(0, 100):
        list_of_times.append(calculate_load_time())

    print(list_of_times)
    #plt.hist(list_of_times, 50, density=True, facecolor='g', alpha=0.75)
    #plt.show()
    

def calculate_load_time():

    url = "http://behst.hoffmanlab.org/"
    start_time = time()
    stream = urllib2.urlopen(url)
    output = stream.read()
    end_time = time()
    stream.close()
    return end_time-start_time


main()