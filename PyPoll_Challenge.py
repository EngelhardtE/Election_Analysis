import csv
import os
from this import d

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")


total_votes = 0


county_options = [] 


county_votes = {} 


winning_county = ""
winning_count = 0
winning_percentage = 0


candidate_options = [] 
candidate_votes = {} 
winning_candidate = ""
winning_candidate_count = 0
winning_candidate_percentage = 0



with open(file_to_load) as election_data:

     file_reader = csv.reader(election_data)


     headers = next(file_reader)
     print(headers)


     for row in file_reader:

          total_votes += 1

          print(total_votes)

          county_name = row[1]
          if county_name not in county_options:
               county_options.append(county_name)
               county_votes[county_name] = 0
          county_votes[county_name] += 1

          candidate_name = row[2]
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               candidate_votes[candidate_name] = 0
          candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:


     election_results = (
          f"\nElection Results\n"
          f"-------------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"-------------------------\n"
          f"\n"
          f"County Votes:\n")
     print(election_results, end="")

     txt_file.write(election_results)
     for county_name in county_votes:
                    
          votes = county_votes[county_name]     
          vote_percentage = float(votes) / float(total_votes) * 100
          county_results = (
               f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
          print(county_results)          
     
          txt_file.write(county_results)

          if (votes > winning_count) and (vote_percentage > winning_percentage):

               winning_count = votes
               winning_percentage = vote_percentage
               winning_county = county_name
     

     turnout_results = (
          f"\n"
          f"-------------------------\n"
          f"Largest County Turnout: {winning_county}\n"
          f"-------------------------\n"
          f"\n")
     txt_file.write(turnout_results)
     print(turnout_results)

     for candidate_name in candidate_votes:
                    
          votes = candidate_votes[candidate_name]     
          vote_percentage = float(votes) / float(total_votes) * 100
          candidate_results = (
               f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          print(candidate_results)          

          txt_file.write(candidate_results)

          if (votes > winning_candidate_count) and (vote_percentage > winning_candidate_percentage):
               winning_candidate_count = votes
               winning_candidate_percentage = vote_percentage
               winning_candidate = candidate_name
               
     winning_county_summary = (
          f"-------------------------\n"
          f"Largest County Turnout: {winning_county}\n"
          f"-------------------------\n")
     winning_candidate_summary = (
          f"\n"
          f"-------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_candidate_count:,}\n"
          f"Winning Percentage: {winning_candidate_percentage:.1f}%\n"
          f"-------------------------\n")
     txt_file.write(winning_candidate_summary) 
     print(winning_candidate_summary)