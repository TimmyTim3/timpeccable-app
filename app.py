import streamlit as st
import datetime
from twilio.rest import Client

st.set_page_config(page_title="TIMpeccable Auto Spa", layout="wide")

# --- DYNAMIC DAILY TRIVIA ---
def get_daily_trivia():
    today = datetime.date.today().day
    all_facts = [
        "Bird droppings are acidic; they can etch paint in 48 hours!",
        "Washing your car regularly prevents rust buildup on the chassis.",
        "A clean car is more aerodynamic and can improve fuel efficiency.",
        "Clear coat is the 'sunscreen' for your car's paint job.",
        "Professional detailing can increase your car's resale value by up to 10%.",
        # ... Add more here ...
    ]
    # Rotate the 5 facts based on the day
    start_idx = today % len(all_facts)
    return all_facts[start_idx : start_idx + 5]

# --- UI DESIGN ---
st.markdown("<h1 style='text-align: center; color: #00ffcc;'>✨ TIMpeccable Auto Spa</h1>", unsafe_allow_html=True)

# Image Grid
col1, col2, col3 = st.columns(3)
col1.image("https://images.unsplash.com/photo-1601362840469-51e4d8d58785?w=500", caption="Precision Detailing")
col2.image("https://images.unsplash.com/photo-1520340356584-f9951d1aaea6?w=500", caption="Interior Refresh")
col3.image("https://images.unsplash.com/photo-1596422846543-75c6fc197f07?w=500", caption="Premium Shine")

# Dynamic Trivia Section
st.subheader("💡 Today's Fun Facts & Trivia")
daily_facts = get_daily_trivia()
for i, fact in enumerate(daily_facts):
    st.info(f"{i+1}. {fact}")

# Booking Form
with st.form("booking"):
    name = st.text_input("Name")
    submitted = st.form_submit_button("Book Now")
    # (Rest of your booking logic remains the same)

