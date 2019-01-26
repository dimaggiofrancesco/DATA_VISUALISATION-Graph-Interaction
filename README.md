# Graph-Interaction

**Project aim:**
* Create a bar chart
* Add the confidence interval
* Let the user choose a y-axis value (interaction)
* The bar colors change in accordance to the y-axis value the uses has selected  
  
**Project summary:**  
The code plots a bar chart of four years of data. Each year has a y-axis value, which is derived from a sample of a larger dataset.  
For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around  
33,000. On top of this is plotted the **95% confidence interval** for the mean. A challenge that users face is that, for a  
given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because  
the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal).  
One of the solutions proposed for this problem is to allow users to indicate the y-axis value of interest (e.g. 42,000)  
and then draw a horizontal line and color bars based on this value.  
*The bar colors change with respect to what value the user has selected.*  
  
**Bar color:**  
Dark Blue: y input value is definitely above the bar  
4 graduations of Blue: y input value is inside the 95% confidence interval (above the bar mean value)  
White: y value is contained in the bar  
4 graduations of Red: y input value is inside the 95% confidence interval (below the bar mean value)  
Dark Red: y input value is definitely below the bar 
  
**The error bar is calculated as:**  
![equation](http://latex.codecogs.com/gif.latex?E%20%3D%20%5Cbar%7Bx%7D%20%5Cpm%20z%20%5Cast%20%5Cfrac%7B%5Csigma%20%7D%7B%5Csqrt%7Bn%7D%7D)

where:  
E is the error bar  
x is the mean  
z is the "Z" value for the Confidence Interval (CI). For CI=95%, the Z value is 1.96  
&sigma; is the standard deviation  
n is the number of observations  
