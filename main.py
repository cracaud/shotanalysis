import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

st.set_page_config(layout="wide")

dfec = pd.read_csv("EC.csv", header=0, index_col=0)
dfproa = pd.read_csv("PROA.csv", header=0, index_col=0)
dfel = pd.read_csv("EL.csv", header=0, index_col=0)
dfgl = pd.read_csv("GL.csv", header=0, index_col=0)
dfnba = pd.read_csv("NBA.csv", header=0, index_col=0)

dfcomparison = pd.read_csv("COMPARISON.csv", header=0, index_col=0)
dfcomparisonrates = pd.read_csv("RATES COMPARISON.csv", header=0)
dfcomparisoneff = pd.read_csv("EFFICIENCY COMPARISON.csv", header=0)

# Calcul League Tables

# Calcul League Chart
dfproa2 = dfproa.drop(index=('Pro A'))
dfec2 = dfec.drop(index=('Eurocup'))
dfel2 = dfel.drop(index=('Euroleague'))
dfgl2 = dfgl.drop(index=('G-League'))
dfnba2 = dfnba.drop(index=('NBA'))

# Calcul League Comparison

#Calcul Team Bar Chart

#DISPLAY
#sidebar
st.sidebar.header('Filters')
st.sidebar.write("Type :")
datatype = st.sidebar.selectbox("",('League Table', 'Team Chart', "League Chart", "Leagues Comparison"), label_visibility="collapsed")
st.sidebar.write("Competition :")
competition = st.sidebar.selectbox("",('Pro A', 'Eurocup', 'Euroleague', 'NBA', 'G-League'), label_visibility="collapsed")

#core
st.title("Shooting Efficiency & Shot Selection")

if competition == "Eurocup" and datatype == "League Table" :
        st.subheader(competition)
        st.dataframe(dfec.style.format("{:.1f}%"), use_container_width=True, height=(21 + 1) * 35 + 3)
elif competition == "Pro A" and datatype == "League Table" :
    st.subheader(competition)
    st.dataframe(dfproa.style.format("{:.1f}%"), use_container_width=True, height=(19 + 1) * 35 + 3)
elif competition == "Euroleague" and datatype == "League Table" :
    st.subheader(competition)
    st.dataframe(dfel.style.format("{:.1f}%"), use_container_width=True, height=(19 + 1) * 35 + 3)
elif competition == "G-League" and datatype == "League Table" :
    st.subheader(competition)
    st.dataframe(dfgl.style.format("{:.1f}%"), use_container_width=True, height=(32 + 1) * 35 + 3)
elif competition == "NBA" and datatype == "League Table" :
    st.subheader(competition)
    st.dataframe(dfnba.style.format("{:.1f}%"), use_container_width=True, height=(31 + 1) * 35 + 3)
    
elif competition == "Pro A" and datatype == "League Chart" :
    st.subheader(competition)
    zoneselection = st.selectbox('Zones :',['0-8 ft', '8-16 ft', '16-24 ft', '3P'], label_visibility="collapsed")
    teams = dfproa2.index
    if zoneselection == "0-8 ft" :
        x = dfproa2['0-8 ft rate']
        y = dfproa2['0-8 ft %']
    elif zoneselection == "8-16 ft" :
        x = dfproa2['8-16 ft rate']
        y = dfproa2['8-16 ft %']
    elif zoneselection == "16-24 ft" :
        x = dfproa2['16-24 ft rate']
        y = dfproa2['16-24 ft %']
    elif zoneselection == "3P" :
        x = dfproa2['3P rate']
        y = dfproa2['3P %']
    else :
        x = 0
        y = 0
    fig1 = px.scatter(x=x, y=y, color=teams, text=teams, labels={"x": zoneselection+" rate", "y": zoneselection+" %"},)
    fig1.update_traces(textposition="bottom right", marker_size=20, marker_line_width=2)
    fig1.update_layout(height=500, font=dict(size=12), showlegend=False)
    st.plotly_chart(fig1, use_container_width=True, height=800)   
elif competition == "Eurocup" and datatype == "League Chart" :
    st.subheader(competition)
    zoneselection = st.selectbox('Zones :',['0-8 ft', '8-16 ft', '16-24 ft', '3P'], label_visibility="collapsed")
    teams = dfec2.index
    if zoneselection == "0-8 ft" :
        x = dfec2['0-8 ft rate']
        y = dfec2['0-8 ft %']
    elif zoneselection == "8-16 ft" :
        x = dfec2['8-16 ft rate']
        y = dfec2['8-16 ft %']
    elif zoneselection == "16-24 ft" :
        x = dfec2['16-24 ft rate']
        y = dfec2['16-24 ft %']
    elif zoneselection == "3P" :
        x = dfec2['3P rate']
        y = dfec2['3P %']
    else :
        x = 0
        y = 0
    fig1 = px.scatter(x=x, y=y, color=teams, text=teams, labels={"x": zoneselection+" rate", "y": zoneselection+" %"},)
    fig1.update_traces(textposition="bottom right", marker_size=20, marker_line_width=2)
    fig1.update_layout(height=500, font=dict(size=12), showlegend=False)
    st.plotly_chart(fig1, use_container_width=True, height=800)
