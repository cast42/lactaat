import io

import lactate_thresholds as lt
import lactate_thresholds.zones as zones
import pandas as pd

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

print(df)


results = lt.determine(df, lactate_col="lactate")

print("ltp1", results.ltp1)
print("lpt2", results.ltp2)
print("lt1_estimate", results.lt1_estimate)
print("lt2_estimate", results.lt2_estimate)

pd.reset_option("display.max_colwidth")

print("Seiler 3 zones:")
zones_seiler3_df = zones.seiler_3_zones(results)
print(zones_seiler3_df)

print("Seiler 5 zones:")
zones_seiler5_df = zones.seiler_5_zones(results)
print(zones_seiler5_df)

print("Friel 7 zones running:")
zones_friel_7_zones_running_df = zones.friel_7_zones_running(results)
print(zones_friel_7_zones_running_df)

chart_heart_rate = lt.plot.heart_rate_intensity_plot(results)
chart_heart_rate.save("chart_heart_rate_intensity.html")

chart_lactate = lt.plot.lactate_intensity_plot(results)
chart_lactate.save("chart_lactate_intensity.html")
