import streamlit as st

st.header(f"EZKJ Veterinary Cheat Sheets")



st.page_link("pages/1_smallies.py", label="# **smallies**", icon="🐕")
st.page_link("pages/2_equines.py", label="**equines**", icon="🐎")
st.page_link("pages/3_ruminants.py", label="**ruminants**", icon="🐃")


st.markdown('send email to KJ (kyjincho@gmail.com) to report error')


page_bg_img = '''
<style>
    .stApp{
        background-image: url("https://img.freepik.com/free-photo/christmas-glitter-bokeh-lights-background_1048-9379.jpg?w=740&t=st=1720329213~exp=1720329813~hmac=da3b3d43c6b299b942f7add5e68474ad57b895b09b13bcb4bd16a8b4fa637756");
        background-size: cover;
    }

</style>
'''

st.markdown(page_bg_img,unsafe_allow_html=True)