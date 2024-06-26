from typing import Any

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# Загрузка данных
url = 'https://raw.githubusercontent.com/Olga57/Start-DS/main/salary_1.csv'
url2 = 'https://raw.githubusercontent.com/Olga57/Start-DS/main/salary_2.csv'
url3 = 'https://raw.githubusercontent.com/Olga57/Start-DS/main/inf.csv'
data = pd.read_csv(url, sep=';')
data2 = pd.read_csv(url2, sep=';')
data3 = pd.read_csv(url3, sep=';')

# Заголовок приложения
st.title('Исследование изменений номинальной заработной платы и инфляции, её влияния в различных сферах')

# Отображение данных

st.write("Данные номинальной заработной платы в различных сферах за 2000-2016")
st.write(data)
st.write("Данные номинальной заработной платы в различных сферах за 2017-2023")
st.write(data2)
st.write("Инфляция за 2000-2023")
st.write(data3)


# Subheader
st.subheader("Анализ изменений номинальной заработной платы в сфере производства продуктов, образования "
                                                 "и строительства")
# Text
text = """
Рассмотрим изменения номинальной заработной платы в сфере производства продуктов, 
                           образования и строительства
"""
st.text(text)

# Фильтрация данных по сфере производства продуктов
data_production = data[data['Вид'] == 'производство пищевых продуктов,   включая напитки, и табака']
values = data_production.values[0][1:].astype(float)
fig, ax = plt.subplots(figsize=(12, 6))
# Построение первого графика
ax.plot(data_production.columns[1:], values, label='производство пищевых продуктов,   включая напитки, и табака')


# Построение второго графика
data2_production = data2[data2['Вид'] == 'производство пищевых продуктов']
values = data2_production.values[0][1:].astype(float)
ax.plot(data2_production.columns[1:], values, label='производство пищевых продуктов')

# Построение третьего графика
data3_production = data2[data2['Вид'] == 'производство напитков']
values = data3_production.values[0][1:].astype(float)

ax.plot(data3_production.columns[1:], values, label='производство напитков')

ax.set_xlabel('Год')  # Подпись оси X
ax.set_ylabel('Заработная плата')  # Подпись оси Y
ax.set_title('Изменения номинальной заработной платы в производстве продуктов, напитков')  # Заголовок графика
ax.legend()  # Добавление легенды
plt.xticks(rotation=45)
st.pyplot(fig)

# Вывод
text = """
Вывод: на основании построенного графика видно, что номинальная заработная плата 
в сфере производства пищевых продутов стабильно растет. Но необходимо отметить, 
что данные за 2001 - 2016 гг включают данные о производстве напитков и табака. 
Поэтому для более точной динамики роста номинальной заработной платы в сфере 
производства пищевых продуктов необходимо исследовать отдельно производство пищевых 
продуктов и напитков. За период с 2017 по 2023 год наблюдается рост зарплат в
производстве пищевых продуктов. Однако рост зарплат в сфере производства напитков 
выше, чем производство продуктов.
"""
st.text(text)

# Построение графика по виду деятельности "Образование"
# Фильтрация данных по сфере "Образование"
data_education = data[data['Вид'] == 'Образование']
data2_education = data2[data2['Вид'] == 'Образование']

# Объединение данных по году
data_combined = pd.merge(data_education, data2_education)

values = data_combined.values[0][2:].astype(float)
fig1, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data_combined.columns[2:], values, label='Образование')


ax1.set_xlabel('Год')  # Подпись оси X
ax1.set_ylabel('Заработная плата')  # Подпись оси Y
ax1.set_title('Изменения номинальной заработной платы в образовании')  # Заголовок графика
ax1.legend()  # Добавление легенды
plt.xticks(rotation=45)
st.pyplot(fig1)

# Вывод
text = """
Вывод: на основании графика можно сделать вывод, что номинальная заработная
плата в сфере "Образования" стабильно растет за период с 2000 по 2023 гг.
"""
st.text(text)


