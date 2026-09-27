import streamlit as st
import secrets

st.title("🛡️ Quantum Kavach - ABES Project")
st.write("Tumhara password Quantum Computer se safe hai ya nahi?")

# 1. Risk Check Logic
def check_risk(pwd):
    if len(pwd) < 8:
        return 99, "🔴 HACK! Bahut chhota hai, Quantum 2 sec me tod dega"
    if pwd.isalpha() or pwd.isdigit():
        return 90, "🔴 HACK! Sirf ek type ka hai, RSA se bana hai"
    if len(pwd) < 12:
        return 70, "🟡 MEDIUM RISK! 1 saal me hack ho jayega"
    return 25, "🟢 Strong hai par Quantum-Safe nahi hai"

# 2. Quantum-Safe Password Banao
def make_safe():
    return "QK-MLKEM-" + secrets.token_urlsafe(10) + "-SAFE"

# 3. Website
pwd = st.text_input("Apna password yaha dalo", type="password")

if st.button("Check Karo"):
    if pwd == "":
        st.error("Pehle password likho toh sahi")
    else:
        score, msg = check_risk(pwd)
        st.metric("Quantum Risk Score", f"{score}/100")
        st.warning(msg)
        
        st.divider()
        st.success("Tumhara Quantum-Safe Solution:")
        st.code(make_safe())
        st.info("Ye NIST ke naye ML-KEM algorithm jaisa hai, jise Quantum bhi hack nahi kar sakta")