

import pandas as pd



csv_file ='earthquake_data_cleaned.csv'
data = pd.read_csv(csv_file)

json_file ='dz.json'
data.to_json(json_file,orient='records',lines=True)

print(f"成功将{csv_file}转换为{json_file}")