"""
BigFix Console Application"""

import besapi
import besapi.plugin_utilities
from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Header, DataTable

global bes_conn

class BigFixConsoleApp(App):
    """A Textual app to manage BigFix actions."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(name="BigFix Console", show_clock=True)
        yield VerticalScroll(DataTable(id="actions_table", show_header=True, show_cursor=True))

    def on_mount(self) -> None:
        """Populate the DataTable with actions after mounting."""
        table = self.query_one(DataTable)
        # Define columns matching get_actions output
        columns = [
            "ID", "State", "Age", "Name", "Multiple", "Offer", "Has Source"
        ]
        table.add_columns(*columns)
        try:
            actions = get_actions()
            for action in actions:
                table.add_row(*[str(item) for item in action])
        except Exception as e:
            table.add_row("Error", str(e), "", "", "", "", "")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


def get_actions(issued_since_days=499):
    """Fetch actions from BigFix server."""
    global bes_conn
    session_relevance = f"""(id of it | 0, state of it | "UnknownState", now - time issued of it, name of it | "UnknownName", multiple flag of it, offer flag of it, exists source fixlet of it) of bes actions whose (state of it = "Open" AND top level flag of it AND time issued of it > (now - {issued_since_days}*day))"""
    return bes_conn.session_relevance_json(session_relevance)["result"]

def main():
    """Main entry point for the application."""

    parser = besapi.plugin_utilities.setup_plugin_argparse()
    args, _unknown = parser.parse_known_args()

    global bes_conn
    print("Connecting to BigFix server...")
    bes_conn = besapi.plugin_utilities.get_besapi_connection(args)

    if not bes_conn:
        print("Failed to connect to BigFix server.")
        return

    app = BigFixConsoleApp()
    app.run()

if __name__ == "__main__":
    main()
