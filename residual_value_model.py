import pandas as pd

# Load JSON from memory
df = pd.read_json("cars.json")

print(df)