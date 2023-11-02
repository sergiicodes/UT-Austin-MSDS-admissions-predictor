import pandas as pd
import re
from datetime import datetime

# Create dataframe from JSON
df = pd.read_json(r"C:\Users\shacosta\Desktop\all_data.json")

## Data Cleaning 
def drop_nulls(df):
  """Drops all rows AND columns from a DataFrame that contain any null values."""
  return df.dropna(how='all')

def cleanStatus(df):
    """Removes rows that don't have a status of 'Accepted' , 'Rejected' , or 'Admitted.' """
    valid_statuses = ["Accepted", "Rejected"]
    return df[df['status'].isin(valid_statuses)]

def normalize_date_format(date_str):
    """Normalize the date formats before converting them to datetime objects"""
    # Split the date string by '/'
    date_parts = date_str.split('/')

    # Pad month and day with leading zeros if needed
    month = date_parts[0].rjust(2, '0')
    day = date_parts[1].rjust(2, '0')

    # Check if year has 2 or 4 digits
    year = date_parts[2]
    if len(year) == 2:
        # Assuming that 2-digit years are in the 2000s
        year = '20' + year

    return f"{month}/{day}/{year}"

def calculate_time_elapsed(df):
    # Normalize date formats
    df['applicationdate'] = df['applicationdate'].apply(normalize_date_format)
    df['decisiondate'] = df['decisiondate'].apply(normalize_date_format)

    # Convert date columns to datetime objects
    df['applicationdate'] = pd.to_datetime(df['applicationdate'], errors='coerce')
    df['decisiondate'] = pd.to_datetime(df['decisiondate'], errors='coerce')

    # Convert date strings to datetime objects
    df['applicationdate'] = pd.to_datetime(df['applicationdate'], format='%m/%d/%Y')
    df['decisiondate'] = pd.to_datetime(df['decisiondate'], format='%m/%d/%Y')
    
    # Calculate the difference in days and create a new column
    df['days_between_apply_and_decide'] = df.apply(lambda row: (row['decisiondate'] - row['applicationdate']).days, axis=1)
    df = df.drop('applicationdate', axis=1)
    df = df.drop('decisiondate', axis=1)

    return df

def extract_largest_number(text):
    """Function to extract the largest number from a string"""
    if isinstance(text, str):
        # Use regular expression to find all floating-point numbers in the text
        numbers = re.findall(r'\d+\.\d+', text)
        
        # If no numbers are found, return None
        if not numbers:
            return None
        
        # Convert the list of numbers to floats and return the largest one
        return max(map(float, numbers))
    
    return None  # Return None for non-string values

# Apply the function to the "education" column and create a new "gpa" column
df['gpa'] = df['education'].apply(extract_largest_number)


def cleanLettersOfRec(text):
    """Function to extract numerical values"""
    if isinstance(text, str):
        # Use regular expression to find numerical values in the text
        numbers = [int(s) for s in text.split() if s.isdigit()]
        
        # If numbers are found, return the first one, else return None
        return numbers[0] if numbers else None
    
    return None  # Return None for non-string values

# Apply the function to the "recommendations" column and create a new "numerical_recommendations" column
df['numerical_recommendations'] = df['recommendations'].apply(cleanLettersOfRec)


def calculate_total_experience(text):
    if isinstance(text, str):
        total_years = 0
        pattern_years = r"(\d+)\s*(year|yr|years)"
        pattern_months = r"(\d+)\s*(month|months)"

        # Find mentions of years
        matches_years = re.findall(pattern_years, text)
        for match in matches_years:
            years = int(match[0])
            total_years += years

        # Find mentions of months and convert to years
        matches_months = re.findall(pattern_months, text)
        for match in matches_months:
            months = int(match[0])
            years = months / 12
            total_years += years

        return total_years

    return 0

# Apply the calculate_total_experience function to the 'experience' column
df['total_experience_in_years'] = df['experience'].apply(calculate_total_experience)
df = df.drop('experience', axis=1)

df = df.drop(df.columns[4:35], axis=1)
print(df)
