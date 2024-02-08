import streamlit as st
import time
import datetime
import zoneinfo
import freecurrencyapi as fca

# Connect to the Free Currency API
client = fca.Client("fca_live_lvjvJUaMcXEk1NXMpxsA3UmjMbOl3llsqdCUXK12")

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

st.divider()

# Currency Converter
st.header("Currency Converter")
currency_list = ["EUR", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK", "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD", "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"]
currency_list = client.currencies(currencies=currency_list)

currency_options = [f"{code} - {info['name']}" for code, info in currency_list['data'].items()]

col1, col2, col3 = st.columns([0.45,0.1,0.45])

with col1:
   option1 = st.selectbox('Select base currency', list(currency_options),key='currency1', index=1)
   st.write(f"1 {option1[:3]}")
   

with col3:
   option2 = st.selectbox('Select the currency you want to convert to', list(currency_options),key='currency2', index=0)
   exchange_rate = client.latest(base_currency=option1[:3], currencies=[option2[:3]])
   exchange_rate = exchange_rate['data'][option2[:3]]
   st.write(f"{exchange_rate} {option2[:3]}")



col4, col5, col6 = st.columns([0.45,0.1,0.45])   
with col4:
    number = st.number_input('Enter a number')

with col5:
    st.markdown("## => ##")

with col6:
    st.write("Converted Value")
    st.write(exchange_rate * number)

cnt = 0
while True:
    for i, zone in enumerate(selected_zones):
        current_time = datetime.datetime.now(tz=zoneinfo.ZoneInfo(zone))
        time_placeholders_1[i].metric(label=f"{zone}: ",value=f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        time_placeholders_2[i].metric(label=f"{zone}: ",value=f"{current_time.timestamp()}")
    # Wait for 1 second before updating again
    time.sleep(1)

