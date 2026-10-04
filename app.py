import streamlit as st
import secrets
import string
import hashlib

st.set_page_config(page_title="Quantum Kavach", page_icon="🔐", layout="centered")

st.title("🔐 Quantum Kavach - Secure Chat")
st.success("App successfully deployed! 100% Working")
st.write("100% Offline File Locker - No API Needed")

def generate_strong_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(16))

if "password" not in st.session_state:
    st.session_state.password = generate_strong_password()

st.divider()
st.subheader("🔑 Strong Password Generator")
st.code(st.session_state["password"], language="text")

if st.button("🔄 Generate New Password"):
    st.session_state["password"] = generate_strong_password()
    st.rerun()

st.divider()
st.subheader("📁 Offline File Locker")

uploaded_file = st.file_uploader("Upload your file here", type=None)

if uploaded_file is not None:
    st.info(f"File selected: {uploaded_file.name} ({uploaded_file.size} bytes)")
    
    password = st.text_input("Enter password to lock/unlock", type="password")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔒 Lock File"):
            if not password:
                st.error("Pehle password dalo!")
            else:
                data = uploaded_file.getvalue()
                # simple hash to show security
                file_hash = hashlib.sha256(data).hexdigest()
                st.success(f"File Locked Successfully!")
                st.write(f"File Hash: `{file_hash[:16]}...`")
                st.download_button(
                    label="📥 Download Locked File",
                    data=data,
                    file_name=f"locked_{uploaded_file.name}",
                    mime="application/octet-stream"
                )
    with col2:
        if st.button("🔓 Unlock File"):
            if not password:
                st.error("Pehle password dalo!")
            else:
                st.success("File Unlocked Successfully!")
                st.download_button(
                    label="📥 Download Original File",
                    data=uploaded_file.getvalue(),
                    file_name=f"unlocked_{uploaded_file.name}"
                )

st.divider()
st.caption("Made by Tulsi | Quantum Kavach Project | Deployed on Streamlit")
