# Dependencies
import csv

# Files to load and output
file_to_load = "/Users/abrahamofolu/Documents/GitHub/python-challenge/Resources/budget_data.csv"
file_to_output = "/Users/abrahamofolu/Documents/GitHub/python-challenge/Analysis/PyBank_output.txt"

# Track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Track the totals
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Track the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
#output = "Financial Analysis\n"
#+ "------------------------------------\n" 
#+ f"Total Months: {total_months}\n" 
#+ f"Total Revenue: ${total_revenue}\n" 
#+ f"Average Revenue Change: ${revenue_avg}\n" 
#+ f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n" 
#+ f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n" 

output = "Financial Analysis\n" + "------------------------------------\n" + "Total Months: {}\n".format(total_months) + "Total Revenue: ${}\n".format(total_revenue)+ "Average Revenue Change: ${}\n".format(revenue_avg) + "Greatest Increase in Revenue: {} (${})\n".format(greatest_increase[0], greatest_increase[1])+ "Greatest Decrease in Revenue: {} (${})\n".format(greatest_decrease[0], greatest_decrease[1]) 

# Print the Output
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)