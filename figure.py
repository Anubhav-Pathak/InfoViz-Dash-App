import plotly.express as px
from plotly import graph_objects as go
import pandas as pd
import os

file_path = os.getcwd()
data = pd.read_excel(os.path.join(file_path, 'Dataset.xlsx'), sheet_name='Data' , nrows=10000)

# Plot 1
institutions = data['inst_name'].value_counts()
institutions = institutions[institutions > 50]
labels = institutions.index
sizes = institutions.values

fig1 = px.pie(names=labels, values=sizes)

# Plot 2
data_top50 = data.head(50)

start_authored = data_top50['nps (ns)'] 
first_authored = data_top50['cpsf (ns)'] 
last_authored = data_top50['npsfl (ns)'] 

df = pd.DataFrame({'start': start_authored, 'first': first_authored, 'last': last_authored})

last_authored = last_authored - first_authored
first_authored = first_authored - start_authored

fig3 = px.bar(
    data_frame=df,
    barmode='group', 
    labels={'variable': 'Publication Type', 'value':'Number of Publications', 'index':'Author Rank'},
)

# Plot 3
global_mean_c = data['c (ns)'].mean()
global_mean_nps = data['nps (ns)'].mean()
global_mean_ncs = data['ncs (ns)'].mean()
global_mean_h_index = data['h21 (ns)'].mean()
global_mean_rank = data['rank (ns)'].mean()

inst = data['inst_name'].value_counts().index

def get_inst(inst):
    fig4 = go.Figure()
    if inst is not None:
        for inst_name in inst: 
            data_inst = data[data['inst_name'] == inst_name]
            
            c = data_inst['c (ns)'].mean() / global_mean_c
            nps = data_inst['nps (ns)'].mean()/ global_mean_nps
            ncs = data_inst['ncs (ns)'].mean() / global_mean_ncs
            h_index = data_inst['h21 (ns)'].mean() / global_mean_h_index
            rank = data_inst['rank (ns)'].mean() / global_mean_rank

            fig4.add_trace(
                go.Scatterpolar(
                    theta=['C-Score','Papers','Citations','h-index','Rank'],
                    r=[c, nps, ncs, h_index, rank],
                    fill='toself',
                    name=inst_name
                ),
            )
    return fig4

# Plot 4    
df = data['cntry'].value_counts().reset_index()[2:]
df['cntry'] = df['cntry'].str.upper()

fig5 = px.choropleth(df, locations="cntry", color='count', color_continuous_scale=px.colors.sequential.Plasma)