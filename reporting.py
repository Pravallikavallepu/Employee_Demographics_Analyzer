# reporting.py
import data_processing
def print_gender_counts(gender_counts):
    """Print count of Males and Females in the organization."""
    print("1. Count of Males and Females in the organization:\n", gender_counts)

def print_gender_counts_department(gender_counts_department):
    """Print count of Males and Females in each department."""
    print("\n2. Count of Males and Females in each department:\n", gender_counts_department)

def print_gender_counts_location(gender_counts_location):
    """Print count of Males and Females in each location."""
    print("\nCount of Males and Females in each location:\n", gender_counts_location)

def print_highest_pay_department(highest_pay_department):
    """Print department with the highest average pay."""
    print("\n3. Department with highest average pay:", highest_pay_department)

def print_highest_pay_location(highest_pay_location):
    """Print location with the highest average pay."""
    print("\n4. Location with highest average pay:", highest_pay_location)

def print_rating_statistics(good_percentage, very_good_percentage, poor_percentage, very_poor_percentage, average_rating):
    """Print percentage of employees with different ratings."""
    print("\n5. Percentage of employees with different ratings:")
    print("Good:", good_percentage)
    print("Very Good:", very_good_percentage)
    print("Poor:", poor_percentage)
    print("Very Poor:", very_poor_percentage)
    print("Average Rating:", average_rating)


def print_gender_pay_gap_department(gender_pay_gap_department):
    """Print gender pay gap for each department."""
    print("\n6. Gender pay gap for each department:\n", gender_pay_gap_department)

def print_gender_pay_gap_location(gender_pay_gap_location):
    """Print gender pay gap for each location."""
    print("\n7. Gender pay gap for each location:\n", gender_pay_gap_location)
