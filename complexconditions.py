question1 = int(input('How large is the loan? '))
question2 = int(input('How good is your credit history? '))
question3 = int(input('How high is your income? '))
question4 = int(input('How large is your down payment? '))


if question1 >= 5:
   if question2 >= 7 and question3 >= 7:
    if question2 >= 7 and question3 >=7:
      if question4 >=5:
        print('yes')
        decision = True
      else:
        print('no')
        if question1 < 5:
           if question2 < 4:
             print('no')
           else:
             if question3 >= 7 or question4 >= 7:
               if question3 >= 4 and question4 >= 4:
                 print('yes')
               else:
                 print('no')
                 decision = False




   
