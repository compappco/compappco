import streamlit as st
import pandas as pd

st.title("CompApp - Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Grader Version 5.0")
st.write("Write the thermal and physical properties of the composite below. For each property, also write the weighing and the required maximum/minimum/optimum values of the data set you want to compare. The application will provide you a grade out of 3 and a total grade out of 100 with respect to your data set.") 

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Type of the composite", "Interfacial Properties with Carbon Fiber Grade", "Coefficient of Thermal Expansion Grade", "Glass Transition Temperature Grade", "Cost Grade", "Strength Grade", "Processing Temperature Grade", "Shrinkage Grade", "Density Grade", "Total Grade"])

composite = st.text_input("Type of the composite (UNFILLED, GF, CF, MINERAL, CONDUCTIVE): ")
col1, col2, col3 = st.columns(3)
with col1:
    ifss = st.number_input("Interfacial Properties with Carbon Fiber (IFSS, in MPa): ")
with col2:
    ifss_weighing = st.number_input("Weighing of Interfacial Properties with Carbon Fiber (%): ")
with col3:
    ifss_max = st.number_input("Maximum IFSS in your data set (IFSS, in MPa): ")

col4, col5, col6 = st.columns(3)
with col4:
    cte = st.number_input("Coefficient of Thermal Expansion (CTE, in microstrain/°C): ")
with col5:
    cte_weighing = st.number_input("Weighing of Coefficient of Thermal Expansion (%): ")
with col6:
    cte_max = st.number_input("Maximum CTE in your data set (CTE, in microstrain/°C): ")

col7, col8, col9 = st.columns(3)
with col7:
    tg = st.number_input("Glass Transition Temperature (Tg, in °C): ")
with col8:
    tg_weighing = st.number_input("Weighing of Glass Transition Temperature (%): ")
with col9:
    tg_optimum = st.number_input("Optimum Glass Transition Temperature for your data set (Tg, in °C): ")

col10, col11, col12 = st.columns(3)
with col10:
    cost = st.number_input("Cost (in USD/kg): ")
with col11:
    cost_weighing = st.number_input("Weighing of Cost (%): ")
with col12:
    cost_max = st.number_input("Maximum Cost in your data set (in USD/kg): ")

col13, col14, col15 = st.columns(3)
with col13:
    strength = st.number_input("Strength (Tensile Modulus or Flexural Modulus, in GPa): ")
with col14:
    strength_weighing = st.number_input("Weighing of Strength (%): ")
with col15:
    strength_max = st.number_input("Maximum Strength in your data set (Tensile Modulus or Flexural Modulus, in GPa): ")

col16, col17, col18, col19 = st.columns(4)
with col16:
    tp = st.number_input("Processing Temperature (Tp, in °C): ")
with col17:
    tp_weighing = st.number_input("Weighing of Processing Temperature (%): ")
with col18:
    tp_min = st.number_input("Minimum Processing Temperature in your data set (Tp, in °C): ")
with col19:
    tp_max = st.number_input("Maximum Processing Temperature in your data set (Tp, in °C): ")

col20, col21, col22, col23 = st.columns(4)
with col20:
    shrinkage = st.number_input("Shrinkage (in %): ")
with col21:
    shrinkage_weighing = st.number_input("Weighing of Shrinkage (%): ")
with col22:
    shrinkage_optimum = st.number_input("Optimum Shrinkage for your data set (in %): ")
with col23:
    shrinkage_max = st.number_input("Maximum Acceptable Shrinkage for your data set (in %): ")

col24, col25, col26, col27, col28 = st.columns(5)
with col24:
    density = st.number_input("Density (in kg/m^3): ")
with col25:
    density_weighing = st.number_input("Weighing of Density (%): ")
with col26:
    density_optimum = st.number_input("Optimum Density for your data set (in kg/m^3): ")
with col27:
    density_min = st.number_input("Minimum Density in your data set (in kg/m^3): ")
with col28:
    density_max = st.number_input("Maximum Density in your data set (in kg/m^3): ")

