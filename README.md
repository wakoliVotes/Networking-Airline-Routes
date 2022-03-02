## Python NetwokX Packagge Use to Visualize Airline Carriers, Routes and Destinations
- [Introduction](#introduction)
- [Example 1](#example-1-airlines-flight-and-destination)
- [Example 2](#example-2-airlines-carrier-and-destination)
- [Example 3](#example-3-airlines-origin-and-destination)
- [Conclusion](#conclusion)


### Introduction
- In this illustration, we rely on data by [Analytics Vidhya](https://bitbucket.org/dipolemoment/analyticsvidhya/src/master/) downloaded from [Bitbucket](https://bitbucket.org/dipolemoment/analyticsvidhya/src/master/)
- First, to use NetworkX, installation and importation are needed
```
pip install networkx            # Installation
```
- For adding data to graphs, pandas is used in this case, as below, then store dataframe relative to data path
```
import pandas as pd
mydata = pd.read_csv(r"D:\Network Science\Airlines.csv")
```
- To create the World into which the graph will exist, import networkx then use "**graph_name = networkx.Graph()**" method, e.g.;
```
import networkx as nx
GG = nx.Graph()
```
- Next, since dataframe data containts several columns, it is important to pick the columns of interent
- In this phase, use the general format (**here, to pick two columns**), as:
> **new_data_frame = original_data_frame[['first_column', 'second_column']]**

### Example 1: Airlines Flight and Destination
![image](https://user-images.githubusercontent.com/77758884/156382455-5ff47276-6bd5-4d47-87ef-c699a25e2935.png)

### Example 2: Airlines Carrier and Destination
![image](https://user-images.githubusercontent.com/77758884/156382518-4d141c73-65c5-482e-8b25-6161d02b6356.png)

### Example 3: Airlines Origin and Destination
![image](https://user-images.githubusercontent.com/77758884/156382542-4c75f629-f1cc-4a58-83a4-2464d0a597b5.png)

## Conclusion
- Read more on Python's NetwokX Package on [Medium Blog](https://medium.com/@dannyvotez/c91dd0982fb9?source=friends_link&sk=e77a0607591e3f2d0c56d5bba9b6748a)
- For additional information, check out NetworkX Documentation on their official [Website](https://networkx.org/documentation/stable/tutorial.html)
