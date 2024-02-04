import streamlit as st
import time
import datetime
import zoneinfo

st.title("World Clock")

zone_list = zoneinfo.available_timezones()
selected_zones = st.multiselect(
    'Which time zones do you want to see?',
    zone_list,
    default = ['America/Los_Angeles'], 
    max_selections=4)

tab1, tab2 = st.tabs(["standard format", "UNIX format"])
time_placeholders_1 = [tab1.empty() for _ in selected_zones]
time_placeholders_2 = [tab2.empty() for _ in selected_zones]


cnt = 0
    

while True:
    for i, zone in enumerate(selected_zones):
        current_time = datetime.datetime.now(tz=zoneinfo.ZoneInfo(zone))
        time_placeholders_1[i].metric(label=f"{zone}: ",value=f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        time_placeholders_2[i].metric(label=f"{zone}: ",value=f"{current_time.timestamp()}")
    # Wait for 1 second before updating again
    time.sleep(1)
    