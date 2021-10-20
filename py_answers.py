import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import sys


def read_NYC_trips(path):
    """Read the taxi trips data in New York, converting a JSON string to pandas
    object.

    Args:
        path (str): JSON url string

    Returns:
        pandas.core.frame.DataFrame
    """
    return pd.read_json(path, lines=True)


# Load the trips to data frames
trips_NYC_2009 = read_NYC_trips(
    'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json')
trips_NYC_2010 = read_NYC_trips(
    'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json')
trips_NYC_2011 = read_NYC_trips(
    'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json')
trips_NYC_2012 = read_NYC_trips(
    'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json')

# Convert Pickup string to datetime.
trips_NYC_2009["pickup_datetime"] = pd.to_datetime(
    trips_NYC_2009["pickup_datetime"])
trips_NYC_2010["pickup_datetime"] = pd.to_datetime(
    trips_NYC_2010["pickup_datetime"])
trips_NYC_2011["pickup_datetime"] = pd.to_datetime(
    trips_NYC_2011["pickup_datetime"])
trips_NYC_2012["pickup_datetime"] = pd.to_datetime(
    trips_NYC_2012["pickup_datetime"])

# Convert Dropoff string to datetime.
trips_NYC_2009["dropoff_datetime"] = pd.to_datetime(
    trips_NYC_2009["dropoff_datetime"])
trips_NYC_2010["dropoff_datetime"] = pd.to_datetime(
    trips_NYC_2010["dropoff_datetime"])
trips_NYC_2011["dropoff_datetime"] = pd.to_datetime(
    trips_NYC_2011["dropoff_datetime"])
trips_NYC_2012["dropoff_datetime"] = pd.to_datetime(
    trips_NYC_2012["dropoff_datetime"])


# Union all the dataframes
all_trips_NYC = pd.concat(
    [trips_NYC_2009, trips_NYC_2010, trips_NYC_2011, trips_NYC_2012])

# ===Question 1 Section===
#
# Output
print("A distância média percorrida por viagens com no máximo 2 passageiros foi de {} milhas".format(
    np.round(all_trips_NYC[all_trips_NYC.passenger_count <= 2].trip_distance.mean(), decimals=3)))

# ===Question 2 Section===
#
# Load the CSV and assign it to the variable
vendor_lookup = pd.read_csv("https://s3.amazonaws.com/data-sprints-eng-test/data-vendor_lookup-csv.csv",
                            usecols=["vendor_id", "name"])

# JOIN all_trips_NYC with vendor_lookup on vendor_id
vendor_trip_merged = all_trips_NYC.merge(vendor_lookup, on="vendor_id")

# Output
print(vendor_trip_merged[["name", "total_amount"]
                         ].groupby("name").sum("total_amount").sort_values(by='total_amount', ascending=False).head(3))

# ===Question 3 Section===
#
#
payment_lookup = pd.read_csv(
    "https://s3.amazonaws.com/data-sprints-eng-test/data-payment_lookup-csv.csv", nrows=17, skiprows=1)

payment_trip_merged = all_trips_NYC.merge(
    payment_lookup, on="payment_type")

# Return the year-month of all trips which the payment type was Cash
cash_trips_by_month = payment_trip_merged["pickup_datetime"].dt.strftime('%Y-%m')[payment_trip_merged.payment_lookup ==
                                                                                  "Cash"].sort_values()

# Plot
plt.hist(cash_trips_by_month, bins=[*range(49)], edgecolor='black')
plt.title('Cash Trips by Year-Month')
plt.xlabel('Year-Month')
plt.ylabel('Total Trips')
plt.tight_layout()
plt.show()

# ===Question 4 Section===
#
# WHERE statement to extract the last 3 months of 2012
end_year_expression = (trips_NYC_2012["pickup_datetime"].dt.month == 10) | (trips_NYC_2012[
    "pickup_datetime"].dt.month == 11) | (trips_NYC_2012["pickup_datetime"].dt.month == 12)

# Load the datetime and tips in a Series
datetime_tips_series = trips_NYC_2012[end_year_expression][trips_NYC_2012.tip_amount != 0].groupby(
    trips_NYC_2012.pickup_datetime.dt.strftime('%m-%d')).tip_amount.size()

# Convert Serie to DataFrame
df = datetime_tips_series.to_frame()

# List with the tip_amount sizes grouped by day
tips = [row for row in df["tip_amount"]]

# List of days of the las 3 month
dates = pd.date_range(start='2012-10-01', end='2012-12-31').tolist()

# Plot
plt.title('Number of tips each day for the last 3 months of 2012')
plt.xlabel('Month-Day')
plt.ylabel('Number of tips')
x_values = dates
y_values = tips + [0]*65
ax = plt.gca()
formatter = mdates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(formatter)
plt.plot(x_values, y_values)

# ===Bônus Section===
#
# WHERE statement to extract weekend days
weekend_expression = (trips_NYC_2009["pickup_datetime"].dt.weekday == 5) | (trips_NYC_2009[
    "pickup_datetime"].dt.weekday == 6)

# Output
print("O tempo médio das corridas nos dias de sábado e domingo foi de {}".format(all_trips_NYC["dropoff_datetime"][weekend_expression].sub(
    all_trips_NYC["pickup_datetime"][weekend_expression]).mean()))
