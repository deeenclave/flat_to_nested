import json
import pandas as pd

data = pd.read_json('example_a.json')
df = pd.DataFrame(data)
# print "before" , df
df.groupby('name').apply(lambda x: x.to_json(orient='records')).to_json('./output.json')
