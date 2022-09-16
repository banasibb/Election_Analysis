
# Add Dependencies.
import csv
from distutils import text_file
import os
# Assign a variable for the file to load the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a varible to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options and declare the empty candidate dictionary.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
    # Get the candidate name from each row.
        candidate_name = row[2]

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's vote count.
        candidate_votes[candidate_name] += 1
    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
        election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
    # Save the final vote count to the text file.
        txt_file.write(election_results)


    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count and a percentage of votes.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name, voter count and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print the candidate vote dictionary.
    # print(candidate_votes)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    # for candidate_name in candidate_votes:
    #     # Retrieve vote count of a candidate.
    #     votes = candidate_votes[candidate_name]
    #     # Calculate the percentage of votes.
    #     vote_percentage = float(votes) / float(total_votes) * 100

        #  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.

        # Determine winning vote count, winning percentage, and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    #  Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    #print(winning_candidate_summary)

# # Print the candidate list.
# print(candidate_options)
# # 3. Print total votes.
# print(total_votes)

# Print the candidate name from each row
    # candidate_name = row[2]
# to do: read and analyse the data here
    # print(election_data)
# Read the file object with the reader function
    # file_reader = csv.reader(election_data)
# Print each row in the csv file
    # for row in file_reader:
    #     print(row)
# # Using the with statement open the file as a text file
# with open (file_to_save, "w") as txt_file:
# # Write three counties to the file.
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# Close the file.
election_data.close()
