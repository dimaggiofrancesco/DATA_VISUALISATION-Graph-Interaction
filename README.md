# Graph-Interaction

In this [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_
Tasks.pdf) the authors describe the challenges users face when trying to make judgements about probabilistic data
generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1).
Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might
be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is
plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).



I added interactivity to the graph, which allows the user to click on the y axis to set the value of interest.
The bar colors change with respect to what value the user has selected.


The code plots a bar chart of four years of data. Each year has a y-axis value, which is derived from a sample of a larger dataset. 
For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 
33,000. On top of this is plotted the 95% confidence interval for the mean. A challenge that users face is that, 
for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, 
because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). 
One of the solutions proposed for this problem is to allow users to indicate the y-axis value of interest (e.g. 42,000)
and then draw a horizontal line and color bars based on this value.
So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely
below this value, or white if they contain this value.


BARS COLORS:
Blue: Bar is definitely below the y input value
White: Bar contains the y input value
Red: Bar is definitely above the y input value

The 95% confidence interval is calculated as 


![equation](http://latex.codecogs.com/gif.latex?%5Cbar%7Bx%7D%3D%20z%20%5Cast%20%5Cfrac%7B%5Csigma%20%7D%7B%5Csqrt%7Bn%7D%7D)
