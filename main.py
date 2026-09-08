from collections import defaultdict

voters = defaultdict(str) # voters dict
parties = ['A', 'B', 'C', 'D'] # parties
party_votes = defaultdict(int) # parties' votes

def get_valid_vote() -> str:
    while True:
        selection = input(f'Choose a party [{', '.join(parties)}]: ')
        if selection in parties:
            return selection
        else:
            print('Invalid selection, try again.')

def output_results():
    print('-' * 5, 'Results', '-' * 5)
    print(f'Sum of all votes: {sum(party_votes.values())}')
    print()
    print('Not Sorted | ', end='')
    for p, amount in party_votes.items():
        print(f'{p}: {amount}', end=' | ')
    print()
    print('Sorted | ', end='')
    for p in sorted(party_votes, key=party_votes.get, reverse=True): # type: ignore
        print(f'{p}: {party_votes[p]}', end=' | ')

while True: # voters loop
    voter_id = input("Enter voter ID: ")
    match voter_id:
        case '-999':
            break
        case n if voters.get(n):
            party = voters.get(n)
            party_votes[party] -= 1
            party_votes['F'] += 1
            voters[n] = 'F'
            print('Your vote is disqualified!')
            continue
    voter_party = get_valid_vote()
    voters[voter_id] = voter_party
    party_votes[voter_party] += 1

output_results()