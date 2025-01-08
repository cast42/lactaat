import io

import lactate_thresholds as lt
import lactate_thresholds.zones as zones
import pandas as pd
from rich.console import Console
from rich.table import Table


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


DATA = """60    89              1,5

100     102             1,7

140     109             1,5

180     126             4,2

220     142             2,5

260     168             6,1

300     175             12,7"""
# Replace multiple spaces with a single space and remove extra newlines
data_cleaned = "\n".join([" ".join(line.split()) for line in DATA.strip().split("\n")])

# Load the data into a DataFrame
# Specify the delimiter as a space and use `decimal=','` to handle European decimal notation
df = pd.read_csv(
    io.StringIO(data_cleaned),
    sep=" ",
    header=None,
    names=["intensity", "heart_rate", "lactate"],
    decimal=",",
)

df["step"] = df.index + 1
df["length"] = 4

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
chart_heart_rate.save("chart_heart_rate_intensity.html")

chart_lactate = lt.plot.lactate_intensity_plot(results)
chart_lactate.save("chart_lactate_intensity.html")
