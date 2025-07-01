from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

def render_tab(df):
    layout = html.Div([
        html.H1('Sprzedaż globalna', style={'text-align': 'center'}),
        html.Div([
            dcc.DatePickerRange(
                id='sales-range',
                start_date=df['tran_date'].min(),
                end_date=df['tran_date'].max(),
                display_format='YYYY-MM-DD'
            )
        ], style={'width': '100%', 'text-align': 'center'}),
        html.Div([
            html.Div([dcc.Graph(id='bar-sales')], style={'width': '50%'}),
            html.Div([dcc.Graph(id='choropleth-sales')], style={'width': '50%'})
        ], style={'display': 'flex'})
    ])
    return layout


def create_bar_sales_figure(df, start_date, end_date):
    truncated = df[(df['tran_date'] >= start_date) & (df['tran_date'] <= end_date)]
    grouped = truncated[truncated['total_amt'] > 0].groupby([pd.Grouper(key='tran_date', freq='M'), 'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(
            x=grouped.index,
            y=grouped[col],
            name=col,
            hoverinfo='text',
            hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]
        ))

    fig = go.Figure(data=traces)
    fig.update_layout(title='Przychody', barmode='stack', legend=dict(x=0, y=-0.5))

    return fig


def create_choropleth_sales_figure(df, start_date, end_date):
    truncated = df[(df['tran_date'] >= start_date) & (df['tran_date'] <= end_date)]
    grouped = truncated[truncated['total_amt'] > 0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(
        colorscale='Viridis',
        reversescale=True,
        locations=grouped.index,
        locationmode='country names',
        z=grouped.values,
        colorbar=dict(title='Sales')
    )

    fig = go.Figure(data=[trace0])
    fig.update_layout(title='Mapa', geo=dict(showframe=False, projection={'type': 'natural earth'}))

    return fig
