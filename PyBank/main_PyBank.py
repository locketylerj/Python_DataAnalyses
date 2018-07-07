
# coding: utf-8

# In[2]:


import os
import csv


# In[3]:


csvpath = os.path.join("..", "Resources", "budget_data.csv")


# In[4]:


csvoutput = os.path.join("..", "Resources", "newbudget_data.csv")


# In[5]:


FinancialAnalysisout = os.path.join("..", "Resources", "financialanalysis.txt")


# In[6]:


#find total number of months included in the dataset
totalmonths = 0
totalrevenue = 0
#The net change list is going to be added to when we loop through the rows and add each new difference(delta) bewteen the cell
#value below and the value above. 
netchange_list=[]
#This list holds two values: one for the date column ("") and one for the values column. The values column value(999999)
#is an arbitrarily large number that the netchange is first compared with in the loop to see if the netchange is less than this
#number. If it is less than it, then that value is added to this list in the place of 999999. If the next netchange below 
#that is less than that net change then that value is put in the place of the last net change and on and on through the loop below. 
#See the csv file "budget_data" for a breakdown of the loop. 
greatest_decrease = ["",99999999]
#The same for greatest increase but flipped so that we first compare the net change with zero and then each net change after that
greatest_increase = ["", 0]

with open(csvpath) as csvbudget:
    
    csvreader = csv.reader(csvbudget)
    #This next gets us to the header. 
    csvheader = next(csvreader)
    #below #prints the entire row with the columns headers. 
    #print(csvheader)
   
    for row in csvreader:
        #Calculates the total months which is essentially the total number of rows with data (each row is a different month)
        #So each time we go through a row, we add one to the totalmonths variable. 
        totalmonths = totalmonths + 1
        #Calculate the total net amount of "Profit/Losses" over the entire period. Similar to the above. Except 
        #each value in row index 1 is added to the each other for every row.
        totalrevenue = totalrevenue + int(row[1])
    #print(totalrevenue)
    #print(totalmonths)    
with open(csvpath) as csvbudget:
    
    csvreader = csv.reader(csvbudget)
    #This next gets us up to the header.
    csvheader = next(csvreader)  
     #This next gets us to the first row with values
    firstrow = next(csvreader)
    #prints the entire row with the first values
    #print(firstrow)
    prevnet = int(firstrow[1])
    #Below print function, prints out the very first value from the csv file. 
    #print(prevnet)
    for row in csvreader:
        #For each row subtract the row after(prevnet)from the row before
        netchange = int(row[1])-prevnet
        #Reset prevnet to the next value down. 
        prevnet = int(row[1])
        #Lists are mutable so you dont need to redefine lists when you are appending. 
        #add the netchange from the above equation to the list. 
        netchange_list.append(netchange)
        #Find the greatest increase by comparing each netchange with zero first and then each net change that 
        #is bigger than what is stored in the greatest increase list. 
        if netchange > greatest_increase[1]:
            #Store the month of the increase that is greater than the net change.
            greatest_increase[0] = row[0]
            #Store the value of the increase that is greater than the net change. 
            greatest_increase[1] = netchange     
        if netchange < greatest_decrease[1] :
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange
#calculate the average monthly change by dividing the length of the list by the sum of the list values         
netmonthlyaverage = round(sum(netchange_list)/len(netchange_list),2)     
# The 'f' at the beginning makes sure that you call the contents in the curly braces as a variable so it eliminates
#the concatenations + signs. 
output = (f"Financial Analysis \nTotal Months: {totalmonths} \n"
         f"Total Revenue is: ${totalrevenue}\n"
         f"Net monthly average change is: ${netmonthlyaverage} \n"
         f"The greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
         f"The greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]}")

print(output)
#print(f"Total Revenue is: ${totalrevenue}\n"
      #f"Net monthly average change is: ${netmonthlyaverage}")    
#print(f"The greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
     #f"The greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

   


# In[7]:


#Print the financial analysis data to the text file specified at the beginning. 
with open(FinancialAnalysisout, "w") as text:
    
    text.write(output)
    

