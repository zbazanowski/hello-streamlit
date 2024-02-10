import streamlit as st

st.title('st.secrets')

st.write(st.secrets['db_password'])
st.write(st.secrets['my_cool_secrets'])