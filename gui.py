
import streamlit as st
import spreadsheet
import locationcontroller

#--HEADER SECTION--
with st.container():
    st.set_page_config(page_title="Can You Drink It?", layout="wide")
    st.subheader("Can You Drink It?")
    st.title("-Built by TheClique ")
    st.write("This website uses location services to provide users with information on safe and clean water sources nearby. Developed to support Sustainable Development Goal 6 (SDG 6), it aims to promote access to safe water and improve water management for healthier communities.")
    st.write("[Learn more about SDG6>](https://sdgs.un.org/goals/goal6)")


#--INPUT--
with st.container():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Use Current Location \U0001F4CD"):
            arr = locationcontroller.getLocation()
            spreadsheet.findMatch(arr[0],arr[1],arr[2])
        st.subheader("Enter Location Details: ")
        district_name=st.text_input("Enter District: ")
        village_name=st.text_input("Enter Village: ")
        withincol1, withincol2, withincol3 = st.columns(3)
        with withincol2:
            if st.button("Check"):
                spreadsheet.findMatch(state_name,district_name,county_name)