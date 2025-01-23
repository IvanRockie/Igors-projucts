import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 40 * np.pi, 1000) 
y_values = np.sin(x_values + np.pi)         
fft_values = np.fft.fft(y_values)            
amplitude = np.abs(fft_values)             
frequency = np.fft.fftfreq(len(x_values), x_values[1] - x_values[0])
frequency_second = 5
sampling_rate = 1000   # Гц
duration = 5 # Время
positive_freqs = frequency[:len(frequency)//2]  
positive_amplitude = amplitude[:len(amplitude)//2]
"""
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, linewidth=2, color='blue')  
plt.title('График функции синуса от 0 до 40π')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(positive_freqs, positive_amplitude, linewidth=2, color='red')
plt.title('Спектр частот (Быстрое преобразование Фурье)')
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.show()
"""
time = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
square_wave = np.sign(np.sin(2 * np.pi * frequency_second* time))

plt.figure(figsize=(10, 5))
plt.plot(time, square_wave)
plt.title('Миандр (прямоугольный сигнал)')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()
