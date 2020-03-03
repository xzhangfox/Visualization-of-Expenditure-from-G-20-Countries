# Libraries ========================================================================================================== #
import pandas as pd

# Data reading ======================================================================================================= #
path = "/Users/Fox/Desktop/Data Science/Data Vis/Project1/Data/"
NAME = "Government expenditure per student, secondary (% of GDP per capita)"
Document = "raw_data/"+ NAME +".csv"
df = pd.read_csv(path + Document, index_col= 0 ,header=2)
# filter the selected countries
df = df.loc[['United States', 'United Kingdom', 'France', 'Canada',
             'Japan', 'China', 'India', 'Mexico', 'Australia', 'Korea, Rep.']]
# filter the data since 2005 and keep the country code
#Code = df.loc[:,'Country Code']
df = df.loc[:, '2010':'2019']
# df['Country Code'] = Code
# print(df)

# Check Data Quality ================================================================================================= #
# duplicate values
print(df.duplicated())
# missing values
print(df.isnull().any())
# number of missing values
for COL in df.columns:
    print(COL + ':', len(df) - df[COL].count())

# drop columns with too many missing values
df = df.drop(['2017', '2018', '2019'], axis=1)

# fill missing values by mean values
df = df.fillna(df.mean())
# drop duplicated values
# df = df.drop_duplicates()

# data skew check
# print(pd.value_counts(df['AdoptionSpeed']))

# outlier check
# calculate relevant statistical indicators
# get descriptive statistics
statDF = df.describe()
# get the maximum and minimum values of each field
Max_min = statDF.loc[['max', 'min']]
# update statDF
# statDF = df.describe()

# number of missing values
print("Final values check")
for COL in df.columns:
    print(COL + ':', len(df) - df[COL].count())
# save the cleaned data
df.to_csv(path + "/cleaned_data/" + NAME + ".csv", index=True)
