
# coding: utf-8

# # Assignment 3 - Building a Custom Visualization
# 
# ---
# 
# In this assignment you must choose one of the options presented below and submit a visual as well as your source code
# for peer grading. The details of how you solve the assignment are up to you, although your assignment must use matplotlib
# so that your peers can evaluate your work. The options differ in challenge level, but there are no grades associated with
# the challenge level you chose. However, your peers will be asked to ensure you at least met a minimum quality for a given
# technique in order to pass. Implement the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.
# 
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). [Sample-oriented task-driven
# visualizations: allowing users to make better, more confident decisions.]
# (https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf)
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems
# (pp. 571-580). ACM. ([video](https://www.youtube.com/watch?v=BI7GAs-va-Q))
# 
# 
# In this [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_
# Tasks.pdf) the authors describe the challenges users face when trying to make judgements about probabilistic data
# generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1).
# Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might
# be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is
# plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).
# 
# <br>
# <img src="readonly/Assignment3Fig1.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 1 from (Ferreira et al, 2014).</h4>
# 
# <br>
# 
# A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis
# values are most likely to be representative, because the confidence levels overlap and their distributions are different
# (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c)
# is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value.
# So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely
# below this value, or white if they contain this value.
# 
# 
# <br>
# <img src="readonly/Assignment3Fig2c.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  Figure 2c from (Ferreira et al. 2014). Note that the colorbar legend at the bottom
# as well as the arrows are not required in the assignment descriptions below.</h4>
# 
# <br>
# <br>
# 
# **Easiest option:** Implement the bar coloring as described above - a color scale with only three colors, (e.g. blue, white, and red).
# Assume the user provides the y axis value of interest as a parameter or variable.
# 
# 
# **Harder option:** Implement the bar coloring as described in the paper, where the color of the bar is actually based on the amount
# of data covered (e.g. a gradient ranging from dark blue for the distribution being certainly below this y-axis, to white if the value
# is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).
# 
# **Even Harder option:** Add interactivity to the above, which allows the user to click on the y axis to set the value of interest.
# The bar colors should change with respect to what value the user has selected.
# 
# **Hardest option:** Allow the user to interactively set a range of y values they are interested in, and recolor based on this
# (e.g. a y-axis band, see the paper for more details).
# 
# ---
# 
# *Note: The data given for this assignment is not the same as the data used in the article and as a
# result the visualizations may look a little different.*

# In[34]:

#get_ipython().magic('matplotlib notebook')
import scipy.stats as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])

dft = df.transpose()  # Transpose df and creates a new df (dft) with its values
dftg = dft.describe()  # Create a new df (dftg) with the info obtained by dft

# Gradient color Blue-Red (Dark Blue, royal blue, deep sky blue, light blue, White, pink, Coral, Red, Firebrick, Dark Red)
gmap = [(0, 0, 0.545),
        (0, 0, 1),
        (0.254, 0.412, 0.882),
        (0, 0.749, 1),
        (0.678, 0.847, 0.902),
        (1, 1, 1),
        (1, 0.752, 0.8),
        (1, 0.498, 0.314),
        (1, 0, 0),
        (0.698, 0.133, 0.133),
        (0.545, 0, 0)]


#Creates first graph before entering the function 'onclick'
print ('Please click with the mouse on the graph to select the y-axis value')
yerr = (1.96 * (dftg.loc['std'] / (math.sqrt(3650)))) #Calculates the 95% confidece interval
plt.bar(df.index, dftg.loc['mean'], width=1, color=('w', 'w', 'w', 'w'), alpha=1, yerr=yerr, capsize=7,edgecolor='k') # Creates the plot
plt.xticks(df.index, ('1992', '1993', '1994', '1995'))  # Sets a new x-axys label
plt.xlim(1990.8, 1996.2)  # Sets the x-axis range
plt.axes().xaxis.set_ticks_position('none')  # Removes ticks from x-axis
plt.xlabel('Year')
plt.ylim(0, 60000)



def onclick(event):
    print ('Please click with the mouse on the graph to select the y-axis value')
    var = event.ydata #Assigns to var the y-value in the graph where the mouse was clicked
    plt.gcf().clear() #Clear the previous graph

    yerr = (1.96 * (dftg.loc['std'] / (math.sqrt(3650)))) #Calculates the 95% confidece interval
    plt.bar(df.index, dftg.loc['mean'], width=1, color=('w', 'w', 'w', 'w'), alpha=1, yerr=yerr, capsize=7,edgecolor='k') # Creates the plot
    plt.xticks(df.index, ('1992', '1993', '1994', '1995'))  # Sets a new x-axys label
    plt.xlim(1990.8, 1996.2)  # Sets the x-axis range
    plt.axes().xaxis.set_ticks_position('none')  # Removes ticks from x-axis
    plt.xlabel('Year')
    plt.ylim(0, 60000)
    plt.axhline(y=event.ydata, zorder=0) # Creates a horizontal line
    plt.annotate(str(int(event.ydata)),xy=(1990.9,event.ydata+1000)) # Adds y axis value on the top of the horizontal line

     # Calculates probability based on the input y value
    zscore = ((var - dftg.loc['mean']) / (1.96 * (dftg.loc['std'] / (math.sqrt(3650)))))

    # Assigns the color depending on the distribution. Dark blue if the distribution is certainly below this y-axis, white
    # if the value is certainly contained, to dark red if the value is certainly not contained as the distribution is above the axis).
    c = []
    for i in range(1992, 1996):
        if zscore.loc[i] < -0.9:
            c.append(gmap[10])
        elif -0.9 <= zscore.loc[i] < -0.7:
            c.append(gmap[9])
        elif -0.7 <= zscore.loc[i] < -0.5:
            c.append(gmap[8])
        elif -0.5 <= zscore.loc[i] < -0.3:
            c.append(gmap[7])
        elif -0.3 <= zscore.loc[i] < -0.1:
            c.append(gmap[6])
        elif -0.1 <= zscore.loc[i] < +0.1:
            c.append(gmap[5])
        elif +0.1 <= zscore.loc[i] < +0.3:
            c.append(gmap[4])
        elif +0.3 <= zscore.loc[i] < +0.5:
            c.append(gmap[3])
        elif +0.5 <= zscore.loc[i] < +0.7:
            c.append(gmap[2])
        elif +0.7 <= zscore.loc[i] < +1.0:
            c.append(gmap[1])
        else:
            c.append(gmap[0])


    plt.bar(df.index, dftg.loc['mean'], width=1, color=[c[0], c[1], c[2], c[3]], alpha=1, yerr=yerr, capsize=7,edgecolor='k')  # Creates the plot
    plt.show()

cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()




