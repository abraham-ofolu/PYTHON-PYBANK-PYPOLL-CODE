from distutils import text_file
import os
import csv


csvpath = "/Users/abrahamofolu/Documents/GitHub/python-challenge/Resources/election_data.csv"

with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)
    #print (f"CSV Header: {csv_headers}"

    # print heading 
    print ("Election Results")
    print ("-----------------------")


    # Total Vote Counter
    total_votes = 0

    # Candidate Options and Vote Counters
    candidate_options = []
    candidate_votes = {}

    # Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0

    # Read in cav and convert into a list of Dictionaries
    with open(csvpath) as election_data:
        reader = csv.DictReader(election_data)

        # For each row..
        for row in reader:

            # Add to the total vote count
            total_votes = total_votes + 1

            # Extract the candidate name from each row
            candidate_name = row["Candidate"]

            # If the candidate does not match any existing candidate
            if candidate_name not in candidate_options:

                #Add it to the list of candidates count
                candidate_options.append(candidate_name)

                ## and begin to track that candidates vote count
                candidate_votes[candidate_name] = 0

            # Then add a vote to that candidates count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# print the results and export the data to text file output
exportpath = ("/Users/abrahamofolu/Documents/GitHub/python-challenge/Analysis/PyPoll_output.txt")
with open(exportpath, "w") as textfile:

    # Print the final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"-----------------------------"
        f"Total Votes: {total_votes}\n"
        f"------------------------------\n"
    )
    print(election_results)

    # Save the final vote count to the text file
    textfile.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidates voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)

        # save each candidates voters count and percentage to text file
        textfile.write(voter_output)

    # Print the winning candidate
    winning_candidate_summary = (
        f"-------------------------------"
        f"Winner: {winning_candidate}\n"
        f"---------------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidates name to the text file
    textfile.write(winning_candidate_summary)