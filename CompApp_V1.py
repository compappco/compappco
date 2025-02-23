import streamlit as st

st.title("CompApp - Composite Application")
st.markdown("### :red[by Ali Baran Arıban]")
st.title("Composite Grader Version 1.0")
st.write("Write the thermal and physical properties of the composite below. For each property, the application will provide you a grade out of 3 and a total grade out of 100.") 

composite = st.text_input("Type of the composite (UNFILLED, GF, CF, MINERAL, CONDUCTIVE): ")
ifss = st.number_input("Interfacial Properties with Carbon Fiber (IFSS, in MPa): ")
cte = st.number_input("Coefficient of Thermal Expansion (CTE, in microstrain/°C): ")
tg = st.number_input("Glass Transition Temperature (Tg, in °C): ")
cost = st.number_input("Cost (in USD/kg): ")
strength = st.number_input("Strength (Tensile Modulus or Flexural Modulus, in GPa): ")
tp = st.number_input("Processing Temperature (Tp, in °C): ")
shrinkage = st.number_input("Shrinkage (in %): ")
density = st.number_input("Density (in kg/m^3): ")

if ifss>=100:
    ifss_grade = 3.00
else:
    ifss_grade = 3.00 - 3.00*((100-ifss)/100)
    ifss_grade = round(ifss_grade,2)

if composite in ["UNFILLED", "CF", "MINERAL", "CONDUCTIVE"]:
    if cte == 7.5:
        cte_grade = 3.00
    elif 0 < cte < 7.5:
        cte_grade = round(3.00 - 3.00 * ((7.5 - cte) / 7.5), 2)
    elif 7.5 < cte < 144:
        cte_grade = round(3.00 - 3.00 * ((cte - 7.5) / (144 - 7.5)), 2)
    else:
        cte_grade = 0
elif composite == "GF":  
    if cte == 22.5:
        cte_grade = 3.00
    elif 0 < cte < 22.5:
        cte_grade = round(3.00 - 3.00 * ((22.5 - cte) / 22.5), 2)
    elif 22.5 < cte < 40:
        cte_grade = round(3.00 - 3.00 * ((cte - 22.5) / (40 - 22.5)), 2)
    else:
        cte_grade = 0
else:
    cte_grade = 0  

if tg<180:
    tg_grade = 0
elif tg>=180:
    tg_grade = 3.00

if cost>=117.5:
    cost_grade = 0
else:
    cost_grade = 3.00 - 3.00*((0-cost)/(0-117.5))
    cost_grade = round(cost_grade,2)

if strength>=18:
    strength_grade = 3.00
else:
    strength_grade = 3.00 - 3.00*((18-strength)/(18-0))
    strength_grade = round(strength_grade,2)

if tp<=119.5:
    tp_grade = 3.00
elif tp>=400:
    tp_grade = 0
else:
    tp_grade = 3.00 - 3.00*((119.5-tp)/(119.5-400))
    tp_grade = round(tp_grade,2)

if shrinkage<=0.5:
    shrinkage_grade = 3.00
elif shrinkage>=1.5:
    shrinkage_grade = 0
else:
    shrinkage_grade = 3.00 - 3.00*((0.5-shrinkage)/(0.5-1.5))
    shrinkage_grade = round(shrinkage_grade,2)

if density == 1400:
    density_grade = 3.00
elif 1000 < density < 1400:
    density_grade = 3.00 - 3.00*((1400-density)/(1400-1000))
    density_grade = round(density_grade,2)
elif 2000 > density > 1400:
    density_grade = 3.00 - 3.00*((1400-density)/(1400-2000))
    density_grade = round(density_grade,2)
else:
    density_grade = 0

st.write("Interfacial Properties with Carbon Fiber Grade: ",ifss_grade,"out of 3.")
st.write("Coefficient of Thermal Expansion Grade: ",cte_grade,"out of 3.")
st.write("Glass Transition Temperature Grade: ",tg_grade,"out of 3.")
st.write("Cost Grade: ",cost_grade,"out of 3.")
st.write("Strength Grade: ",strength_grade,"out of 3.")
st.write("Processing Temperature Grade: ",tp_grade,"out of 3.")
st.write("Shrinkage Grade: ",shrinkage_grade,"out of 3.")
st.write("Density Grade: ",density_grade,"out of 3.")

total_grade = ((ifss_grade*20)+(cte_grade*20)+(tg_grade*15)+(cost_grade*12.5)+(strength_grade*12.5)+(tp_grade*10)+(shrinkage_grade*5)+(density_grade*5))/3.00
total_grade = round(total_grade,2)
st.write("Total Grade: ",total_grade,"out of 100.")