elif competition == "Euroleague" and datatype == "League Chart" :
    st.subheader(competition)
    zoneselection = st.selectbox('Zones :',['0-8 ft', '8-16 ft', '16-24 ft', '3P'], label_visibility="collapsed")
    teams = dfel2.index
    if zoneselection == "0-8 ft" :
        x = dfel2['0-8 ft rate']
        y = dfel2['0-8 ft %']
    elif zoneselection == "8-16 ft" :
        x = dfel2['8-16 ft rate']
        y = dfel2['8-16 ft %']
    elif zoneselection == "16-24 ft" :
        x = dfel2['16-24 ft rate']
        y = dfel2['16-24 ft %']
    elif zoneselection == "3P" :
        x = dfel2['3P rate']
        y = dfel2['3P %']
    else :
        x = 0
        y = 0
    fig1 = px.scatter(x=x, y=y, color=teams, text=teams, labels={"x": zoneselection+" rate", "y": zoneselection+" %"},)
    fig1.update_traces(textposition="bottom right", marker_size=20, marker_line_width=2)
    fig1.update_layout(height=500, font=dict(size=12), showlegend=False)
    st.plotly_chart(fig1, use_container_width=True, height=800)
elif competition == "NBA" and datatype == "League Chart" :
    st.subheader(competition)
    zoneselection = st.selectbox('Zones :',['0-8 ft', '8-16 ft', '16-24 ft', '3P'], label_visibility="collapsed")
    teams = dfnba2.index
    if zoneselection == "0-8 ft" :
        x = dfnba2['0-8 ft rate']
        y = dfnba2['0-8 ft %']
    elif zoneselection == "8-16 ft" :
        x = dfnba2['8-16 ft rate']
        y = dfnba2['8-16 ft %']
    elif zoneselection == "16-24 ft" :
        x = dfnba2['16-24 ft rate']
        y = dfnba2['16-24 ft %']
    elif zoneselection == "3P" :
        x = dfnba2['3P rate']
        y = dfnba2['3P %']
    else :
        x = 0
        y = 0
    fig1 = px.scatter(x=x, y=y, color=teams, text=teams, labels={"x": zoneselection+" rate", "y": zoneselection+" %"},)
    fig1.update_traces(textposition="bottom right", marker_size=20, marker_line_width=2)
    fig1.update_layout(height=500, font=dict(size=12), showlegend=False)
    st.plotly_chart(fig1, use_container_width=True, height=800)
elif competition == "G-League" and datatype == "League Chart" :
    st.subheader(competition)
    zoneselection = st.selectbox('Zones :',['0-8 ft', '8-16 ft', '16-24 ft', '3P'], label_visibility="collapsed")
    teams = dfgl2.index
    if zoneselection == "0-8 ft" :
        x = dfgl2['0-8 ft rate']
        y = dfgl2['0-8 ft %']
    elif zoneselection == "8-16 ft" :
        x = dfgl2['8-16 ft rate']
        y = dfgl2['8-16 ft %']
    elif zoneselection == "16-24 ft" :
        x = dfgl2['16-24 ft rate']
        y = dfgl2['16-24 ft %']
    elif zoneselection == "3P" :
        x = dfgl2['3P rate']
        y = dfgl2['3P %']
    else :
        x = 0
        y = 0
    fig1 = px.scatter(x=x, y=y, color=teams, text=teams, labels={"x": zoneselection+" rate", "y": zoneselection+" %"})
    fig1.update_traces(textposition="bottom right", marker_size=20, marker_line_width=2)
    fig1.update_layout(height=500, font=dict(size=12), showlegend=False)
    st.plotly_chart(fig1, use_container_width=True, height=800)
    
