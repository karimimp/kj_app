import streamlit as st
import numpy as np

def fluid_calc():
    st.subheader("Inputs:")
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')
    if bw >=2 and bw <=50:
        fluid = (bw*30.0) + 70
    else:
        fluid = pow(bw,0.75)*70
    d = st.number_input(label = "Dehydration (%)", value=0.0, format='%.1f')
    result = round(bw*(d)*10.0)
    on_going = st.number_input(label = "ongoing loss (mL/24hr)", value = 0.0, format='%.1f')
    T_re = st.number_input(label = "rehydrate over (hr)", value = 24.0, format='%.1f')
    F_re = (fluid+on_going)*T_re/24 + result
 
    st.subheader ('fluid deficit')
    st.markdown(f"Maintenance fluid = {fluid:.1f} [mL/24hr]")
    st.markdown(f"Dehydration = {result:.1f} [mL]")
    st.markdown(f"On going loss = {on_going:.1f} [mL/24hr]")
    st.markdown(f"total fuid deficit = {fluid + result + on_going:.1f} [mL/24hr]")    
    st.markdown(f"**rehydrate {F_re:.1f} [mL] over {T_re} [hrs] = {F_re/T_re:.1f} [mL/hr]**")    

    st.subheader ('dripset')
    if bw >= 15:
        st.markdown("20 drops/mL **macro** dripset")
        drops = 20*F_re/(T_re*60*60)
    else:
        st.markdown("60 drops/mL **micro** dripset")
        drops = 60*F_re/(T_re*60*60)
    st.markdown(f"{drops:.1f} drops/s = **1 drop every {1/drops:.0f} seconds**")  

    st.divider()
#############################################
    st.subheader("ml into drip:")
    conc4 = st.number_input(label = "concentration (%)", value = 0.5, format='%.1f')
    dosage4 = st.number_input(label = "dosage (mg/kg)", value = 0.5, format='%.1f')  
    drip = st.number_input(label = "drip rate (mL/hr)", value = 0.5, format='%.1f')    
    dose = bw*dosage4/conc4 #
    st.markdown(f"give **:blue[{1000*dose/(drip*24)}mL]**") 

    # drip*24 : 1000 = dose : ???
    # shock rates
###############################################
# glucose


def hypokalaemia():
    st.subheader("Inputs:")
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')  
    drip_rate = st.number_input(label = "drip rate (mL/hr)", value = 10.0, format='%.1f')  
    no_vial = ((0.5*bw*1000)/drip_rate-4)/20
    st.subheader("Max number of KCl vials")
    st.markdown(f"1 vial KCL = 20 meq = 20 mmol")
    st.markdown(f"Ringer's has 4 mmol of K in 1 L")   
    st.markdown(f"max rate = 0.5 mmol/kg/hr = {0.5*bw} mmol/hr")
    st.markdown(f"**maximum number of vials = {no_vial:.1f} vials in 1000 mL ringer's**")  

    st.divider()
    st.subheader("Inputs:")
    bw2 = st.number_input(label = "Body weight (kg)", value = 0.0, format='%.1f')  
    vial = st.number_input(label = "number of vials of KCl want to admin", value = 0.0, format='%.1f')  
    drip_rate2 = st.number_input(label = "drip rate (mL/hr)", value = 0.0, format='%.1f')  
    K_rate = (vial*20+4)*drip_rate2/1000
    max_rate = 0.5*bw2
    st.subheader("check if safe to give X number of KCl vials")
    st.markdown(f"{vial} vials in 1000 mL ringer's with {drip_rate2} mL/hr drip rate will give the **K admin rate @ {K_rate:.1f} mmol/hr**")
    st.markdown(f"**max allowable K rate = {max_rate:.1f} mmol/hr**")

    if max_rate <= K_rate:
        st.markdown(f"**:red[reduce number of KCl vials!]**")
    else:
        st.markdown(f"{max_rate:.1f} > {K_rate:.1f} **:green[safe]**")
   


 


def blood():
    st.subheader("Inputs for blood:")
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')
    blood = st.number_input(label = "blood loss (mL)", value=1.0, format='%.1f')
    st.markdown("10 drops/mL")



