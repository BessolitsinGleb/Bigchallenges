# import numpy as np
# import pandas as pd
# from sqlalchemy import create_engine

# # 1. Генерация ваших данных (для примера)
# # Массив (3 слоя, 30 рядов, 3 элемента X,Y,Z)
# data = np.random.uniform(0, 100, (3, 30, 3))

# layers = ['A', 'B', 'C']
# coords = ['X', 'Y', 'Z']
# rows = []

# # 2. Преобразование в плоский список (Flattening)
# for i, layer in enumerate(layers):
#     for j in range(30):
#         for k, coord in enumerate(coords):
#             # Формируем адрес: AX1, AY1, AZ1 ... CZ30
#             cell_id = f"{layer}{coord}{j+1}"
#             value = data[i, j, k]
#             rows.append([cell_id, layer, j+1, coord, value])

# # Создаем DataFrame
# df = pd.DataFrame(rows, columns=['cell_id', 'layer', 'row_num', 'coord_type', 'value'])

# # 3. Подключение к PostgreSQL
# # Формат: 'postgresql://username:password@localhost:5432/database_name'
# engine = create_engine('postgresql://postgres:pass@localhost:5432/my_parking_db')

# # 4. Загрузка в БД
# # Если таблица существует, она будет заменена (replace). Можно использовать append.
# df.to_sql('container_storage', engine, if_exists='replace', index=False)

# print("Данные успешно загружены в PostgreSQL!") посмотреть что чат гпт понаписал, разобрать протестить. подгружать эндпоинты 
