import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error

def arma_model(data, p, q):
    """
    Реализация модели ARMA (p, q).
    
    :param data: Временной ряд данных.
    :param p: Порядок авторегрессии (AR).
    :param q: Порядок скользящего среднего (MA).
    :return: Тренд (значения ARMA) и параметры модели.
    """
    n = len(data)
    
    # Проверяем, что данных достаточно
    if n < max(p, q) + 1:
        raise ValueError("Недостаточно данных для указанного p и q.")
    
    # Инициализация коэффициентов
    ar_params = np.random.uniform(-0.5, 0.5, p)  # Коэффициенты AR
    ma_params = np.random.uniform(-0.5, 0.5, q)  # Коэффициенты MA
    
    # Инициализация тренда
    arma_trend = np.zeros(n)
    
    # Итеративный расчет ARMA
    for t in range(max(p, q), n):
        # Авторегрессия (AR)
        ar_part = sum(ar_params[i] * data[t - i - 1] for i in range(p))
        # Скользящее среднее (MA)
        ma_part = sum(ma_params[i] * (data[t - i - 1] - arma_trend[t - i - 1]) for i in range(q))
        # Итоговая модель
        arma_trend[t] = ar_part + ma_part
    
    return arma_trend, ar_params, ma_params

df = pd.read_excel('file.xlsx')
data = df['column_name'].dropna().tolist()  # Преобразуем данные столбца в список

# Параметры модели ARMA
p = 2  # Порядок авторегрессии
q = 2  # Порядок скользящего среднего

# Расчет модели ARMA
arma_trend, ar_params, ma_params = arma_model(data, p, q)

# Метрики качества
mse = mean_squared_error(data[max(p, q):], arma_trend[max(p, q):])
mae = mean_absolute_error(data[max(p, q):], arma_trend[max(p, q):])
print(f"MSE ARMA: {mse:.2f}, MAE ARMA: {mae:.2f}")
print(f"AR-параметры: {ar_params}")
print(f"MA-параметры: {ma_params}")

# График
plt.figure(figsize=(12, 6))
plt.plot(data, label="Данные", linestyle="-")
plt.plot(arma_trend, label="ARMA (тренд)", linestyle="--", color="red")
plt.title("Модель ARMA")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.grid()
plt.show()
