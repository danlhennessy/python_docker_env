"""
This script is used to extract data from the OpenPowerlifting database and
display it in a Streamlit app. The data is used to investigate the correlation
between age and 1rm strength in the deadlift for the 90kg weight class.
"""

import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px


def titles():
    """
    Writes titles for streamlit
    """
    st.title("Age/Strength correlation in Powerlifting")
    st.write("Data source: http://old.openpowerlifting.org/data.html")
    st.write("Weight Class: 90kg")
    st.header(" ")


df = pd.read_csv(
    './entries.csv'
    )


def organise_data(dataframe):
    """
    Splits out just data for 90kg weight class, and for deadlift only.
    Returns a shortened dataframe with above restrictions.
    """
    weightclass_ninety = dataframe[dataframe['WeightClassKg'] == '90']
    deadlift_ninety = weightclass_ninety[
        ['Age', 'Best3DeadliftKg']
        ].dropna(axis=0)
    deadlift_ninety['Best3DeadliftKg'] = deadlift_ninety[
        'Best3DeadliftKg'
        ].abs()
    deadlift_ninety.rename(
        columns={'Best3DeadliftKg': 'Deadlift 1RM (kg)'},
        inplace=True
        )
    return deadlift_ninety


def chart_data(dataframe):
    """
    Creates a scatter plot of the data, with a lowess trendline.
    Chart will adapt to changes to the age range slider.
    """
    fig = px.scatter(
        dataframe,
        x='Age',
        y='Deadlift 1RM (kg)',
        trendline="lowess",
        trendline_color_override="red"
        )
    st.plotly_chart(fig)


def calculate_coefficients(dataframe):
    """Calculates Pearson's r, Spearman's rho and Kendall's tau coefficients
    """
    ages = dataframe['Age'].to_numpy()
    lifts = dataframe['Deadlift 1RM (kg)'].to_numpy()
    pearson, spearman, kendalltau = (scipy.stats.pearsonr(ages, lifts),
                                     scipy.stats.spearmanr(ages, lifts),
                                     scipy.stats.kendalltau(ages, lifts))
    st.write(f"""Coefficients:\n
    Pearson's r = {pearson[0]}\n
    Spearman's rho = {spearman[0]}\n
    Kendall's tau = {kendalltau[0]}
    """)


if __name__ == '__main__':
    titles()
    data = organise_data(df)
    lower, upper = st.slider("Age Range", value=[7, 90])
    data = data[(data.Age >= lower) & (data.Age <= upper)]
    chart_data(data)
    calculate_coefficients(data)
