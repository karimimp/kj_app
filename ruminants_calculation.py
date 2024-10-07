import streamlit as st
import numpy as np
from PIL import Image

def antibiotics():
    
    box = st.selectbox("Model: ", ('Advocin 180', 'Amphoprim', # A
                                   'Baytril 100', 'Bivatop 200 LA', # B
                                   'Clamoxyl RTU',  # C
                                   'Depocillin', "Depomycin",'Doxymycin QA', "Draxxin", "Duplocillin", # D
                                   'Engemycin 10%','Excede','Excenel RTU', # E
                                   'Hi-Tet 120', # H
                                   'Mildox', # M
                                   'Nuflor', # N
                                   'Pendistrep', # P
                                   'Sulfatrim', 'Synulox RTU', # S
                                   'Terramycin LA' # T
                                   ))

### A
    if box == 'Advocin 180': # 1
        conc = 180  
        st.subheader("Danofloxacin (Fluoroquinolone)")
        image = Image.open('ruminant_antibiotics\dvocin.jpg')
        st.image(image)
        st.markdown("•	Uses: Treatment of bovine respiratory disease (BRD) caused by Mannheimia haemolytica and Pasteurella multocida. It's effective against gram-negative bacteria.")
        st.markdown(" •	Concentration: 180 mg/mL Danofloxacin.")
        st.markdown("•	Dosage: 8 mg/kg as a single dose or 6 mg/kg as 2 injections q24 hrs.")
        st.markdown(f"•	meat withdrawal 4 days")
        st.markdown(f"❗Do not use in dairy cattle producing milk for human consumption")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*8/conc:.1f}mL SC single does] or :blue[{bw*6/conc:.1f}mL SC 2 injections q24 hrs]")

    
    if box == 'Amphoprim': # 2
        st.subheader("Amphotericin B/Trimethoprim (Sulphonamides)")
        image = Image.open('ruminant_antibiotics\mphoprim.jpg')
        st.image(image)
        st.markdown("•	Uses: Bacterial infections of respiratory, urinary, genital & alimentary tract. effective against Gram-positive and Gram-negative bacteria, especially E. coli and Staphylococcus spp")
        st.markdown(f"•	NOT effective against: Leptospira spp., Pseudomonas spp., Erysipelothrix spp. ")
        st.markdown("•	Concentration: 40 mg/mL trimethoprim and 200 mg/mL sulphadimethylpyrimidine.")
        st.markdown("•	Dosage: one injection or repeat q24 hrs")
        st.markdown(f"•	meat withdrawal 5 days, milk widrawal 48 hrs (4 milkings)")
        st.divider()
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[25 mL IM/SC/slow IV]")
        st.markdown(f"< 10 ml one site")  
        st.markdown('') 
        st.markdown(f"**young cattle/pig**")
        st.markdown(f"give :blue[10 mL IM/SC/slow IV]")
        st.markdown('') 
        st.markdown(f"**calves/sheep**")
        st.markdown(f"give :blue[5 mL IM/SC/slow IV]")     
        st.markdown('') 
        st.markdown(f"**lambs/piglets**")
        st.markdown(f"give :blue[1 mL IM/SC/slow IV]")
### B
    if box == 'Baytril 100': # 3
        conc = 100
        st.subheader("Enrofloxacin (Fluoroquinolone)")
        image = Image.open('ruminant_antibiotics\ytril.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory disease associated with Mannheimia haemolytica, Pasteurella multocida, Histophilus somni, Mycoplasma spp.")
        st.markdown(" •	Concentration: 100 mg/mL (1g/10mL)")
        st.markdown("•	Dosage: 7.5-12.5 mg/kg as a single dose and 2.5-5 mg/kg q24 for 3 to 5 days")
        st.markdown(f"•	meat withdrawal 14 days (dairy cows), 28 days (beef cattle)")
        st.markdown(f"•	milk withdrawal 3 days")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**beef cattle**")
        st.markdown(f"give :blue[{bw*7.5/conc:.1f} - {bw*12.5/conc:.1f} mL SC single does]")
        st.markdown(f"< 15 ml one site")  
        st.markdown('') 
        st.markdown(f"**lactating cow**")
        st.markdown(f"give :blue[{bw*7.5/conc:.1f} mL SC single does]")
        st.markdown(f"< 15 ml one site") 

    if box == 'Bivatop 200 LA': # 4
        conc = 200
        dose = 20
        st.subheader("Long acting Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\ivatop.jpg')
        st.image(image)
        st.markdown("•	Uses: Treatment of a broad range of bacterial infections in cattle, including bovine respiratory infection, foot rot, metritis, infectious bovine keratoconjunctivitis")
        st.markdown(" •	Concentration: 200 mg/mL Oxytetracycline")
        st.markdown("•	Dosage: 20 mg/kg (1 mL/10kg), administered once q48-72 hrs IM/SC")
        st.markdown(f"•	meat withdrawal: 21 days (beef), 35 days (sheep)")
        st.markdown(f"•	milk withdrawal: 7 days")
        st.markdown(f"❗Administer carefully to avoid tissue irritation or muscle damage with intramuscular injections.")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dose/conc:.1f} mL IM/SC q48-72 hrs]")

