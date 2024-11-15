import pandas as pd

def moving_average(data, window_size):
    if window_size <= 0:
        raise ValueError("Размер окна должен быть положительным")

    result = []  # Инициализируем пустой список для хранения результатов

    # Проходим по индексам от 0 до len(data) - window_size
    for i in range(len(data) - window_size + 1):
        # Берем подсписок данных от i до i + window_size
        window = data[i:i + window_size]
        # Вычисляем среднее значение этого подсписка
        average = sum(window) / window_size
        # Добавляем среднее значение в результат
        result.append(average)

    return result

# Пример использования
# Загрузка данных из файла Excel
file_path = 'path_to_your_file.xlsx'  # Путь
column_name = 'название_столбца'  # Столбец

# Чтение колонки из файла Excel
df = pd.read_excel(file_path)
data = df[column_name].tolist()  # Преобразуем в список

window_size = 3
result = moving_average(data, window_size)

# Визуализация
plt.figure(figsize=(12, 6))
plt.plot(data, label='Основной сигнал', color='blue', alpha=0.5)
plt.plot(range(window_size - 1, len(data)), result, label='Скользящее среднее', color='orange')
plt.title('Основной сигнал и скользящее среднее')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()
plt.grid()
plt.show()
