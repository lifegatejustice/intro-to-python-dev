clients =[]
new_client = ''
while new_client != 'quit':
    new_client = input('Whats the name of your Client?')
    clients.append(new_client)

for client in clients:
    print(client)
