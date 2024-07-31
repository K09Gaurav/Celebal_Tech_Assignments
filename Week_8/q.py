
import pandas as pd
import json
#  Q2.2
def Q2_2():
    data = json.loads(json_data.json)
    flattened_data = pd.json_normalize(data)
    df = pd.DataFrame(flattened_data)
    print(df)
    df.to_csv('flattened_data.csv', index=False)
#  Q2.3
def Q2_3():
    data = json.loads(json_data.json)
    flattened_data = pd.json_normalize(data)
    df = pd.DataFrame(flattened_data)
    output_path = 'flattened_data.parquet'
    df.to_parquet(output_path, engine='pyarrow', index=False)

if __name__ == "__main__":
    Q2_2()
    Q2_3()
