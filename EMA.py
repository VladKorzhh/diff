import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def exponential_moving_average(data, alpha):
    """
    Вычисление экспоненциального скользящего среднего (EMA).
    
    :param data: Список чисел (данные).
    :param alpha: Коэффициент сглаживания (0 < alpha <= 1).
    :return: Список значений EMA.
    """
    if not 0 < alpha <= 1:
        raise ValueError("Alpha должно быть в диапазоне (0, 1].")
    if not data:
        raise ValueError("Данные не должны быть пустыми.")
    
    # Вычисление весов для всех данных
    weights = np.array([(1 - alpha) ** i for i in range(len(data))])
    weights = weights[::-1]  # Инвертируем веса (самый свежий элемент с наибольшим весом)
    weighted_sum = np.cumsum(weights * data[::-1])[::-1]  # Вычисляем взвешенную сумму справа налево
    normalization_factors = np.cumsum(weights[::-1])[::-1]  # Нормализационные коэффициенты
    
    # EMA для всех точек
    ema = weighted_sum / normalization_factors
    return ema

# Загрузка данных из Excel
file_path = "your_file.xlsx"  # Путь
column_name = "data"         # Столбец

# Считываем данные
df = pd.read_excel(file_path)
data = df[column_name].dropna().tolist()  # Преобразуем данные столбца в список

# Параметр сглаживания (alpha)
alpha = 0.2  # Настройте alpha (чем больше, тем быстрее реагирует EMA)

# Расчет EMA
ema = exponential_moving_average(data, alpha)

# Подготовка данных для графика
data_indices = range(len(data))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(data_indices, data, label="Данные", marker="o")
plt.plot(data_indices, ema, label="Экспоненциальное скользящее среднее (EMA)", color="red", linestyle="--")
plt.title("Данные и экспоненциальное скользящее среднее")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.grid()
plt.show()
