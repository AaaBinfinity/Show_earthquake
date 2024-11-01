import pandas as pd



csv_file ='modified_data2.csv'
data = pd.read_csv(csv_file)

json_file ='new_data.json'
data.to_json(json_file,orient='records',lines=True)

print(f"成功将{csv_file}转换为{json_file}")