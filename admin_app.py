import streamlit as st

# --- Identity & Theme ---
st.set_page_config(page_title="Ghulam AI Admin", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #064e3b; color: white; }
    .stButton>button { background-color: #10b981; color: white; border-radius: 8px; border: none; }
    .stTextInput>div>div>input { background-color: #d1fae5; color: #064e3b; font-weight: bold; }
    .status-box { padding: 20px; border-radius: 10px; background-color: #059669; border-left: 5px solid #34d399; }
    </style>
    """, unsafe_allow_html=True)

# Master Identity
st.sidebar.markdown(f"### 🚀 Ghulam AI Studio\n**Admin:** Ghulam Hussain")

# Security Gateway
if "auth" not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("🔒 Admin Login")
        pwd = st.text_input("Master Password", type="password")
        if st.button("Unlock System"):
            if pwd == "GHULAM_HUSAIN_786":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Invalid Master Key!")
    st.stop()

# --- Main Admin UI ---
st.title("🛡️ Master Control Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["🔗 Database Sync", "🔑 Key Vault", "⚡ Kill-Switches", "💰 Payments"])

with tab1:
    st.header("Section 10: Firebase Master Sync")
    st.text_area("Paste Firebase JSON", placeholder="Paste your service account JSON here...", height=200)
    if st.button("Sync Globally"):
        st.toast("Success: System Synced!", icon="✅")

with tab2:
    st.header("9-Section Key Vault")
    col_a, col_b = st.columns(2)
    with col_a:
        st.text_input("Video AI Key", type="password")
        st.text_input("Image Gen Key", type="password")
    with col_b:
        st.text_input("Text Model Key", type="password")
        st.text_input("Voice API Key", type="password")
    st.button("Update Cloud Keys")

with tab3:
    st.header("Global Feature Kill-Switches")
    st.toggle("Enable AI Video Generation", value=True)
    st.toggle("Enable Voice Execution", value=True)
    st.toggle("Enable Live Vision/Camera", value=True)
    
    st.subheader("Voice Tuning")
    st.select_slider("Speech Speed", options=[0.5, 1.0, 1.5, 2.0], value=1.0)
    st.radio("Voice Gender", ["Male", "Female"])

with tab4:
    st.header("Payment Method Manager")
    st.text_input("Easypaisa Account", value="03461785207")
    st.text_input("JazzCash Account")
    st.text_input("Bank IBAN")
    if st.button("Save Payment Info"):
        st.success("User App Updated with New Payment Details!")
  
