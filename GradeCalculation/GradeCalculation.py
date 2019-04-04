# Major: Information Technology
# Creation Date: 11/4/17
# Due Date: 11/6/17
# Course: Adv Scientific Programming
# Assignment: 4
# Filename: assignment4.py
# Purpose: To plot data using matplotlib, to exercise all concepts of matplotlib,
#           to manipulate data to show statistical results, to stylize
#           results to make it user understandable
#
# Run: ipython in directory of file -> %run ./assignment4 grades.csv
# Version: 1

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

#sources

# 1: understanding the different ways to plot graphs in same figure
#https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111

# 2: https://matplotlib.org/users/tight_layout_guide.html

if __name__ == '__main__':
    #check to make sure grades.csv is passed as cl argument
    if (len(sys.argv) != 2):
        print('Usage: [input CSV file]')
        sys.exit(0)

    #Create the blank figure for plotting
    # assigning to fig var seems to be the standard on most sources
    fig = plt.figure()

    # read the final grades into a numpy array
    final_grades = []
    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            final_grades.append(float(row[4]))
    final_grades = np.array(final_grades)
    
    #calculate mean and std dev of final_grades
    # obviously a distribution needs further calculation
    final_mean = np.mean(final_grades)
    final_stddev = np.std(final_grades)
    
    #create the formula for normal distribution curve
    #x value as shown in assignment formula
    #returns evenly spaced numbers between 0 and 100
    form_x = np.linspace(0, 100)
    
    #formula as given in assignment implemented in numpy
    # make sure parenthesis are all correct, if not, you will be very mad at yourself
    form_y = 1.0 / (final_stddev * np.sqrt(2 * np.pi)) * np.exp(-(form_x - final_mean) **2 / (2 * final_stddev **2))
    
    #Categorize all grades by letter
    ##testing in ipython
    #x = [100, 100, 92, 84, 99, 45, 56, 76, 77, 82, 89, 91]
    #
    #AGrade = [x for x in x if int(x) >= 90]
    #
    #AGrade
    #Out[3]: [100, 100, 92, 99, 91]
    #
    #AGrade = len(AGrade)
    #
    #AGrade
    #Out[5]: 5
    
    #seprate all grades by letter grade scale using list comprehension
    #using int(x) to cast to integer
    aGrade = [x for x in final_grades if int(x) >= 90]
    aGrade = len(aGrade) #show how many grades are A
    
    bGrade = [x for x in final_grades if int(x) >= 80 and int(x) <= 89]
    bGrade = len(bGrade) #show how many grades are B
    
    cGrade = [x for x in final_grades if int(x) >= 70 and int(x) <= 79]
    cGrade = len(cGrade) #show how many grades are C
    
    dGrade = [x for x in final_grades if int(x) >= 60 and int(x) <= 69]
    dGrade = len(dGrade) #show how many grades are D
    
    #else all grades lower than 60
    fGrade = [x for x in final_grades if int(x) < 60]
    fGrade = len(fGrade) #show how many grades are F
    
    ### histogram ###
    #subplot for histogram on top of bar graph
    # originally had 222, but figure had a very small width
    # 211 complements assignment diagram nicely
    # source 1, sort of
    plt.subplot(211)
    
    #define the number of bins as per assignment requirement
    # n_bins seems to the be the standard for defining this variable
    n_bins = 20
    
    #different styles found by print(plt.style.available) in ipython
    #use classic style to match assignment
    #plt.style.use('classic')
    
    #seaborn-talk adds different style bar lines
    plt.style.use('seaborn-talk')
    
    #for those who want that spooky feel
    #plt.style.use('dark_background')
    
    #create the histo
    # normed=True creates the y axis auto based off of numbers
    #n, bins, patches seems to be standard
    n, bins, patches = plt.hist(final_grades, n_bins, range=(0,100), normed=True)
    
    ######### Line Style 1 #########
    #plot the distribution line
    #want a randomly generated line, sure, why not
    plt.plot(form_x, form_y, color=(plt.cm.gist_ncar(np.random.random())), linewidth=2)
    
    ######### Style Option 1 #########
    #use a colormap to set histo bar colors
    # some of the diff colormaps below
    #https://matplotlib.org/tutorials/colors/colormaps.html
    cm = plt.cm.get_cmap('autumn')
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    #scale values
    #stylizing found here, thought it was too neat to not copy
    #https://stackoverflow.com/questions/23061657/plot-histogram-with-colors-taken-from-colormap
    col = bin_centers - min(bin_centers)
    col /= max(col)
    
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    
    ### axis ###
    #set the x values to match a scale of 0 to 100
    plt.xticks(np.arange(0,110,10))
    
    ### title ###
    #set the title of the histo
    plt.title('Grade Distribution')
    
    ### labels ###
    #label the x axis
    plt.xlabel('Numeric Grade\n')
    #label the y axis
    plt.ylabel('Probability')
    
    ### bar graph ###
    #subplot for horizontal bar graph on bottom of histogram ###
    #subplot 212 creates a replica of 211, just on the bottom
    plt.subplot(212)
    
    #define the letter grades
    # however, must define them backwards in order to have A start on top
    # this is not enough or data won't match grade letters, change y_grades
    lgrades = ('F', 'D', 'C', 'B', 'A')
    
    #set the bounds of the y-axis based off how many letter grades exist
    #this does not set the y-axis to the letters, if just determines the amount
    # and makes an array of that amount
    y_axis = np.arange(len(lgrades))
    
    #now to bring those calculated letter grades from list comprehension to here
    #setting grades in descending order in order to start with A
    y_grades = [fGrade, dGrade, cGrade, bGrade, aGrade]
    
    #plot a horizontal bar graph
    #output the y-axis length (5), assign letter grades (ABCDF)
    # align='center' will put appropriate padding on the top and bottom of graph
    f,d,c,b,a = plt.barh(y_axis, y_grades, align='center')
    
    #set colors to appropriate letter grade colors, if that makes sense
    a.set_facecolor('navy') #dark green
    b.set_facecolor('yellowgreen') #yellowgreen
    c.set_facecolor('yellow') #yellow
    d.set_facecolor('orange') #orange
    f.set_facecolor('red') #red
    
    ### axis ###
    #plot the y axis based off how many letter grades there are and what their
    #       corresponding letter grade is
    plt.yticks(y_axis, lgrades)
    
    
    ### title ###
    #set the title of the bar
    plt.title('Letter Grades')
    
    ### labels ###
    #label the x axis
    plt.xlabel('Number of Students')
    #label the y axis
    plt.ylabel('Grades')
    
    #if you're wondering why it looks like trash, it's because you forgot this
    #source 2
    fig.tight_layout()
    
    #show everything onto the figure, without thise you'd cry
    plt.show()
