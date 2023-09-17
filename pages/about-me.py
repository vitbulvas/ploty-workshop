from dash import register_page, html
import dash_mantine_components as dmc

register_page(__name__)

about_me_text = (
    "Prvý kontakt s programovaním som mal ešte v študentských časoch a odvtedy sa moje kódovanie stalo "
    "súčasťou môjho DNA. Mojím poslaním je prinášať riešenia prostredníctvom kódu, ktoré majú skutočný "
    "dopad na svet. Vo svojej voľnej chvíli ma nájdete buď hlboko ponoreného do nového projektu alebo "
    "hľadajúceho inšpiráciu v prírode a technológii."
)

layout = dmc.Grid([
    dmc.Col([
        dmc.Grid([
            dmc.Col([
                dmc.Divider(label="Who am I?", size="sm")
            ])
        ]),
        dmc.Grid([
            dmc.Col(dmc.Text(about_me_text), sm=8),
            dmc.Col(dmc.Image(src="/assets/profile_picture_pingu.svg"), sm=4),
        ])
    ], sm=6, offsetSm=3, span=10, offset=1)
])
