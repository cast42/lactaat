import io

import lactate_thresholds as lt
import lactate_thresholds.zones as zones
import pandas as pd
from rich.console import Console
from rich.table import Table

# Edit this DATA constant with your measurements

DATA = """10 100 1.07 104 0.5 83
13 140 1.50 106 0.5 83
16 180 1.93 125 0.5 84
19 220 2.36 137 0.9 86
22 260 2.79 162 2.3 84
25 300 3.22 173 5.0 88
28 340 3.65 187 7.6 83
31 380 4.08 187 11.7 66"""


def dataframe_to_rich_table(df: pd.DataFrame, title: str = "") -> Table:
    """
    Convert a pandas DataFrame to a Rich Table.

    Args:
        df (pd.DataFrame): The pandas DataFrame to convert.
        title (str): The title of the table.

    Returns:
        Table: A Rich Table representation of the DataFrame.
    """
    table = Table(title=title)

    # Add columns
    for column in df.columns:
        table.add_column(column, justify="left", no_wrap=True)

    # Add rows
    for _, row in df.iterrows():
        table.add_row(*[str(value) for value in row])

    return table


# Load the data into a DataFrame
# Specify the delimiter as a space and use `decimal=','` to handle European decimal notation
df = pd.read_csv(
    io.StringIO(DATA),
    sep=" ",
    header=None,
    names=["time", "intensity", "intensity per kg", "heart_rate", "lactate", "rpm"],
    # decimal=",",
)

df["step"] = df.index + 1
df["length"] = 3

# Create a Rich Table
console = Console()
table = dataframe_to_rich_table(df, title="Measurement input")

# Print the table
console.print(table)


results = lt.determine(df, lactate_col="lactate")

console.print("lpt1", results.ltp1)
console.print("lpt2", results.ltp2)
console.print("lt2_estimate", results.lt1_estimate)
console.print("lt2_estimate", results.lt2_estimate)

zones_seiler3_df = zones.seiler_3_zones(results)
table_seiler_3 = dataframe_to_rich_table(zones_seiler3_df, title="Seiler 3 zones")
console.print()
console.print(table_seiler_3)

zones_seiler5_df = zones.seiler_5_zones(results)
table_seiler_5 = dataframe_to_rich_table(zones_seiler3_df, title="Seiler 5 zones")
console.print()
console.print(table_seiler_5)

zones_friel_7_zones_running_df = zones.friel_7_zones_running(results)
table_friel_7_zones_running = dataframe_to_rich_table(
    zones_friel_7_zones_running_df, title="Friel 7 zones running"
)
console.print()
console.print(table_friel_7_zones_running)

chart_heart_rate = lt.plot.heart_rate_intensity_plot(results)
chart_heart_rate.save("images/chart_heart_rate_intensity.html")
chart_heart_rate.save("images/chart_heart_rate_intensity.png")

chart_lactate = lt.plot.lactate_intensity_plot(results)
chart_lactate.save("images/chart_lactate_intensity.html")
chart_lactate.save("images/chart_lactate_intensity.png")
