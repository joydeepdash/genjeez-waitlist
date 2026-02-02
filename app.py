import streamlit as st
import streamlit_shadcn_ui as ui


#hide default Streamlit header bar
st.markdown("""
<style>
header { visibility: hidden; }
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
        
    st.form_submit_button("Submit")

    
