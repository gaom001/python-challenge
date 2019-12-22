# import the modules (os and csv)
import os
import csv

# open and read csv file by usng absolute path
pybank_csv=os.path.join("C:/MG/2019 SMU DS/Homework MG/Python/Instructions/PyPoll/Resources/election_data.csv")

# initaite empty dictionaries and list, declare variables
candidate_count={}
candidate_count_percent={}
total_votes=[]
winner=""
winner_count=0

# Open and read csv file
with open(pybank_csv,"r", newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    # skip header
    header = next(csvreader,None)
    # Loop data from csv file,
    for row in csvreader:  
        total_votes.append(row[0])
        vote_total=len(total_votes)
    
# check if candidate names (as key) are in candidate{} or not, do the counting votes (key-paried value) for each candidate name in the candidate{}
        if row[2] in candidate_count.keys():
            candidate_count[row[2]] += 1
        else:
            candidate_count[row[2]] = 1

# for loop, add the percent_value into a new dictionary{candidate_count_percent} paried with the key from the old dictionary{candidate_count}
for key,value in candidate_count.items():
    candidate_count_percent[key]=round((value/vote_total)*100,2)


# for loop, use if condition to find the winner and winner votes
for key in candidate_count.keys(): 
    if  candidate_count[key]>winner_count:
        winner=key
        winner_count=candidate_count[key]  

# print out the results
print("Election Results")
print("------------------------------")
print(f'Total votes: {vote_total}')
print("------------------------------")
# for loop to print out all itmes
for key,value in candidate_count.items():
    print(f"{key}: {candidate_count_percent[key]}% ({value})")
print("------------------------------")
print(f"Winner: {winner}")        

# write out the output
output_path=os.path.join('C:/MG/2019 SMU DS/Homework MG/Python/Instructions/PyPoll/PyPoll Output.txt')
with open(output_path,"w") as text:
    text.write("Election Results \n")
    text.write("------------------------------------- \n")
    text.write(f"Total Votes: {vote_total} \n")
    text.write("------------------------------------- \n")
    for key, value in candidate_count.items():
        text.write(f"{key}: {candidate_count_percent[key]}% ({value}) \n")
    text.write("------------------------------------- \n")
    text.write(f"Winner: {winner} \n")
    text.write("------------------------------------- \n")

