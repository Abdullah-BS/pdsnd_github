import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city not in (1, 2, 3):
        city = eval(input("Would you like to see data for Chicago, New York, or Washington?\n1:Chicago \t 2:New York \t 3:Washington\n"))
        if city not in (1, 2, 3):
            print("\nInvalid input. Please choose 1, 2, or 3.")
    
    if city == 1:
        city = "Chicago"
    elif city == 2:
        city = "New York"
    else:
        city = "Washington"
            
            
    # get user input for month (all, january, february, ... , june)
    month = None
    while month not in (1, 2, 3, 4, 5, 6, 7):
        month = eval(input("Which month do you want?\n1:January \t 2:February \t 3:March \t 4:April \t 5:May \t 6:June \t 7:All\n"))
        if month not in (1, 2, 3, 4, 5, 6, 7):
            print("\nInvalid input. Please choose 1, 2, 3, 4, 5, 6 or 7.")
    
    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    else:
        month = "All"
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    while day not in (1, 2, 3, 4, 5, 6, 7, 8):
        day = eval(input("Which day do you want?\n1:Monday \t 2:Tuesday \t 3:Wednesday \t 4:Thursday \t 5:Friday \t 6:Saturday \t 7:Sunday \t 8:All\n"))
        if day not in (1, 2, 3, 4, 5, 6, 7, 8):
            print("\nInvalid input. Please choose 1, 2, 3, 4, 5, 6, 7 or 8.")
    
    if day == 1:
        day = "Monday"
    elif day == 2:
        day = "Tuesday"
    elif day == 3:
        day = "Wednesday"
    elif day == 4:
        day = "Thursday"
    elif day == 5:
        day = "Friday"
    elif day == 6:
        day = "Saturday"
    elif day == 7:
        day = "Sunday"
    else:
        day = "All"

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
    
    data = pd.read_csv(CITY_DATA[city])
    df = pd.DataFrame(data)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != "All":   
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != "All":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    
    if common_month == 1:
        common_month = "January"
    elif common_month == 2:
        common_month = "February"
    elif common_month == 3:
        common_month = "March"
    elif common_month == 4:
        common_month = "April"
    elif common_month == 5:
        common_month = "May"
    else:
        common_month = "June"
    
    print(f"The most common month is: {common_month}")

    

    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print(f"The most common day is: {common_day}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print(f"The most common hour is: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print(f"The most common start station is: {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print(f"The most common end station is: {common_end_station}")


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].value_counts().idxmax()
    print(f"The most common combination of start station and end station trip: {common_trip}")
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    for name, count in user_types.items():
        print(f"{name}: {count}")

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        for name, count in gender_counts.items():
            print(f"{name}: {count}")
    else:
        print('\nNo gender information available')
        
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        
        print(f"\nEarliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {most_common_birth_year}")
    else:
        print('No birth year information available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """
    Asks the user if they want to see 5 rows of data at a time, continuing until the user says 'no' or until all data is shown.

    Args:
        df - Pandas DataFrame containing city data.
    """

    # Start from the first row
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ').lower()

    # Loop to display 5 rows at a time
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5 
        view_data = input('\nDo you wish to continue? Enter yes or no: ').lower()




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#Comment 1