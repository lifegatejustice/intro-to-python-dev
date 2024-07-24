# friends = ['luc','kristi', 'rex']
# tips = [12.25, 13.95, 0.50]
# running_total: float
# running_total = 0

# for tip_amount in tips:
#     running_total = running_total + tip_amount
# print(f'The total is: {running_total:.2f}')

friends = []
new_friends = ''

while new_friends != 'quit':
    new_friends = input('What are the names of your friends')
    if new_friends != 'end':
        friends.append(new_friends)
        


print()
print('Your new friends are:')

for friend in friends:
    
    print(friend)