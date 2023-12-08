## Solution explanation


I started by studying the data provided in the challenge.
Found outlier points of data that I filtered with the central results.


By inspection of the exercise I chose a statistical method to tackle the problem.
If the data was simetric I could divide the problem in equal parts and define the regions where to search for a food truck in equal parts.


Instead I narrow the problem in 2 parts:

1) create a model using k-means algorithm to reduce the ammount of data.
2) store the data in a database for better data type threatment and querying. with the cluster id associated to each food truck.
3) use a live algorithm to find the 5 closest food trucks.

Point 1), I separate the data in 10 different regions. SInce there are 481 entry rows to train the data, 10 regions is proportional. In theory, if simmetrical, 48 points per cluster is considered reasonable quantity of data per cluster

Point 3) I had in mind to use radix sort solution to find the 5 nearest neighbours to a certain latitude and longitude.
THen with further research I chose to use the KDTree, which works well with geographical coordinates. Also it behaves with O(n*log(n)) time complexity which is close to ideal. with the warning that for big samples wouldnt be a better option because we have to load the data in a data structure.

In conclusion I create a model with kmeans to classify the regions where each food truck stands.

when requested per rest API, the code does the following steps:
- identify the cluster from the latitude and longitude from the input args using the trained k-means model. Built with preprocessed data.
- filter in the database all the objects that are correspondent to that area.
- find the 5 closest trucks to display


Checkout the Jupyter notebooks in the study folder.