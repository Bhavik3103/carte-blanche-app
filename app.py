import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def read_file(file):
    df=pd.read_csv(file)
    return df

def visuliazation(df):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df1=df[df["Device_id"]==1]
    # st.write(df1)
    df2=df[df["Device_id"]==2]
    df3=df[df["Device_id"]==3]
    colum=df.columns[2:]
    # st.write(colum)

    for i in colum:
        # plt.xticks(df["time"])
        st.write(i," Visulization")
        plt.plot(df1["time"],df1[i])
        plt.plot(df2["time"],df2[i])
        plt.plot(df3["time"],df3[i])
        plt.legend()
        st.pyplot()
    
    plt.legend()

    


def main():
    st.set_page_config(page_title="DFA to REGEX Converter", layout="wide", initial_sidebar_state="collapsed")

    st.title("CSV file reader and Visulization")
    with st.sidebar:
        st.header("Input Csv File")
        upload=st.file_uploader("Choose a CSV file",type="csv")

    if upload is not None:
        df=read_file(upload)

        st.subheader("Data")
        st.write(df)

        st.subheader("Visualization")
        visuliazation(df)


if __name__=='__main__':
    main()