import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from IPython.display import display

df = pd.read_csv('effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv')

print(df.head())

df.info()

df.describe()

df.columns

df.rename(columns={'Direction' : 'Direção', 
                   'Year' : 'Ano', 
                    'Date': 'Data', 
                    'Weekday' : 'Dias da Semana',
                   'Country' : 'País', 
                    'Commodity' : 'Mercadoria',
                    'Transport_Mode' : 'Modo de Transporte',
                    'Measure' : 'Medida',
                    'Value' : 'Valor',
                    'Cumulative': 'Acumulado'}, inplace=True)

display(df.columns)


df['País'] = df['País'].replace({
    'All': 'Todos',
    'China': 'China',
    'East Asia': 'Leste Asiático',
    'United States': 'Estados Unidos',
    'Australia': 'Austrália',
    'United Kingdom': 'Reino Unido',
    'Japan': 'Japão',
    'European Union (27)': 'União Europeia (27)',
    'Total (excluding China)': 'Total (excluindo China)',
    
})



df['Mercadoria'] = df['Mercadoria'].replace({
    'All': 'Todas',
    'Milk powder, butter, and cheese': 'Leite em pó, manteiga e queijo',
    'Meat and edible offal': 'Carne e miudezas comestíveis',
    'Logs, wood, and wood articles': 'Toros, madeira e artigos de madeira',
    'Fish, crustaceans, and molluscs': 'Peixes, crustáceos e moluscos',
    'Non-food manufactured goods': 'Bens manufaturados não alimentícios',
    'Electrical machinery and equip': 'Máquinas e equipamentos elétricos',
    'Mechanical machinery and equip': 'Máquinas e equipamentos mecânicos',
    'Fruit': 'Frutas'

})

df['Modo de Transporte'] = df['Modo de Transporte'].replace({
    'All': 'Todos(as)',
    'Air': 'Avião',
    'Sea': 'Navio',
})

df['Medida'] = df['Medida'].replace({
    'All': 'Todos(as)',
    'Value': 'Valor',
    'Weight': 'Peso'
})

df['Medida'] = df['Medida'].replace({
    '$' : 'Dólares',
    'Tonnes' : 'Toneladas'
})

df['Dias da Semana'] = df['Dias da Semana'].replace({
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo',
})

df['Direção'] = df['Direção'].replace({
    'Imports': 'Importações',
    'Exports': 'Exportações',
    'Reimports': 'Reimportações',
})


colunas = ['Ano', 'País', 
           'Mercadoria', 'Modo de Transporte', 
           'Medida', 'Valor','Direção', 'Dias da Semana']
           


for coluna in colunas:
    print(f"Valores únicos na coluna {coluna}")
    print(df[coluna].value_counts())
    input("\nPressione Enter para ver a proxima tabela...")


print(df.head())

print(df.describe())


df[df.isnull().any(axis=1)]