### C
    if box == 'Clamoxyl RTU': # 5
        conc = 150
        dose = 7
        st.subheader("Amoxicillin (Penicillin)")
        image = Image.open('ruminant_antibiotics\clamoxyl.jpg')
        st.image(image)
        st.markdown("•	Uses: Broad-spectrum antibiotic effective against Gram-positive (Streptococcus, Staphylococcus spp.) and may be effective against Gram-negative bacteria (E. coli, Proteus mirabilis).")
        st.markdown(" •	Concentration: 150 mg/mL")
        st.markdown("•	Dosage: 7 mg/kg (0.25 mL/5 kg) q24h up to 5 days. IM/SC")
        st.markdown(f"•	meat withdrawal: 30 days")
        st.markdown(f"•	milk withdrawal: 72 hrs")
        st.markdown(f"❗Administer up to 5 days")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle/sheep/pig**")
        st.markdown(f"give :blue[{bw*dose/conc:.1f} mL IM/SC q24 hrs]")
        st.markdown(f"up to 5 days")


### D
    if box == 'Depocillin': # 6
        conc = 300
        dose1 = 20
        dose2 = 25
        st.subheader("Procaine penicillin (Penicillin)")
        image = Image.open('ruminant_antibiotics\depocillin.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory, skin, and soft tissue infections")
        st.markdown("•	Concentration: 150 mg/mL")
        st.markdown("•	Dosage (Cattle): 20 mg/kg or 1mL/15kg q24-48h IM")
        st.markdown("•	Dosage (Sheep): 25 mg/kg or 1mL/12kg q24-48h IM")
        st.markdown(f"•	meat withdrawal: 10 days")
        st.markdown(f"•	milk withdrawal: 108 hrs (9 milkings)")
        st.markdown(f"❗Avoid IV injection to prevent procaine toxicity")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dose1/conc:.1f} mL IM q24-48 hrs]")
        st.markdown('') 
        st.markdown(f"**sheep**")
        st.markdown(f"give :blue[{bw*dose2/conc:.1f} mL IM q24-48 hrs]")

    if box == 'Depomycin': # 7
        st.subheader("Dihydrostreptomycin + Procaine Penicillin (Aminoglycoside + Penicillin)")
        image = Image.open('ruminant_antibiotics\depomycin.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, soft tissue infections, and foot rot. Broad-spectrum activity. Penicillin is effective against Gram-positive bacteria, and Dihydrostreptomycin is effective against Gram-negative bacteria (Brucella, Pasteurella, Klebsiella")
        st.markdown("•	Concentration: 200,000 IU/mL procaine penicillin and 200 mg/mL dihydrostreptomycin")
        st.markdown("•	Dosage (cattle): 1 mL/25 kg q24h IM")
        st.markdown("•	Dosage (sheep): 1 mL/20 kg q24h IM")
        st.markdown(f"•	meat withdrawal: 15 days, 21 days (cattle offal), 35 days (sheep offal)")
        st.markdown(f"•	milk withdrawal: 4 milkings")
        st.markdown(f"❗Procaine toxicity can occur with overdose. Use with caution in animals with kidney disease")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw/25:.1f} mL IM q24 hrs]")
        st.markdown(f"repeat injection at different site")
        st.markdown('') 
        st.markdown(f"**sheep**")
        st.markdown(f"give :blue[{bw/20:.1f} mL IM q24 hrs]")
        st.markdown(f"repeat injection at different site")
    
    if box == 'Doxymycin QA': # 14
        st.subheader("Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\doxymycin.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, Pink eye, Foot rot, Tick-born diseases. Broad-spectrum activity against both Gram-positive and Gram-negative bacteria.")
        st.markdown("•	Concentration: 100 mg/mL")
        st.markdown("•	Dosage (Bacterial infection): 2-4 mL/100 kg IM/slow IV q24 hr for 2-3 days")
        st.markdown("•	Dosage (Heartwater): 2 mL/100 kg IM/IV single injection")
        st.markdown("•	Dosage (Anaplasmosis): 4 mL/100 kg IM/IV can repeat once q24 hr")
        st.markdown("•	meat withdrawal: 14 days")
        st.markdown("•	milk withdrawal: 2 days")
        st.markdown(f"❗deep IM @ neck preferred")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle**")
        st.markdown(f"give :blue[{bw*2/100:.1f} - {bw*4/100:.1f} mL IM/slow IV q24 hr for 2-3 days]")
        st.markdown(f"< 20 ml one site") 
        st.markdown(f"") 
        st.markdown(f"**Heartwater**")
        st.markdown(f"give :blue[{bw*2/100:.1f} mL IM/slow IV single injection]") 
        st.markdown(f"< 20 ml one site") 
        st.markdown(f"") 
        st.markdown(f"**Anaplasmosis**")
        st.markdown(f"give :blue[{bw*4/100:.1f} mL IIM/slow IV can repeat once q24 hr]")
        st.markdown(f"< 20 ml one site") 


    if box == 'Draxxin': # 8
        conc = 100
        dosage = 2.5  
        st.subheader("Long acting Tulathromycin (macrolide)")
        image = Image.open('ruminant_antibiotics\draxxin.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, pneumonia. Primarily effective against Gram-negative bacteria (Mannheimia haemolytica, Pasteurella multocida, Histophilus somni) and some Gram-positive bacteria.")
        st.markdown("•	Concentration: 100 mg/mL")
        st.markdown("•	Dosage: 2.5 mg/kg or 1 mL/40 kg once (long-acting)")
        st.markdown(f"•	meat withdrawal: 40 days")
        st.markdown(f"❗Not approved for use in lactating cows")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL SC]")
        st.markdown(f"< 10 ml one site")  

    if box == 'Duplocillin': # 9
        conc_p = 150
        conc_b = 115
        dosage1 = 1/25
        dosage2 = 1/20
        st.subheader("procaine benzylpenicillin 150 mg + benzathine benzylpenicillin 115 mg")
        image = Image.open('ruminant_antibiotics\duplo.jpg')
        st.image(image)
        st.markdown("•	Uses: Treatment of infections caused by penicillin-sensitive organisms, such as respiratory infections, skin infections, and infections of the urogenital tract. Primarily effective against Gram-positive bacteria (Streptococcus, Staphylococcus) and some Gram-negative bacteria")
        st.markdown("•	Concentration: 150,000 IU/mL Procaine Penicillin and 150,000 IU/mL Benzathine Penicillin")
        st.markdown("•	Dosage (cattle): 1 mL/25 kg IM q72 hrs")
        st.markdown("•	Dosage (sheep): 1 mL/20 kg IM q72 hrs")
        st.markdown("•	meat withdrawal: 14 days, 70 days (cattle injection site), 56 days (sheep injection site)")
        st.markdown("•	milk withdrawal: 5 milkings")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dosage1:.1f} mL IM]")
        st.markdown(f"repeat injection at different site")
        st.markdown('') 
        st.markdown(f"**sheep**")
        st.markdown(f"give :blue[{bw*dosage2:.1f} mL IM]")
        st.markdown(f"repeat injection at different site")
    
