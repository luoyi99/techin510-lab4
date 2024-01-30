"""
Change this to a world clock app
"""

import time

import streamlit as st

import os


try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

placeholder = st.empty()

cnt = 0
while True:
    with placeholder.container():
        placeholder.metric("Seconds since you arrived this page", cnt)
        cnt += 1
        
    time.sleep(1)