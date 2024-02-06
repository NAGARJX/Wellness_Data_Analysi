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
- ```python
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  plt.style.use('ggplot')
  import datetime as dt
  #pd.set_option('mac_column')
  
## LOAD NECESSARY DATASETS
There are many datasets available but I will only be loading the ones necessary for analysis.
- ```python
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
- ```python
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


