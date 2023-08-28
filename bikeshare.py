import pandas as pd
import time
import bikeshareart

# Create dictionary of csv files from which to extract city data for analysis
city_data = {"Chicago": 'chicago.csv',
             "New York": 'new_york_city.csv',
             "Washington": 'washington.csv'}

print("\nEXPLORING US BIKESHARE DATA")
print("_" * 60)

print(bikeshareart.logo_initialize)

print("Welcome! Let's explore some bikesharing data from 3 major US Cities!\n")


def find_filters():
    '''
    Prompts the user for a city, as well as a month and/or day as filters for the DataFrame

    Returns:
    city (str) : provided city, additionally accessing the city bikeshare .csv file from dictionary city_data
    month (str) : optional month filter
    day (str) : optional day filter

    '''
    while True:
        # Ask the user from which city they would like to view bikeshare data
        city = input("Which US city data would you like to view? Chicago, New York or Washington ").title()

        if city == "Chicago" or city == "New York" or city == "Washington":
            print(f"You will be viewing {city} Bikesharing data!")
            break
        else:
            print("Invalid input. Please select one of the three cities above.")
            continue

    # Set filter variables to None value types for cases where filtering is not applicable
    month = None
    day = None

    # Create list of months and days to ensure correct input for both variables month and day
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Ask user if they would like to filter the data
    while True:
        time_filter = input(
            "\nWould you like to filter the data by the month, day or both? Type 'other or none' to skip to other filters ").lower()
        if time_filter == 'both':
            while True:
                try:
                    month, day = input(
                        "\nPlease enter the month, followed by the day of the week, separated by a comma (ex. June, Sunday) ").title().split(
                        ", ")
                    if month in months and day in days:
                        break
                    else:
                        print("Invalid input. Please enter a correct month and day")
                        continue
                except ValueError:
                    print("Invalid input. Please enter both a month and a day of the week")
                    continue
            break
        elif time_filter == 'month':
            while True:
                month = input("\nWhich month would you like to filter by? ").title()
                if month in months:
                    break
                else:
                    print("Invalid input. Please enter a correct month")
                    continue
            break
        elif time_filter == 'day':
            while True:
                day = input("\nWhich day would you like to filter by? ").title()
                if day in days:
                    break
                else:
                    print("Invalid input. Please enter a correct day")
                    continue
            break
        elif time_filter == 'other' or time_filter == 'none':
            break

        else:
            print("Invalid input. Please type month, day, both or other/none.")
            continue

    return city, month, day


def additional_filters(city):
    '''
    Additional optional filtering parameters such as user type, gender and birth year
    Only Chicago and New York contain additional columns regarding gender and birth year

    Argument:
    city: user selected city from find_filters() function

    Returns:
    user (str) : optional user type filter
    gender (str) : optional gender filter
    birth year (float) : optional birth year filter

    '''
    # Set filter variables to None value types for cases where filtering is not applicable
    user = None
    gender = None
    birth_year = None

    while True:
        more_filters = input("\nWould you like to filter by user type, gender or birth year? Type Yes or No ").lower()
        if more_filters == 'yes':
            # Filtering for Chicago or New York DataFrame
            if city == "Chicago" or city == "New York":
                while True:
                    user = input("\nFilter by user type? Type Subscriber, Customer or None ").title()
                    if user == 'Subscriber' or user == 'Customer':
                        break
                    elif user == 'None':
                        user = None
                        break
                    else:
                        print("Invalid input. Please enter a valid input")
                        continue
                while True:
                    gender = input("\nFilter by gender? Type Male, Female or None ").title()
                    if gender == 'Male' or gender == 'Female':
                        break
                    elif gender == 'None':
                        gender = None
                        break
                    else:
                        print("Invalid input. Please enter a valid input")
                        continue
                while True:
                    try:
                        birth_year = float(
                            input("\nFilter by birth year? Please type the year (For no filter, type 0) "))
                        if birth_year == 0.0:
                            birth_year = None
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number")
                        continue
                break
            # Filtering for Washington DataFrame
            elif city == "Washington":
                while True:
                    user = input("\nWhich user type would you like to filter by? Subscriber or Customer ").title()
                    if user == 'Subscriber' or user == 'Customer':
                        break
                    else:
                        print("Invalid input. Please enter a valid input")
                        continue
                break
        elif more_filters == 'no':
            break

        else:
            print("Invalid input. Please enter yes or no")
            continue

    return user, gender, birth_year


