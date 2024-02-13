# Wellness_Data_Analysis
## BUSINESS TASK
1 - Bellabeat is a fitness company that manufactures products to help with their customers health. We will be analysing their smart business data to gain inights into how the company can grow from deriving value and patterns from their customers.

2 - Our overall goal is to use the new found information to make impactiful and well informed data driven recommendations to the company.

3 - To ensure that the stakeholders are provided guidance in areas such as sleep, ectivity, health, beauty and nutrition.
## KEY STAKEHOLDERS
1- Urška Sršen: Bellabeat’s cofounder and Chief Creative Officer

2 - Sando Mur: Mathematician and Bellabeat’s cofounder; key member of the Bellabeat executive team

3 - Bellabeat marketing analytics team
## PREPARATION
1 - The data is public and open source meaning it is available to everyone. I will be using the data stored in the Kaggle cloud.

2 - The data contains fitness and health information from over 30 users of FitBit.

3 - The data uses long format, wide format and some merged data sets.

4 - The source of the data is known and its quality is not an issue. Analysing over 30 users means we can gain some valuable insights.
## PROCESS
1.For analysis I will be using Python so it is essential that the required tools are available

2.Loading the necessary libarires to be used for analysis
```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  plt.style.use('ggplot')
  import datetime as dt
  #pd.set_option('mac_column')
  
## LOAD NECESSARY DATASETS
There are many datasets available but I will only be loading the ones necessary for analysis.
```python
  import os
  for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesWide_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteMETsNarrow_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/heartrate_seconds_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteSleep_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteStepsNarrow_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteStepsWide_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteIntensitiesNarrow_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/minuteCaloriesWide_merged.csv
  /kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv
  sleep_day_df = pd.read_csv('/kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/sleepDay_merged.csv')
  daily_activity_df = pd.read_csv('/kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')
  hourly_steps_df = pd.read_csv('/kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv')
  hourly_calories_df = pd.read_csv('/kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv')
  weight_df = pd.read_csv('/kaggle/input/bellabeat-dataset/Fitabase Data 4.12.16-5.12.16/weightLogInfo_merged.csv')
## Data Exploration
Now that the data is loaded, we need to look through it and check if it is clean
```python
  print("Sleep day:", sleep_day_df.columns)
  print("Hourly Steps:", hourly_steps_df.columns)
  print("Daily Activity:", daily_activity_df.columns)
  print("Hourly Calories:", hourly_calories_df.columns)
  print("Weight : ", weight_df.columns)
  Sleep day: Index(['Id', 'SleepDay', 'TotalSleepRecords', 'TotalMinutesAsleep',
         'TotalTimeInBed'],
        dtype='object')
  Hourly Steps: Index(['Id', 'ActivityHour', 'StepTotal'], dtype='object')
  Daily Activity: Index(['Id', 'ActivityDate', 'TotalSteps', 'TotalDistance', 'TrackerDistance',
         'LoggedActivitiesDistance', 'VeryActiveDistance',
         'ModeratelyActiveDistance', 'LightActiveDistance',
         'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes',
         'LightlyActiveMinutes', 'SedentaryMinutes', 'Calories'],
        dtype='object')
  Hourly Calories: Index(['Id', 'ActivityHour', 'Calories'], dtype='object')
  Weight :  Index(['Id', 'Date', 'WeightKg', 'WeightPounds', 'Fat', 'BMI',
         'IsManualReport', 'LogId'],
        dtype='object')
## Data Types and Shapes
### Sleep Day DataFrame
```python
print(sleep_day_df.dtypes)
print(sleep_day_df.shape)
Id                     int64
SleepDay              object
TotalSleepRecords      int64
TotalMinutesAsleep     int64
TotalTimeInBed         int64
dtype: object
(100, 5)
print(hourly_steps_df.dtypes)
print(hourly_steps_df.shape)
Id               int64
ActivityHour    object
StepTotal        int64
dtype: object
(200, 3)
print(daily_activity_df.dtypes)
print(daily_activity_df.shape)
Id                            int64
ActivityDate                 object
TotalSteps                    int64
TotalDistance               float64
TrackerDistance             float64
LoggedActivitiesDistance    float64
VeryActiveDistance          float64
ModeratelyActiveDistance    float64
LightActiveDistance         float64
SedentaryActiveDistance     float64
VeryActiveMinutes             int64
FairlyActiveMinutes           int64
LightlyActiveMinutes          int64
SedentaryMinutes              int64
Calories                      int64
dtype: object
(150, 14)
print(hourly_calories_df.dtypes)
print(hourly_calories_df.shape)
Id               int64
ActivityHour    object
Calories         int64
dtype: object
(300, 3)
print(weight_df.dtypes)
print(weight_df.shape)
Id                  int64
Date               object
WeightKg          float64
WeightPounds      float64
Fat               float64
BMI               float64
IsManualReport       bool
LogId               int64
dtype: object
(50, 8)
 ```
## Handling Missing values
```python
print("Sleep Day Dataset has",sleep_day_df.isnull().values.sum(), "missing values")
print("Hourly Steps Dataset has",hourly_steps_df.isnull().values.sum(), "missing values")
print("Daily Activity Dataset has",daily_activity_df.isnull().values.sum(), "missing values")
print("Hourly Calories Dataset has",hourly_calories_df.isnull().values.sum(), "missing values")
print("Weight Dataset has ", weight_df.isnull().values.sum(), "missing values")
```

- Sleep Day Dataset has 0 missing values
- Hourly Steps Dataset has 0 missing values
- Daily Activity Dataset has 0 missing values
- Hourly Calories Dataset has 0 missing values
- Weight Dataset has  65 missing values
## Handling Duplicates
```python
print(f'Sleep day data set has {sleep_day_df.duplicated().sum()} duplicates')
print(f'Hourly Steps data set has {hourly_steps_df.duplicated().sum()} duplicates')
print(f'Daily Activity data set has {daily_activity_df.duplicated().sum()} duplicates')
print(f'Hourly Calories data set has {hourly_calories_df.duplicated().sum()} duplicates')
print(f'Weight data set has {weight_df.duplicated().sum()} duplicates')
```

- Weight Dataset has 8 unique users
- Sleep day data set has 3 duplicates
- Hourly Steps data set has 0 duplicates
- Daily Activity data set has 0 duplicates
- Hourly Calories data set has 0 duplicates
- Weight data set has 0 duplicates
## Unique Values
```python
print(f'Sleep Day Dataset has {sleep_day_df.Id.nunique()} unique users')
print(f'Hourly Steps Dataset has {hourly_steps_df.Id.nunique()} unique users')
print(f'Daily Activity Dataset has {daily_activity_df.Id.nunique()} unique users')
print(f'Hourly Calories Dataset has {hourly_calories_df.Id.nunique()} unique users')
print(f'Weight Dataset has {weight_df.Id.nunique()} unique users')
```

- Sleep Day Dataset has 24 unique users
- Hourly Steps Dataset has 33 unique users
- Daily Activity Dataset has 33 unique users
- Hourly Calories Dataset has 33 unique users
## Data Exploratory summary

- Maximum users that are being analysed is 33.
- Columns where time is used such as ActivityHour have the object data type instead of dateitme, this will need to be changed.
- Hourly calories & hourly steps have same shape so can be easily merged if needed.
- Sleep day data set has less users but will still provide valuable information. Also includes some duplicates.
- Weight Data set has even less users and many missing values. Maybe some Fitbit participants did not consent into giving out this data.

-After exploring there are some key things that need to be addressed and cleaned
### DUPLICATES IN SLEEP DAY DF
```python
sleep_df_dup = sleep_day_df.duplicated()
duplicate_rows = sleep_day_df[sleep_df_dup]
print(duplicate_rows)
             Id               SleepDay  TotalSleepRecords  TotalMinutesAsleep  \
