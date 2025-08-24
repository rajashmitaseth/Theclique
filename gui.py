''''#from tkinter import*

#theclique_root=Tk();
import tkinter as tk
from tkinter import messagebox

def submit_village():
    village = village_entry.get()
    if village.strip():
        messagebox.showinfo("Village Submitted", f"You entered: {village}")
    else:
        messagebox.showwarning("Input Error", "Please enter a village name.")

# Create the main application window
root = tk.Tk()
root.title("Village Name Input")
root.geometry("300x150")  # Width x Height

# Label
label = tk.Label(root, text="Enter Village Name:")
label.pack(pady=10)

# Entry widget
village_entry = tk.Entry(root, width=30)
village_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_village)
submit_button.pack(pady=10)

# Run the application
root.mainloop()'''


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
                st.write("Safe Water Found")

