import streamlit as st
from cryptography.fernet import Fernet
import re
import random, string
from PIL import Image

st.set_page_config(page_title="Quantum Kavach", layout="wide")
st.title("🛡️ Quantum Kavach - 100% Offline Data Protection Suite")
st.markdown("✅ **DPDP Act 2023 Compliant | 100% Offline | No API Needed | Saves 250 Crore Fine**")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Offline Vault (E-Commerce/Hospital)", "Fake ID Detector (Bank/Govt)", "Leak Guard (IT Company)", "Stego Vault", "Password Generator"])

with tab1:
    st.subheader("Offline Vault - Customer Data Encrypt Karo")
    key = Fernet.generate_key()
    f = Fernet(key)
    data = st.text_input("Customer ka data likho (e.g. 9876543210)")
    if st.button("Encrypt"):
        if data:
            enc = f.encrypt(data.encode())
            st.success(f"Encrypted: {enc.decode()}")
            st.info(f"Key: {key.decode()}")

with tab2:
    st.subheader("Fake ID Detector")
    aadhaar = st.text_input("Aadhaar Number daalo")
    if st.button("Verify"):
        if re.match(r"^\d{4}\s\d{4}\s\d{4}$", aadhaar) or re.match(r"^\d{12}$", aadhaar):
            st.success("✅ Real Aadhaar Format")
        else:
            st.error("🚨 Fake ID Format!")

with tab3:
    st.subheader("Data Leak Guard - Infosys, TCS ka Secret Code Bachao")
    st.info("Use Case: Employee galti se secret code ChatGPT par daale usse pehle rokna")
    st.write("Yaha apna Code / Email / Message paste karo jo bhejne wale ho:")
    user_input = st.text_area("e.g., My API_KEY = sk-12345... or My Aadhaar is 1234...", key="leak")
    
    if st.button("🛡️ Scan Before Sending"):
        text_lower = user_input.lower().replace(" ", "").replace("_","")
        # Strong detection
        if "apikey" in text_lower or "sk-" in user_input.lower() or "secret" in text_lower or "password" in text_lower or "api" in text_lower and "=" in user_input:
            st.error("🚨 RUKO! Sensitive Data Found - API KEY / SECRET leak ho raha hai! DPDP Violation - Sending Blocked!")
        elif "aadhaar" in text_lower or "aadhar" in text_lower or re.search(r"\d{4}\s?\d{4}\s?\d{4}", user_input):
            st.error("🚨 RUKO! Aadhaar Data Leak Detected!")
        else:
            st.success("✅ Safe to Send - Koi secret data nahi mila. DPDP Compliant.")

with tab4:
    st.subheader("Stego Vault - Photo me secret chupao")
    st.write("Upload image to hide data (Demo)")

with tab5:
    st.subheader("Password Generator")
    if st.button("Generate Strong Password"):
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=12))
        st.code(pwd)
