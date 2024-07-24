flashstorytwo = 'You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? '
storyone = input('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ')
if storyone == 'match':
    storytwo= input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
    if storytwo == 'run':
        print("As you sprint away from the bear, you stumble upon a mysterious cave entrance. The darkness inside is overwhelming. Do you want to ENTER the cave or CONTINUE running deeper into the forest? ")
        if storytwo == 'enter':
            print('')

        else:
            print('{flashstorytwo}')
            
            
                 
                 