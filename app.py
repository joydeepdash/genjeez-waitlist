import streamlit as st
import streamlit_shadcn_ui as ui
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import re


#hide default Streamlit header bar
st.markdown("""
<style>
header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

#remove header bar gap
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


#choose theme
THEME = "quirk"
# options: "gradient" | "dark" | "minimal" | "quirk" | "none"

if THEME == "gradient":
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #fde2e4, #e0c3fc);
    }

    input {
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(8px);
        border-radius: 12px !important;
        border: 1px solid rgba(0,0,0,0.08) !important;
    }
    </style>
    """, unsafe_allow_html=True)

elif THEME == "dark":
    st.markdown("""
    <style>
    .stApp {
        background-color: #0f1117;
        color: white;
    }

    input {
        background-color: #1c1f26 !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid #2a2e38 !important;
    }

    input::placeholder {
        color: #9aa0aa !important;
    }
    </style>
    """, unsafe_allow_html=True)


elif THEME == "minimal":
    st.markdown("""
    <style>
    .stApp {
        background-color: #fafafa;
    }

    input {
        background-color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #e6e6e6 !important;
    }
    </style>
    """, unsafe_allow_html=True)


elif THEME == "quirk":
    st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }

    input {
        background-color: #fffdf8 !important;
        border-radius: 14px !important;
        border: 1px solid #f0e6d8 !important;
    }

    .subtle {
        font-style: italic;
        opacity: 0.75;
    }
    </style>
    """, unsafe_allow_html=True)



#st.title("Join the Genjeez Waitlist")
#we don't use the above since there's no way to center it
st.markdown("<h1 style = 'text-align: center;'>Join the Genjeez Waitlist</h1>", unsafe_allow_html = True)
if THEME == "quirk":
    st.markdown(
    "<p class='subtle'>A slower way to meet people.</p>",
    unsafe_allow_html=True)

#add a bit of spacing before the form
st.markdown("<br>", unsafe_allow_html=True)
    
st.caption("Enter your information below to be notified when Genjeez launches and for any important updates.")

with st.form("waitlist"):
    st.markdown("**Name**")
    name = ui.input(default_value = "", type = "text", placeholder = "What's your name?", key = "input1")

    st.markdown("**Email Address**")
    email = ui.input(default_value = "", type = "text", placeholder = "What's your email address?", key = "input2")

    st.markdown("**Instagram ID**")
    insta = ui.input(default_value = "", type = "text", placeholder = "What's your Instagram ID?", key = "input3")

    st.markdown("**Queries (optional)**")
    queries = ui.input(default_value = "", type = "text", placeholder = "Any queries?", key = "input4")
        
    submitted = st.form_submit_button("Submit")
    

#connecting to google sheet and caching the live handle
@st.cache_resource
def get_sheet():
    scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=scopes
    )
    client = gspread.authorize(creds)
    return client.open("Contact Information (Responses)").sheet1


#open the cached handle and check if email already exists else append and output message
sheet = get_sheet()
EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

if submitted:
    if not name or not email or not insta:
        st.error("Name, email address, and Instagram ID are required fields.")
        st.stop()

    if not re.match(EMAIL_REGEX, email):
        st.error("Enter a valid email address.")
        st.stop()
    
    emails_norm = [e.strip().lower() for e in sheet.col_values(3)]
    email_norm = email.strip().lower()
    if email_norm in emails_norm:
        st.warning("Submission already exists for this email.")
    else:
        sheet.append_row([datetime.now().isoformat(), name, email_norm, insta, queries])
        st.success("Thank you for your submission!")
    st.stop()
        

    
