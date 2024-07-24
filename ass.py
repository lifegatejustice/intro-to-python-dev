#stories
stories1 = input('Welcome to the dark forest! You find yourself surrounded by towering trees, and as you explore, you come across two intriguing items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ')

storymatch = 'You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? '

storymatchrun = 'As you sprint away from the bear, you stumble upon a mysterious cave entrance. The darkness inside is overwhelming. Do you want to ENTER the cave or CONTINUE running deeper into the forest? '

storymatchenter = 'You cautiously enter the cave, and as you delve deeper, you notice strange markings on the walls. Suddenly, you encounter a fork in the cave. Do you want to TURN LEFT or TURN RIGHT?'

storymatchcontinue = 'As you keep running through the forest, you stumble upon a mystical pond with glowing water. However, a mysterious figure appears on the other side. Do you want to APPROACH the figure or CIRCLE around the pond? '

story1matchhide = 'You successfully conceal yourself behind a tree, and the grizzly bear loses interest. However, you notice a faint glow coming from a distant clearing. Do you want to INVESTIGATE the glow or STAY hidden? '

story1matchhideinvestigate ='Upon investigating, you find a hidden campsite with remnants of a recent fire. You hear distant footsteps approaching. Do you want to WAIT silently or HIDE behind a bush? '

story1matchhidewait = 'You remain hidden and observe as a mysterious figure with a lantern passes by. A narrow path leads towards a mystical grove. Do you want to FOLLOW the figure or EXPLORE the grove on your own? '

story1matchhidestay = 'You remain hidden and observe as a mysterious figure with a lantern passes by. A narrow path leads towards a mystical grove. Do you want to FOLLOW the figure or EXPLORE the grove on your own? '

story1matchhidefollow = 'As you ascend the uphill path, you encounter a rickety bridge spanning a chasm. The other side seems to lead to a hidden garden. Do you want to CROSS the bridge or TURN BACK? '

story2flashlight = 'You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? '

story2flashlightfollow = 'As you follow the illuminated path, you reach a fork in the road. One path leads uphill, and the other descends into a mysterious fog. Do you want to GO uphill or DESCEND into the fog?'

story2flashlightlook = 'You search the trees and discover a hidden nest of glowing fireflies. Mesmerized by their beauty, you notice a narrow trail leading deeper into the forest. Do you want to FOLLOW the trail or IGNORE the fireflies and explore on your own? '

story2flashlightfollowfire = "You decide to follow the mesmerizing trail of fireflies. The path leads you to a tranquil meadow bathed in their soft glow. In the center, there's a mystical fountain. Do you want to DRINK from the fountain or OBSERVE the surroundings first? "

story2flashlightfollowgo = 'You decide to venture into the mystical grove on your own. As you explore, you come across an ancient altar surrounded by fireflies. A mysterious voice whispers a riddle. Do you want to SOLVE the riddle or IGNORE it and MOVE on? '

story2flashlightdescend = 'You descend into the fog, and the surroundings become ethereal. A mysterious voice calls out, offering guidance. Do you want to LISTEN to the voice or IGNORE it and forge ahead? '

storyfirefliesignore = 'You decide to ignore the trail of fireflies and continue exploring on your own. As you venture deeper into the forest, you come across a mysterious mist-covered clearing. Do you want to ENTER the clearing or CIRCLE around it cautiously? '

if stories1.lower() == 'match':
    print(storymatch)
    user_chioce = input().lower()
    
    if user_chioce.lower() == 'run':
        print(storymatchrun)
        user_chioce = input().lower()
        if user_chioce.lower() == 'enter':
            print(storymatchenter)
        elif user_chioce.lower() == 'continue':
            print(storymatchcontinue)
        else:
            print('Invalid Choice')
    elif user_chioce.lower() == 'hide':
        print(story1matchhide)
        user_chioce = input().lower()
    else:
        print('Invalid Choice')
        if user_chioce.lower() == 'investigate':
            print(story1matchhideinvestigate)
            if user_chioce.lower() == 'wait':
                print(story1matchhidewait)
        elif user_chioce.lower() == 'stay':
            print(story1matchhidestay)
            user_chioce = input().lower()
        else:
            print('Invalid Choice')
elif stories1.lower() == 'flashlight':
        print(story2flashlight)
        user_chioce = input().lower()
        if user_chioce.lower() == 'follow':
            print(story2flashlightfollow)
            user_chioce = input().lower()
            if user_chioce.lower() == 'go':
                print(story2flashlightfollowgo)
                user_chioce = input().lower()
                if user_chioce.lower() == 'solve' or user_chioce.lower() == 'ignore' or user_chioce.lower() == 'move':
                    print("😁😁you have no idea what's instore for you")
                else:
                    print('Invalid Choice')

        elif user_chioce.lower() == 'look':
            print(story2flashlightlook)
            user_chioce = input().lower()
        else:
            print('Invalid Choice')
            if user_chioce.lower() == 'follow':
                print(story2flashlightfollowfire)
                user_chioce = input().lower()
            elif user_chioce.lower() == 'ignore':
                    print(storyfirefliesignore)
            else:
                print('Try Again')

else:
   print('Invalid Choice')
        
        

            



        

