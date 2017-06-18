from __future__ import print_function
import pandas as pd
import numpy
import os

try:
	workbook = pd.ExcelFile("python_input.xlsx")
	work_sheets = workbook.sheet_names
except Exception, e:
	print ("python_input.xlsx is not in current directory!")
	raise e

# print ("List of work sheets in the workbook are :", work_sheets)

df_list = list()

# work_sheets[:-2] to escape last two worksheets.
for sheet in work_sheets[:-2]:
	if sheet == "Revenue":
		new_coulumn_names = ["Fiscal Quarter", "BU", "Revenue"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "RISO":
		new_coulumn_names = ["Fiscal Quarter", "BU", "RISO"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "ROSO":
		new_coulumn_names = ["Fiscal Quarter", "BU", "ROSO"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "VE Savings":
		new_coulumn_names = ["BU", "Fiscal Quarter", "VE Savings"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "Gross Margin":
		new_coulumn_names = ["Fiscal Quarter", "BU", "Sum of Product BGM $", "Sum of Product BGM %"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "Cost Weights":
		pass
		# new_coulumn_names = ["BU", "Cost Weight BU Wise"]
		# one_df = workbook.parse(sheet)
		# one_df.columns = new_coulumn_names

	if sheet == "WOS Pipeline":
		new_coulumn_names = ["Fiscal Quarter", "BU", "Actual Pipeline WOS", "Pipeline"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "Turns Ent":
		new_coulumn_names = ["Fiscal Quarter", "BU", "Total Oh", "Ent", "Commit",
							"Gap", "OH Vs Ent", "Turns", "Commit Turns", "Ent Turns"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "NMS Cost":
		new_coulumn_names = ["BU", "Fiscal Quarter", "NMS Cost"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "LAS LTA":
		new_coulumn_names = ["BU", "Fiscal Quarter", "LAS%", "LTA%"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "FA":
		new_coulumn_names = ["Fiscal Quarter", "BU", "Total CSP Bias1",	"Total CSP Accuracy1",
							"Total CSP Accuracy", "Total CSP Bias"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	if sheet == "E&O":
		new_coulumn_names = ["BU", "YYYYQQ", "% of Book Rev", "Forecast", "Actual",
					        "Bias",	"Accuracy", "Year", "Quarter Number","FY", "Q", 
					        "Quarter", "year1", "Fiscal Quarter"]
		one_df = workbook.parse(sheet)
		one_df.columns = new_coulumn_names

	# Delete duplicate rows having same 'BU' and 'Fiscal Quarter'
	one_df.drop_duplicates(subset=['BU', 'Fiscal Quarter'], keep='first', inplace=True)
	df_list.append(one_df)


merged_df = reduce(lambda df1, df2: pd.merge(df1, df2, how="outer", on=['BU', 'Fiscal Quarter']), df_list)
merged_df['VE Savings'].fillna(0, inplace=True)


# Do same thing for other values and you will get the output.
print ("Sum of all VE Savings is :", sum(merged_df['VE Savings']))
# print (merged_df.head())
# print (merged_df.info())

try:
    os.remove("combined_result.csv")
except OSError:
    pass

merged_df.to_csv("combined_result.csv", sep='\t')

