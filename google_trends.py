from pytrends.request import TrendReq

from graph_output import ascii_colorful_horizontal_bar_chart

import pandas as pd
from pytrends.request import TrendReq

def sort_by_popularity(topics):
    def fetch_interest_over_time(topics):
        pytrends = TrendReq(hl='en-US', tz=360)
        data_frames = []

        for topic in topics:
            pytrends.build_payload(kw_list=[topic])
            interest_over_time_df = pytrends.interest_over_time()
            data_frames.append(interest_over_time_df[topic])

        return pd.concat(data_frames, axis=1)

    # Fetch interest over time data for all topics
    interest_over_time_data = fetch_interest_over_time(topics)

    # Calculate the average popularity for each topic
    average_popularity = interest_over_time_data.mean(axis=0)

    # Normalize the popularity scores
    normalized_popularity = (average_popularity - average_popularity.min()) / (average_popularity.max() - average_popularity.min())

    # Sort the topics by their normalized popularity
    sorted_topics = normalized_popularity.sort_values(ascending=False)

    # Print or use the sorted topics as needed
    return sorted_topics

def get_trend(topic):
    # Create a pytrends object
    pytrends = TrendReq(hl='en-US', tz=360)

    # Build the payload
    pytrends.build_payload(kw_list=[topic])

    # Get interest over time
    interest_over_time_df = pytrends.interest_over_time()

    ttime_labels = interest_over_time_df.index
    vvalues = interest_over_time_df[topic].tolist()

    time_labels = []
    values = []

    start = False
    for i in range(len(vvalues)):
        if vvalues[i] != 0:
            start = True

        if start:
            values.append(vvalues[i])
            time_labels.append(ttime_labels[i])

    N = 10
    INTERVAL = len(values) // N

    com_values = []
    com_time_labels = []

    for i in range(0, len(values), INTERVAL):
        average = 0
        for j in range(i, i + INTERVAL):
            average += values[i]
        average /= INTERVAL

        com_values.append(average)
        com_time_labels.append(time_labels[i])

    ascii_colorful_horizontal_bar_chart(com_time_labels, com_values)
