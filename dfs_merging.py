import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'D': ['D0', 'D1', 'D2']})
print "DF1 :"
print df1.head()

df2 = pd.DataFrame({'A': ['A4', 'A0', 'A1'],                     
                     'E': ['C4', 'C5', 'C6'],
                     'B': ['B4', 'B0', 'B1'],
                     'F': ['D4', 'D5', 'D6']})
print "DF2 :"
print df2.head()

dfMerged = pd.merge(df1, df2, on=['A', 'B'], how='outer')
print "Result df :"
print dfMerged.head()

