import pandas as pd
import os

from analytics_api import analytics_api


def load_data():

    file_path = os.path.join(analytics_api.settings.BASE_DIR, 'mockupinterviewdata.csv')
    return pd.read_csv(file_path)


# Calculate conversion rates per customer_id
def calculate_conversion_rate(df):
    # Group by customer_id and aggregate the sums of conversions and revenue
    aggregated = df.groupby('customer_id').agg({
        'revenue': 'sum',
        'conversions': 'sum'
    }).reset_index()

    # Calculate conversion rate (conversions / revenue) for each customer
    aggregated['conversion_rate'] = aggregated['conversions'] / aggregated['revenue']

    highest = aggregated.loc[aggregated['conversion_rate'].idxmax()]
    lowest = aggregated.loc[aggregated['conversion_rate'].idxmin()]

    return aggregated, highest, lowest


# Analyze distribution of status across types and categories, and calculate total revenue and conversions per status
def status_based_analysis(df):
    # Group by status, type, and category and count the number of occurrences
    distribution = df.groupby(['status', 'type', 'category']).size().reset_index(name='count')

    # Group by status and sum up revenue and conversions
    revenue_conversions_by_status = df.groupby('status').agg({
        'revenue': 'sum',
        'conversions': 'sum'
    }).reset_index()

    return distribution, revenue_conversions_by_status


def category_type_performance(df):
    # Group by category and type to calculate total revenue and conversions
    grouped = df.groupby(['category', 'type']).agg({
        'revenue': 'sum',
        'conversions': 'sum'
    }).reset_index()

    top_combination = grouped.loc[grouped['conversions'].idxmax()]

    return grouped, top_combination


def filtered_aggregation(df):
    # Filter the data to include only rows where type is 'CONVERSION'
    filtered_df = df[df['type'] == 'CONVERSION']

    # Aggregate this filtered data to provide the average revenue and conversions per customer_id
    aggregated = filtered_df.groupby('customer_id').agg({
        'revenue': 'mean',
        'conversions': 'mean'
    }).reset_index()

    return aggregated