161  4388161847   5/5/2016 12:00:00 AM                  1                 471   
223  4702921684   5/7/2016 12:00:00 AM                  1                 520   
380  8378563200  4/25/2016 12:00:00 AM                  1                 388   

     TotalTimeInBed  
161             495  
223             543  
380             402
```
-Identified duplictaes but it is not an issue
## CHANGE COLUMN DATA TYPES TO DATETIME
```python
#Change relevant columns to datetime for better analysis 

daily_activity_df['ActivityDate'] =  pd.to_datetime(daily_activity_df['ActivityDate'])
hourly_steps_df['ActivityHour'] = pd.to_datetime(hourly_steps_df['ActivityHour'])
hourly_calories_df['ActivityHour'] = pd.to_datetime(hourly_calories_df['ActivityHour'])
sleep_day_df['SleepDay'] = pd.to_datetime(sleep_day_df['SleepDay'])
weight_df['Date'] = pd.to_datetime(weight_df['Date'])


#check if changes were successful
print("Daily Acitivity data type is", daily_activity_df["ActivityDate"].dtypes, "data type")
print("Hourly Steps data type is", hourly_steps_df["ActivityHour"].dtypes, "data type")
print("Hourly Calories data type is", hourly_calories_df["ActivityHour"].dtypes, "data type")
print("Sleep Day data type is", sleep_day_df["SleepDay"].dtypes, "data type")
print("Weight data type is", weight_df["Date"].dtypes, "data type")
/tmp/ipykernel_18/3055217396.py:4: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
  hourly_steps_df['ActivityHour'] = pd.to_datetime(hourly_steps_df['ActivityHour'])
/tmp/ipykernel_18/3055217396.py:5: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
  hourly_calories_df['ActivityHour'] = pd.to_datetime(hourly_calories_df['ActivityHour'])
Daily Acitivity data type is datetime64[ns] data type
Hourly Steps data type is datetime64[ns] data type
Hourly Calories data type is datetime64[ns] data type
Sleep Day data type is datetime64[ns] data type
Weight data type is datetime64[ns] data type
/tmp/ipykernel_18/3055217396.py:6: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
  sleep_day_df['SleepDay'] = pd.to_datetime(sleep_day_df['SleepDay'])
