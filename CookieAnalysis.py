#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)
            
    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    t_mean = np.mean(times)
    t_std = np.std(times)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    title = "Data Visualization"
                
    # make Nmeas figure
    plt.figure()
    plt.hist(times, Nmeas+1, density=True, facecolor='b', alpha=0.5)
    plt.axvline(x=t_mean, linewidth=4, color='r')
    plt.axvline(x=t_mean+t_std, linewidth=4, color='g')
    plt.axvline(x=t_mean-t_std, linewidth=4, color='g')
    plt.annotate('t_avg', (t_avg,-.5), annotation_clip=False, color='r')
    #plt.hist(times_avg, Nmeas+1, density=True, facecolor='g', alpha=0.5)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title)
    plt.grid(True)

    plt.show()
