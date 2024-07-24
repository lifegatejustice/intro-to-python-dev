# 
#THE ELIF WILL LET THE PYTHON CHECK FOR THE CODITION AND MOVE TO THE NEXT IF THERE ARE MULTIPLE CONDITIONS
    

province = input('Where do you live in? ')
tax = 0
if province.lower() == 'Abia':
    tax = 1.5
elif province.lower() == 'Ananbara':
    tax = 1.5
elif province.lower() == 'Enugu':
    tax = 1.5
else:
    tax = 100
    print(tax)