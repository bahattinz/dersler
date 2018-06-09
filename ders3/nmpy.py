import numpy as np

boy = np.random.randint(175,200,10)
print(boy)
kilo = np.random.randint(75,100,10)
print(kilo)

#NORMALDE:
# for i in range(len(boy)):
#     bmi.append(kilo[i]/boy[i]**2)

#NUMPY İLE
bmi = kilo / boy**2

print(bmi)

fvalues = [0, 12, 45.21, 34, 99.91]
F = np.array(fvalues)
print("Values in Fahrenheit degrees:")
print(F)
print("Values in  Centigrade degrees:")
print(5*F/9 - 5*32/9)