### E

    if box == 'Engemycin 10%': # 10
        conc = 100
        dosage = 10
        st.subheader("Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\engemycin.jpg')
        st.image(image)
        st.markdown("•	Uses: foot rot, tick-borne diseases (gall-sickness/theileriosis), bacterial pneumonia, mastitis, navel/joint ill, wound infection")
        st.markdown("•	Concentration: 100 mg/mL")
        st.markdown("•	Dosage (bacterial): 10 mg/kg (1mL/10kg) IM/slow IV (over 1 min) q24-48h for 3-5 days")
        st.markdown("•	Dosage (heartwater, anaplasmosis): 20 mg/kg")
        st.markdown("•	meat withdrawal: 14 days")
        st.markdown("•	milk withdrawal: 60 hrs")
        st.markdown(f"❗Avoid in young animals due to potential effects on bone growth")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL IM/slow IV]")
        st.markdown(f"< 20 ml one site")     
        st.markdown("")
        st.markdown(f"**sheep/goats**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL IM/slow IV]")
        st.markdown(f"if > 50 kg, devide dose into 2 injection sites")   
        st.markdown("")
        st.markdown(f"**heartwater/anaplasmosis**")
        st.markdown(f"give :blue[{bw*dosage/conc*2:.1f} mL IM/slow IV]")      


    if box == 'Excede': # 11
        conc = 200
        dosage = 6.6
        st.subheader("Ceftiofur (Cephalosporin)")
        image = Image.open('ruminant_antibiotics\excede.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, foot rot, bacterial infections. Effective against Gram-negative bacteria (E. coli, Pasteurella multocida) and some Gram-positive organisms (Streptococcus spp.).")
        st.markdown("•	Concentration: 200 mg/mL")
        st.markdown("•	Dosage: 6.6 mg/kg (1 mL/30 kg) SC @ base of ear")
        st.markdown("•	meat withdrawal: 13 days")
        st.markdown("•	milk withdrawal: not needed if single injection")
        st.markdown(f"❗shake for 30 s before injection.")
        st.markdown(f"❗SC @ base of ear only")
        st.markdown(f"❗Not for calves to be processed for veel")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL SC @ base of ear]")

    if box == 'Excenel RTU': # 12
        conc = 50
        dosage = 1
        st.subheader("Ceftiofur (Cephalosporin)")
        image = Image.open('ruminant_antibiotics\excenel.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, acute post partum metritis within 14 days, mastitis, foot rot. Effective against Gram-negative bacteria (E. coli, Pasteurella multocida) and some Gram-positive organisms (Streptococcus spp.).")
        st.markdown("•	Concentration: 50 mg/mL")
        st.markdown("•	Dosage: 1 mg/kg (1 ml/50 kg) IM/SC q24 hr for 3-5 days")
        st.markdown("•	meat withdrawal: 4 days")
        st.markdown(f"❗shake for 60 s before injection.")
        st.markdown(f"❗discolouration of muscle at IM injection site up to 28 days")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL IM/SC q24 hr for 3-5 days]")
