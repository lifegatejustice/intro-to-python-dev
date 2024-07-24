#I added my own cretive questions in the code for my full 100%😉.

#I added children and adluts drinks and appettizers. Comments with creativity signifies that the next code is part of my creativity for my 100%😉

#I used double qoutes because a word in my first question contains a single quote.
question_one = float(input("What is the price of a child's meal? "))

#creativity
creative_quesion1 = float(input("What is the price of a child's drink? "))

question_two = float(input("What is the price of an adult's meal? "))

#creativity
creative_quesion2 = float(input("What is the price of an adult's drink? "))

#creativity
creative_quesion3 = float(input("What is the price of a child's appetizer? "))

#creativity
creative_quesion4 = float(input("What is the price of an adult's appetizer? "))

question_three = int(input('How many children are there? '))

question_four = int(input('How many adults are there? '))

determsubtotal = question_three * question_one * creative_quesion1 *creative_quesion3

determsubtotal2 = question_four * question_two * creative_quesion2 * creative_quesion4
finaldetermsubtotal = determsubtotal + determsubtotal2

print(f'Subtotal: ${finaldetermsubtotal:.2f}'+ str(finaldetermsubtotal))

question_five = float(input('What is the sales tax rate? '))

determsalestax = finaldetermsubtotal * question_five / 100

print('Sales Tax: $' + str(determsalestax))
total = finaldetermsubtotal + determsalestax
print('Total: $' + str(total))

question_six = float(input('What is the payment amount? '))
change = question_six - total 

print('Change: $' + str(change))