/tmp/ipykernel_18/3055217396.py:7: UserWarning: Could not infer format, so each element will be parsed individually, falling back to `dateutil`. To ensure parsing is consistent and as-expected, please specify a format.
  weight_df['Date'] = pd.to_datetime(weight_df['Date']
```
## CLEAN WEIGHT DATA FRAME OF NULL VALUES
```python
#From the head we can see that the fat column has some null values
weight_df.head()
Id	Date	WeightKg	WeightPounds	Fat	BMI	IsManualReport	LogId
0	1503960366	2016-05-02 23:59:59	52.599998	115.963147	22.0	22.650000	True	1462233599000
1	1503960366	2016-05-03 23:59:59	52.599998	115.963147	NaN	22.650000	True	1462319999000
2	1927972279	2016-04-13 01:08:52	133.500000	294.317120	NaN	47.540001	False	1460509732000
3	2873212765	2016-04-21 23:59:59	56.700001	125.002104	NaN	21.450001	True	1461283199000
4	2873212765	2016-05-12 23:59:59	57.299999	126.324875	NaN	21.690001	True	1463097599000
#Previous analysis showed that there are 65 null values in the data set, lets check the fat column
print("The Fat column in the weight data set has ", weight_df['Fat'].isnull().values.sum(), "missing values")
The Fat column in the weight data set has  65 missing values
#In some scenarios we could calculate the mean of all values and populate it into each null row.
#But it is best to remove the whole column because it is not useful
weight_df = weight_df.drop('Fat', axis =1)
weight_df.columns
Index(['Id', 'Date', 'WeightKg', 'WeightPounds', 'BMI', 'IsManualReport',
       'LogId'],
      dtype='object')
```
## NEW DAY OF WEEK COLUMN
- Create day of week columns for analysis
- Help to understand trends over time
 ```python
day_of_week = daily_activity_df['ActivityDate'].dt.day_name()
daily_activity_df['DayOfWeek'] = day_of_week
daily_activity_df.head(5)
```
## Merge Datasets
- In order to simplify the data sets and get more detailed analysis, we will be merging some data sets
## Calorie steps
- Merge hourly calories and hourly steps data sets by id and activity hour for clarity and to gather better information
  ```python
  for col in hourly_steps_df.columns, hourly_calories_df.columns:
    print (col)
  Index(['Id', 'ActivityHour', 'StepTotal'], dtype='object')
  Index(['Id', 'ActivityHour', 'Calories'], dtype='object')
  merged_cal_steps_df = pd.merge(hourly_steps_df, hourly_calories_df,
                               on=['Id', 'ActivityHour'], how = 'inner')

#drop activity hour to get specific hour 
 ```python
  merged_cal_steps_df["DateHour"] = merged_cal_steps_df["ActivityHour"].dt.hour
  merged_cal_steps_df = merged_cal_steps_df.drop("ActivityHour", axis = 1)
  merged_cal_steps_df.head(5)
        Id	  StepTotal	Calories	DateHour
  0	1503960366	373	      81	      0
  1	1503960366	160	      61	      1
  2	1503960366	151	      59	      2
  3	1503960366	 0	      47	      3
  4	1503960366	 0	      48	      4
```
## Calories & Steps
- Merge hourly calories and hourly steps data sets by id and activity hour for clarity and to gather better information
## Analyse
-Now that we have merged the data set, we should et statistical informtion of data frames for further analysis.
Our data sets now include:
- merged_cal_steps_df
- daily_activity_df
- weight_df
- sleep_day_df
- Further analysis in the future may produce more concise data sets
```Python
  daily_activity_df.describe()
  merged_cal_steps_df.describe()
  sleep_day_df.describe()
  weight_df.describe()
# Find the range of dates
min_date = weight_df['Date'].min()
max_date = weight_df['Date'].max()
print(f"The data spans from {min_date} to {max_date}")
```
## Findings
- From the summary statistics here is some informaiton found:
- Potential outliers in sleep_day_df: 58 min sleep is too short and 13 hours sleep is too high
- Average of 2304 calories burnt daily which is inline with what we know
- Correlation between steps and calories
- Data is over a 1 month period which may not be long enough to provide valuable insights
## Visualizations
``` python
# Make the bar chart look nicer
fig, axs = plt.subplots(figsize=(10, 6), facecolor='#f7f7f7')

# Get average steps per hour
merged_cal_steps_df.groupby('DateHour')['StepTotal'].mean().plot(kind='bar', rot=0, ax=axs, color='blue', edgecolor='black', width=0.8)

# Labels and title
axs.set_title('Average Steps per Hour', fontsize=16)
axs.set_xlabel('Hour of the Day', fontsize=14)
axs.set_ylabel('Total Steps', fontsize=14)

#Improve x axis readabiliyu
axs.set_xticklabels(axs.get_xticklabels(), rotation=45, ha='right', fontsize=12)

#Average line
overall_average = merged_cal_steps_df['StepTotal'].mean()
axs.axhline(overall_average, color='red', linestyle='--', label='Overall Average')
axs.legend()

#Add Grid lines
axs.grid(axis='y', linestyle='--', alpha=0.7)
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)

plt.show()
![Steps/Hr]()


