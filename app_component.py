import streamlit as st
import numpy as np
import pandas as pd
#from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

#df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')


df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e']
)
#profile = pandas_profiling.ProfileReport(df)
#pr = df.profile_report()
#st_profile_report(pr)
