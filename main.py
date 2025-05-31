import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=1000, key="refresh")  # Refresh every 1 second

def time_to_binary(current_time):
    return [format(int(current_time[i:i+2]), '06b') for i in range(0, len(current_time), 2)]

current_time = time.strftime('%H%M%S')
binary_time = time_to_binary(current_time)

st.write(f"**Time:** {current_time[:2]}:{current_time[2:4]}:{current_time[4:6]}")
st.write("**Binary:**")
st.write(f"Hours:   {binary_time[0]}")
st.write(f"Minutes: {binary_time[1]}")
st.write(f"Seconds: {binary_time[2]}")
