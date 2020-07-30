#import dependencies
import csv
import os

#import csv file
Election_Data_File=os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#define variables
total_votes=0
candidates_list=[]
candidate_vote_percentage={}
total_candidate_votes=0
election_winner=""


with open (Election_Data_File) as Election_Data:
    reader= csv.reader(Election_Data)
    header= next(reader)
    print(header)

    for row in reader:
        total_votes=total_votes + 1
        candidatename=row[2]
        if candidatename not in candidates_list:
            candidates_list.append (candidatename)
            candidate_vote_percentage[candidatename]=0
        candidate_vote_percentage[candidatename]=candidate_vote_percentage[candidatename]+1



with open ("Output.txt","w") as textfile: 
    #output of data
    output=(
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
             )

    print(output)

    textfile.write(output)

    for candidate in candidate_vote_percentage: 
        votes=candidate_vote_percentage[candidate]
        percentage=float(votes)/float(total_votes)*100
        if votes>total_candidate_votes:
            total_candidate_votes=votes
            election_winner=candidate

        output=(
            f"{candidate}: {percentage:.3f}% ({votes})\n"
            )
        print(output)

        textfile.write(output)
    output=(
        f"-------------------------\n"
        f"Winner: {election_winner}\n"
        f"-------------------------\n"
        )
    print(output)

    textfile.write(output)