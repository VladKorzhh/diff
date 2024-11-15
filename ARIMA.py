import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def difference(data, d):
    """
    Применяет интегрирование (разности) к данным.
    
    :param data: Исходный временной ряд.
    :param d: Степень разности.
    :return: Преобразованный временной ряд.
    """
    for _ in range(d):
        data = [data[i] - data[i - 1] for i in range(1, len(data))]
    return data

def inverse_difference(orig_data, diff_data, d):
    """
    Восстанавливает ряд после разностей.
    
    :param orig_data: Исходный временной ряд.
    :param diff_data: Дифференцированный ряд.
    :param d: Степень разности.
    :return: Восстановленный ряд.
    """
    restored = orig_data[:d]
    for value in diff_data:
        restored.append(restored[-1] + value)
    return restored

def arma_model(data, p, q):
    """
    Реализует модель ARMA.
    
    :param data: Исходный временной ряд.
    :param p: Порядок AR (авторегрессии).
    :param q: Порядок MA (скользящего среднего).
    :return: Сгенерированные значения ARMA.
    """
    n = len(data)
    ar_params = np.random.uniform(-0.5, 0.5, p)
    ma_params = np.random.uniform(-0.5, 0.5, q)
    
    arma_values = np.zeros(n)
    errors = np.zeros(n)
    
    for t in range(max(p, q), n):
        ar_part = sum(ar_params[i] * data[t - i - 1] for i in range(p))
        ma_part = sum(ma_params[i] * errors[t - i - 1] for i in range(q))
        errors[t] = data[t] - (ar_part + ma_part)
        arma_values[t] = ar_part + ma_part
    return arma_values, ar_params, ma_params

def arima_model(data, p, d, q):
    """
    Реализует модель ARIMA.
    
    :param data: Исходный временной ряд.
    :param p: Порядок AR.
    :param d: Степень интеграции (разностей).
    :param q: Порядок MA.
    :return: Предсказанные значения, параметры AR и MA.
    """
    # Применяем разности
    diff_data = difference(data, d)
    
    # Строим модель ARMA
    arma_values, ar_params, ma_params = arma_model(diff_data, p, q)
    
    # Восстанавливаем исходный ряд
    arima_values = inverse_difference(data, arma_values[max(p, q):], d)
    
    return arima_values, ar_params, ma_params

# Загрузка данных из Excel
file_path = "your_file.xlsx"  # Путь
column_name = "data"         # Столбец

df = pd.read_excel(file_path)
data = df[column_name].dropna().tolist()

# Параметры модели ARIMA
p = 2  # Порядок AR
d = 1  # Степень разности
q = 2  # Порядок MA

# Построение модели ARIMA
arima_values, ar_params, ma_params = arima_model(data, p, d, q)

# Вычисление метрик
mse = mean_squared_error(data[d:], arima_values[d:])
print(f"MSE ARIMA: {mse:.2f}")
print(f"AR-параметры: {ar_params}")
print(f"MA-параметры: {ma_params}")

# График
plt.figure(figsize=(12, 6))
plt.plot(data, label="Исходные данные", marker="o")
plt.plot(range(len(arima_values)), arima_values, label="ARIMA (тренд)", linestyle="--", color="red")
plt.title("Модель ARIMA на чистом Python")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.grid()
plt.show()
