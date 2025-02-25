import streamlit as st
import numpy as np
from PIL import Image


def spay():
    st.subheader("Inputs:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    if bw < 5:
        drip_set = 60
    else:
        drip_set = 20
    st.markdown(f"Morphine = :blue[{bw*0.3/10:.2f}] mL")
    st.markdown(f"Medetomidine = :blue[{bw*0.01/1:.2f}] mL")
    st.markdown(f"Propofol 4mg/kg = :blue[{bw*4/10:.2f}] mL")
    st.markdown(f"Propofol 6mg/kg = :blue[{bw*6/10:.2f}] mL")
    st.markdown(f"Cefazolin = :blue[{bw*20/100:.2f}] mL")
    st.markdown(f"Metacam = :blue[{bw*0.2/5:.2f}] mL")
    st.markdown(f"Morphine = :blue[{bw*0.2/10:.2f}] mL")
    st.markdown(f"Cefazolin = :blue[{bw*20/100:.2f}] mL")
    st.markdown(
        f"Ringers = :blue[{bw*5*drip_set/(60*60):.2f}] drops/s = {1/(bw*5*drip_set/(60*60)):.0f}s/drop"
    )


def fluid_calc():
    st.subheader("Inputs:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    if bw >= 2 and bw <= 50:
        fluid = (bw * 30.0) + 70
    else:
        fluid = pow(bw, 0.75) * 70
    d = st.number_input(label="Dehydration (%)", value=0.0, format="%.1f")
    result = round(bw * (d) * 10.0)
    on_going = st.number_input(label="ongoing loss (mL/24hr)", value=0.0, format="%.1f")
    T_re = st.number_input(label="rehydrate over (hr)", value=24.0, format="%.1f")
    F_re = (fluid + on_going) * T_re / 24 + result

    st.subheader("fluid deficit")
    st.markdown(f"Maintenance fluid = {fluid:.1f} [mL/24hr]")
    st.markdown(f"Dehydration = {result:.1f} [mL]")
    st.markdown(f"On going loss = {on_going:.1f} [mL/24hr]")
    st.markdown(f"total fuid deficit = {fluid + result + on_going:.1f} [mL/24hr]")
    st.markdown(
        f"**rehydrate {F_re:.1f} [mL] over {T_re} [hrs] = {F_re/T_re:.1f} [mL/hr]**"
    )

    st.subheader("dripset")
    if bw >= 15:
        st.markdown("20 drops/mL **macro** dripset")
        drops = 20 * F_re / (T_re * 60 * 60)
    else:
        st.markdown("60 drops/mL **micro** dripset")
        drops = 60 * F_re / (T_re * 60 * 60)
    st.markdown(f"{drops:.1f} drops/s = **1 drop every {1/drops:.0f} seconds**")

    st.divider()
    #############################################
    st.subheader("ml into drip:")
    conc4 = st.number_input(label="concentration (%)", value=0.5, format="%.1f")
    dosage4 = st.number_input(label="dosage (mg/kg)", value=0.5, format="%.1f")
    drip = st.number_input(label="drip rate (mL/hr)", value=0.5, format="%.1f")
    dose = bw * dosage4 / conc4  #
    st.markdown(f"give **:blue[{1000*dose/(drip*24):.0f}mL]**")

    # drip*24 : 1000 = dose : ???
    # shock rates


###############################################
# glucose


def hypokalaemia():
    st.subheader("Inputs:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    drip_rate = st.number_input(label="drip rate (mL/hr)", value=10.0, format="%.1f")
    no_vial = ((0.5 * bw * 1000) / drip_rate - 4) / 20
    st.subheader("Max number of KCl vials")
    st.markdown(f"1 vial KCL = 20 meq = 20 mmol")
    st.markdown(f"Ringer's has 4 mmol of K in 1 L")
    st.markdown(f"max rate = 0.5 mmol/kg/hr = {0.5*bw} mmol/hr")
    st.markdown(
        f"**maximum number of vials = :blue[{no_vial:.1f} vials] in 1000 mL ringer's**"
    )
    st.markdown(
        f"**maximum number of vials = :blue[{no_vial/5:.1f} vials] in 200 mL ringer's**"
    )

    st.divider()
    st.subheader("check if safe to give X number of KCl vial in 1000 mL Ringer's")
    bw2 = st.number_input(label="Body weight (kg)", value=0.0, format="%.1f")
    vial = st.number_input(
        label="number of vials of KCl want to admin in 1000 mL ringer's",
        value=0.0,
        format="%.1f",
    )
    drip_rate2 = st.number_input(label="drip rate (mL/hr)", value=0.0, format="%.1f")
    K_rate = (vial * 20 + 4) * drip_rate2 / 1000
    max_rate = 0.5 * bw2
    st.markdown(
        f"{vial} vials in 1000 mL ringer's with {drip_rate2} mL/hr drip rate will give the **K admin rate @ {K_rate:.1f} mmol/hr**"
    )
    st.markdown(f"**max allowable K rate = {max_rate:.1f} mmol/hr**")

    if max_rate <= K_rate:
        st.markdown(f"**:red[reduce number of KCl vials!]**")
    else:
        st.markdown(f"{max_rate:.1f} > {K_rate:.1f} **:green[safe]**")

    st.divider()
    st.subheader("check if safe to give X number of KCl vials in 200 mL Ringer's")
    bw3 = st.number_input(label="Body weight (kg)", value=1.0, format="%.1f")
    vial3 = st.number_input(
        label="number of vials of KCl want to admin in 200 mL ringer's",
        value=1.0,
        format="%.1f",
    )
    drip_rate3 = st.number_input(label="drip rate (mL/hr)", value=1.0, format="%.1f")
    K_rate3 = (vial3 * 20 + 4 / 5) * drip_rate3 / 200
    max_rate = 0.5 * bw3
    st.markdown(
        f"{vial3} vials in 200 mL ringer's with {drip_rate3} mL/hr drip rate will give the **K admin rate @ {K_rate3:.1f} mmol/hr**"
    )
    st.markdown(f"**max allowable K rate = {max_rate:.1f} mmol/hr**")

    if max_rate <= K_rate3:
        st.markdown(f"**:red[reduce number of KCl vials!]**")
    else:
        st.markdown(f"{max_rate:.1f} > {K_rate3:.1f} **:green[safe]**")


def blood():
    st.subheader("Inputs for blood:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    blood = st.number_input(label="blood loss (mL)", value=1.0, format="%.1f")
    st.markdown("10 drops/mL")


def drug():
    st.subheader("Inputs for liquid [mg/mL]:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    conc = st.number_input(label="concentration (mg/mL)", value=1.0, format="%.1f")
    dosage = st.number_input(label="dosage (mg/kg)", value=1.0, format="%.1f")
    st.markdown(f"give **:blue[{bw*dosage/conc}mL]**")

    st.divider()

    st.subheader("Inputs for liquid [%]:")
    bw2 = st.number_input(label="Body weight (kg)", value=0.0, format="%.1f")
    conc2 = st.number_input(label="concentration (%)", value=0.1, format="%.1f")
    dosage2 = st.number_input(label="dosage (mg/kg)", value=0.0, format="%.1f")
    st.markdown(f"give **:blue[{bw2*dosage2/(conc2*10)}mL]**")
    # 100% = 1kg/L = 1000g/L = 1000mg/1mL
    # 1% = 10mg/mL

    st.divider()
    st.subheader("Inputs for tablets [mg/tablet]:")
    bw3 = st.number_input(label="Body weight (kg)", value=1.0, format="%.1f")
    conc3 = st.number_input(
        label="concentration (mg/tablet)", value=10.0, format="%.1f"
    )
    dosage3 = st.number_input(label="dosage (mg/kg)", value=10.0, format="%.1f")
    st.markdown(f"give **:blue[{bw3*dosage3/(conc3)} tablets]**")

    st.divider()

    ##############################################
    st.subheader("ml into drip:")
    bw4 = st.number_input(label="Body weight (kg)", value=5.0, format="%.1f")
    conc4 = st.number_input(label="concentration (%)", value=0.5, format="%.1f")
    dosage4 = st.number_input(label="dosage (mg/kg)", value=0.5, format="%.1f")
    drip = st.number_input(label="drip rate (mg/kg)", value=0.5, format="%.1f")
    st.markdown(f"give **:blue[{bw4*dosage4/(conc4)*1000/drip}mL]**")


#######################################################################################


def nutrition():
    st.subheader("Inputs:")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")
    tin_cal = st.number_input(label="kCal in one tin", value=10.0, format="%.1f")
    tin_vol = st.number_input(label="volume of one tin (mL)", value=10.0, format="%.1f")
    dil = st.number_input(label="dilution ratio water/tin", value=1.0, format="%.1f")
    no_meal = st.number_input(label="number of meals per day", value=1.0, format="%.1f")

    if bw >= 2 and bw <= 50:
        feed = (bw * 30.0) + 70
    else:
        feed = pow(bw, 0.75) * 70
    tot = feed / tin_cal * tin_vol * (dil + 1)

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
    st.markdown(
        f"**volume feed per meal (including flushing) = {tot/no_meal+5:.1f} mL per meal**"
    )
    if 10 * bw <= tot / no_meal + 5:
        st.markdown("❗:red[reduce feed volume]")
    if 5 * bw <= (tot / no_meal + 5) and 10 * bw > (tot / no_meal + 5):
        st.markdown(":orange[reduce feed volume if vomit]")
    if 5 * bw > (tot / no_meal + 5):
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

    bw = st.number_input(label="Body weight (kg)", value=5.0, format="%.1f")

    st.header("Day treatment: Day 1")
    st.subheader("Rx at hospital")
    st.markdown("**IP fluid**")
    st.markdown("green or pink jelco, just below umbilirus @ linea alba")
    st.markdown("1 L Ringers + 1 vial (20 mmol) KCL")
    st.markdown("warm the bag to 38 deg")
    st.markdown(f"give :blue[at least {bw*89:.1f} - {bw*100:.1f} mL] IP")
    st.markdown("**IV fluid**")
    st.markdown(
        f":grey[hypovolaemic]: give :blue[{bw*100*0.1:.1f} -{bw*100*0.2:.1f} mL] IV up to shock volume :blue[{90*bw}] + leave catheter in (bandage)"
    )
    st.markdown(f"**cerenia**")
    st.markdown(f":blue[{bw/10} mL] SC")
    st.markdown(f"**synulox**")
    st.markdown(f":blue[{bw/20} mL] SC")
    st.markdown("**Panacure**")
    st.markdown(f":blue[{bw} mL] per oral up to day 3")

    st.divider()

    st.subheader("medication to dispense")
    st.markdown("**metoclopramide** (antiemetic)")
    conc = 5 / 5
    st.markdown(
        "trade name: Clopamon/Metoclopramide 10/Clomax/Bio-metoclopramide/Adco-contromet"
    )
    st.markdown("concentration: 10 mg/tablet; 5 mg/5 mL syrup")
    st.markdown("dosage: 0.3 - 0.5 mg/kg tid")
    st.markdown(
        f"give tablet: {0.3*bw/10:.2f} - {0.5*bw/10:.2f} tablets 3 times a day or syrup: {0.3*bw/conc:.2f} - {0.5*bw/conc:.2f} mL 3 times a day"
    )
    st.markdown(
        f"*dispense tablet: :blue[{0.3*bw/10*3*5:.2f} - {0.5*bw/10*3*5:.2f} tablets for 5 days] or syrup: :blue[{0.3*bw/conc*3*5:.2f} - {0.5*bw/conc*3*5:.2f} mL for 5 days]*"
    )
    st.markdown("")
    st.markdown("**cisapride** (prokinetic) - if worried of ileusl")
    st.markdown("dosage: 0.5 mL/kg tid on oral mucosa")
    st.markdown(f"{bw*0.5} ml oral mucosa 3 times a day = {0.5*bw*3:.2f} mL per day")
    st.markdown(f"*dispense :blue[{0.5*bw*3*5:.2f} mL for 5 days]*")
    st.markdown("**Clavet**")
    st.markdown("see package insert")
    st.markdown("**Prolyte/Probiflora** - if no cost constraint")
    st.markdown("prolyte (electrolyte): = :blue[5 sachets] for 5 days")
    st.markdown("probiflora (probiotics): see package insert")
    st.markdown("ID/AD food if no constraint")

    st.divider
    st.header("Day treatment: Day 2-5")
    st.subheader("Rx at hospital")
    st.markdown("**IP fluid**")
    st.markdown("green or pink jelco, just below umbilirus @ linea alba")
    st.markdown("1 L Ringers + 1 vial (20 mmol) KCL")
    st.markdown("warm the bag to 38 deg")
    st.markdown(f"give :blue[at least {bw*89:.1f} - {bw*100:.1f} mL] IP")
    st.markdown(f"**cerenia**")
    st.markdown(f":blue[{bw/10} mL] SC")
    st.markdown("**Panacure**")
    st.markdown(f":blue[{bw} mL] per oral up to day 3")

    st.divider()

    st.subheader("nutrition")
    if bw >= 2 and bw <= 50:
        feed = (bw * 30.0) + 70
    else:
        feed = pow(bw, 0.75) * 70

    st.markdown(f"required kCal/day = {feed} kCal")
    st.markdown(f"aim for 25% of required to start = {feed*0.25} kCal")
    st.markdown("encourage to syringe feed, not force feed")


def shock():

    st.title("Shock therapy")
    bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.1f")

    st.subheader("emergency drugs")
    st.markdown("**adrenaline** - anaphylaxis")
    st.markdown("dosage: 0.01 mg/kg")
    st.markdown(f"conc: 1 mg/mL -> give :blue[{bw*0.01/1:.2f} mL]")
    st.markdown("**adrenaline** - cardiac arrest")
    st.markdown("dosage: 0.1 mg/kg")
    st.markdown(f"conc: 1 mg/mL -> give :blue[{bw*0.1/1:.2f} mL]")
    st.markdown("")
    st.markdown("**atropine**")
    st.markdown("dosage: 0.05 mg/kg")
    st.markdown(f"conc: 0.5 mg/mL -> give :blue[{bw*0.05/0.5:.2f} mL]")
    st.markdown(f"conc: 10 mg/mL -> give :blue[{bw*0.05/10:.2f} mL]")
    st.markdown("")
    st.markdown("**vasopressin** - ")
    st.markdown("dosage: 0.8 units/kg")
    st.markdown("")
    st.markdown("**doxapram + O2** - respiratory arrest")
    st.markdown("dosage: 1 mg/kg")
    st.markdown(f"conc: 400 mg/20 mL -> give :blue[{bw*1/(400/20):.2f} mL]")
    st.markdown("")
    st.markdown("**Lignocaine** - ventricular arrhythmia")
    st.markdown("dosage: 0.5 mg/kg")
    st.markdown(f"conc: 20 mg/mL -> give :blue[{bw*0.5/20:.2f} mL]")
    st.divider()

    st.subheader("parameter monitoring")
    st.markdown("Ht 35 - 45%")
    st.markdown(f"urine 1-2 mL/kg/hr = {1*bw:.0f}-{2*bw:.0f} mL/hr")
    st.markdown("RR 20-30")
    st.markdown("temp 37-38.5")
    st.markdown("HR 80-100")
    st.markdown("CRT <1.2")
    st.markdown("MAP > 60")
    st.divider()

    st.subheader("fluid")
    st.markdown("**crystalloid**")
    st.markdown(f"dog: :blue[{5*bw} - {20*bw} mL over 10 - 20 min]")
    st.markdown(f"cat: :blue[{5*bw} - {15*bw} mL over 15 - 30 min]")
    st.markdown("check parameters + repeat up to 3 times")
    st.markdown("**colloid**")
    st.markdown(
        f"dog: colloid {5*bw} - {20*bw} mL + crystalloid {5*bw/2} - {20*bw/2} mL"
    )
    st.markdown(
        f"cat: colloid {5*bw} - {15*bw} mL + crystalloid {5*bw/2} - {15*bw/2} mL "
    )


def antidotes():
    st.subheader("organophosphate/carbamate")
    st.markdown("*atropine*")
    st.markdown("*2-PM* (OP only)")

    st.subheader("acetaminophen (paracetamol)")
    st.markdown("*N-acetylcystein* (within 4 hrs)")
    st.markdown("*SAM-E* (antioxidant for liver)")
    st.markdown("*cimetidine* (inhibit p450)")

    st.subheader("anticoagulant rodenticides")
    st.markdown("*vit K1*")

    st.subheader("ethylene glycol")
    st.markdown("*ethanol 5%*")
    st.markdown("*4-methylprazole*")

    st.subheader("emetics")
    st.markdown("cat: xylazine")
    st.markdown("dog: apomorphine")


def antibiotics():
    box = st.selectbox(
        "Model: ", ("Synulox RTU", "Co-amoxy", "Amikacin", "Clavet", "Flagyl")
    )  # C

    # C
    if box == "Synulox RTU":  #
        st.subheader("Amoxicillin + Clavulanic Acid")
        image = Image.open("ruminant_antibiotics/synulox.jpg")
        c = 175
        d = 8.75
        st.image(image)
        st.markdown(
            "•	Uses: Respiratory infections, soft tissue infections (e.g., joint/navel ill, abscesses), metritis, mastitis. Broad-spectrum antibiotic, effective against Gram-positive and Gram-negative bacteria, including beta-lactamase producing strains (E. coli, Staphylococcus) "
        )
        st.markdown("•	Concentration: Amoxicillin 140 mg/mL + Clavulanic Acid 35 mg/mL")
        st.markdown("•	Dosage: 8.75 mg/kg SC q24 hr for 3-5 days")
        st.markdown(f"❗No IV")
        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*d/c:.2f} mL SC q24 hr for 3-5 days]")
    elif box == "Co-amoxy":
        st.subheader("Co-amoxy")
        dose = 20
        conc = 30
        st.markdown("•	Concentration: 30 mg/ml")
        st.markdown("•	Dosage: 20 mg/kg IV q8 hr")

        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*dose/conc:.2f} mL slow IV q8 hr]")
    elif box == "Amikacin":
        st.subheader("Amikacin")
        conc = 250.0
        dose = 20.0
        st.markdown("•	Uses: Gram negative")
        st.markdown("•	Concentration: 250 mg/ml")
        st.markdown("•	Dosage: 20 mg/kg IV q24 hr")
        st.markdown(f"❗Not longer than 7 days, nephrotoxic")

        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*dose/conc:.2f} mL slow IV q24 hr]")
    elif box == "Clavet":
        st.subheader("Clavet")
        st.markdown("Clavet tablet")
        clavet_info = {
            "Body mass (kg)": [
                "1-2",
                "3-5",
                "6-9",
                "10-13",
                "14-18",
                "19-25",
                "26-35",
                "36-50",
                ">50",
            ],
            "Clavet 50": [
                "0.5-1",
                "1-1.5",
                "1.5-2.5",
                "2.5-3.5",
                "3.5-4.5",
                "-",
                "-",
                "-",
                "-",
            ],
            "Clavet 250": ["-", "-", "-", "0.5", "1", "1-1.5", "1.5-2", "2-2.5", "3"],
        }
        st.dataframe(clavet_info)
    elif box == "Flagyl":
        st.subheader("Flagyl [metronidazole]")
        st.markdown("•	Uses: Gram negative-positive, anaerobes")
        choice = st.radio("", ["Oral suspension", "IV"])
        if choice == "Oral suspension":
            conc = 40.0
            dose = 15.0
            st.markdown("•	Concentration: 40 mg/ml")
            st.markdown("•	Dosage: 15 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(f"give :blue[{bw*dose/conc:.2f} mL oral ]")
        else:
            conc = 5.0
            dose = 15.0
            st.markdown("•	Concentration: 5 mg/ml")
            st.markdown("•	Dosage: 15 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(f"give :blue[{bw*dose/conc:.2f} mL IV ]")


def antiinflammatory():
    box = st.selectbox("Model: ", ("Paracetamol", "Meloxicam"))
    if box == "Paracetamol":
        st.subheader("Paracetamol")
        choice = st.radio("", ["Slow IV", "Syrup", "Tablet"])
        st.markdown(f"❗No cat!")

        if choice == "Slow IV":
            conc = 10.0
            dose_load = 25.0
            dose_main = 10.0
            st.markdown("•	Concentration: 10 mg/ml")
            st.markdown("•	Loading dosage: 25 mg/kg")
            st.markdown("•	Maintenance dosage: 10 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(
                f"give loading dose of :blue[{bw*dose_load/conc:.2f} mL slow IV q12 hr]"
            )
            st.markdown(
                f"give maintenance dose of :blue[{bw*dose_main/conc:.2f} mL slow IV q12 hr]"
            )
        elif choice == "Syrup":
            conc = 24.0
            dose_load = 25.0
            dose_main = 10.0
            st.markdown("•	Concentration: 24 mg/ml")
            st.markdown("•	Loading dosage: 25 mg/kg")
            st.markdown("•	Maintenance dosage: 10 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(
                f"give loading dose of :blue[{bw*dose_load/conc:.2f} mL syrup q12 hr]"
            )
            st.markdown(
                f"give maintenance dose of :blue[{bw*dose_main/conc:.2f} mL syrup q12 hr]"
            )
        elif choice == "Tablet":
            conc = 500.0
            dose_load = 25.0
            dose_main = 10.0
            st.markdown("•	Concentration: 500 mg/tablet")
            st.markdown("•	Loading dosage: 25 mg/kg")
            st.markdown("•	Maintenance dosage: 25 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(
                f"give loading dose of :blue[{bw*dose_load/conc:.2f} tablets  q12 hr]"
            )
            st.markdown(
                f"give maintenance dose of :blue[{bw*dose_main/conc:.2f} tablets  q12 hr]"
            )
    elif box == "Meloxicam":
        st.subheader("Meloxicam")
        choice = st.radio("", ["IV", "Syrup"])
        st.markdown(f"❗Not for cats less than 2 kg, and puppies younger than 6 weeks.")

        if choice == "IV":
            conc = 5.0
            dose_load = 0.2
            dose_main = 0.1
            st.markdown("•	Concentration: 5 mg/ml")
            st.markdown("•	Loading dosage: 0.2 mg/kg")
            st.markdown("•	Maintenance dosage: 0.1 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(
                f"give loading dose of :blue[{bw*dose_load/conc:.2f} mL IV q24 hr]"
            )
            st.markdown(
                f"give maintenance dose of :blue[{bw*dose_main/conc:.2f} mL IV q24 hr]"
            )
        elif choice == "Syrup":
            conc = 1.5
            dose_load = 0.2
            dose_main = 0.1
            st.markdown("•	Concentration: 1.5 mg/ml")
            st.markdown("•	Loading dosage: 0.2 mg/kg")
            st.markdown("•	Maintenance dosage: 0.1 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(
                f"give loading dose of :blue[{bw*dose_load/conc:.2f} mL syrup q24 hr]"
            )
            st.markdown(
                f"give maintenance dose of :blue[{bw*dose_main/conc:.2f} mL syrup q24 hr]"
            )


def antiemetic():
    box = st.selectbox(
        "Model: ",
        (
            "Cerenia",
            "Clopamon",
            "Ondansteron",
            "Cisapride",
        ),
    )
    if box == "Cerenia":
        st.subheader("Cerenia")
        dose = 1.0
        conc = 10.0
        st.markdown("•	Concentration: 10 mg/ml")
        st.markdown("•	Dosage: 1 mg/kg")

        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*dose/conc:.2f} mL IV q24 hr]")
    elif box == "Clopamon":
        st.subheader("Clopamon")
        choice = st.radio("", ["IV", "Syrup", "Tablet"])
        if choice == "IV":
            conc = 5.0
            dose = 0.5
            st.markdown("•	Concentration: 5 mg/ml")
            st.markdown("•	Dosage: 0.5 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(f"give :blue[{bw*dose/conc:.2f} mL IV q8 hr]")
        elif choice == "Syrup":
            conc = 1.0
            dose = 0.5
            st.markdown("•	Concentration: 1 mg/ml")
            st.markdown("•	Dosage: 0.5 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(f"give :blue[{bw*dose/conc:.2f} mL syrup q8 hr]")
        elif choice == "Tablet":
            conc = 10.0
            dose = 0.5
            st.markdown("•	Concentration: 10 mg/tablet")
            st.markdown("•	Loading dosage: 0.5 mg/kg")
            st.divider()
            bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
            st.markdown(f"**dog**")
            st.markdown(f"give :blue[{bw*dose/conc:.2f} tablets  q8 hr]")
    elif box == "Ondansteron":
        conc = 2.0
        dose = 0.5
        st.markdown("•	Concentration: 2 mg/ml")
        st.markdown("•	Dosage: 0.5 mg/kg")
        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*dose/conc:.2f} mL slow IV q8 hr]")
    elif box == "Cisapride":
        conc = 10.0
        dose = 1
        st.markdown("•	Concentration: 10 mg/ml")
        st.markdown("•	Dosage: 1 mg/kg")
        st.divider()
        bw = st.number_input(label="Body weight (kg)", value=10.0, format="%.2f")
        st.markdown(f"**dog**")
        st.markdown(f"give :blue[{bw*dose/conc:.2f} mL gum q24 hr]")
