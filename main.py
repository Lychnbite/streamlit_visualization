import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(filename):
    df = pd.read_excel(filename)
    return df

def main():
    st.title("Security Officer Skills Dashboard")

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.dataframe(df)

        st.subheader("Overall Skills Comparison (Bar Chart)")

        # Create a bar chart using Plotly
        fig_bar = px.bar(df, x='Name', y=df.columns[1:], barmode='group', title='Overall Skills Comparison')
        st.plotly_chart(fig_bar)

        st.subheader("Individual Skills (Pie Chart)")

        # Dropdown to select security officer
        selected_name = st.selectbox("Select a security officer", df['Name'])

        # Create a pie chart for selected officer
        selected_index = df[df['Name'] == selected_name].index[0]
        selected_officer = df.iloc[selected_index].drop('Name')  # Remove 'Name' column for pie chart
        fig_pie = px.pie(selected_officer, values=selected_officer.values, names=selected_officer.index,
                         title=f'Skills Distribution for {selected_name}')
        st.plotly_chart(fig_pie)

if __name__ == "__main__":
    main()
