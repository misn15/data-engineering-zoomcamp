import pandas as pd

# read in data files
path = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet"
df = pd.read_parquet(path)
zones = pd.read_csv("https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv")

# Question 3 Counting Short Trips
# For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), 
# how many trips had a trip_distance of less than or equal to 1 mile?

df = df[(df['lpep_pickup_datetime'] >= '2025-11-01') & (df['lpep_pickup_datetime'] < '2025-12-01')]
df_short_trips = df[df['trip_distance'] <= 1.0]
df_short_trip_count = df_short_trips.shape[0]
print(f"Number of trips with trip_distance <= 1 mile in November 2025: {df_short_trip_count}")

# Question 4 Longest trip for each day
# Which was the pick up day with the longest trip distance? 
# Only consider trips with trip_distance less than 100 miles (to exclude data errors).

longest_trip = df[df['trip_distance'] < 100]
maxx = longest_trip.loc[longest_trip['trip_distance'].idxmax()][['lpep_pickup_datetime']]
print(f"Pick up day with the longest trip distance: {maxx['lpep_pickup_datetime'].date()}")

# Question 5 Biggest pickup zone
# Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

df = df.merge(zones, left_on='PULocationID', right_on='LocationID', how='left')
df_nov_18 = df[df['lpep_pickup_datetime'].dt.date == pd.Timestamp('2025-11-18').date()]
largest_pickup_zone = df_nov_18.groupby(['Zone'])['total_amount'].sum().reset_index()
max_zone = largest_pickup_zone.loc[largest_pickup_zone['total_amount'].idxmax()]
print(f"Pickup zone with the largest total_amount on November 18th, 2025: {max_zone['Zone']} with total amount {max_zone['total_amount']}")

# Question 6. Largest tip
# For the passengers picked up in the zone named "East Harlem North" in November 2025, 
# which was the drop off zone that had the largest tip?

df = df.merge(zones, left_on='DOLocationID', right_on='LocationID', how='left', suffixes=['', '_DO'])
east_harlem_north_trips = df[df['Zone'] == 'East Harlem North']
largest_tip_dropoff_zone = east_harlem_north_trips.loc[east_harlem_north_trips['tip_amount'].idxmax()]
print(f"Drop off zone with the largest tip for pickups in East Harlem North: {largest_tip_dropoff_zone['Zone_DO']} with tip amount {largest_tip_dropoff_zone['tip_amount']}")
