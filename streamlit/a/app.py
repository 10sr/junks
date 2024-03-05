#!/usr/bin/env python -m streamlit run
# https://docs.streamlit.io/get-started/installation/command-line
# https://docs.streamlit.io/get-started/fundamentals/main-concepts

import streamlit as st
# Installed with streamlit!
import pandas as pd
import numpy as np

st.write("Hello world")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

# same as st.write(df) ?
df

"abc"


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
