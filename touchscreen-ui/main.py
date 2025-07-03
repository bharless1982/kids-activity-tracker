import streamlit as st

st.set_page_config(page_title="Kids Activity Tracker", layout="wide")

st.title("Kids Activity Tracker")
st.subheader("Welcome!")

st.markdown("""
This is the beginning of your touchscreen-friendly dashboard app for kids and parents.

- ✅ Track chores  
- ✅ Visualize reward progress  
- ✅ View data insights from SQL + Tableau  
""")

if st.button("Log a Task"):
    st.success("✅ Task Logged!")
