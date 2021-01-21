import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). Using a while loop to handle invalid inputs
    city = str(input('Would you like to see data from Chicago, New York City, or Washington? \n').lower())
    citys = ('chicago', 'new york city', 'washington')
    while True:
        if city in citys:
            city = city
            break
        else:
            print('please enter only one of the three states')
            city = input().lower()
            continue

        # get user input for month (all, january, february, ... , june)
    month = str(input('Which month? use \'all\' for all months  \n').lower())
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    while True:
        if month in months:
            month = month
            break
        else:
            print('please enter correct month name!')
            month = input().lower()
            continue

        # get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Which day? use \'all\' for all days  \n').lower())
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    while True:
        if day in days:
            day = day
            break
        else:
            print('please enter correct day name!')
            day = input().lower()
            continue
    print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is:', df['month'].mode()[0],',count:', df['month'].value_counts().max())

    # display the most common day of week
    print('the most common day is:', df['day_of_week'].mode()[0],',count:', df['day_of_week'].value_counts().max())


    # TO DO: display the most common start hour
    print('the most common start hour is:', pd.to_datetime(df['Start Time']).dt.hour.mode()[0],',count:', pd.to_datetime(df['Start Time']).dt.hour.value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('the most common used start station is:', df['Start Station'].mode()[0],',count:', df['Start Station'].value_counts().max())

    # display most commonly used end station
    print('the most common used end station is:', df['End Station'].mode()[0],',count:', df['End Station'].value_counts().max())

    # display most frequent combination of start station and end station trip
    print('the most common trip from start to end is: ', (df['Start Station'] + ' To ' + df['End Station']).mode()[0], ',count:', (df['Start Station'] + df['End Station']).value_counts().max())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time is:', df['Trip Duration'].sum(), 'Seconds', ',Total time is:', pd.to_timedelta(df["Trip Duration"].sum(), unit='s'))

    # display mean travel time
    print('mean travel time is:', df['Trip Duration'].mean(), 'Seconds', ',mean time is:', pd.to_timedelta(df["Trip Duration"].mean(), unit='s'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('counts of gender:')
    if city != 'washington' :
       print(df['Gender'].value_counts())
    else:
        print('gender type is not available for washington state')


    # Display earliest, most recent, and most common year of birth
    
    if city != 'washington' :
        print('Earliest year of birth:')
        print(df['Birth Year'].min())
        print(' most recent year of birth:')
        print(df['Birth Year'].max())
        print(' most common year of birth:')
        print(df['Birth Year'].mode())
    else:
        print('year of birth is not available for washington state')
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    while True:
        answer = input('Do you want to see a sample of the raw data -5 rows at a time- ?\n').lower()
        if answer != 'yes':
            break
        else:
            print(df.sample(n=5))
            continue
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
        

if __name__ == "__main__":
	main()
