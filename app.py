from dash import Dash, html, callback, Input, Output, State, page_container
import dash_mantine_components as dmc

from utils import navigacny_panel

app = Dash(__name__, use_pages=True)
server = app.server

# app.layout = dmc.Text("Hello World!")
# app.layout = html.Div([
#     dmc.NumberInput(
#         id="input-1",
#         label="First number:",
#     ),
#     dmc.NumberInput(
#         id="input-2",
#         label="Second number:",
#     ),
#     dmc.Button(
#         id="button",
#         children="Press me"
#     ),
#     dmc.Text(
#         id="output"
#     )
# ])
#
#
# @callback(
#     Output("output", "children"),
#     Input("button", "n_clicks"),
#     State("input-1", "value"),
#     State("input-2", "value"),
#     prevent_initial_call=True
# )
# def addition(n_clicks, value1, value2):
#     return value1 + value2

links = {
    "about-me": {"label": "About Me"},
    "experiences": {"label": "Experiences"},
    "projects": {"label": "Projects"},
    "contacts": {"label": "Contacts"},
    "addition-analysis": {"label": "Foo"},
}

app.layout = dmc.MantineProvider(
    [
        navigacny_panel(odkazy=links, logo="tabler:square-rounded-letter-v"),
        html.Div(page_container, style={"margin-top": "40px"})
    ],
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    id="provider-temy"
)


@callback(
    Output("provider-temy", "theme"),
    Input("tlacidlo-zmena-temy", "n_clicks"),
    State("provider-temy", "theme"),
    prevent_initial_call=True
)
def change_theme(n_clicks, theme):
    if theme["colorScheme"] == "dark":
        return {"colorScheme": "light"}
    else:
        return {"colorScheme": "dark"}


if __name__ == "__main__":
    app.run(debug=False)
