import os
import csv


input_file = csv.DictReader(open("election_data.csv"))
for row in input_file:
    print (row)

# Path to collect data from the Resources folder
# csvpath = os.path.join("election_data.csv")
# with open(csvpath, 'r', newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
    # # for row in csvreader:
    # #     print (row[0] + row[1] + row[2])
    
    # next(csvreader, None) # Skip first row

    # votes_tot=0
    # votes_per=0
    # candidates=[]
    # dic = {}


    # for row in csvreader:
    #     # votes_tot += 1 # votes count
    #     if row[2] not in candidates:
    #         candidates.append(row[2]) # create list of candidates
    # print(len(candidates)) # 4 candidates

    # votes_list=[0,0,0,0]

    # dic = dict(zip(candidates, votes_list))
    # print(dic)
    # print(sum(dic.values()))



    # dict["a"] += 1

            
input_file = csv.DictReader(open("election_data.csv"))
for row in input_file:
    print (row)

#     #sum the values with same keys 
# dic_collapse = {} 
# for d in dic: 
#     for k in d.keys(): 
#         dic_collapse[k] = dic_collapse.get(k, 0) + d[k] 

# print(str(dic_collapse))

# The total number of votes cast:
    # print("Total votes: " + str(votes_tot))

# # A complete list of candidates who received votes
    # for x in range(len(candidates)): 
    #     print (candidates[x])

# The percentage of votes each candidate won
    

# The total number of votes each candidate won


# The winner of the election based on popular vote.