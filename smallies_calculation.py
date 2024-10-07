import streamlit as st
import numpy as np
from PIL import Image

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
    st.markdown(f"give **:blue[{1000*dose/(drip*24):.0f}mL]**") 

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

def parvo():
    st.title("parvo")

    st.subheader('TPR') 
    

    bw = st.number_input(label = "Body weight (kg)", value = 5.0, format='%.1f')

    st.subheader('IP fluid') 
    st.markdown('green or pink jelco, just below umbilirus @ linea alba')
    st.markdown('1 L Ringers + 1 vial (20 mmol) KCL')
    st.markdown('warm the bag to 38 deg')
    st.markdown(f"give :blue[at least {bw*100:.1f} mL] IP")
    st.markdown(f":grey[hypovolaemic]: give :blue[{bw*100*0.1:.1f} -{bw*100*0.2:.1f} mL] IV  + leave catheter in (bandage)")

    st.divider()

    st.subheader('medication')
    st.markdown('**metoclopramide** (antiemetic)')
    conc = 5/5
    st.markdown('trade name: Clopamon/Metoclopramide 10/Clomax/Bio-metoclopramide/Adco-contromet')
    st.markdown('concentration: 10 mg/tablet; 5 mg/5 mL syrup')
    st.markdown('dosage: 0.3 - 0.5 mg/kg tid')
    st.markdown(f'give tablet: :blue[{0.3*bw/10:.2f} - {0.5*bw/10:.2f} tablets 3 times a day] or syrup: :blue[{0.3*bw/conc:.2f} - {0.5*bw/conc:.2f} mL 3 times a day]')
    st.markdown(f'dispense tablet: :blue[{0.3*bw/10*3*5:.2f} - {0.5*bw/10*3*5:.2f} tablets for 5 days] or syrup: :blue[{0.3*bw/conc*3*5:.2f} - {0.5*bw/conc*3*5:.2f} mL for 5 days]')
    st.markdown('')
    st.markdown('**Maropitant** (antiemetic)')
    conc1 = 10
    st.markdown('trade name: cerenia')
    st.markdown('concentration: 16/24/60 mg tablets; 10 mg/mL injection')
    st.markdown('dosage: 1 mg/kg q24 hrs up to 5 days')
    image = Image.open('smallies\cerenia.jpg')
    st.image(image)
    st.markdown(f'SC injection: :blue[{bw/conc1:.2f} mL SC q24 hrs up to 5 days]')
    st.markdown('')
    st.markdown('**cisapride** (prokinetic) - if not recovering well')
    st.markdown('dosage: 0.5 mL/kg tid on oral mucosa')
    st.markdown(f'give tablet: :blue[{0.5*bw:.2f} mL 3 times a day]')
    st.markdown(f'dispense tablet: :blue[{0.5*bw*3:.2f} mL per day]')
    st.markdown('')
    st.markdown('**Prolyte/Probiflora**')
    st.markdown('electrolyte and gluytamine for enterocyte nutrition')

    st.divider()

    st.subheader('nutrition')
    if bw >=2 and bw <=50:
        feed = (bw*30.0) + 70
    else:
        feed = pow(bw,0.75)*70

    st.markdown(f"required kCal/day = {feed} kCal")     
    st.markdown(f"aim for 25% of required to start = {feed*0.25} kCal")  
    st.markdown('encourage to syringe feed, not force feed')   


