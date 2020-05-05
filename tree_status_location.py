import pandas as pd

tree_census = pd.read_csv(r"C:\Users\zpoet\Downloads\2015StreetTreesCensus_TREES.csv")

y = tree_census[['status', 'boroname', 'longitude', 'Latitude']]

y.to_csv(r"C:\Users\zpoet\Downloads\tree_status.csv", index = None, header=True)
