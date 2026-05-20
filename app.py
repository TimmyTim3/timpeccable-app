import streamlit as st
import datetime
from twilio.rest import Client

# --- PAGE CONFIG ---
st.set_page_config(page_title="TIMpeccable Auto Spa", layout="wide")

# --- CSS STYLES ---
st.markdown("""
<style>
.graffiti-title { font-family: 'Permanent Marker', cursive; font-size: 50px; color: #00ffcc; text-shadow: 2px 2px #000; }
.section-header { color: #ff5733; border-bottom: 2px solid #ff5733; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Home", "Polls", "Reviews", "Trivia Central"])

# --- DATA: DAILY TRIVIA ---
def get_daily_trivia():
    today = datetime.date.today().day
    all_facts = [
        "Bird droppings are acidic; they can etch paint in 48 hours!",
        "Regular washes prevent rust buildup on the chassis.",
        "A clean car is more aerodynamic, improving fuel efficiency.",
        "Clear coat is the 'sunscreen' for your car's paint.",
        "Detailing can increase resale value by 10%.",
        "Tires contain UV inhibitors to stop cracking.",
        "Modern paint is applied in layers."
    ]
    return all_facts[today % (len(all_facts)-4) : today % (len(all_facts)-4) + 5]

# --- PAGES ---
if page == "Home":
    st.markdown('<h1 class="graffiti-title">✨ TIMpeccable Auto Spa</h1>', unsafe_allow_html=True)
    st.subheader('"For a TIMpeccable shine, every single time."')
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h2 class="section-header">Our Story</h2>', unsafe_allow_html=True)
        st.write("We restore your car's soul with precision.")
    with col2:
        st.markdown('<h2 class="section-header">Our Objective</h2>', unsafe_allow_html=True)
        st.write("World-class detailing for every customer.")
    
    st.write("---")
    st.markdown('<h2 class="section-header">Find Us</h2>', unsafe_allow_html=True)
    st.write("**📍 Address:** The Rock Hair Salon, Old Location, Bethlehem")
    st.write("**📞 Contact:** 065 913 2846 (WhatsApp/Calls)")

elif page == "Polls":
    st.header("📊 Customer Polls")
    poll = st.radio("What's your favorite wash?", ["Hand Wash", "Steam Clean", "Full Detail"])
    if st.button("Vote"):
        st.success(f"Thanks for voting for {poll}!")

elif page == "Reviews":
    st.header("⭐ Customer Reviews")
    review = st.text_area("Leave your feedback here:")
    if st.button("Submit Review"):
        st.success("Thank you for your feedback!")

elif page == "Trivia Central":
    st.header("💡 Daily Trivia")
    for fact in get_daily_trivia():
        st.info(fact)

# --- BOOKING (Visible on all pages) ---
st.sidebar.write("---")
if st.sidebar.button("Book an Appointment"):
    st.sidebar.write("Call 065 913 2846 to lock in your slot!")

