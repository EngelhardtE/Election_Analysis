import csv
import os
from this import d
# Create a filename variable to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Initialize candidate_options
candidate_options = [] 

#Declare an empty votes dictionary
candidate_votes = {} 

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     #Read the file object with the reader function.
     file_reader = csv.reader(election_data)

     #Read the header row
     headers = next(file_reader)
     print(headers)

     #Print each row in the csv 
     for row in file_reader:
          #Add to the total vote count
          total_votes += 1
          #print total votes
          print(total_votes)
          #Print the candidate name from each row
          candidate_name = row[2]
          if candidate_name not in candidate_options:
               #Add the candidate name to the candidate list
               candidate_options.append(candidate_name)
               #Begin tracking vote count by candidate
               candidate_votes[candidate_name] = 0
          #Add a vote to the candidate's count
          candidate_votes[candidate_name] += 1

     # Determine the percentage of votes for each candidate by looping through the counts.
     # 1. Iterate through the candidate list.

with open(file_to_save, "w") as txt_file:

     # Print the final vote count to the terminal.
     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)
     for candidate_name in candidate_votes:
                    
          votes = candidate_votes[candidate_name]     
          vote_percentage = float(votes) / float(total_votes) * 100
          candidate_results = (
               f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          print(candidate_results)          
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)
          # Determine winning vote count and candidate
          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent = vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name
               
     winning_candidate_summary = (
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-------------------------\n")
     # Save the winning candidate's name to the text file.
     txt_file.write(winning_candidate_summary)