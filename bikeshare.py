""" import packages """
import time
import pandas as pd
import numpy as np


# Define dict for importing the correct data based on user input later on
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# Define a list for valid user inputs for the month filter
Month_Filter = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
# Define a list for valid user inputs for the weekday filter
Day_Filter = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
   
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Gets user input for city (chicago, new york city, washington)
    city = str(input('Please enter the City you\'re interested in: ')).lower()
    # Gives a hint for the input and ask for another input until it's valid, if first input is not valid
    # Lower the input to match with the CITY_DATA keys
    while city not in CITY_DATA.keys():
        city = str(input('That\'s not a valid input. Please Choose from \'chicago\', \'new york city\' and \'washington\'. Please enter again: ')).lower()
    # Confirms that the filter was set according to the valid input
    print('you have set the following filter for the city: ', city)    
 
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Please enter the month you want to filter, type \'all\' if you don\'t want to set a month filter: ')).lower()
    # Gives a hint for the input and ask for another input until it's valid, if first input is not valid
    while month not in Month_Filter:
        month = str(input('That\'s not a valid input. Please Choose from \'january\', \'february\', \'march\', \'april\', \'may\', \'june\' and \'all\'. Please enter again: ')).lower()
    # Confirm that the filter was set according to the valid input
    print('you have set the following filter for the month: ', month)
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Please enter the day of the week, type \'all\' if you don\'t want to set a filter for the day of the week: ').lower())
    while day not in Day_Filter:
        day = str(input('That\'s not a valid input. Please Choose from \'monday\', \'tuesday\', \'wednesday\', \'thursday\', \'friday\', \'saturday\', \'sunday\' and \'all\'. Please enter again: ')).lower()
    print('you have set the following filter for the day: ', day)
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
    #loading the data for the choosen city
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] =  df['Start Time'].dt.hour
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable, if not applicable go to next if-statement
    if month != 'all':
        # use the index of the Month_Filter list to get the corresponding int
        month = Month_Filter.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
   
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

              
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel
    Args:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    """ 
    Checks if there is a month filter. If that's true, the filtered month will be the most common month anyway, so nothing will be displayed       """
    if month == 'all':
        # Calculates the most common month as an int
        # Uses the index of the Month_Filter list to convert month as an integer to month as a string (written)
        # Uses .title() function so that the first letter is capitalised when displayed
        mc_month = Month_Filter[(df['month'].mode()[0])-1].title()
        print('The most common month for travelling is: ', mc_month)

    # TO DO: display the most common day of week
    """ 
    Checks if there is a day filter. If that's true, the filtered weekday will be the most common weekdayanyway, so nothing will be               displayed
    """
    if day == 'all':
        # Calculates the most common weekday and returns it as a string (first letter already capitalised in the column)
        mc_day = df['day_of_week'].mode()[0]
        print('The most common day of the week for travelling is: ', mc_day)

    # TO DO: display the most common start hour
    mc_hour = df['hour'].mode()[0]
    # Calculates the most common start hour as an int
    print('the most common hour for travelling is: ', mc_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args: (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # Calculates the most commonly used start location (string)
    mc_start = df['Start Station'].mode()[0]
    print('The most common Start Station is: ', mc_start)
    # TO DO: display most commonly used end station
    # Calculates the most commonly used end location (string)
    mc_end = df['End Station'].mode()[0]
    print('The most common End Station is: ', mc_end)
    # TO DO: display most frequent combination of start station and end station trip
    # Creates a new column 'Start End' with the start and the end station first
    # Then calculates the most common combination with the new column 
    df['Start End'] = df['Start Station'] + ' to ' + df['End Station']
    mc_start_end = df['Start End'].mode()[0]
    print('The most frequent combination of start and end station for a trip is: ', mc_start_end)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df, month, day):
    """Displays statistics on the total and average trip duration.
    Args:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    """
    Depending on the set filters the is a different ouput displayed:
    --> Information about the weekday, if weekday filter is set, will be displayed
    --> Information about the month, if month filter is set, will be displayed
    --> Information about the both month and weekday, if both filters are set, will be displayed
    --> The total travel time is converted from seconds to hours and rounded by two decimals
    """
    total_tt = (df['Trip Duration'].sum()) / 60 / 60
    if month == 'all' and day == 'all':
        print(('The total trip duration is {} hours.').format(round(total_tt, 2)))
    elif month == 'all':
        print(('The total trip duration on {}s is {} hours.').format(day, round(total_tt, 2)))
    elif day == 'all':
        print(('The total trip duration over all weekdays in {} is {} hours.').format(month, round(total_tt, 2)))
    else:
        print(('The total trip duration on {}s in {} is {} hours.').format(day, month, round(total_tt, 2)))
    
    # TO DO: display mean travel time
    # The mean of the travel time is calculated and convertet from second to minutes
    mean_tt = (df['Trip Duration'].mean()) / 60
    # The mean of the travel time is rounded to two decimals before printing
    print(('The mean travel time is {} minutes').format(round(mean_tt, 2)))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args: (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
          (str) city - name of the city to analyze
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
   
    # Calculation and printing of frequency of the User Type and Gender 
    user_type = df['User Type'].value_counts()
    print(user_type)
    # TO DO: Display counts of gender
    # As there is no 'Gender' data availible for washington, in case the month_filter is set to washington, nothing will be displayed 
    if city != 'washington':
        gender_types = df['Gender'].value_counts()
        print(gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    # As there is no 'Birth Year' data availible for washington, in case the month_filter is set to washington, nothing will be displayed 
    if city != 'washington':
    # Calculation and printing of the min, max and the most common year of birth
        min_by = int(df['Birth Year'].min())
        print('The earliest year of birth is: ', min_by)
        max_by = int(df['Birth Year'].max())
        print('The most recent year of birth is: ', max_by)
        mc_by = int(df['Birth Year'].mode()[0])
        print('The most common year of birth is: ', mc_by)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_first(df):
    """
    Displays the filtered raw data, if user wants to.
    Args: (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
          (str) city - name of the city to analyze
    """
    start_row = 0
    # Set start row to zero for first iteration
    max_rows = df.shape[0]
    # Get max_rows to stop iteration, in case there is no more data to display
    shown_rows = 5
    # Defines the number of rows which are displayed in each iteration
    show_data = str(input('Do you want to have a look a the first five rows of the filtered raw data? Enter \'yes\' or \'no\': ')).lower()
    # aks if user wants to display data. If not, while loop will not be started
    while show_data == 'yes':
        if (start_row + shown_rows) > max_rows:
            shown_rows = max_rows - start_row
        # Check if there are enough rows left to display, otherwise sets number of rows to number of remaining rows
        print(df.iloc[start_row:(start_row + shown_rows)])
        # prints up to five rows
        show_data = str(input('Do you want to have a look at the next five rows? Enter \'yes\' or \'no\': ')).lower()
        # only if user enters 'yes' the next iteration will start
        start_row += shown_rows
        if start_row >= max_rows:
        # Checks if there are rows left. If not msg appears and quit the loop
            print('there is no more data to display')
            show_data = 'no'
        
def main():
    while True:      
        city, month, day = get_filters()
        df = load_data(city, month, day)
        show_first(df)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df, month, day)
        user_stats(df, city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