def drug():
    st.subheader("Inputs for liquid [mg/mL]:")
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')  
    conc = st.number_input(label = "concentration (mg/mL)", value = 1.0, format='%.1f')
    dosage = st.number_input(label = "dosage (mg/kg)", value = 1.0, format='%.1f')  
    st.markdown(f"give **:blue[{bw*dosage/conc}mL]**") 

    st.divider()

    st.subheader("Inputs for liquid [%]:")
    bw2 = st.number_input(label = "Body weight (kg)", value = 0.0, format='%.1f')  
    conc2 = st.number_input(label = "concentration (%)", value = 0.1, format='%.1f')
    dosage2 = st.number_input(label = "dosage (mg/kg)", value = 0.0, format='%.1f')  
    st.markdown(f"give **:blue[{bw2*dosage2/(conc2*10)}mL]**") 
    # 100% = 1kg/L = 1000g/L = 1000mg/1mL
    # 1% = 10mg/mL 

    st.divider()
    st.subheader("Inputs for tablets [mg/tablet]:")
    bw3 = st.number_input(label = "Body weight (kg)", value = 1.0, format='%.1f')  
    conc3 = st.number_input(label = "concentration (mg/tablet)", value = 10., format='%.1f')
    dosage3 = st.number_input(label = "dosage (mg/kg)", value = 10.0, format='%.1f')  
    st.markdown(f"give **:blue[{bw3*dosage3/(conc3)} tablets]**")  

    st.divider()

##############################################
    st.subheader("ml into drip:")
    bw4 = st.number_input(label = "Body weight (kg)", value = 5.0, format='%.1f')  
    conc4 = st.number_input(label = "concentration (%)", value = 0.5, format='%.1f')
    dosage4 = st.number_input(label = "dosage (mg/kg)", value = 0.5, format='%.1f')  
    drip = st.number_input(label = "drip rate (mg/kg)", value = 0.5, format='%.1f')     
    st.markdown(f"give **:blue[{bw4*dosage4/(conc4)*1000/drip}mL]**") 
#######################################################################################    

def nutrition():
    st.subheader("Inputs:")
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')  
    tin_cal = st.number_input(label = "kCal in one tin", value = 10.0, format='%.1f') 
    tin_vol = st.number_input(label = "volume of one tin (mL)", value = 10.0, format='%.1f')
    dil = st.number_input(label = "dilution ratio water/tin", value = 1.0, format='%.1f')
    no_meal = st.number_input(label = "number of meals per day", value = 1.0, format='%.1f')

    if bw >=2 and bw <=50:
        feed = (bw*30.0) + 70
    else:
        feed = pow(bw,0.75)*70
    tot = feed/tin_cal*tin_vol*(dil + 1)

    st.markdown(f"required kCal/day = {feed} kCal")        
    st.markdown(f"No. tin required = {feed/tin_cal}") 
    st.markdown(f"volume feed per day = {tot} mL") 

    st.divider()

    st.subheader(f"IF eating on its own")  
    st.markdown(f"**volume feed per meal= {tot/no_meal:.1f} mL per meal**")

    st.divider()

    st.subheader(f"IF syringe/tube fed")      
    st.markdown(f"flush volume per meal= 5 mL per meal")  
    st.markdown(f"gastric capacity = {5*bw:.1f} ~ {10*bw:.1f} mL per meal")
    st.markdown(f"**volume feed per meal (including flushing) = {tot/no_meal+5:.1f} mL per meal**")  
    if 10*bw <= tot/no_meal+5:
        st.markdown("❗:red[reduce feed volume]")
    if 5*bw <= (tot/no_meal+5) and 10*bw > (tot/no_meal+5):
        st.markdown(":orange[reduce feed volume if vomit]")
    if 5*bw > (tot/no_meal+5):
        st.markdown(":green[feed volume ok]")

    st.divider()

    st.subheader(f"IF prolonged starvation") 
    st.markdown(f"Day 1 = 50% = {tot/no_meal*0.5:.1f} mL per meal") 
    st.markdown(f"Day 2 = 75% = {tot/no_meal*0.75:.1f} mL per meal") 
    st.markdown(f"Day 3 = 100% = {tot/no_meal:.1f} mL per meal") 
    st.markdown(f"add 5 mL flush volume") 

    st.divider()

    st.subheader("Tube placements")
    st.markdown(f"NO tube: nose ~ 7/8th ICS") 
    st.markdown(f"NG tube: nose ~ last rib") 
    st.markdown(f"oesophagostomy: mid cervical oesophagus ~ 5-8th ICS") 

