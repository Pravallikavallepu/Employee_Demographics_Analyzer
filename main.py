# main.py
import data_loading
import data_processing
import reporting

df = data_loading.load_data('data.xlsx')

# Process data
gender_counts = data_processing.gender_counts(df)
gender_counts_department = data_processing.gender_counts_department(df)
gender_counts_location = data_processing.gender_counts_location(df)
highest_pay_department = data_processing.highest_pay_department(df)
highest_pay_location = data_processing.highest_pay_location(df)
good_percentage, very_good_percentage, poor_percentage, very_poor_percentage, average_rating = data_processing.rating_statistics(df)
gender_pay_gap_department = data_processing.gender_pay_gap_department(df)
gender_pay_gap_location = data_processing.gender_pay_gap_location(df)

# Print results
reporting.print_gender_counts(gender_counts)
reporting.print_gender_counts_department(gender_counts_department)
reporting.print_gender_counts_location(gender_counts_location)
reporting.print_highest_pay_department(highest_pay_department)
reporting.print_highest_pay_location(highest_pay_location)
reporting.print_rating_statistics(good_percentage, very_good_percentage, poor_percentage, very_poor_percentage, average_rating)
reporting.print_gender_pay_gap_department(gender_pay_gap_department)
reporting.print_gender_pay_gap_location(gender_pay_gap_location)