import streamlit as st

from iapws import IAPWS97
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from iapws import IAPWS97 as WSP
import math as M
from PIL import Image
import streamlit.components.v1 as components


st.write("Выполнили: Парнова Екатерина ФПэ-01-19, Юричковский Кирилл ТФэ-01-19")

st.write("# Колебания лопаток")
st.write(""" # """)

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
ksi=0.98
Hb=0.226
m1=0.56
m2=3.51
m3=9.82
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
    

st.write(" *Изменить исходные данные:* ")

dsr = st.number_input('Введите средний диаметр последней ступени dsr, м', value=dsr)
st.session_state.dsr =dsr
l2 = st.number_input('Введите длину рабочей лопатка l2, м', value=l2)
st.session_state.l2 = l2
Fx = st.number_input('Введите площадь сечения профиля Fx, м2', value=Fx)
st.session_state.Fx = Fx
Jx = st.number_input('Введите момент инерции Jx, м4', value=Jx)
st.session_state.Jx = Jx
betau = st.number_input('Введите угол установки betau, гр', value=betau)
st.session_state.Jx = Jx
ro = st.number_input('Введите плотность стали ro, гр', value=ro)
st.session_state.ro = ro
ro = st.number_input('Введите плотность стали ro, кг/м3', value=ro)
st.session_state.ro = ro
E = st.number_input('Введите модуль упругости E, Па ', value=E)
st.session_state.E = E
z2 = st.number_input('Введите число рабочих лопаток z2, шт ', value=z2)
st.session_state.z2 = z2
Bb = st.number_input('Введите размер бандажной ленты Bb, мм ', value=Bb)
st.session_state.Bb = Bb
delta = st.number_input('Введите размер бандажной ленты delta, мм ', value=delta)
st.session_state.delta = delta
Hb = st.number_input('Качество присоединения бандажа Hb ', value=Hb)
st.session_state.Hb = Hb
i=(Jx/Fx)**0.5
lyambda=l2/i

st.write("""# """)

st.write(""" Так как значения частот колебаний оказываетсются ниже рассчитанных, используют поправочный коэффициент ksi=fдейств/fрасч для первого тона колебаний  """)
st.write(""" lyambda = """ + str(lyambda))
ksi = st.number_input('Введите ksi, ', value=ksi)
st.session_state.ksi = ksi

st.write(""" # """)
st.write(""" Действительная частота колебаний f1: """)
f1=ksi*(m1/l2**2)*(E*Jx/(ro*Fx))
st.write(""" f1 = """ + str(f1) + """ Гц """)
st.write(""" # """)
st.write(""" Действительная частота колебаний f2: """)
f2=1*(m2/l2**2)*(E*Jx/(ro*Fx))
st.write(""" f2 = """ + str(f2) + """ Гц """)
st.write(""" # """)
st.write(""" Действительная частота колебаний f3: """)
f3=1*(m3/l2**2)*(E*Jx/(ro*Fx))
st.write(""" f3 = """ + str(f3) + """ Гц """)
st.write(""" # """)

