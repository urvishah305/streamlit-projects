import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page title
st.title('NFL Football Stats (Rushing) Explorer')

st.markdown("""
This app performs simple webscraping of NFL Football player stats data (focusing on Rushing)!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

# Sidebar for user input
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2020))))

# Load data with modern caching
@st.cache_data
def load_data(year):
    url = f"https://www.pro-football-reference.com/years/{year}/rushing.htm"
    html = pd.read_html(url, header=1)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)  # Remove repeated headers
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats

playerstats = load_data(selected_year)

# Sidebar - Team and Position filters
sorted_unique_team = sorted([str(team) for team in playerstats['Team'].unique()])
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

unique_pos = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filter and make a deep copy to avoid SettingWithCopyWarning
df_selected_team = playerstats[
    playerstats['Team'].isin(selected_team) & playerstats['Pos'].isin(selected_pos)
].copy()

# Convert only mixed-type columns to strings to avoid ArrowTypeError
for col in df_selected_team.columns:
    if df_selected_team[col].apply(type).nunique() > 1:
        df_selected_team.loc[:, col] = df_selected_team[col].astype(str)


# Display filtered data
st.header('Display Player Stats of Selected Team(s)')
st.write(f"Data Dimension: {df_selected_team.shape[0]} rows and {df_selected_team.shape[1]} columns.")
st.dataframe(df_selected_team)

# CSV Download Link
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

# Heatmap Button
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    
    # Reload as numeric data
    df_numeric = playerstats[
        (playerstats['Team'].isin(selected_team)) & 
        (playerstats['Pos'].isin(selected_pos))
    ]
    df_numeric = df_numeric.select_dtypes(include='number')

    if df_numeric.empty:
        st.warning("No numeric data available to compute correlation.")
    else:
        corr = df_numeric.corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True

        with sns.axes_style("white"):
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.heatmap(corr, mask=mask, vmax=1, square=True, ax=ax, annot=True)
            st.pyplot(fig)
