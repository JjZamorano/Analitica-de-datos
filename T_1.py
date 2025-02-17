import pandas as pd
import numpy as np


df_csv_visual = pd.read_csv("listings.csv")


columnas_mantener = [
    'id', 'listing_url', 'scrape_id', 'last_scraped', 'source', 'name',
    'description', 'neighbourhood', 'host_id', 'host_name', 'host_since',
    'host_is_superhost', 'neighbourhood_cleansed', 'latitude', 'longitude',
    'property_type', 'room_type', 'accommodates', 'bathrooms', 'bedrooms',
    'beds', 'amenities', 'price', 'minimum_nights', 'maximum_nights',
    'has_availability', 'availability_30', 'availability_60', 'availability_90',
    'calendar_last_scraped', 'number_of_reviews', 'first_review', 'last_review',
    'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',
    'review_scores_checkin', 'review_scores_communication', 'review_scores_location',
    'review_scores_value', 'license', 'instant_bookable',
    'calculated_host_listings_count', 'reviews_per_month', 'host_identity_verified',
    'host_listings_count', 'host_location', 'host_about', 'host_response_time',
    'host_neighbourhood', 'neighborhood_overview'
]

df_filtered = df_csv_visual[columnas_mantener]

print(df_filtered.info())
