
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
        if st.button("Use Current Location \U0001F4CD"):


        st.subheader("Enter Location Details: ")
        state_name=st.text_input("Enter State: ")
        district_name=st.text_input("Enter District: ")
        county_name=st.text_input("Enter County: ")
        withincol1, withincol2, withincol3 = st.columns(3)
        with withincol2:
            if st.button("Check"):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
               # st.write("Safe Water Found")

=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
                match=test.findMatch(district_name)

#--OUTPUT--
with st.container():
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    st.write("---")                
>>>>>>> Stashed changes
=======
    st.write("---")                
>>>>>>> Stashed changes
=======
    st.write("---")                
>>>>>>> Stashed changes
