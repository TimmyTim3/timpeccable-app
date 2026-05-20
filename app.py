import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="TIMpeccable Auto Spa", layout="wide")

# --- CUSTOM CSS & GRAFFITI FONTS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&family=Roboto:wght@300;400&display=swap');
.graffiti-title { font-family: 'Permanent Marker', cursive; font-size: 50px; color: #00ffcc; text-shadow: 2px 2px #000; }
.slogan { font-family: 'Permanent Marker', cursive; font-size: 24px; color: #ffffff; }
.section-header { font-family: 'Roboto', sans-serif; font-weight: 400; color: #ff5733; border-bottom: 2px solid #ff5733; }
.trivia-box { background-color: #f9f9f9; padding: 15px; border-radius: 10px; color: #333; border-left: 5px solid #00ffcc; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<h1 class="graffiti-title">✨ TIMpeccable Auto Spa</h1>', unsafe_allow_html=True)
st.markdown('<p class="slogan">"For a TIMpeccable shine, every single time."</p>', unsafe_allow_html=True)

# --- STORY & OBJECTIVE ---
col1, col2 = st.columns(2)
with col1:
    st.markdown('<h2 class="section-header">Our Story</h2>', unsafe_allow_html=True)
    st.write("Born from a passion for precision, we treat every vehicle like a luxury craft. We don't just wash cars; we restore their soul.")
with col2:
    st.markdown('<h2 class="section-header">Our Objective</h2>', unsafe_allow_html=True)
    st.write("To provide world-class detailing that protects your investment and ensures you turn heads on every street corner.")

st.write("---")

# --- TRIVIA SECTION ---
st.markdown('<h2 class="section-header">Did You Know?</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="trivia-box">
<b>🚗 Car Care Trivia:</b> Bird droppings can etch into your car's clear coat within 48 hours due to their high acidity. 
Professional cleaning isn't just about looks—it's vital for your paint's long-term health!
</div>
""", unsafe_allow_html=True)

# --- BOOKING FORM ---
with st.form("booking_form"):
    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    package = st.selectbox("Choose a Package", ["The TIMe Saver", "The TIMpeccable Standard", "The Executive Detail"])
    submitted = st.form_submit_button("Secure My Booking")
    
    if submitted:
        try:
            sms_text = f"New Booking: {name} ({phone}) for {package}."
            # Accessing keys from the Vault
            client = Client(st.secrets["TWILIO_ACCOUNT_SID"], st.secrets["TWILIO_AUTH_TOKEN"])
            client.messages.create(from_=st.secrets["TWILIO_NUMBER"], body=sms_text, to="+27659132846")
            st.success("Booking Request Received! We'll be in touch.")
        except Exception as e:
            st.error("Booking saved, but notification failed. Please call us directly!")

# --- LOCATION & CONTACT ---
st.write("---")
st.markdown('<h2 class="section-header">Find Us</h2>', unsafe_allow_html=True)
st.write("**📍 Address:** The Rock Hair Salon, Old Location, Bethlehem")
st.write("**📞 Contact:** 065 913 2846 (WhatsApp/Calls)")
st.write("**📱 Facebook:** [Timmy Tim](https://www.facebook.com)")

