
import streamlit as st

#--HEADER SECTION--
with st.container():
    st.set_page_config(page_title="Safe Water Locator", layout="wide")
    st.subheader("Safe Water Locator")
    st.title("-Built by TheClique ")
    st.write("This website uses location services to provide users with information on safe and clean water sources nearby. Developed to support Sustainable Development Goal 6 (SDG 6), it aims to promote access to safe water and improve water management for healthier communities.")
    st.write("[Learn more about SDG6>](https://sdgs.un.org/goals/goal6)")


#--INPUT--
with st.container():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.subheader("Enter Location Details: ")
        district_name=st.text_input("Enter District: ")
        village_name=st.text_input("Enter Village: ")
        withincol1, withincol2, withincol3 = st.columns(3)
        with withincol2:
            if st.button("Check"):
               # st.write("Safe Water Found")

