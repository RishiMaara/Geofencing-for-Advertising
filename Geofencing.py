from geopy.distance import geodesic
import pandas as pd
geofence_center = (37.7749, -122.4194)
geofence_radius = 5000  
user_data = [
    {'user_id': 1, 'latitude': 37.7750, 'longitude': -122.4195},
    {'user_id': 2, 'latitude': 37.7800, 'longitude': -122.4200},
]

df = pd.DataFrame(user_data)
def is_inside_geofence(row):
    user_location = (row['latitude'], row['longitude'])
    distance = geodesic(geofence_center, user_location).meters
    return distance <= geofence_radius
df['inside_geofence'] = df.apply(is_inside_geofence, axis=1)
targeted_users = df[df['inside_geofence']]

print(targeted_users)
