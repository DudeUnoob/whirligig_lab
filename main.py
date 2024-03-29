import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


torque = [0.149676742, 0.164609714, 0.298613252, 0.3133501, 0.46149007]
angular_acceleration = [0.02155053, 0.023653692, 0.046224945, 0.052377763, 0.075482368]


slope, intercept, r_value, p_value, std_err = stats.linregress(angular_acceleration, torque)

print(slope, intercept)

x = np.linspace(min(angular_acceleration), max(angular_acceleration), 100)


y = slope * x + intercept

plt.figure(figsize=(10, 6))
plt.scatter(angular_acceleration, torque, color='b', label='Data')
plt.plot(x, y, color='r', label='Fit: y = {:.2f}x + {:.2f}'.format(slope, intercept))
plt.title('Torque vs Angular Acceleration')
plt.xlabel('Angular Acceleration (rad/s^2)')
plt.ylabel('Torque (Nm)')
plt.legend()
plt.grid(True)
#plt.savefig("graph.png", pad_inches=1)
plt.show()

