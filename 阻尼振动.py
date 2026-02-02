import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint

omega = 2.0
x_0 = 0.0
v_0 = 0.0
t_max = 15
dt = 0.01
gamma = 0.2
F = 1

def ho(t,y):
    '''
    定义该系统的微分方程组
    '''
    x,v = y
    dxdt = v
    dvdt =  -omega**2 * x + F*np.cos(1.9*t) - gamma * v
    '''
    这是受到简谐力驱动的阻尼系统
    '''
    return [dxdt, dvdt]
y_0 = [x_0,v_0]
t_span = np.linspace(0, t_max, int(t_max/dt))
sol = solve_ivp(ho, (0, t_max), y_0, t_eval=t_span)
t = sol.t
x = sol.y[0]
v = sol.y[1]

plt.figure(figsize = (10,10))

plt.subplot(3,1,1)
plt.plot(t, x, 'b-', label = '1')
plt.xlabel('Time')
plt.ylabel('Displacement x')
plt.grid()
plt.legend('y',loc = 'upper left', fontsize = 'large')

plt.subplot(3,1,2)
plt.plot(t,v,'r-', label = '1')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.grid()
plt.legend('v', loc = 'upper left', fontsize = 'large')

plt.subplot(3,1,3)
plt.plot(x,v, 'g-', label = '2')
plt.xlabel('Displacement')
plt.ylabel('Velocity')
plt.title('Phase space')
plt.tight_layout()
plt.show()

plt.savefig('无阻尼受迫振动.pdf')
