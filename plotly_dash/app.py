import pandas as pd
import datetime as dt
import os
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go

# 1. Klasa DB
class DB:
    def __init__(self):
        self.transactions = self._load_transactions()
        self.cc = pd.read_csv(r'db\country_codes.csv', index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv', index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')

    @staticmethod
    def _load_transactions():
        dfs = []  # lista do przechowywania pojedynczych DataFrame'ów
        for fn in os.listdir(r'db\transactions'):
            df = pd.read_csv(os.path.join(r'db\transactions', fn), index_col=0)
            dfs.append(df)  # dodajemy do listy
        transactions = pd.concat(dfs, ignore_index=True)  #łączenie DataFrame z metodą concatenate (nie append) -> kolejny błąd w kursie

        def convert_dates(x):
            try:
                return dt.datetime.strptime(x, '%d-%m-%Y')
            except:
                return dt.datetime.strptime(x, '%d/%m/%Y')

        transactions['tran_date'] = transactions['tran_date'].apply(convert_dates)
        return transactions


    def merge(self):
        df = self.transactions.join(
            self.prod_info.drop_duplicates('prod_cat_code')
                .set_index('prod_cat_code')['prod_cat'],
            on='prod_cat_code', how='left'
        )
        df = df.join(
            self.prod_info.drop_duplicates('prod_sub_cat_code')
                .set_index('prod_sub_cat_code')['prod_subcat'],
            on='prod_subcat_code', how='left'
        )
        cust_full = self.customers.join(self.cc, on='country_code')
        df = df.join(cust_full.set_index('customer_Id'), on='cust_id', how='left')
        self.merged = df

# 2. Przygotowanie danych
df = DB()
df.merge()

# 3. Inicjalizacja Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

# 4. Layout
app.layout = html.Div([
    html.Div([
        dcc.Tabs(id='tabs', value='tab-1', children=[
            dcc.Tab(label='Sprzedaż globalna', value='tab-1'),
            dcc.Tab(label='Produkty', value='tab-2'),
            dcc.Tab(label='Kanały sprzedaży', value='tab-3')            #dodana 3 zakładka
        ]),
        html.Div(id='tabs-content')
    ], style={'width': '80%', 'margin': 'auto'})
], style={'height': '100%'})

# 5. Callback na zmianę zakładki
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_tab(tab):
    if tab == 'tab-1':
        from tab1 import render_tab
        return render_tab(df.merged)
    elif tab == 'tab-2':
        from tab2 import render_tab
        return render_tab(df.merged)
    
    elif tab == 'tab-3':                        #dodana 3 zakładka
        from tab3 import render_tab
        return render_tab(df.merged)    
    
## tab1 callbacks
@app.callback(Output('bar-sales','figure'),
    [Input('sales-range','start_date'),Input('sales-range','end_date')])

def tab1_bar_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='M'),'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig


@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Mapa',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig


## tab2 callbacks
@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])
def tab2_barh_prod_subcat(chosen_cat):

    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))
    return fig


##tab3 callbacks

@app.callback(
    Output('customer-profile', 'figure'),
    Input('store-dropdown', 'value')
)
def update_customer_profile(store_type):
    df_filtered = df.merged[(df.merged['Store_type'] == store_type) & (df.merged['Gender'].notna())]

    grouped = df_filtered['Gender'].value_counts()

    fig = go.Figure(data=[go.Pie(labels=grouped.index, values=grouped.values)],
                   layout=go.Layout(title=f'Struktura płci klientów w kanale: {store_type}'))
    return fig


if __name__ == '__main__':
    app.run(debug=True)
