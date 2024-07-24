
    adjective = get_word ('adjective')
    animal = get_word ('animal')
    verb = get_word ('verb')
    exclamation = get_word ('exclamation'.capitalize())
    verb2 = get_word ('verb2')
    verb3 = get_word ('verb3')



main_story = f'The other day, I was really in trouble. It all started when I saw a very\n'\
f'{'adjective'} {'animal'} {'verb'} down the hallway. {'exclamation'}! I yelled. But all \n '\
f'I could think to do was to {'verb2'} over and over. Miraculously,\n'\
f'that caused it to stop, but not before it tried to {'verb3'}\n'\
f'right in front of my family.\n'

print('Your story is: ' )
print('The other day, I was really in trouble. It all started when I saw a very ' + {'adjective'} + 'animal' + 'verb' + 'exclamation' + 'verb2' + 'verb3')
# story_1 = input('The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb}') 
# print(' ' + ' down the hallway.')
# story_2 =input('{exclamation}!')
# story_3 = input('I yelled. But all I could think to do was to {verb2}')
# story_4 = input('over and over. Miraculously, that caused it to stop, but not before it tried to {verb3}')
# print('right in front of my family.')

#experimenting if any word the user inputs can be gotten from the story and show automatically

#print(main_story)
clever_stories()
#print('Your story is: ' '\n The other day, I was really in trouble. It all started when I saw a very' + ' ' + story_1 +  'down the hallway.' + ' ' + story_2.capitalize() + ' ' + 'I yelled. But all I could think to do was to' + ' ' + story_3 + 'over and over. Miraculously, that caused it to stop, but not before it tried to ' + story_4 + ' ' + 'right in front of my family.')