def shock():
    
    st.title('Shock therapy')
    bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f') 
    
    st.subheader('emergency drugs')
    st.markdown('**adrenaline** - anaphylaxis') 
    st.markdown('dosage: 0.01 mg/kg')
    st.markdown(f'conc: 1 mg/mL -> give :blue[{bw*0.01/1:.2f} mL]')
    st.markdown('**adrenaline** - cardiac arrest')
    st.markdown('dosage: 0.1 mg/kg')  
    st.markdown(f'conc: 1 mg/mL -> give :blue[{bw*0.1/1:.2f} mL]')    
    st.markdown('')
    st.markdown('**atropine**')
    st.markdown('dosage: 0.05 mg/kg')
    st.markdown(f'conc: 0.5 mg/mL -> give :blue[{bw*0.05/0.5:.2f} mL]')
    st.markdown(f'conc: 10 mg/mL -> give :blue[{bw*0.05/10:.2f} mL]')
    st.markdown('')
    st.markdown('**vasopressin** - ')
    st.markdown('dosage: 0.8 units/kg')
    st.markdown('')
    st.markdown('**doxapram + O2** - respiratory arrest') 
    st.markdown('dosage: 1 mg/kg')
    st.markdown(f'conc: 400 mg/20 mL -> give :blue[{bw*1/(400/20):.2f} mL]')
    st.markdown('')
    st.markdown('**Lignocaine** - ventricular arrhythmia') 
    st.markdown('dosage: 0.5 mg/kg')
    st.markdown(f'conc: 20 mg/mL -> give :blue[{bw*0.5/20:.2f} mL]')
    st.divider()

    st.subheader('parameter monitoring')
    st.markdown('Ht 35 - 45%')
    st.markdown(f'urine 1-2 mL/kg/hr = {1*bw:.0f}-{2*bw:.0f} mL/hr')
    st.markdown('RR 20-30')
    st.markdown('temp 37-38.5')
    st.markdown('HR 80-100')
    st.markdown('CRT <1.2')
    st.markdown('MAP > 60')
    st.divider()

    st.subheader('fluid')
    st.markdown('**crystalloid**')
    st.markdown(f'dog: :blue[{5*bw} - {20*bw} mL over 10 - 20 min]')
    st.markdown(f'cat: :blue[{5*bw} - {15*bw} mL over 15 - 30 min]')
    st.markdown('check parameters + repeat up to 3 times')
    st.markdown('**colloid**')
    st.markdown(f'dog: colloid {5*bw} - {20*bw} mL + crystalloid {5*bw/2} - {20*bw/2} mL')
    st.markdown(f'cat: colloid {5*bw} - {15*bw} mL + crystalloid {5*bw/2} - {15*bw/2} mL ')    


def antidotes():
    st.subheader ('organophosphate/carbamate')
    st.markdown('*atropine*')
    st.markdown('*2-PM* (OP only)')
    
    st.subheader('acetaminophen (paracetamol)')
    st.markdown('*N-acetylcystein* (within 4 hrs)')
    st.markdown('*SAM-E* (antioxidant for liver)')
    st.markdown('*cimetidine* (inhibit p450)')
    
    st.subheader('anticoagulant rodenticides')
    st.markdown('*vit K1*')
    
    st.subheader ('ethylene glycol')
    st.markdown('*ethanol 5%*')
    st.markdown('*4-methylprazole*')

    st.subheader ('emetics')
    st.markdown('cat: xylazine')
    st.markdown('dog: apomorphine')




    # st.subheader("Inputs:")
    # bw = st.number_input(label = "Body weight (kg)", value = 10.0, format='%.1f')  
    # st.markdown(f"IV bolus 90 ml/kg in total = **{90*bw:.1f} mL**") 
    # st.markdown(f"10% =  {90*bw*0.1:.1f} mL;   20% = {90*bw*0.2:.1f} mL;  30% = {90*bw*0.3:.1f} mL") 
    # st.divider() 

    # F_m = 80*bw # maintenance
    # d = st.number_input(label = "Dehydration (%)", value=0.0, format='%.1f')
    # F_d = bw*d*10  # dehydration
    # F_l = st.number_input(label = "ongoing loss (mL/24hr)", value = 0.0, format='%.1f')
    # R = (F_m + F_d + F_l)/24 # fluid rate
    # st.markdown(f"maintenance 80 ml/kg/24hr = {F_m:.1f} mL/24hr") 
    # st.markdown(f"dehydration = {F_d:.1f} mL/24hr") 
    # st.markdown(f"estimated loss = {F_l:.1f} mL/24hr") 
    # st.markdown(f"fluid needed over 24 hr = {F_m + F_d + F_l:.1f} mL/24hr")     
    # st.markdown(f"      = {(F_m + F_d + F_l)/2:.1f} mL/12hr ={R:.1f} mL/hr" ) 
    