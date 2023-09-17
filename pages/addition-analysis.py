from utils import priprava_dat
import dash_mantine_components as dmc
from dash import register_page, html, dcc, callback, Input, Output
from plotly.express import bar

register_page(__name__)

df = priprava_dat()  # `df` means `data frame`, it's usual Pandas syntax
print(df[["uzemi_txt", "vzdelani_txt", "hodnota"]])

layout = dmc.Stack([
    dmc.Select(
        id="select-area",
        value="Česká republika",
        label="Select Area",
        data=[{"value": v, "label": v} for v in df["uzemi_txt"].drop_duplicates().sort_values()],
    ),
    dcc.Graph(id="graf-vzdelania")
])


@callback(
    Output("graf-vzdelania", "figure"),
    Input("select-area", "value")
)
def graph_data(area):
    w_df = df.copy()  # working data frame
    w_df = w_df[w_df["uzemi_txt"] == area]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()

    fig = bar(w_df, x="vzdelani_txt", y="hodnota")

    return fig
