
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


csvpath = os.path.join("..", "Resources", "budget_data.csv")


# In[44]:


csvoutput = os.path.join("..", "Resources", "newbudget_data.csv")


# In[45]:


FinancialAnalysisout = os.path.join("..", "Resources", "financialanalysis.txt")


# In[43]:


#find total number of months included in the dataset
totalmonths = 0
totalrevenue = 0
netchange_list=[]
greatest_decrease = ["",99999999]
greatest_increase = ["", 0]

with open(csvpath) as csvbudget:
    
    csvreader = csv.reader(csvbudget)
    #This next gets us to the header. 
    csvheader = next(csvreader)
    #prints the entire row with the header of columns. 
    #print(csvheader)
    #This next gets us to the first row with values
    for row in csvreader:
        #print(prevnet)
        totalmonths = totalmonths + 1
        #Calculate the total net amount of "Profit/Losses" over the entire period
        totalrevenue = totalrevenue + int(row[1])
    #print(totalrevenue)
    #print(totalmonths)    
with open(csvpath) as csvbudget:
    
    csvreader = csv.reader(csvbudget)
    #This next gets us to the header. 
    csvheader = next(csvreader)  
    firstrow = next(csvreader)
    #prints the entire row with the first values
    #print(firstrow)
    prevnet = int(firstrow[1])
    #print(prevnet)
    
    for row in csvreader:
        netchange = int(row[1])-prevnet
        prevnet = int(row[1])
        #Lists are mutable so you dont need to redifine lists when you are appending. 
        netchange_list.append(netchange)
        #Find the greatest increase by comparing each netchange with zero first and then each net change that 
        #is bigger than what is stored in the greatest increase list. 
        if netchange > greatest_increase[1]:
            #Store the month of the increase that is greater than the net change.
            greatest_increase[0] = row[0]
            #Store the value of the increase that is greater than the net change. 
            greatest_increase[1] = netchange     
        if netchange < greatest_decrease[1] :
            greatest_decrease[0]= row[0]
            greatest_decrease[1]=netchange
        
netmonthlyaverage = round(sum(netchange_list)/len(netchange_list),2)     
 # The 'f' at the beginning makes sure that you call the contents in the curly braces as a variable so it eliminates
    #the concatenations + signs. 
output = (f"Financial Analysis \nTotal Months: {totalmonths}") 

print(output)
print(f"Total Revenue is: ${totalrevenue}\n"
      f"Net monthly average change is: ${netmonthlyaverage}")    
print(f"The greatest increase in profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
     f"The greatest decrease in profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

   


# In[57]:


with open(FinancialAnalysisout, "w") as text:
    
    text.write("Financial Analysis.\nTotal Months: 86. \nTotal Revenue is: $38382578. \nNet monthly average change is: $-2315.12. \nThe greatest increase in profits: Feb-2012 ($1926159). \nThe greatest decrease in profits: Sep-2013 ($-2196167)")