# Построение графика по виду деятельности "Строительство"
# Фильтрация данных по сфере "Строительство"
data_construction = data[data['Вид'] == 'Строительство']
data2_construction = data2[data2['Вид'] == 'Строительство']

# Объединение данных по году
data2_combined = pd.merge(data_construction, data2_construction)

values = data2_combined.values[0][2:].astype(float)
fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.plot(data2_combined.columns[2:], values, label='Строительство')


ax2.set_xlabel('Год')  # Подпись оси X
ax2.set_ylabel('Заработная плата')  # Подпись оси Y
ax2.set_title('Изменения номинальной заработной платы в строительство')  # Заголовок графика
ax2.legend()  # Добавление легенды
plt.xticks(rotation=45)
st.pyplot(fig2)
# Вывод
text = """
Вывод: на основании графика можно сделать вывод о стабильном росте номинальной
заработной платы в сфере "Строительство". Необходимо отметить, что рост ускорился
с 2020 года.
"""
st.text(text)

# Subheader
st.subheader("Анализ влияния инфляции на изменение заработной платы в сфере "
             "производства продуктов, образования и строительства")
# Рассматриваемый вид
st.markdown('Вид деятельности: **Образование**.')

# Расчет влияния инфляции

# Рассмотрим данные по номинальной заработной плате в образовании в переменной `data_combined'
# и подготовим данные для расчетов

data_ed_inf = pd.concat([data_combined, data3], axis=0)
st.write("Данные номинальной заработной платы в сфере образования и инфляции за 2000-2023")
st.write(data_ed_inf) # вывод данных для анализа

# транспонируем датафрейм
data_ed_inf_tr = data_ed_inf.set_index('Вид').T

# изменяем формат данных на int и float
data_ed_inf_tr['Образование'] = data_ed_inf_tr['Образование'].astype(int)
data_ed_inf_tr['инфляция'] = data_ed_inf_tr['инфляция'].str.rstrip('%').astype(float)
data_ed_inf_tr['инфляция'] = data_ed_inf_tr['инфляция'] / 100

# рассчитываем накопленную инфляцию и ее влияние на заработную плату.
# Находим ежегодное отклонение заработной платы в процентах
data_ed_inf_tr['накопленная инфляция'] = (1 + data_ed_inf_tr['инфляция']).cumprod() - 1
data_ed_inf_tr['зарплата_инф'] = (data_ed_inf_tr['Образование'] / (1 + data_ed_inf_tr['накопленная инфляция'])).round(2)
data_ed_inf_tr['изменение_зарплаты_%'] = data_ed_inf_tr['зарплата_инф'].pct_change() * 100
data_ed_inf_tr['инфляция_%'] = data_ed_inf_tr['инфляция'] * 100

st.write("Изменение заработной платы в сфере образования с учетом влияния инфляции за 2000-2023")
st.write(data_ed_inf_tr) # вывод данных для анализа

# построим график результатов
plt.figure(figsize=(10, 6))
plt.plot(data_ed_inf_tr.index, data_ed_inf_tr['изменение_зарплаты_%'], marker='o', color='b', label='Изменение зарплаты в %')
plt.plot(data_ed_inf_tr.index, data_ed_inf_tr['инфляция_%'], marker='o', color='r', label='Инфляция в %')
plt.xlabel('Год')
plt.ylabel('Значение в %')
plt.title('Изменение зарплаты и инфляции в % по годам')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
st.pyplot(plt)

# Вывод
text = """
Вывод: заработная плата с учетом влияния инфляции росла выше уровня инфляции в 
периоды: 2001 - 2002, 2004 - 2008, 2011-2013, 2017 - 2019, то есть рост реальной
заработной платы был выше роста инфляции, в среднем - 8%-12%. Самый значительный
рост (25-30%) наблюдался в период 2001 - 2002 гг.

За периоды: 2002 - 2004, 2008 - 2011, 2013 - 2017, 2019 - 2023 уровень инфляции 
выше, чем рост реальной заработной платы, в среднем рост составлял в эти периоды
0%-5% и есть периоды (2014-2016), где реальная заработная плата снижалась до -8%.
"""
st.text(text)



