import numpy as np
import matplotlib.pyplot as plt
import math

# Угол 
angle_degrees = 60

#радиан
angle_radians = math.radians(angle_degrees)
angle_radians_cos = math.radians(angle_degrees)

# Время 
time = np.linspace(0, 2 * np.pi, 1000)  # Время в интервале pi

# Вычисление синуса
sin_wave = np.sin(time + angle_radians)  # смещение
# Вычисление косинуса
cos_wave = np.cos(time + angle_radians_cos) # косинус

# Построение графика Синус
plt.figure(figsize=(12, 6))
plt.plot(time, sin_wave, time, cos_wave, linewidth=2, color='green', label='Синус', color='red', label='Косинус')
plt.title('График синуса')
plt.title('График косинуса')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()