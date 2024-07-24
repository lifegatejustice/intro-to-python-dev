#I used double qoutes because a word in my first question contains a single quote.
question_one = float(input("What is the price of a child's meal? "))

question_two = float(input("What is the price of an adult's meal? "))

question_three = int(input('How many children are there? '))

question_four = int(input('How many adults are there? '))

determsubtotal = question_three * question_one
determsubtotal2 = question_four * question_two
finaldetermsubtotal = determsubtotal + determsubtotal2

print('Subtotal: $'+ str(finaldetermsubtotal))

question_five = float(input('What is the sales tax rate? '))

determsalestax = finaldetermsubtotal * question_five / 100

print('Sales Tax: $' + str(determsalestax))
total = finaldetermsubtotal + determsalestax
print('Total: $' + str(total))

question_six = float(input('What is the payment amount? '))
change = question_six - total 

print('Change: $' + str(change))