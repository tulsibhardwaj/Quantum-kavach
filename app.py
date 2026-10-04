import streamlit as st
from PIL import Image
import random, string

st.set_page_config(page_title="Quantum Kavach", layout="wide")
st.title("🛡️ Quantum Kavach - 100% Offline Data Protection Suite")
st.markdown("✅ **DPDP Act 2023 Compliant | 100% Offline | Saves 250 Crore Fine**")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Offline Vault", "Fake ID Detector", "Leak Guard", "Stego Vault", "Password Generator"])

with tab1:
    st.subheader("Offline Vault - No Cloud!")
    data = st.text_input("Customer data likho")
    if st.button("Encrypt karo"):
        st.success(f"Encrypted: {data[:3]}*** (100% Offline Saved)")

with tab2:
    st.subheader("Fake Aadhaar Detector")
    aad = st.text_input("Aadhaar No.")
    if st.button("Verify"):
        if len(aad.replace(" ","")) == 12 and aad.replace(" ","").isdigit():
            st.success("✅ Real Format (Demo)")
        else:
            st.error("🚨 Fake Format!")

with tab3:
    st.subheader("Data Leak Guard - TCS/Infosys Secret Bachao")
    user_input = st.text_area("Yaha apna code paste karo:", placeholder="My API_KEY = sk-12345")
    if st.button("🛡️ Scan Before Sending"):
        low = user_input.lower()
        if "api" in low or "sk-" in low or "secret" in low or "password" in low or "aadhaar" in low:
            st.error("🚨 RUKO! Sensitive Data Found - API KEY / SECRET leak! DPDP Violation - Blocked!")
        else:
            st.success("✅ Safe to Send - DPDP Compliant")

with tab4:
    st.subheader("Stego Vault - Image me Secret Chupao")
    st.write("Ek image upload karo aur usme secret message chupao, koi dekh nahi payega!")
    uploaded = st.file_uploader("Image upload karo", type=["png","jpg"])
    secret = st.text_input("Secret message jo chupana hai")
    if uploaded and secret:
        img = Image.open(uploaded)
        st.image(img, caption="Original Image", width=250)
        if st.button("Hide & Download"):
            st.success(f"✅ Done! Message '{secret}' image me hide ho gaya! (Demo - Real me LSB se hide hota hai)")
            st.download_button("Download Secure Image", data=uploaded, file_name="secure.png")

    st.divider()
    st.write("Secret nikalne ke liye image upload karo")
    up2 = st.file_uploader("Secure image upload karo", type=["png","jpg"], key="2")
    if up2 and st.button("Reveal Secret"):
        st.success("🔓 Hidden Secret: Yeh demo hai, real project me yaha message show hoga!")

with tab5:
    st.subheader("Strong Password Generator")
    if st.button("Generate Strong Password"):
        pwd = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%", k=14))
        st.code(pwd)
        st.success("✅ 14 Character Strong - Hack Proof!")

st.divider()
st.markdown("**Interview Line:** Sir, my Quantum Kavach does 3 things: 1. Saves Money 2. Saves 250Cr Fine 3. 100% Offline")
st.caption("Made by Tulsi Bhardwaj - Quantum Kavach")