if ifss_weighing+cte_weighing+tg_weighing+cost_weighing+strength_weighing+tp_weighing+shrinkage_weighing+density_weighing<100 or ifss_weighing+cte_weighing+tg_weighing+cost_weighing+strength_weighing+tp_weighing+shrinkage_weighing+density_weighing>100:
    st.markdown("### :red[WARNING: Make sure that the sum of the weighings equals 100!]")

if ifss>ifss_max:
    ifss_grade = 3.00
else:
    if ifss_max != 0:
        ifss_grade = 3.00 - 3.00*((ifss_max-ifss)/ifss_max)
        ifss_grade = round(ifss_grade,2)
    else:
        ifss_grade = 0

if composite in ["UNFILLED", "CF", "MINERAL", "CONDUCTIVE"]:
    if cte == 7.5:
        cte_grade = 3.00
    elif 0 < cte < 7.5:
        cte_grade = round(3.00 - 3.00 * ((7.5 - cte) / 7.5), 2)
    elif 7.5 < cte < cte_max:
        cte_grade = round(3.00 - 3.00 * ((cte - 7.5) / (cte_max - 7.5)), 2)
    else:
        cte_grade = 0
elif composite == "GF":  
    if cte == 22.5:
        cte_grade = 3.00
    elif 0 < cte < 22.5:
        cte_grade = round(3.00 - 3.00 * ((22.5 - cte) / 22.5), 2)
    elif 22.5 < cte < cte_max:
        cte_grade = round(3.00 - 3.00 * ((cte - 22.5) / (cte_max - 22.5)), 2)
    else:
        cte_grade = 0
else:
    cte_grade = 0  

if tg<tg_optimum:
    tg_grade = 0
elif tg>=tg_optimum:
    tg_grade = 3.00

if cost>=cost_max:
    cost_grade = 0
else:
    cost_grade = 3.00 - 3.00*((0-cost)/(0-cost_max))
    cost_grade = round(cost_grade,2)

if strength>=strength_max:
    strength_grade = 3.00
else:
    strength_grade = 3.00 - 3.00*((strength_max-strength)/(strength_max-0))
    strength_grade = round(strength_grade,2)

if tp<=tp_min:
    tp_grade = 3.00
elif tp>=tp_max:
    tp_grade = 0
else:
    tp_grade = 3.00 - 3.00*((tp_min-tp)/(tp_min-tp_max))
    tp_grade = round(tp_grade,2)

if shrinkage<=shrinkage_optimum:
    shrinkage_grade = 3.00
elif shrinkage>=shrinkage_max:
    shrinkage_grade = 0
else:
    shrinkage_grade = 3.00 - 3.00*((shrinkage_optimum-shrinkage)/(shrinkage_optimum-shrinkage_max))
    shrinkage_grade = round(shrinkage_grade,2)

if density == density_optimum:
    density_grade = 3.00
elif density_min < density < density_optimum:
    density_grade = 3.00 - 3.00*((density_optimum-density)/(density_optimum-density_min))
    density_grade = round(density_grade,2)
elif density_max > density > density_optimum:
    density_grade = 3.00 - 3.00*((density_optimum-density)/(density_optimum-density_max))
    density_grade = round(density_grade,2)
else:
    density_grade = 0

total_grade = ((ifss_grade*ifss_weighing)+(cte_grade*cte_weighing)+(tg_grade*tg_weighing)+(cost_grade*cost_weighing)+(strength_grade*strength_weighing)+(tp_grade*tp_weighing)+(shrinkage_grade*shrinkage_weighing)+(density_grade*density_weighing))/3.00
total_grade = round(total_grade,2)

st.write("The individual and total grades are given below.")

if st.button("Add Column"):
    new_row = pd.DataFrame({
    "Type of the composite": [composite],
    "Interfacial Properties with Carbon Fiber Grade": [ifss_grade],
    "Coefficient of Thermal Expansion Grade": [cte_grade],
    "Glass Transition Temperature Grade": [tg_grade],
    "Cost Grade": [cost_grade],
    "Strength Grade": [strength_grade],
    "Processing Temperature Grade": [tp_grade],
    "Shrinkage Grade": [shrinkage_grade],
    "Density Grade": [density_grade],
    "Total Grade": [total_grade]
})
    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)

st.write(st.session_state.data.T)
