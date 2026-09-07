voted_ids = {}
parties = ['A', 'B', 'C', 'D']
votes = {}
while True:
    voter_id = input('Enter your ID: ')
    if voter_id == '-999':
        break
    if voted_ids.get(voter_id) is not None:
        party = voted_ids.get(voter_id)
        votes.update(F=votes.get('F', 0) + 1)
        votes.update({party: votes.get(party, 1) - 1})  # Setting the default doesn't make a sense but I got type warning without it.
        print('Your vote is disqualified.')
        continue
    while True:
        vote_selection = input(f'Choose a party [{','.join(parties)}]: ')
        match vote_selection:
            case n if n in parties:
                voted_ids.update({voter_id: vote_selection})
                votes.update({vote_selection: votes.get(vote_selection, 0) + 1})
                break
            case _:
                print('Invalid vote, try again.')
print(f'Sum of all votes: {sum(votes.values())}')
print('-' * 10)
for party, amount in votes.items():
    print(f'Party: {party} got {amount} votes.')
print('-' * 10)
for party in sorted(votes, key=votes.get, reverse=True):
    amount = votes.get(party)
    print(f'Party: {party} got {amount} votes.')