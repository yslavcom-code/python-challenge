import os
import pandas as pd

def get_file_data():
    directory = 'Resources'
    file_name = 'election_data.csv'
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, mode='r') as f:
        return pd.read_csv(f)
        

def output_data(str):
    # print to terminal
    print(str)
    
    # print to file
    directory = 'analysis'
    file_name = 'election_data.txt'
    file_path = os.path.join(directory, file_name)

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write to the file
    with open(file_path, 'w') as f:
        print(str, file=f)


if __name__ == "__main__":
    data = get_file_data()
    if data is not None:
        
        ballot_id = data['Ballot ID']
        total_votes = len(ballot_id)
        
        candidates = data['Candidate']
        candidate_vote_count = {}
        for candidate in candidates:
            if candidate in candidate_vote_count:
                counter = candidate_vote_count[candidate]
                candidate_vote_count[candidate] = counter + 1
            else:
                candidate_vote_count[candidate] = 0
        
        winner = max(candidate_vote_count, key=candidate_vote_count.get)
        
        # output        
        delimiter = '-------------------------'
        formatted_list = str(f"Election Results\n")
        formatted_list += str(f"{delimiter}\n")
        formatted_list += str(f"Total Votes: {total_votes}\n")
        formatted_list += str(f"{delimiter}\n")
        for name, votes in candidate_vote_count.items():
            formatted_list += str(f"{name}: {round((votes/total_votes*100), 3)}% ({votes})\n")
        formatted_list += str(f"{delimiter}\n")
        formatted_list += str(f"Winner: {winner}\n")
        formatted_list += str(f"{delimiter}\n")
        print(formatted_list)
                          