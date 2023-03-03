import time
import pandas as pd
import numpy as np
from IPython.display import display

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters(): 
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ''
    while True:
        city = input('what is the city? ').lower()
        if city in CITY_DATA.keys():
            break
        print('please enter chicago, new york city, or washington')

    month = ''
    while True:
        month = input('please enter your month from january to june or "all" for all months: ').lower()
        if month in MONTHS:
            break
        print('please enter full name of the month')

    day = ''
    while True:
        day = input('please enter day of week not a number ie. friday or "all" for all days: ').lower()
        if day in DAYS:
            break
        print('please enter a valid day of week')
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])  
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name() 
    
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['Start Time'].dt.month == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    lines(df)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time())

    common_month = df['month'].mode()[0]
    month_name = MONTHS[int(common_month) - 1]
    print('the most common month is '+ month_name.title())

    common_day = df['day_of_week'].mode()[0]
    print('the most common day is '+ str(common_day))
    
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour is '+ str(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    lines(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 
    common_start = df['Start Station'].mode()[0]
    print('the most commonly used start station is ' + str(common_start))
    n
    common_end = df['End Station'].mode()[0]
    print('the most commonly used end station is ' + str(common_end))

    combo_station = (df['Start Station'] + " " + df['End Station']).mode()[0]
    print('the most frequent combination of stations is ' + str(combo_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    lines(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time is ' + str(total_travel_time))
    

    mean_travel_time = df['Trip Duration'].mean()
    print('the average time of travel is ' + str(mean_travel_time))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    lines(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    subscribers = df[df == 'Subscriber'].count()[6]
    customers = df[df == 'Customer'].count()[6]
    print('the number of subscribers is ' + str(subscribers))
    print('the number of customers is ' + str(customers))
   
    if 'Gender' in df:    
        males = df[df == 'Male'].count()[7]
        females = df[df == 'Female'].count()[7]
        print('\nthe number of males is ' + str(males))
        print('the number of females is ' + str(females))
    
    if 'Birth Year' in df:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nthe earliest birth year is ' + str(int(oldest)))
        print('the most recent birth year is ' + str(int(youngest)))
        print('the most common birth year is ' + str(int(common_birth)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    lines(df)
    
def lines(df):
    x = 0
    while True:
        display = input('would you like to see five lines of raw data? (y/n) ')
        if display == 'y':    
           print(df.iloc[x:5+x])
           x+=5
        else:
            break
"""function outputs first 5 lines of raw data upon request yes or no. Every subsequent yes will display the next 5 lines until user enters n (no)"""
               
def main():
    while True:
          city, month, day = get_filters()
          df = load_data(city, month, day)
          time_stats(df)
          station_stats(df)
          trip_duration_stats(df)
          user_stats(df)

          restart = input('\nWould you like to restart? Enter yes or no.\n')
          if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

