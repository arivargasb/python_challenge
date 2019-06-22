#++++++++++++++++++++++++++++++
# NAME OF PROGRAM: PyPoll2.py
#++++++++++++++++++++++++++++++

import os
import csv


csvpath = os.path.join("election_data.csv")
with open(csvpath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # for row in csvreader:
    #     print (row[0] + row[1] + row[2])
    
    next(csvreader, None) # Skip first row

    votes_tot=0
    votes_per=0
    candidates=[]
    dic = {}

    all_votes=[] # this one is for storing all votes (each time a candidate is mentioned in the file)

    for row in csvreader:
#---------------------------
# I. TOTAL NUMBER OF VOTES
#---------------------------
        votes_tot += 1 # votes count
        all_votes.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2]) # create list of candidates
    
    # print(len(candidates)) # number of candidates: 4 
    # print(str(votes_tot)) # total number of votes

    # for x in range(len(all_votes)): 
    #     print (all_votes[x])
#------------------------------
# II. LIST OF THE 4 CANDIDATES
#------------------------------

    # for x in range(len(candidates)): 
        # print (candidates[x])

#------------------------------------
# III. NUMBER OF VOTES PER CANDIDATE
#------------------------------------

    votes_list=[0,0,0,0] # create list for counting the votes of each candidate

    d_candidates = dict(zip(candidates, votes_list)) # dictionary for storing candidates and total votes

    # print(sum(dic.values()))

    for k in d_candidates.keys(): # for each candidate (each one is a key)
        for x in range(len(all_votes)): #... search 
            if all_votes[x]==k:
                d_candidates[k]+=1                

    # print(d_candidates)

#---------------------------------------
# IV. PERCENTAGE OF VOTES PER CANDIDATE
#---------------------------------------

    d_candidates_per={}
    d_candidates_per = dict.fromkeys(d_candidates)
    # print(d_candidates_per)

    for k in d_candidates.keys(): # for each candidate (each one is a key)
        d_candidates_per[k] = d_candidates[k]/votes_tot
    # print (d_candidates_per)

    from collections import defaultdict
    d_candidates_all = defaultdict(list)
    for d in (d_candidates, d_candidates_per):
        for key, value in d.items():
            d_candidates_all[key].append(value)
    # print(d_candidates_all)

    votes_winner=0
    for k,v in d_candidates_all.items():
        if v[0]>votes_winner:
            votes_winner=v[0]
    # print(str(votes_winner))
    winner= [k for k, v in d_candidates_all.items() if v[0] == votes_winner ]
    # print(winner)
    winner_can=' '.join(map(str, winner))
    print(winner_can)
#---------------------------------------
# V. PRINT RESULTS IN TERMINAL
#---------------------------------------

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes_tot))
print("-------------------------")
for k,v in d_candidates_all.items():
    print(k + " : " + str("{0:.3%}".format(v[1]) ) + " (" + str(v[0]) + ")")
print("-------------------------")
print ("Winner: " + winner_can+"\n")
print("-------------------------")


# #---------------------------------------
# # V. PRINT RESULTS IN TXT FILE
# #---------------------------------------

file = open("PyPoll.txt","w") 
 
file.write("Election Results \n")
file.write("-------------------------\n")
file.write("Total Votes: " + str(votes_tot)+ "\n")
# file.write("-------------------------")
for k,v in d_candidates_all.items():
    file.write(k + " : " + str("{0:.3%}".format(v[1]) ) + " (" + str(v[0]) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + winner_can + "\n")
file.write("-------------------------\n")

file.close() 