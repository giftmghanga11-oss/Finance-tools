import streamlit as st

st.set_page_config(page_title="Gift's Finance Tools", layout="wide")

pages = [
    st.Page("views/report.py", title="Report", icon="📊"),
    st.Page("views/bank_recons.py", title="Bank Recons", icon="🏦"),
    st.Page("views/mpesa_statement_consolidator.py", title="M-Pesa Statement Consolidator", icon="📱"),
    st.Page("views/c2b_form_filler.py", title="M-Pesa C2B Form Filler", icon="📝"),
]

st.navigation(pages).run()