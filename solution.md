## Solution Explanation

I began by examining the challenge dataset and identified outlier data points, which I filtered out to focus on the central results.

Upon reviewing the exercise, I opted for a statistical approach to address the problem. While a symmetric dataset would have allowed for an equal division of the problem, I chose a two-fold strategy:

1. **Model Creation with K-Means Algorithm:**
   I employed the K-means algorithm to create a model that reduces the amount of data. I divided the data into 10 different regions, considering that there were 481 entry rows for training. The goal was to proportionally distribute the data, with approximately 48 points per cluster if the data were symmetrical.

2. **Database Storage and Querying:**
   I stored the data in a database for improved data type treatment and querying. Each food truck was associated with a cluster ID for better organization and retrieval efficiency.

3. **Live Algorithm for Finding 5 Closest Food Trucks:**
   Initially considering a radix sort solution, I later opted for the KDTree, which proved effective for geographical coordinates. Despite a warning about its scalability for large samples due to data structure loading, its O(n*log(n)) time complexity made it a suitable choice.

In conclusion, I developed a model with K-means to classify regions where each food truck operates. For REST API requests, the code follows these steps:

- Identifies the cluster based on the latitude and longitude from the input arguments using the trained K-means model built with preprocessed data.
- Filters the database to retrieve all objects corresponding to that area.
- Finds and displays the 5 closest trucks.

Please check out the Jupyter notebooks in the "study" folder for further details.