elif competition == "Eurocup" and datatype == "Team Chart" :
    st.subheader(competition)
    teamselection = st.selectbox('Team :',['Paris Basketball', '7bet-Lietkabelis Panevezys', 'Aris Midea Thessaloniki', 'Besiktas Emlakjet Istanbul', 
                                               'Mincidelice JL Bourg en Bresse', 'Buducnost VOLI Podgorica', 'Cedevita Olimpija Ljubljana', 'Dolomiti Energia Trento', 
                                               'Dreamland Gran Canaria', 'Hapoel Shlomo Tel Aviv', 'Joventut Badalona', 'London Lions',
                                               'Prometey Slobozhanske', 'ratiopharm Ulm', 'Slask Wroclaw', 'Turk Telekom Ankara', 'U-BT Cluj-Napoca', 
                                               'Umana Reyer Venice', 'Veolia Towers Hamburg', 'Wolves Vilnius', 'Eurocup'], label_visibility="collapsed")
    dfec = dfec.reset_index(names=['teams'])
    dfec = dfec[dfec['teams'] == teamselection]
    dfec = dfec.reset_index(drop=True)
    dfperc = dfec.filter(items=['0-8 ft %', '8-16 ft %', '16-24 ft %', '3P %'])
    dfrate = dfec.filter(items=['0-8 ft rate', '8-16 ft rate', '16-24 ft rate', '3P rate'])
    perc = dfperc.loc[0, :].values.flatten().tolist()
    rate = dfrate.loc[0, :].values.flatten().tolist()
    fig2 = px.scatter(x=['0-8 ft', '8-16 ft', '16-24 ft', '3P'], y=perc, size=rate, labels={"x": "distance", "y": "efficiency", "size": "rate"})
    fig2.update_layout(yaxis_range=[0,80])
    st.plotly_chart(fig2, height=500) 
elif competition == "Pro A" and datatype == "Team Chart" :
    st.subheader(competition)
    teamselection = st.selectbox('Team :',['Paris', 'Blois', 'Boulogne-Levallois', 'Bourg-en-Bresse',  'Chalon/Saone', 'Cholet',
                                               'Dijon',  'Gravelines-Dunkerque', 'Le Mans', 'Le Portel', 'Limoges', 'Lyon-Villeurbanne', 'Monaco', 'Nancy',
                                               'Nanterre', 'Roanne', 'Saint-Quentin', 'Strasbourg', 'Pro A'], label_visibility="collapsed")
    dfproa = dfproa.reset_index(names=['teams'])
    dfproa = dfproa[dfproa['teams'] == teamselection]
    dfproa = dfproa.reset_index(drop=True)
    dfperc = dfproa.filter(items=['0-8 ft %', '8-16 ft %', '16-24 ft %', '3P %'])
    dfrate = dfproa.filter(items=['0-8 ft rate', '8-16 ft rate', '16-24 ft rate', '3P rate'])
    perc = dfperc.loc[0, :].values.flatten().tolist()
    rate = dfrate.loc[0, :].values.flatten().tolist()
    fig2 = px.scatter(x=['0-8 ft', '8-16 ft', '16-24 ft', '3P'], y=perc, size=rate, labels={"x": "distance", "y": "efficiency", "size": "rate"})
    fig2.update_layout(yaxis_range=[0,80])
    st.plotly_chart(fig2, height=500)
elif competition == "Euroleague" and datatype == "Team Chart" :
    st.subheader(competition)
    teamselection = st.selectbox('Team :',['LDLC ASVEL Villeurbanne', 'Crvena Zvezda Meridianbet Belgrade', 'Partizan Mozzart Bet Belgrade', 'Maccabi Playtika Tel Aviv', 
                                               'FC Barcelona', 'Anadolu Efes Istanbul', 'FC Bayern Munich', 'ALBA Berlin',
                                               'Zalgiris Kaunas', 'Virtus Segafredo Bologna', 'EA7 Emporio Armani Milan', 'Fenerbahce Beko Istanbul', 'Olympiacos Piraeus', 
                                               'Panathinaikos AKTOR Athens', 'Baskonia Vitoria-Gasteiz', 'Real Madrid', 'Valencia Basket', 'AS Monaco', 'Euroleague'], label_visibility="collapsed")
    dfel = dfel.reset_index(names=['teams'])
    dfel = dfel[dfel['teams'] == teamselection]
    dfel = dfel.reset_index(drop=True)
    dfperc = dfel.filter(items=['0-8 ft %', '8-16 ft %', '16-24 ft %', '3P %'])
    dfrate = dfel.filter(items=['0-8 ft rate', '8-16 ft rate', '16-24 ft rate', '3P rate'])
    perc = dfperc.loc[0, :].values.flatten().tolist()
    rate = dfrate.loc[0, :].values.flatten().tolist()
    fig2 = px.scatter(x=['0-8 ft', '8-16 ft', '16-24 ft', '3P'], y=perc, size=rate, labels={"x": "distance", "y": "efficiency", "size": "rate"})
    fig2.update_layout(yaxis_range=[0,80])
    st.plotly_chart(fig2, height=500)
