import streamlit as st
import streamlit_shadcn_ui as ui

#st.title("Join the Genjeez Waitlist")
#we don't use the above since there's no way to center it
st.markdown("<h1 style = 'text-align: center;'>Join the Genjeez Waitlist</h1>", unsafe_allow_html = True)
st.caption("Enter your information below to be notified when Genjeez launches and for any important updates.")

with st.form("waitlist"):
    st.markdown("**Name**")
    name = ui.input(default_value = "", type = "text", placeholder = "What's your name?", key = "input1")

    st.markdown("**Email Address**")
    name = ui.input(default_value = "", type = "text", placeholder = "What's your email address?", key = "input2")

    st.markdown("**Instagram ID**")
    name = ui.input(default_value = "", type = "text", placeholder = "What's your Instagram ID?", key = "input3")

    st.markdown("**Queries**")
    name = ui.input(default_value = "", type = "text", placeholder = "Any queries?", key = "input4")
        
    st.form_submit_button("Submit")

    