### H

    if box == 'Hi-Tet 120': # 13
        st.subheader("Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\Hi_Tet.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, Pink eye, Foot rot, Tick-born diseases. Broad-spectrum activity against both Gram-positive and Gram-negative bacteria.")
        st.markdown("•	Concentration: 120 mg/mL")
        st.markdown("•	Dosage (bacterial infection): 1 mL/30 kg IM/SC/slow IV q24-48 hr")
        st.markdown("•	Dosage (tick-born disease): 2 mL/30 kg IM/SC/slow IV q24-48 hr")
        st.markdown("•	meat withdrawal: 7 days")
        st.markdown("•	milk withdrawal: 48 hrs")
        st.markdown(f"❗Use cautiously in young animals due to potential effects on bone growth.")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{bw/30:.1f} mL IM/SC/slow IV q24 hr as required]")
        st.markdown(f"< 25 ml one site")  
        st.markdown(f"") 
        st.markdown(f"**Anaplasmosis/heartwater**")
        st.markdown(f"give :blue[{bw/30*2:.1f} mL IM/SC/slow IV q24 hr as required]")
        st.markdown(f"< 25 ml one site")  

### M

    if box == 'Mildox': # 14
        st.subheader("Lipid soluble Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\mildox.jpg')
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, Pink eye, Foot rot, Tick-born diseases. Broad-spectrum activity against both Gram-positive and Gram-negative bacteria.")
        st.markdown("•	Concentration: 100 mg/mL")
        st.markdown("•	Dosage (Bacterial infection): 2-4 mL/100 kg IM/IV q24 hr for 3-5 days")
        st.markdown("•	Dosage (Heartwater): 2 mL/100 kg IM/IV single injection")
        st.markdown("•	Dosage (Anaplasmosis): 4 mL/100 kg IM/IV can repeat once q24 hr")
        st.markdown("•	meat withdrawal: 14 days")
        st.markdown("•	milk withdrawal: 2 days")
        st.markdown(f"❗deep IM @ neck preferred")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle**")
        st.markdown(f"give :blue[{bw*2/100:.1f} - {bw*4/100:.1f} mL IM/IV q24 hr for 3-5 days]")
        st.markdown(f"") 
        st.markdown(f"**Heartwater**")
        st.markdown(f"give :blue[{bw*2/100:.1f} mL IM/IV single injection]") 
        st.markdown(f"") 
        st.markdown(f"**Anaplasmosis**")
        st.markdown(f"give :blue[{bw*4/100:.1f} mL IIM/IV can repeat once q24 hr]")

### N
    if box == 'Nuflor': # 15
        st.subheader("Florfenicol (Phenicol)")
        image = Image.open('ruminant_antibiotics\lor.jpg')
        conc = 300
        dosage = 20
        st.image(image)
        st.markdown("•	Uses: Respiratory infections, pneumonia. Broad-spectrum, effective against Gram-negative bacteria (Mannheimia haemolytica, Pasteurella) and Gram-positive bacteria (Staphylococcus, Streptococcus spp.).")
        st.markdown("•	Concentration: 300 mg/mL")
        st.markdown("•	Dosage (cattle): 20 mg/kg (1 ml/15 kg) IM repeat once q48 hr with 16G needle or 40 mg/kg SC single injection")
        st.markdown("•	Dosage (sheep): 20 mg/kg IM q 24hr for 3 days")
        st.markdown("•	meat withdrawal: 30 days (IM), 44 days (SC), 37 days (Sheep)")
        st.markdown(f"❗Not approved for dairy")
        st.markdown(f"❗Not for breeding bulls")
        st.markdown(f"❗IM @ neck only")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL IM repeat once q48 hr with 16G needle] or :blue[{bw*dosage/conc*2:.1f} mL SC single injection]")
        st.markdown(f"< 10 ml one site") 
        st.markdown(f"") 
        st.markdown(f"**Sheep**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f} mL IM q 24hr for 3 days]") 
        st.markdown(f"repeat injection at different site")

