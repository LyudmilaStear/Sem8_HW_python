"""
Этот и другие файлы с примерами данных доступны следующим образом:
1. Заходим в Google Colab.
2. Переходим в режим редактирования блокнота
 (создаем новый блокнот или открываем имеющийся).
3. В левой части экрана есть панель инструментов,
по умолчанию выбран первый инструмент "Содержание", нижняя кнопка на
этой панели инстурментов с иконкой папки называется "Файлы". Нажимаем её.
4. По умолчанию блокнот выполняется в папке "Content", где есть
папка "sample_data", в которой есть 4 файла с данными.
"""
# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')

# 1. Изобразите отношение households к population с
# помощью точечного графика
sns.scatterplot(data=df, x="households", y="population")


# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
sns.relplot(x="longitude", y="median_house_value", kind="line", data=df)

# 3. Представить гистограмму по housing_median_age
sns.histplot(data=df, x="housing_median_age")

# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age
sns.histplot(data=df, x="median_house_value", hue='housing_median_age')


plt.show()