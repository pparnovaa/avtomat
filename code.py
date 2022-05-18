import streamlit as st

from iapws import IAPWS97
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from iapws import IAPWS97 as WSP
import math as M
from PIL import Image
#from fpdf import FPDF
import streamlit.components.v1 as components
from sympy import *
from colorama import *


st.write("Выполнили: Парнова Екатерина ФПэ-01-19, Юричковский Кирилл ТФэ-01-19")

st.write("# Колебания лопаток")
st.write(""" # """)


if page == "Дано":

    dsr = 0.8355
    Fx=2.44e-4
    l2 = 0.211
    Jx=0.43e-8
    betau=85
    ro=8000
    E=2e11
    z2=132
    Bb=40
    delta=5
    m=12
    Hb=0.226

    st.write("# Решение ")
    
    st.write("""# """)

    st.write(""" # """)
    st.write(" *Дано:* ")
    st.write(""" Средний диаметр последней ступени: """)
    st.write(""" dsr = """ + str( dsr) + """ м""")
    st.write(""" Длина рабочей лопатка: """)
    st.write(""" l2 = """ + str(l2) + """ м""")
    st.write(""" Площадь сечения профиля: """)
    st.write(""" Fx = """ + str(Fx) + """ м2 """)
    st.write(""" Момент инерции: """)
    st.write(""" Jx = """ + str(Jx) + """ м4 """)
    st.write(""" Угол установки: """)
    st.write(""" betau = """ + str(betau) + """ гр  """)
    st.write(""" Плотность стали: """)
    st.write(""" ro = """ + str(ro) + """ кг/м3  """)
    st.write(""" Модуль упругости: """)
    st.write(""" E = """ + str(E) + """ Па  """)
    st.write(""" Число рабочих лопаток: """)
    st.write(""" z2 = """ + str(z2) + """ шт  """)
    st.write(""" Размеры бандажной ленты: """)
    st.write(""" Bb = """ + str(Bb) + """ мм  """)
    st.write(""" delta = """ + str(delta) + """ мм  """)
    st.write(""" Число лопаток в пакете: """)
    st.write(""" m = """ + str(m) + """ шт """)
    st.write(""" Качество присоединения бандажа: """)
    st.write(""" Hb = """ + str(Hb))
    

    st.write(" *Возможность изменить исходные данные:* ")

    G = st.number_input('Введите расход пара G, кг/с', value=G)
    st.session_state.G = G
    n = st.number_input('Введите частота вращения n, 1/c', value=n)
    st.session_state.n = n
    l2 = st.number_input('Введите разм. раб. лоп. l2, м', value=l2)
    st.session_state.l2 = l2

    tetta = st.number_input('Введите разм. раб. лоп. tettaG, ', value=tetta)
    st.session_state.tetta = tetta
