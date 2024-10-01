import streamlit as st
import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Simple Streamlit App")
    data = pd.DataFrame({
        'first column' : [i for i in range(1, 5, 1)],
        'second column' : [10*i for i in range(1, 5, 1)]
    })
    st.write("Here's our first attempt at using data to create a table")
    st.write(data)
    with st.form("Hello"):
        message = "Goodbye"
        submit = st.form_submit_button("Say hello")
        if(submit):
            message = "Why hello there!"
        st.write(message)
    randData = np.random.rand(20, 3)
    colVals = ['a', 'b', 'c'] 
    randDF = pd.DataFrame(data = randData,  columns = colVals)
    fig, ax = plt.subplots()
    ax.plot(randDF['a'], randDF['b'])
    st.pyplot(fig)

    

if __name__ == "__main__":
    main()
