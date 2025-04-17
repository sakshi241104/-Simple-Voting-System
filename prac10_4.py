# Simple Voting System

# Dictionary to store votes
votes = {}

def vote(candidate_name):
    # Convert to title case to avoid duplicates due to case differences
    candidate_name = candidate_name.title()
    if candidate_name in votes:
        votes[candidate_name] += 1
    else:
        votes[candidate_name] = 1
    print(f"Vote casted for {candidate_name}. Total votes: {votes[candidate_name]}")

def show_results():
    print("\n--- Voting Results ---")
    if not votes:
        print("No votes casted yet.")
    else:
        for candidate, count in votes.items():
            print(f"{candidate}: {count} votes")

# Main loop
while True:
    print("\n1. Cast Vote")
    print("2. Show Results")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter candidate name: ")
        vote(name)
    elif choice == "2":
        show_results()
    elif choice == "3":
        print("Exiting voting system.")
        break
    else:
        print("Invalid choice. Try again.")