# Рассматриваемый вид
st.markdown('Вид деятельности: **Строительство**.')

# Расчет влияния инфляции

# Рассмотрим данные по номинальной заработной плате в строительстве в переменной `data2_combined'
# и подготовим данные для расчетов

# Объединим данные по номинальной заработной плате и инфляции в один датафрейм
data_cons_inf = pd.concat([data2_combined, data3], axis=0)
st.write("Данные номинальной заработной платы в сфере строительства и инфляции за 2000-2023")
st.write(data_cons_inf) # вывод данных для анализа

# транспонируем полученный датафрейм
data_cons_inf_tr = data_cons_inf.set_index('Вид').T
# проверим типы данных перед расчетом
data_cons_inf_tr.info()
# изменим формат данных
data_cons_inf_tr['Строительство'] = data_cons_inf_tr['Строительство'].astype(int)
data_cons_inf_tr['инфляция'] = data_cons_inf_tr['инфляция'].str.rstrip('%').astype(float)
data_cons_inf_tr['инфляция'] = data_cons_inf_tr['инфляция'] / 100

# рассчитаем столбец с накопленной инфляцией
data_cons_inf_tr['накопленная инфляция'] = (1 + data_cons_inf_tr['инфляция']).cumprod() - 1

# пересчитаем заработную плату с учетом влияния инфляции
data_cons_inf_tr['зарплата_инф'] = (data_cons_inf_tr['Строительство'] / (1 + data_ed_inf_tr['накопленная инфляция'])).round(2)

# рассчитаем столбец изменения в % заработной платы с учетом влияния инфляции
data_cons_inf_tr['изменение_зарплаты_%'] = data_cons_inf_tr['зарплата_инф'].pct_change() * 100

# добавим столбец с инфляцией в %
data_cons_inf_tr['инфляция_%'] = data_cons_inf_tr['инфляция'] * 100

st.write("Изменение заработной платы в сфере строительства с учетом влияния инфляции за 2000-2023")
st.write(data_cons_inf_tr) # вывод данных для анализа


# построим график изменения в % заработной платы с учетом вляиния инфляции и инфляции за 2000-2023
plt.figure(figsize=(10, 6))
plt.plot(data_cons_inf_tr.index, data_cons_inf_tr['изменение_зарплаты_%'], marker='o', color='b', label='Изменение зарплаты в %')
plt.plot(data_cons_inf_tr.index, data_cons_inf_tr['инфляция_%'], marker='o', color='r', label='Инфляция в %')
plt.xlabel('Год')
plt.ylabel('Значение в %')
plt.title('Изменение зарплаты в сфере строительства с учетом инфляции и инфляции в % по годам')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
st.pyplot(plt)

# Вывод
text = """
Вывод: заработная плата с учетом влияния инфляции росла выше уровня инфляции в 
периоды:2001, 2003, 2002, 2005 - 2008, 2018 - 2019, то есть рост реальной 
заработной платы был выше роста инфляции, в среднем - 8%-10%. Самый значительный
рост (22-23%) наблюдался в период 2001 гг.

За периоды: 2002, 2004, 2009 - 2017, 2020 - 2023 уровень инфляции выше, чем
рост реальной заработной платы, в среднем рост составлял в эти периоды 0%-2%
и есть периоды (2009, 2013 - 2015), где реальная заработная плата снижалась до -10%.
"""
st.text(text)


# Рассматриваемый вид
st.markdown('Вид деятельности: **Производство пищевых продуктов**.')
# Объединим данные по номинальной заработной плате и инфляции в один датафрейм
data_prod_inf = pd.concat([data_production, data2_production, data3], axis=0)

