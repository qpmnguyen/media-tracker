from shiny import App, ui
from typing import List
from shiny import *
from shiny.types import NavSetArg
from shiny.ui import h4 


app_ui = ui.page_fluid(
    ui.navset_tab_card(
        ui.nav("a", "Tab a content")
    )
)

def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Effect
    def _():
        print("Current navbarpage ", input.navbar_id())

app = App(app_ui, server)