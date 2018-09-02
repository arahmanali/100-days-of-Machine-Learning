# mean = (xbar . ybar - xybar) / (xbar)**2 -x**2bar
# b = ybar -mxbar
#trasnslating to python
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs =np.array([1,2,3,4,5,6], dtype=np.float64)
ys =np.array([5,4,6,5,6,7], dtype=np.float64)
#plt.scatter(xs,ys) #test show
#plt.show()
#lets generate best fit slop

def best_fit_slope_and_intercept(xs, ys):
    x_bar = np.mean(xs) # mean of xs
    y_bar = np.mean(ys) # means of ys 
    xy_bar = np.mean(xs*ys)
    numerator = (x_bar * y_bar)- (xy_bar) #mean of xs * mean of y - mean of x*y
    denominator = (x_bar**2) - np.mean(xs**2)
    m = numerator/denominator # this is mean
    b = y_bar - (m*x_bar) # this is b 

    return m,b 


m,b = best_fit_slope_and_intercept(xs,ys)
print(m,b)

regression_line = (m*xs)+b 

#prediction
predict_x = 8
predict_y = (m*predict_x) +b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y , color='g')
plt.plot(xs, regression_line)
plt.show()


