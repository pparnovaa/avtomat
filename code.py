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


st.write("Выполнено: Сильянов С.А. Афанасьева О.Д. Струнникова В.И. Ушкарёв М.В. Митин А.А. ФПэ-01-19")
#st.write("Github: " + " Вставить ссылку")
st.write("# Задание: Расчёт ступени большой поверхности")
st.write(""" # """)


page = st.sidebar.selectbox(
    "Выберите задание",
    ("Дано", "Первый этап", "Второй этап", "Третий этап", "Четвёртый этап","Переопределение необходимых для расчёта параметров"))

if page == "Дано":

    G = 64.8
    n = 50
    l2 = 0.950
    d2 = 2.550
    tetta = 2.68
    l1 = 0.920
    d1 = 2.530
    po_sh = 15.5
    h0_sh = 2480.4
    p2 = 3.4
    H0 = 203.0
    otnoV = 0.623

    st.write("# Решение Задания № 1 ")
    st.write(""" Повторить ход решения из методички """)
    st.write("""# """)

    st.write(""" # """)
    st.write(" *Дано:* ")
    st.write(""" Расход пара: """)
    st.write(""" G = """ + str(G) + """ кг/с""")
    st.write(""" Частота вращения: """)
    st.write(""" n = """ + str(n) + """ 1/с""")
    st.write(""" Размеры рабочих лопаток: """)
    st.write(""" l2 = """ + str(l2) + """ м """)
    st.write(""" d2 = """ + str(d2) + """ м""")
    st.write(""" tetta = """ + str(tetta) + """  """)
    st.write(""" Размеры сопловых лопаток: """)
    st.write(""" l1 = """ + str(l1) + """ м """)
    st.write(""" d1 = """ + str(d1) + """ м """)
    st.write(""" Параметры торможения перед ступенью: """)
    st.write(""" po_sh = """ + str(po_sh) + """ кПа """)
    st.write(""" h0_sh = """ + str(h0_sh) + """ кДж/кг """)
    st.write(""" Давление пара за ступенью: """)
    st.write(""" p2 = """ + str(p2) + """ кПа """)
    st.write(""" Распологаемый теплоперепад: """)
    st.write(""" H0 = """ + str(H0) + """ кДж/кг """)
    st.write(""" Отношение скоростей на среднем диаметре: """)
    st.write(""" otnoV = """ + str(otnoV) + """  """)

    st.write(" *Возможность изменить исходные данные:* ")

    G = st.number_input('Введите расход пара G, кг/с', value=G)
    st.session_state.G = G
    n = st.number_input('Введите частота вращения n, 1/c', value=n)
    st.session_state.n = n
    l2 = st.number_input('Введите разм. раб. лоп. l2, м', value=l2)
    st.session_state.l2 = l2

    tetta = st.number_input('Введите разм. раб. лоп. tettaG, ', value=tetta)
    st.session_state.tetta = tetta