def load_filter_data(city, month=None, day=None, user=None, gender=None, birth_year=None):
    '''
    Loads the DataFrame for the selected city and creates new columns for filtering data
    Function takes 6 arguments (only city variable is mandatory)
    Filters by month, day of the week, user type, gender and/or birth year

    Arguments:
    month (str, default=None) : Filters the data by the first 6 months of the year
    day (str, default=None) : Filters the data by the day of the week
    user (str, default=None) : Filters the data by the user type, subscribers or customers
    gender (str, default=None) : Filters the data by gender, male or female
    birth year (float, default=None) : Filters the data by year of birth

    Returns:
    df : Pandas Dataframe containing filtered data for the selected city

    '''

    # Load csv file into a dataframe
    df = pd.read_csv(city_data[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Rename Trip Duration column to Duration in Seconds
    df = df.rename(columns={'Trip Duration': 'Duration in Seconds'})

    # Insert a new column representing the start and end stations for trips
    df.insert(6, 'Trip Start and End', df['Start Station'] + ' to ' + df['End Station'])

    # Extract month, day and hour from Start Time
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day of Week'] = df['Start Time'].dt.day_name()
    df['Hour'] = df['Start Time'].dt.strftime('%-I%p')

    # Filter by month if applicable
    if month != None:
        df = df.loc[df['Month'] == month]

    # Filter by day of the week if applicable
    if day != None:
        df = df.loc[df['Day of Week'] == day]

    # Filter by user type if applicable
    if user != None:
        df = df.loc[df['User Type'] == user]

    # Filter by gender if applicable
    if gender != None:
        df = df.loc[df['Gender'] == gender]

    # Filter by birth year if applicable
    if birth_year != None:
        df = df.loc[df['Birth Year'] == birth_year]

    # Returns Pandas DataFrame
    return df


def check_empty(df):
    '''
    Check if filtered DataFrame is empty due to non-existent values from applied filters
    If DataFrame is empty, prompt the user to re-select a city with new filters

    Arguments:
    df : returned filtered DataFrame

    Returns:
    Boolean value True or False

    '''
    check = df.empty

    return check


# Displays various statistics regarding the most/least popular month, day of the week and hour
def time_stats(df, city, month, day, user, gender, birth_year):
    # Initialize start time and save to a variable
    start_time = time.time()

    # Display the filters that have been applied to the DataFrame
    print("\n{} Bikeshare Statistics".format(city))
    print(
        f"\nFilters applied: Month: {month} | Day: {day} | User Type: {user} | Gender: {gender} | Birth Year: {birth_year}")
    print("\nCalcuating the most and least popular travel times...")

    # Display the most and least popular month and number of rides if month is not filtered
    if month == None:
        high_month = df['Month'].mode()[0]
        high_month_count = df['Month'].value_counts()[0]
        low_month = df['Month'].value_counts().keys()[-1]
        low_month_count = df['Month'].value_counts()[-1]

        print(
            f"Most popular month: {high_month} ({high_month_count}) | Least popular month: {low_month} ({low_month_count})")

    # Display the most and least popular day and number of rides if day is not filtered
    if day == None:
        high_day = df['Day of Week'].mode()[0]
        high_day_count = df['Day of Week'].value_counts()[0]
        low_day = df['Day of Week'].value_counts().keys()[-1]
        low_day_count = df['Day of Week'].value_counts()[-1]

        print(f"Most popular day: {high_day} ({high_day_count}) | Least popular day: {low_day} ({low_day_count})")

    # Displays the most and least popular hours of the day including their frequency
    try:
        pop_hour = df['Hour'].mode()[0]
        pop_hour_count = df['Hour'].value_counts()[0]
        unpop_hour = df['Hour'].value_counts().keys()[-1]
        unpop_hour_count = df['Hour'].value_counts()[-1]

        print(
            f"Most popular hour: {pop_hour} ({pop_hour_count}) | Least popular hour: {unpop_hour} ({unpop_hour_count})")

    except KeyError:
        print("There are no records with the selected filters.")

    print("Processing request: %s seconds." % (time.time() - start_time))


# Displays various statistics regarding the most/least popular start and end stations, including the most popular trip
def station_stats(df):
    # Initialize start time and save to a variable
    start_time = time.time()

    print("\nCalcuating the most and least popular stations and trips...")

    # Display the most and least popular start stations
    high_start_station = df['Start Station'].mode()[0]
    high_start_count = df['Start Station'].value_counts()[0]
    low_start_station = df['Start Station'].value_counts().keys()[-1]
    low_start_count = df['Start Station'].value_counts()[-1]

    print(
        f"Most popular start station: {high_start_station} ({high_start_count}) | Least popular start station: {low_start_station} ({low_start_count})")

    # Display the most and least popular end stations
    high_end_station = df['End Station'].mode()[0]
    high_end_count = df['End Station'].value_counts()[0]
    low_end_station = df['End Station'].value_counts().keys()[-1]
    low_end_count = df['End Station'].value_counts()[-1]

    print(
        f"Most popular end station: {high_end_station} ({high_end_count}) | Least popular end station: {low_end_station} ({low_end_count})")

    # Displays the most common trip (most frequent start and end station combination)
    pop_trip = df['Trip Start and End'].mode()[0]
    trip_count = df['Trip Start and End'].value_counts()[0]

    print(f"Most popular trip: {pop_trip} ({trip_count})")

    print("Processing request: %s seconds." % (time.time() - start_time))


# Displays various statistics regarding trip durations such as total, average, longest and shortest ride times
def trip_duration_stats(df):
    # Initialize start time and save to a variable
    start_time = time.time()

    print("\nCalcuating statistics on ride times in minutes...")

    # Display the total and average ride times
    total_min = df['Duration in Seconds'].sum() // 60 + round((df['Duration in Seconds'].sum() % 60 / 100), 2)
    average_ride = df['Duration in Seconds'].mean() // 60 + round((df['Duration in Seconds'].mean() % 60 / 100), 2)
    num_of_rides = len(df)

    print(
        f"Total ride time (min.sec): {total_min} | Average ride time (min.sec): {average_ride} | Number of rides: {num_of_rides}")

    # Display the longest and shortest ride times
    longest_ride = df['Duration in Seconds'].max() // 60 + (df['Duration in Seconds'].max() % 60 / 100)
    shortest_ride = df['Duration in Seconds'].min() // 60 + (df['Duration in Seconds'].min() % 60 / 100)

    print(f"Longest ride (min.sec): {longest_ride} | Shortest ride (min.sec): {shortest_ride}")

    print("Processing request: %s seconds." % (time.time() - start_time))


# Displays various statistics regarding users, such as the user type, gender, and birth year where applicable (Chicago and New York data only)
def user_stats(df, city, user, gender, birth_year):
    # Initialize start time and save to a variable
    start_time = time.time()

    print("\nCalcuating statistics on user types, gender and birth year...")

    if city == "Chicago" or city == "New York":
        # Display the number of subscribers and customers if user type is not filtered
        if user == None:
            subscriber_count = (df['User Type'] == 'Subscriber').sum()
            customer_count = (df['User Type'] == 'Customer').sum()

            print(f"Number of subscribers: {subscriber_count} | Number of customers: {customer_count}")

        # Display the number of male and female riders if gender is not filtered
        if gender == None:
            male_riders_count = (df['Gender'] == 'Male').sum()
            female_riders_count = (df['Gender'] == 'Female').sum()

            print(f"Male riders: {male_riders_count} | Female riders: {female_riders_count}")

        # Display the number of male and female riders if gender is not filtered
        if birth_year == None:
            try:
                pop_birth_year = int(df['Birth Year'].mode()[0])
                unpop_birth_year = int(df['Birth Year'].value_counts().keys()[-1])

                avg_birth_year = int(df['Birth Year'].mean())
                old_birth_year = int(df['Birth Year'].max())
                young_birth_year = int(df['Birth Year'].min())

                print(f"Most common birth year: {pop_birth_year} | Least common birth year: {unpop_birth_year}")
                print(
                    f"Average birth year: {avg_birth_year} | Oldest birth year: {old_birth_year} | Youngest birth year: {young_birth_year}")

            except KeyError:
                print("There are no records with the selected filters.")

    elif city == "Washington":
        # Display the number of subscribers and customers regardless if filtered or not
        subscriber_count = (df['User Type'] == 'Subscriber').sum()
        customer_count = (df['User Type'] == 'Customer').sum()

        print(f"Number of subscribers: {subscriber_count} | Number of customers: {customer_count}")

    print("Processing request: %s seconds." % (time.time() - start_time))

    # Display the number of records (trips) given the filters applied
    records = len(df)
    print(f"\nThere are {records} records in the DataFrame")


# Allows user to view the raw data in iterations of 5, printed to the terminal
def view_data(df, city):
    rows = 1
    while True:
        print("\n{} Bikeshare Data".format(city))
        print(df.iloc[rows - 1:rows + 4])
        more_data = input(f"\nWould you like to view more individual ride data in {city}? Type Yes or No ").lower()
        if more_data == "yes":
            rows += 5
            continue
        elif more_data == "no":
            break
        else:
            print("Invalid input. Please enter Yes or No.")
            continue


def main():
    while True:
        city, month, day = find_filters()
        user, gender, birth_year = additional_filters(city)
        df = load_filter_data(city, month, day, user, gender, birth_year)

        empty_df = check_empty(df)
        if empty_df != True:

            time_stats(df, city, month, day, user, gender, birth_year)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city, user, gender, birth_year)

            while True:
                # Ask user if they would like to view the individual rides for the selected city
                user_input = input(f"Would you like to view individual ride data for {city}? Type Yes or No ").lower()
                if user_input == "yes":
                    view_data(df, city)
                    break
                elif user_input == 'no':
                    break
                else:
                    print("Invalid input. Please enter Yes or No")
                    continue
            while True:
                # Ask user if they would like to reset the DataFrame and view another city
                restart = input("\nWould you like to reset the data or view another city? Type Yes or No ").lower()
                if restart == 'yes':
                    break
                elif restart == 'no':
                    exit()
                else:
                    print("Invalid input. Please enter Yes or No")
                    continue
            continue

        else:
            print("DataFrame is empty! Please select a city and different filters\n")
            continue


if __name__ == "__main__":
    main()
