# data_processing.py
import pandas as pd

def gender_counts(df):
    """Count of Males and Females in the organization."""
    return df['Gender'].value_counts()

def gender_counts_department(df):
    """Count of Males and Females in each department."""
    return df.groupby('Department')['Gender'].value_counts()

def gender_counts_location(df):
    """Count of Males and Females in each location."""
    return df.groupby('Loc')['Gender'].value_counts()

def highest_pay_department(df):
    """Department with the highest average pay."""
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    return df.groupby('Department')['Salary'].mean().idxmax()

def highest_pay_location(df):
    """Location with the highest average pay."""
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    return df.groupby('Loc')['Salary'].mean().idxmax()

def rating_statistics(df):
    """Percentage of employees with different ratings."""
    rating_counts = df['Rating'].value_counts()
    good_rating_percentage = rating_counts.get('Good', 0) / len(df) * 100
    very_good_rating_percentage = rating_counts.get('Very Good', 0) / len(df) * 100
    poor_rating_percentage = rating_counts.get('Poor', 0) / len(df) * 100
    very_poor_rating_percentage = rating_counts.get('Very Poor', 0) / len(df) * 100
    average_rating = df['Rating'].map({'Good': 3, 'Very Good': 4, 'Poor': 1, 'Very Poor': 0}).mean()
    return good_rating_percentage, very_good_rating_percentage, poor_rating_percentage, very_poor_rating_percentage, average_rating

def gender_pay_gap_department(df):
    """Gender pay gap for each department."""
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    return df.groupby(['Department', 'Gender'])['Salary'].mean().unstack().assign(Gap=lambda x: (x['Female'] - x['Male']) / x['Male'] * 100)

def gender_pay_gap_location(df):
    """Gender pay gap for each location."""
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    return df.groupby(['Loc', 'Gender'])['Salary'].mean().unstack().assign(Gap=lambda x: (x['Female'] - x['Male']) / x['Male'] * 100)