# транспонируем полученный датафрейм
data_prod_inf_tr = data_prod_inf.set_index('Вид').T

# проверим типы данных перед расчетом
data_prod_inf_tr.info()

# заменим пропуски на нулевые значения для дальнейшего анализа
data_prod_inf_tr['производство пищевых продуктов,   включая напитки, и табака'] = data_prod_inf_tr['производство пищевых продуктов,   включая напитки, и табака'].fillna(0)
data_prod_inf_tr['производство пищевых продуктов'] = data_prod_inf_tr['производство пищевых продуктов'].fillna(0)


data_prod_inf_tr['производство пищевых продуктов,   включая напитки, и табака'] = data_prod_inf_tr['производство пищевых продуктов,   включая напитки, и табака'].astype(int)
data_prod_inf_tr['производство пищевых продуктов'] = data_prod_inf_tr['производство пищевых продуктов'].astype(int)
data_prod_inf_tr['инфляция'] = data_prod_inf_tr['инфляция'].str.rstrip('%').astype(float)

data_prod_inf_tr['инфляция'] = data_prod_inf_tr['инфляция'] / 100

# рассчитаем столбец с накопленной инфляцией
data_prod_inf_tr['накопленная инфляция'] = (1 + data_prod_inf_tr['инфляция']).cumprod() - 1

# пересчитаем заработную плату с учетом влияния инфляции
data_prod_inf_tr['зарплата1_инф'] = (data_prod_inf_tr['производство пищевых продуктов,   включая напитки, и табака'] / (1 + data_ed_inf_tr['накопленная инфляция'])).round(2)
data_prod_inf_tr['зарплата2_инф'] = (data_prod_inf_tr['производство пищевых продуктов'] / (1 + data_ed_inf_tr['накопленная инфляция'])).round(2)

# рассчитаем столбец изменения в % заработной платы с учетом влияния инфляции
data_prod_inf_tr['изменение1_зарплаты_%'] = data_prod_inf_tr['зарплата1_инф'].pct_change() * 100
data_prod_inf_tr['изменение2_зарплаты_%'] = data_prod_inf_tr['зарплата2_инф'].pct_change() * 100

# добавим столбец с инфляцией в %
data_prod_inf_tr['инфляция_%'] = data_prod_inf_tr['инфляция'] * 100

st.write("Изменение заработной платы в сфере производства пищевых продуктов"
         " с учетом влияния инфляции за 2000-2023")
st.write(data_prod_inf_tr) # вывод данных для анализа

# построим график изменения в % заработной платы с учетом вляиния инфляции и инфляции за 2000-2023
plt.figure(figsize=(15, 7))
plt.plot(data_prod_inf_tr.index, data_prod_inf_tr['изменение1_зарплаты_%'], marker='o', color='b', label='Изменение зарплаты в производстве пищевых продуктов, включая напитки, и табака  в %')
plt.plot(data_prod_inf_tr.index, data_prod_inf_tr['изменение2_зарплаты_%'], marker='o', color='b', label='Изменение зарплаты в производстве пищевых продуктов в %')
plt.plot(data_prod_inf_tr.index, data_prod_inf_tr['инфляция_%'], marker='o', color='r', label='Инфляция в %')
plt.xlabel('Год')
plt.ylabel('Значение в %')
plt.title('Изменение зарплаты в сфере производства пищевых продуктов с учетом инфляции и инфляции в % по годам')
plt.legend(loc='center left')
plt.grid(True)
plt.xticks(rotation=45)
st.pyplot(plt)

# Вывод
text = """
Вывод: несмотря на то, что рассмотрены данные с различной группировкой
(с 2000 - 2016 - производство пищевых продуктов, напитков и табака, 
2017 - 2023 - производство только пищевых продуктов, по графику видно, 
что рост реальной заработной платы ниже уровня инфляции, за исключением 2001, 2006 и 2019.
"""
st.text(text)