### P
    if box == 'Pendistrep': # 16
        st.subheader("Procaine Penicillin + Dihydrostreptomycin (Penicillin + Aminoglycoside)")
        image = Image.open('ruminant_antibiotics\pendistrep.png')
        st.image(image)
        st.markdown("•	Uses: Treatment of respiratory infections, soft tissue infections, foot rot, urogenital infections, septicaemia. Effective against Gram-positive bacteria (Streptococcus spp., Clostridium spp., Listeria spp.) and Gram-negative bacteria (Brucella spp., Pasteurella spp., Klebsiella spp.)")
        st.markdown("•	Concentration: 200,000 IU/mL Procaine Penicillin + 200 mg/mL Dihydrostreptomycin")
        st.markdown("•	Dosage: 1 ml/20 kg IM q24 hrs")
        st.markdown("•	meat withdrawal: 35 days")
        st.markdown("•	milk withdrawal: 3 days")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle**")
        st.markdown(f"give :blue[{bw/20:.1f} mL IM q24 hrs]")

### S
    if box == 'Sulfatrim': # 17
        st.subheader("Sulfamethoxazole + Trimethoprim")
        image = Image.open('ruminant_antibiotics\sulfatrim.jpg')

        st.image(image)
        st.markdown("•	Uses: Urinary tract infections, skin infections, respiratory infections. Effective against Actinobacillus, Actinomyces, Bordatella, Corynebacterium, Erysipelothrix, E.coli, Klebsiella, Listeria ")
        st.markdown("•	Concentration: Sulfamethoxazole 20% + Trimethoprim 4%")
        st.markdown("•	Dosage: 1 mL/10 kg IM/IV q24 hr for 3-5 days")
        st.markdown("•	meat withdrawal: 7 days (Cattle), 14 days (Sheep/goats)")
        st.markdown("•	milk withdrawal: 3 days (cows), 5 days (sheep/goats)")
        st.markdown(f"❗Total daily dose should be divided into 2 equal doses")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle/sheep**")
        st.markdown(f"give :blue[{bw/10:.1f} mL IM/IV q24 hr for 3-5 days]")
        st.markdown(f"= give :blue[{bw/10/2:.1f} mL IM/IV x2 per day]")
        st.markdown(f"alternate injection site") 

    if box == 'Synulox RTU': # 18
        st.subheader("Amoxicillin + Clavulanic Acid")
        image = Image.open('ruminant_antibiotics\Synulox.jpg')

        st.image(image)
        st.markdown("•	Uses: Respiratory infections, soft tissue infections (e.g., joint/navel ill, abscesses), metritis, mastitis. Broad-spectrum antibiotic, effective against Gram-positive and Gram-negative bacteria, including beta-lactamase producing strains (E. coli, Staphylococcus) ")
        st.markdown("•	Concentration: Amoxicillin 140 mg/mL + Clavulanic Acid 35 mg/mL")
        st.markdown("•	Dosage: 1 mL/20 kg IM/SC q24 hr for 3-5 days")
        st.markdown("•	meat withdrawal: 28 days")
        st.markdown("•	milk withdrawal: 24 hrs")
        st.markdown(f"❗No IV")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle/sheep**")
        st.markdown(f"give :blue[{bw/20:.1f} mL IM/SC q24 hr for 3-5 days]")

