import math
import numpy as np
import matplotlib.pyplot as plt
def sigmoid(z):
    return 1.0/( 1.0 + np.exp(-z) )

a = np.linspace(-10,10,100)
x = np.linspace(-10,10,100)
j = 0;
for i in a :
    x[j] = sigmoid( a[j] )
    j = j + 1

plt.plot(a,x)
plt.show()
print a
