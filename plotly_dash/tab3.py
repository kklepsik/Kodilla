from dash import html, dcc, Input, Output
import plotly.graph_objs as go
import pandas as pd

def render_tab(df):
    # Dni tygodnia jako liczby i nazwy
    df = df[df['total_amt'] > 0].copy()
    df['weekday'] = df['tran_date'].dt.day_name()

    # Tworzymy wykres słupkowy: dzień tygodnia vs sprzedaż, podzielone wg Store_type
    grouped = df.groupby(['weekday', 'Store_type'])['total_amt'].sum().reset_index()

    # Kolejność dni
    weekdays_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    grouped['weekday'] = pd.Categorical(grouped['weekday'], categories=weekdays_order, ordered=True)
    grouped = grouped.sort_values('weekday')

    traces = []
    for store in grouped['Store_type'].unique():
        subset = grouped[grouped['Store_type'] == store]
        traces.append(go.Bar(x=subset['weekday'], y=subset['total_amt'], name=store))

    bar_fig = go.Figure(data=traces, layout=go.Layout(title='Sprzedaż wg dni tygodnia i kanału sprzedaży', barmode='group'))

    # Dropdown + drugi wykres
    layout = html.Div([
        html.H1('Kanały sprzedaży', style={'textAlign': 'center'}),

        dcc.Graph(id='bar-weekday-sales', figure=bar_fig),

        html.Div([
            dcc.Dropdown(
                id='store-dropdown',
                options=[{'label': store, 'value': store} for store in df['Store_type'].dropna().unique()],
                value=df['Store_type'].dropna().unique()[0],
                style={'width': '50%'}
            ),
            dcc.Graph(id='customer-profile')
        ])
    ])
    return layout
