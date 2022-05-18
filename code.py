import streamlit as st

from iapws import IAPWS97
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from iapws import IAPWS97 as WSP
import math as M
from PIL import Image
import streamlit.components.v1 as components


st.write("Выполнили: Парнова Екатерина ФПэ-01-19, Юричковский Кирилл ТФэ-01-19")

st.write("# Колебания лопаток")

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
dp=1.046

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
dp = st.number_input('Введите периферийный диаметр, м', value=dp)
st.session_state.dp = dp
i=(Jx/Fx)**0.5
lyambda=l2/i
st.write(""" # """)
st.write(" *Дано:* ")
st.write(""" Средний диаметр последней ступени: """)
st.write(""" dsr = """ + str( dsr) + """ м""")
st.write(""" Длина рабочей лопатки: """)
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
st.write(""" Периферийный диаметр: """)
st.write(""" dp = """ + str(dp))   

st.write("""# """)
st.write("# Определение собственной частоты колебаний одиночной лопатки в статических условиях")

x_list= [3.565,3.739,4.174,4.696,5.478,6.696,7.826,9.739,12.087, 13.913,16.435,20.083,22.407,25.228,27.884,30.539,33.776,36.515,40.513,43.59,46.154,48.462,51.282,53.761,56.923,59.658]
y_list= [0.463,0.482,0.514,0.552,0.595,0.639,0.675,0.716,0.764,0.795,0.828,0.862,0.881,0.904,0.924,0.938,0.952,0.961,0.975,0.981,0.986,0.988,0.989,0.989,0.991, 0.991]
st.write(""" Так как значения частот колебаний оказываетсются ниже рассчитанных, используют поправочный коэффициент ksi=fдейств/fрасч для первого тона колебаний  """)
st.write(""" lyambda = """ + str(lyambda))
x_list_y_list = plt.figure()
fig = figure(
title='Зависимость ksi для первого тона колебаний от гибкости лопатки',
x_axis_label='Гибкость лопатки',
y_axis_label='Поправочный коэффициент')

fig.line(x_list, y_list , line_width=3)
st.bokeh_chart(fig, use_container_width=True)
ksi=5e**(-6)*lyambda**4-(0.0003*lyambda**3)+0.0037*lyambda**2+0.0203*lyambda+0.4318
st.write(""" ksi = """ + str(ksi)
st.write(""" # """)
st.write("# Определение собственной частоты колебаний пакета лопаток в статических условиях")
st.write(""" # """)
st.write(""" Действительная частота колебаний fst1: """)
f1=ksi*(m1/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f1 = """ + str(f1) + """ Гц """)
st.write(""" Действительная частота колебаний fst2: """)
f2=1*(m2/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f2 = """ + str(f2) + """ Гц """)
st.write(""" Действительная частота колебаний fst3: """)
f3=1*(m3/l2**2)*(E*Jx/(ro*Fx))**0.5
st.write(""" f3 = """ + str(f3) + """ Гц """)

st.write(""" # """)
st.write("# Определение собственной частоты колебаний пакета лопаток в статических условиях")
Eb=E
dp= 1.046 

Jb=Bb/12*delta**3
tb=(M.pi*dp)/z2
betta=90-betau
bettarad=betta*M.pi/180
#kb=(12*(m-1)*Hb*Eb*Jb*M.cos(betta)*M.cos(betta)*l2)/(m*tb*E*Jx)
#st.write(""" Коэффициент жесткости бандажа: """)
#st.write(""" kb = """ + str(kb))
nub=(Bb*10**-3*delta*10**-3*tb*ro)/(Fx*l2*ro)
st.write(""" Относительная масса бандажа """ + str(nub))

fiA0=1.14
fiB0=4.76
fiA1=6.39
fstA0=fiA0*f1
fstB0=fiB0*f1
fstA1=fiA1*f1
st.write(""" fstA0 = """ + str(fstA0))
st.write(""" fstB0 = """ + str(fstB0))
st.write(""" fstA1 = """ + str(fstA1))



st.write("""# Влияние вращения ротора на собственные частоты колебаний лопаток""")

