import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="TIMpeccable Auto Spa", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');
.graffiti-title { font-family: 'Permanent Marker', cursive; font-size: 50px; color: #00ffcc; text-shadow: 2px 2px #000; }
.section-header { color: #ff5733; border-bottom: 2px solid #ff5733; }
</style>
""", unsafe_allow_html=True)

# --- RETRACTABLE MENU LOGIC ---
show_menu = st.sidebar.checkbox("Show/Hide Menu", value=True)

if show_menu:
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Polls", "Reviews", "Trivia Central"])
else:
    page = "Home"

# --- DATA: DAILY TRIVIA ---
def get_daily_trivia():
    today = datetime.date.today().day
    all_facts = [
        "Bird droppings are acidic; they can etch paint in 48 hours!",
        "Regular washes prevent rust buildup on the chassis.",
        "A clean car is more aerodynamic, improving fuel efficiency.",
        "Clear coat is the 'sunscreen' for your car's paint.",
        "Detailing can increase resale value by 10%."
    ]
    return all_facts

# --- PAGES ---
if page == "Home":
    st.markdown('<h1 class="graffiti-title">✨ TIMpeccable Auto Spa</h1>', unsafe_allow_html=True)
    st.subheader('"For a TIMpeccable shine, every single time."')
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h2 class="section-header">Our Story</h2>', unsafe_allow_html=True)
        st.write("Born from a passion for precision, we treat every vehicle like a luxury craft. We don't just wash cars; we restore their soul.")
    with col2:
        st.markdown('<h2 class="section-header">Our Objective</h2>', unsafe_allow_html=True)
        st.write("To provide world-class detailing that protects your investment and ensures you turn heads on every street corner.")
    
    st.write("---")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1601362840469-51e4d8d58785?w=500", caption="Precision Detailing")
    i2.image("https://images.unsplash.com/photo-1520340356584-f9951d1aaea6?w=500", caption="Interior Refresh")
    i3.image("https://images.unsplash.com/photo-1596422846543-75c6fc197f07?w=500", caption="Premium Shine")
    
    st.write("---")
    st.markdown('<h2 class="section-header">Find Us</h2>', unsafe_allow_html=True)
    st.write("**📍 Address:** The Rock Hair Salon, Old Location, Bethlehem")
    st.write("**📞 Contact:** 065 913 2846 (WhatsApp/Calls)")

elif page == "Polls":
    st.header("📊 Customer Polls")
    poll = st.radio("What's your favorite wash?", ["Hand Wash", "Steam Clean", "Full Detail"])
    if st.button("Vote"):
        st.success(f"Thanks for voting!")

elif page == "Reviews":
    st.header("⭐ Customer Reviews")
    review = st.text_area("Leave your feedback here:")
    if st.button("Submit Review"):
        st.success("Thank you!")

elif page == "Trivia Central":
    st.header("💡 Daily Trivia")
    for fact in get_daily_trivia():
        st.info(fact)

# --- SIDEBAR BOOKING ---
st.sidebar.write("---")
st.sidebar.markdown("### Ready for a shine?")
if st.sidebar.button("Book Now"):
    st.sidebar.write("Call 065 913 2846")

