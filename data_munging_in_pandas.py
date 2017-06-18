with open('temp_data.txt', 'r') as read_obj:
	if read_obj:
		with open('formated_data.txt', 'w') as write_obj:
			for index, line in enumerate(read_obj):	
				if index == 0:
					line = line + '\n'				
					write_obj.write(line)
				elif index == 1: 
					continue
				else:
					if line.startswith(';'):
						line = line[2:-1]
					elif len(line)==1:
						continue
					else:
						line = line[1:-1]

					line = line + '\n'				
					write_obj.write(line)

# import time
# time.sleep(10)

import pandas as pd

required_columns = ['area', 'productname', 'GUID', 'Loops', 'step name']
df = pd.read_csv('formated_data.txt', sep=',')
columns = df.columns

columns = [col.strip() for col in columns]
df.columns = columns
# print df.columns
df.drop([col for col in df.columns if col not in required_columns], axis=1, inplace=True)

writer = pd.ExcelWriter('reuired_output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
