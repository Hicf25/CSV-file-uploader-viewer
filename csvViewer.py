import streamlit as st
import pandas as pd
from tkinter import messagebox

try:
    st.write(
        '''# CSV file uploader/viewer

        '''
    )

    up_file = st.file_uploader(label='Upload a csv file', type=['csv'])
    if up_file is not None:
        data = pd.read_csv(up_file)
        dataFrame = pd.DataFrame(data)
        st.dataframe(dataFrame)
except:
    messagebox.showinfo('There was an error')