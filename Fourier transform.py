import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(0, 40 * np.pi, 1000)
y_values = np.sin(x_values + np.pi)
fft_values = np.fft.fft(y_values)
amplitude = np.abs(fft_values)
frequency = np.fft.fftfreq(len(x_values), x_values[1] - x_values[0])

positive_freqs = frequency[:len(frequency)//2]
positive_amplitude = amplitude[:len(amplitude)//2]

frequency_square = 5  # Частота миандра
sampling_rate = 1000   # Частота дискретизации
duration = 5           # Длительность сигнала

# Генерация времени для миандра
time = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Генерация миандра
square_wave = np.sign(np.sin(2 * np.pi * frequency_square * time))

# Преобразование Фурье для миандра
fft_square_wave = np.fft.fft(square_wave)
amplitude_square_wave = np.abs(fft_square_wave)
frequency_square = np.fft.fftfreq(len(time), time[1] - time[0])

positive_freqs_square = frequency_square[:len(frequency_square)//2]
positive_amplitude_square = amplitude_square_wave[:len(amplitude_square_wave)//2]

# Обрезаем x_values и y_values
min_len = min(len(x_values), len(time))
x_values = x_values[:min_len]
y_values = y_values[:min_len]

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, linewidth=2, color='blue', label='Синус')
plt.title('График функции синуса от 0 до 40π')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(positive_freqs, positive_amplitude, linewidth=2, color='red', label='Спектр частот синуса')
plt.title('Спектр частот (Быстрое преобразование Фурье для синуса)')
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(positive_freqs_square, positive_amplitude_square, linewidth=2, color='green', label='')
plt.title('Спектр частот (Быстрое преобразование Фурье)')
plt.xlabel('Частота')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(time, square_wave, linewidth=2, color='green', label='Миандр')
plt.title('Миандр (прямоугольный сигнал)')
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()
plt.show()
