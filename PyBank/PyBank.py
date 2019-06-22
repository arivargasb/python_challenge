#++++++++++++++++++++++++++++++
# NAME OF PROGRAM: PyBank.py
#++++++++++++++++++++++++++++++

import os
import csv
import textwrap


# Path to collect budget data
csvpath = os.path.join("budget_data.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader, None) # Skip first row

    months=0 # define variable for counting months
    profits=0 # define variable for adding profits/losses
    profits_list = [] # define list for pulling profits
    months_list=[] # define list for pulling months
    for row in csvreader:
#---------------------------
# I. TOTAL NUMBER OF MONTHS
#---------------------------
        months += 1 # counting total number of months included in the dataset
        profits_list.append(row[1]) # List of profits/losses
#---------------------------
# II. NET AMOUNT OF PROFITS
#---------------------------
        profits=profits+int(row[1]) # adding up profits
        months_list.append(row[0]) # List of months
# print("total profits: "+ str(profits))
# for x in range(len(months_list)): 
#     print (months_list[x]) 

# Create a dictionary with months and profits
dict_profits = dict(zip(months_list, profits_list)) # pulling together months and profits lists 
#print(dict_profits)

# Average of changes in "Profit/Losses" over the entire period

change_list=[0] # list for storing monthly change in profits where first value is zero
change=0 # step 1: create a variable for monthly change in profits
for i in range(len(profits_list)-1): #loop over profits list...
    change=int(profits_list[i+1])-int(profits_list[i]) # ... and subtract previous month's profits to calculate monthly change 
    change_list.append(change) # step 2: append all values from monthly profits' change variable to it's list

#---------------------------------
# III. AVERAGE CHANGES IN PROFITS
#---------------------------------          
change_average=sum(change_list)/len(change_list) # calculating average monthly change in profits
# print("Average monthly change in profits: " + str(round(change_average, 2))) 

#-----------------------------------------------
# IV. GREATEST AND LOWEST INCREASE IN PROFITS
#-----------------------------------------------


# Greatest increase in profits (date and amount) over the entire period
change_greatest=0 
change_lowest=0

for i in range(len(change_list)-1): # search through list of monthly changes 
    if change_list[i] > change_greatest : # replace value of variable for greatest change each time a higher value is found
        change_greatest=change_list[i]  
    if change_list[i] < change_lowest : # replace value of variable for lowest change each time a lower value is found
        change_lowest=change_list[i]

dict_change = dict(zip(months_list, change_list)) # put together list with months and changes in profits into a dictionary


#print("lowest change: "+str(change_lowest) + ", highest change: " + str(change_greatest))

for month, profchan in dict_change.items(): # search through dictionary for the month of the highest and lowest value
    if profchan==change_greatest:
        month_greatest=month
        # print("month of greatest change: " + month_greatest )
    if profchan==change_lowest:
        month_lowest=month
        # print("month of lowest change: " + month_lowest ) 

#-----------------------------------------------
# V. PRINT SUMMARY OF RESULTS IN TERMINAL
#-----------------------------------------------

print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(months))
print( "Average change: $"+ str(round(change_average,2)))
print("Greatest Decrease in Profits: " + str(month_greatest) + " (" + str(change_greatest) + ")" )
print("Greatest Decrease in Profits: " + str(month_lowest) + " (" + str(change_lowest) + ")" )

#-----------------------------------------------
# VI. PRINT RESULTS IN TXT FILE
#-----------------------------------------------

file = open("PyBank.txt","w") 

file.write("Financial Analysis\n")
file.write("-----------------------\n")
file.write("Total Months: " + str(months) + "\n")
file.write( "Average change: $"+ str(round(change_average,2))+ "\n")
file.write("Greatest Decrease in Profits: " + str(month_greatest) + " (" + str(change_greatest) + ")\n" )
file.write("Greatest Decrease in Profits: " + str(month_lowest) + "(" + str(change_lowest) + ")\n" )

file.close() 