## T
    if box == 'Terramycin LA': # 18
        st.subheader("Long acting Oxytetracycline (Tetracycline)")
        image = Image.open('ruminant_antibiotics\erra.jpg')

        st.image(image)
        st.markdown("•	Uses: Long-acting treatment for respiratory infections, pink eye, foot rot, tick-borne diseases (gall sickness, heartwater, Broad-spectrum, effective against both Gram-positive and Gram-negative bacteria (Staphylococcus, E. coli, Pasteurella).")
        st.markdown("•	Concentration: 200 mg/mL")
        st.markdown("•	Dosage: 1 mL/10 kg IM single injection. Can repeat q72 hr (esp. pink eye)")
        st.markdown("•	meat withdrawal: 28 days")
        st.markdown("•	milk withdrawal: 5-7 days")
        st.markdown(f"❗Use cautiously in young animals due to potential effects on bone growth")
        st.divider()
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.markdown(f"**Cattle**")
        st.markdown(f"give :blue[{bw/10:.1f} mL IM single injection. Can repeat q72 hr]")
        st.markdown(f"< 10 ml one site")  
        st.markdown(f"**Sheep/goats**")
        st.markdown(f"give :blue[{bw/10:.1f} mL IM single injection. Can repeat q72 hr]")
        st.markdown(f"if > 50 kg, devide dose into 2 injection sites") 

    st.divider()
    st.markdown(f"✅:grey[Acknolowlegement:] Danielle Weenink's summary of IDR 2021/22")   


####################    

def repro():
    
    box = st.selectbox("Model: ", ('Doxapram', #D
                                   'Estrumate', # E
                                   'Fentocin', # F
                                   ))
### E
    if box == 'Doxapram': # 1
        conc = 2
        dosage = 2
        bw = st.number_input(label = "Body weight (kg)", value = 100.0, format='%.0f')  
        st.subheader("Doxapram (respiratory stimulator)")
        st.markdown("•	Uses: asphyxia")
        st.markdown(" •	Concentration: 2 mg/mL")
        st.markdown("•	Dosage: 2 mg/kg IV for neonate calves")
        st.markdown(f"❗check concentration")
        st.divider()
        st.markdown(f"**Neonate calve**")
        st.markdown(f"give :blue[{bw*dosage/conc:.1f}mL IV]")
        st.markdown(f"average birth weight 40kg = 40 mL IV")

    if box == 'Estrumate': # 1
        conc = 180  
        st.subheader("Cloprostenol Sodium (synthetic PFG2a)")
        image = Image.open('ruminant_repro\estrumate.jpg')
        st.image(image)
        st.markdown("•	Uses: Silent heat, chronic endometritis with persistent CL, pyometra, induction of parturition < 10 days, termination of pregnancy < 100 days, mummified foetus, ovarian luteal cyst, controlled breeding ")
        st.markdown(" •	Concentration: 250 ug/mL Cloprostenol")
        st.markdown("•	Dosage:2 mL deep IM for cattle")
        st.markdown(f"•	meat withdrawal 24 hrs")
        st.markdown(f"•	milk withdrawal 8 hrs")
        st.markdown(f"❗Woman of childbearing age, asthmatics should not handle this product")
        st.markdown(f"❗Not for pregnant animals (unless induction). Causes abortion")
        st.divider()
        st.markdown(f"**cattle**")
        st.markdown(f"give :blue[{2.0:.1f} mL deep IM]")

    