elif competition == "NBA" and datatype == "Team Chart" :
    st.subheader(competition)
    teamselection = st.selectbox('Team :',['San Antonio Spurs', 'Denver Nuggets', 'Los Angeles Lakers', 'Golden State Warriors', 'Phoenix Suns',  'Charlotte Hornets', 'Atlanta Hawks',
                                               'Indiana Pacers',  'Washington Wizards', 'New York Knicks', 'Boston Celtics', 'Orlando Magic', 'Houston Rockets', 'Brooklyn Nets', 'Cleveland Cavaliers',
                                               'Miami Heat', 'Detroit Pistons', 'Toronto Raptors', 'Minnesota Timberwolves', 'Chicago Bulls', 'Oklahoma City Thunder', 'Memphis Grizzlies',
                                               'New Orleans Pelicans', 'Utah Jazz', 'Sacramento Kings', 'Dallas Mavericks', 'LA Clippers', 'Portland Trail Blazers', 'Milwaukee Bucks',
                                               'Philadelphia 76ers', 'NBA'], label_visibility="collapsed")
    dfnba = dfnba.reset_index(names=['teams'])
    dfnba = dfnba[dfnba['teams'] == teamselection]
    dfnba = dfnba.reset_index(drop=True)
    dfperc = dfnba.filter(items=['0-8 ft %', '8-16 ft %', '16-24 ft %', '3P %'])
    dfrate = dfnba.filter(items=['0-8 ft rate', '8-16 ft rate', '16-24 ft rate', '3P rate'])
    perc = dfperc.loc[0, :].values.flatten().tolist()
    rate = dfrate.loc[0, :].values.flatten().tolist()
    fig2 = px.scatter(x=['0-8 ft', '8-16 ft', '16-24 ft', '3P'], y=perc, size=rate, labels={"x": "distance", "y": "efficiency", "size": "rate"})
    fig2.update_layout(yaxis_range=[0,80])
    st.plotly_chart(fig2, height=500)
elif competition == "G-League" and datatype == "Team Chart" :
    st.subheader(competition)
    teamselection = st.selectbox('Team :',['Austin Spurs', 'Capital City Go-Go', 'Maine Celtics', 'Cleveland Charge', 'Wisconsin Herd',  'Delaware Blue Coats', 'Westchester Knicks',
                                               'Long Island Nets',  'Raptors 905', 'Birmingham Squadron', 'Iowa Wolves', 'Windy City Bulls', 'Memphis Hustle', 'Rio Grande Valley Vipers', 'Texas Legends',
                                               'Oklahoma City Blue', 'Mexico City Capitanes', 'Osceola Magic', 'G League Ignite', 'Ontario Clippers', 'Santa Cruz Warriors', 'Stockton Kings',
                                               'South Bay Lakers', 'Rip City Remix', 'Greensboro Swarm', 'Sioux Falls Skyforce', 'Indiana Mad Ants', 'Salt Lake City Stars', 'College Park Skyhawks', 'Grand Rapids Gold',
                                               'Motor City Cruise', 'G-League'], label_visibility="collapsed")
    dfgl = dfgl.reset_index(names=['teams'])
    dfgl = dfgl[dfgl['teams'] == teamselection]
    dfgl = dfgl.reset_index(drop=True)
    dfperc = dfgl.filter(items=['0-8 ft %', '8-16 ft %', '16-24 ft %', '3P %'])
    dfrate = dfgl.filter(items=['0-8 ft rate', '8-16 ft rate', '16-24 ft rate', '3P rate'])
    perc = dfperc.loc[0, :].values.flatten().tolist()
    rate = dfrate.loc[0, :].values.flatten().tolist()
    fig2 = px.scatter(x=['0-8 ft', '8-16 ft', '16-24 ft', '3P'], y=perc, size=rate, labels={"x": "distance", "y": "efficiency", "size": "rate"})
    fig2.update_layout(yaxis_range=[0,80])
    st.plotly_chart(fig2, height=500) 
    
elif datatype == "Leagues Comparison" :
    st.subheader("Shot Selection")
    fig = px.bar(dfcomparisonrates, x="leagues", y="percentages", color="zones", text="percentages")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.subheader("Shot Efficiency")
    fig = px.histogram(dfcomparisoneff, x="zones", y="percentages", color="leagues", barmode='group', text_auto=True)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.dataframe(dfcomparison.style.format("{:.1f}%"), use_container_width=True, height=(5 + 1) * 35 + 3)
else:
    st.subheader("Error")

# Add table with data for every charts