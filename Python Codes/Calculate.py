# Libraries ========================================================================================================== #
import pandas as pd
# Data reading ======================================================================================================= #
path = "/Users/Fox/Desktop/Data Science/Data Vis/Project1/Data/"
NAME = "Government expenditure on education, total (US$)"
Document = "cleaned_data/"+ NAME + ".csv"
GDP_ = "GDP"
GDP__ = "cleaned_data/"+ GDP_ + ".csv"
GDP = pd.read_csv(path + GDP__, index_col= 0)
POP_ = "Population, total"
POP__ = "cleaned_data/"+ POP_ + ".csv"
POP = pd.read_csv(path + POP__, index_col= 0)
df0 = pd.read_csv(path + Document, index_col= 0)

# Calculate the education expenditure in US$
# df = GDP * df0 / 100
# Calculate the per capita data
# df = df0 / POP
# Calculate the growth rate
df= ((df0["2016"] - df0["2010"])/df0["2010"])/7
NEWNAME = "Education Growth Rate"
# save the cleaned data
df.to_csv(path + "/cleaned_data/" + NEWNAME + ".csv", index=True)








