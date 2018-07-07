
# coding: utf-8

# In[133]:


import os
import csv
csvpath = os.path.join("..","Resources", "election_data.csv")
outputpath = os.path.join("..", "Resources", "electionsmry.txt")
totalvotes = 0
candidatelist = []
khantotal = 0
correytotal = 0
litotal = 0
otooleytotal = 0
winner=["", 0]
percentagelist=[]


# In[134]:


with open(csvpath) as electioncsv:
    csvreader = csv.reader(electioncsv)
    csvheader = next(csvreader)
    for row in csvreader:
        #calculates the total number of votes cast by basically counting all the individual rows.
        totalvotes = totalvotes + 1
        #provides the complete list of candidates who received votes. 
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
    print(f"{candidatelist}")
    print(f"{totalvotes}")

    


# In[135]:


with open(csvpath) as electioncsv:
    csvreader = csv.reader(electioncsv)
    csvheader = next(csvreader)
    
    for row in csvreader:
        if (row[2]=="Khan"):
            khantotal = khantotal + 1
        elif (row[2]=="Correy"):
            correytotal = correytotal +1
            
        elif (row[2]=="Li"):
              litotal = litotal +1
        elif (row[2]=="O'Tooley"):
            otooleytotal = otooleytotal + 1

    khanpercentage = round((khantotal/totalvotes)*100,3)
    correypercentage =round((correytotal/totalvotes)*100,3)
    lipercentage = round((litotal/totalvotes)*100,3)
    otooleypercentage = round((otooleytotal/totalvotes)*100,3)
    percentagelist.append(khanpercentage)
    percentagelist.append(correypercentage)
    percentagelist.append(lipercentage)
    percentagelist.append(otooleypercentage)
    
    for percent in percentagelist:
        imax = percentagelist.index(max(percentagelist))
        if percent > winner[1]:
            winner[1] = percent
            winner[0] = candidatelist[imax]
    output=(f"Election Results \n"
            f"Total Votes: {totalvotes} \n"
            f"Khan: {khanpercentage}% ({khantotal}) \n"
            f"Correy: {correypercentage}% ({correytotal})\n"
            f"Li: {lipercentage}% ({litotal})\n"
            f"O'Tooley: {otooleypercentage}% ({otooleytotal})\n"
            f"Winner: {winner[0]}: {winner[1]}%")
    
    print(output)


# In[136]:


with open(outputpath, "w") as text:
    text.write(output)

