import re
import pandas as pd

def preprocess(data):
    """
    Preprocess the chat data.
    """
    pattern = r"\[(\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}:\d{2}\s?[APM]{2})\] (.+)"
     # Extract timestamp and message pairs
    matches = re.findall(pattern, data)
    # Separate into two lists
    dates, messages = zip(*matches)  # Unzipping into two separate variables
   # Convert tuples to lists
    dates = list(dates)
    messages = list(messages)
    # Convert dates to pandas datetime format
    dates = pd.to_datetime(dates, format="%d/%m/%y, %I:%M:%S %p")
    df = pd.DataFrame({'Date': dates, 'User_Message': messages})
     # Creating a new column 'User' with default value 'Group_Message'
    df['User'] = df['User_Message'].apply(lambda x: x.split(':', 1)[0] if ':' in x else 'Group_Message')

 # Creating a new column 'Message' that contains the actual message
    df['Message'] = df['User_Message'].apply(lambda x: x.split(':', 1)[1].strip() if ':' in x else x)

 # Dropping the old 'User_Message' column
    df.drop(columns=['User_Message'], inplace=True)
  # Adding new columns by extracting date and time components
    df['Year'] = df['Date'].dt.year
    df['Day'] = df['Date'].dt.day
    df['Hour'] = df['Date'].dt.hour
    df['Minute'] = df['Date'].dt.minute
    df['AM_PM'] = df['Date'].dt.strftime('%p')  # Extracts AM or PM
    df['Month_Name'] = df['Date'].dt.month_name()  # Extracts the full name of the month
    df['Month_num'] = df['Date'].dt.month  # Extracts the month as an integer
    df['Day_Name'] = df['Date'].dt.day_name()  # Extracts the day of the week
    df['Day_of_Week'] = df['Date'].dt.dayofweek  # Extracts the day of the week as an integer
    df['Weekend'] = df['Date'].dt.dayofweek >= 5  # Boolean indicating if the day is a weekend
    period = []
    for hour in df[['Day_Name', 'Hour']]['Hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    return df 
        
