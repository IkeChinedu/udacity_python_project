import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. This would determine the data displayed.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('Which of these city data would you like to explore : chicago, new york city or washington? ').lower()
        
        if city in cities:
            break
        else:
            print('Invalid Selection')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
      month = input('Kindly enter a month you would like to analyze \n> {} \n> '.format(months)).lower()
      if month in months:
            break
      else:
            print('Invalid Selection')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    while True:
       day = input(' enter a day to you would like to analyze \n> {} \n> '.format(days)).lower()
       if day in days:
            break
       else:
            print('Invalid Selection')

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
    df=pd.read_csv(CITY_DATA[city])
 
    # TO DO: convert the Start Time column to datetime type
    df['Start Time']=pd.to_datetime(df['Start Time'])
 
    # TO DO: extract month and day of week from Start Time and create as data columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
 
    # TO DO: filter by month if applicable
    if month != 'all':
        #use the index of the month list to get the corresponding int
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
 
        # TO DO : filter by month to create the new dataframe
        df = df[df['month'] == month]
 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    print('\nFILTER CRITERIA:\nCity: {}\nMonthIndex: {}\nDay: {}'.format(city, month, day))     

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months=['january','february','march','april','may','june']
    print('\nMost common month is :')
    df['month'] = df['Start Time'].dt.month
    most_month = df['month'].mode()[0]
    print(months[most_month - 1])

    

    # TO DO: display the most common day of week
    print('\nMost common day of week is :')
    print(list(df['day_of_week'].mode()))


    # TO DO: display the most common start hour 
    print('\nMost common start hour is :')
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station is :')
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)
 

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station is :')
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station trip is :')
    df['combination_station'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination_station = df['combination_station'].mode()[0]
    print(common_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time is :')
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)
   

    # TO DO: display mean travel time
    print('\nMean travel time is :')
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser type count is :")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print("\nGender count is :")
    if 'Gender' in df:
     gender = df['Gender'].value_counts()
     print(gender)
    else:
     print("There is no gender information for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nEarliest, most recent, and most common year of birth is :")
    if 'Birth Year' in df:
     earliest_birth = df['Birth Year'].min()
     print(earliest_birth)
     recent_birth = df['Birth Year'].max()
     print(recent_birth)
     common_birth = df['Birth Year'].mode()[0]
     print(common_birth)
    else:
     print("There is no birth year information available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    """Ask if the would like to see 5 lines of sample raw data
     and display if answer is yes """
    
def raw_data(df,city):
   responses = ['yes','no']
   while True:
    responses = input("Would you like to see 5 rows of the raw data? enter yes or no : ").lower()
    if responses == 'yes' and city != 'washington' :
      print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year']].head())
      break
    elif responses == 'yes' and city == 'washington' :
      print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type']].head())
      break
    elif responses == 'no':
      print('')
      break
    elif responses not in ['yes','no']:
      print("Invalid Selection, please try again inputting yes or no")    
      
   
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
