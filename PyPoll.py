import csv
import os


# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# 1. Initialize a total vote counter
total_votes = 0

# candidate_options is an empty list created/declared that will have all the candidates
candidate_options = []

# candidate_votes is an empty dictionary created/declared that will have candidate's name as key and the vote count as value for the key
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the elections results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row. Skip the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Use an if statement to check if the candidate name has been already added to the list, therefore it won't print all the names in each row
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking the candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
            
    # Print the final vote count to the terminal
    election_results = (f"\nElection Results\n------------\nTotal Votes: {total_votes: ,}\n-----------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)
      
# 3. Print the total votes after the loop has gone through all the rows        
#print(total_votes)

# 4. Print the candidate list
#print(candidate_options)

# Print the candidate vote dictionary
#print(candidate_votes)

    # Calculates/Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
    
        # retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")

        # Print each candidate, their vote count and percentage to the terminal
        print(candidate_results)

        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            # if true then set winning_count = votes and winning_percentage = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (f"-------------\nWinner: {winning_candidate}\nWinning Vote Count: {winning_count: ,}\nWinning Percentage: {winning_percentage: .1f}%\n-----------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
        





# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
