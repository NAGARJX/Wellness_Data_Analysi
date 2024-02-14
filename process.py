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