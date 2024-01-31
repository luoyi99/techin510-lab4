"""
Change this to a world clock app
"""

import time
import streamlit as st
import datetime
import zoneinfo


st.title("World Clock")

zone_list = zoneinfo.available_timezones()

selected_zone = st.multiselect(
    'Which time zones do you want to see?',
     zone_list,default = ['America/Los_Angeles'])


for zone in selected_zone:
    st.markdown("zone: " + zone)
    time = now.astimezone(zoneinfo.ZoneInfo(zone))
    st.markdown(time.strftime("%Y-%m-%d %H:%M:%S"))


# now.astimezone(zoneinfo.ZoneInfo(zone))

# placeholder = st.empty()

# cnt = 0
# while True:
#     with placeholder.container():
#         placeholder.metric("Seconds since you arrived this page", cnt)
#         cnt += 1
        
#     time.sleep(1)