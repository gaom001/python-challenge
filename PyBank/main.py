# import the modules (os and csv)
import os
import csv

# open and read csv file by usng relative path
pybank_csv=os.path.join("C:/MG/2019 SMU DS/Homework MG/Python/Instructions/PyBank/Resources/budget_data.csv")

# create empty list for months(index:0) and amount(index:1)
month =[]
amount=[]
change=[]

# initial variables
total_amount=0
pre_amount=0
change_amount=0

# Open and read csv file
with open(pybank_csv,"r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # skip header
    header = next(csvreader,None)
    # Loop data from csv file, apppend row[0] and row[1] into two new lists[month] and [amount]
    for row in csvreader:  
        month.append(row[0])
        amount.append(row[1])
    # calculate total_amount    
        total_amount = total_amount + int(row[1])
    # first_monthly_change calculation 
        next_amount=int(row[1])
        monthly_change= next_amount-pre_amount
    # reset the pre_amount to next    
        pre_amount=next_amount
    # put all monthly_change value into [change] list   
        change.append(monthly_change)
    # replace the first value of change list to "0"  
    change[0]=0
    # sum all values in the list which first value has been change to "0"
    average_of_change=round(sum(change)/(len(change)-1),2)
    print(average_of_change)   
    # max and min the monthly_change,using index() function to locate the date in list [month]
    max_amount=max(change)
    max_amount_month= month[change.index(max_amount)]     
    min_amount=min(change)
    min_amount_month= month[change.index(min_amount)]  

# print out all results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(month)}")
print(f"Total Profit: ${total_amount}")
print(f"Average Change: ${average_of_change}")
print(f"Greatest Increase in Profits: {max_amount_month} ${max_amount}")
print(f"Greatest Decrease in Profits: {min_amount_month} ${min_amount}")



output_path=os.path.join("C:/MG/2019 SMU DS/Homework MG/Python/Instructions/PyBank/Financial Analysis Output.txt")
file = open(output_path,'w')

#Writing output to the file
file.write("Financial Analysis")
file.write("\n-----------------------------------------------")
file.write("\nTotal Month: " + str(len(month)))
file.write("\nTotal Revenue : $" + str(total_amount))
file.write("\nAverage Change : $" + str(average_of_change))
file.write("\nGreatest Increase in Profits : " + str(max_amount_month) + " (" + str(max_amount) + ")")
file.write("\nGreatest Decrease in Profits : " + str(min_amount_month) + " (" + str(min_amount) + ")")

file.close()