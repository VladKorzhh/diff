import pandas as pd
import matplotlib.pyplot as plt

def weighted_moving_average(data, weights):
    """
    Вычисление взвешенного скользящего среднего (WMA).
    
    :param data: Список чисел (данные).
    :param weights: Список весов (должен совпадать по длине с окном).
    :return: Список значений WMA.
    """
    if not data or not weights:
        raise ValueError("Данные и веса не должны быть пустыми.")
    if len(weights) > len(data):
        raise ValueError("Размер весов не должен превышать размер данных.")
    
    # Длина окна
    window_size = len(weights)
    # Нормализация весов (на случай, если они не нормализованы)
    weight_sum = sum(weights)
    normalized_weights = [w / weight_sum for w in weights]
    
    # Результирующий список WMA
    wma = []
    
    # Скользящее окно
    for i in range(len(data) - window_size + 1):
        # Текущие данные в окне
        window = data[i:i + window_size]
        # Скалярное произведение данных окна и нормализованных весов
        wma_value = sum(x * w for x, w in zip(window, normalized_weights))
        wma.append(wma_value)
    
    return wma

# Загрузка данных из Excel
file_path = "your_file.xlsx"  # Путь
column_name = "data"         # Столбец

# Считываем данные
df = pd.read_excel(file_path)
data = df[column_name].dropna().tolist()  # Преобразуем данные столбца в список

# Весовые коэффициенты
weights = [0.1, 0.3, 0.6]  # Настройка веса

# Расчет WMA
wma = weighted_moving_average(data, weights)

# Подготовка данных для графика
data_indices = range(len(data))
wma_indices = range(len(weights) - 1, len(data))  # Индексы для WMA (начиная с конца первого окна)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(data_indices, data, label="Данные", marker="o")
plt.plot(wma_indices, wma, label="Скользящее среднее (WMA)", color="red", linestyle="--")
plt.title("Данные и взвешенное скользящее среднее")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.grid()
plt.show()
