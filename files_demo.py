# with open('courses.txt') as courses_file:
#     for line in courses_file:
#         print(line)
    

# colors = 'red,green,yellow'

# color_paths = colors.split(',')

# print(colors)
# print(color_paths)


# name = '\tLifegate Justice \n'
# name = name.strip()
# print(f'___(name)___')

with open('courses.txt') as courses_file:
    for line in courses_file:
        parts = line.split(',')

        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f'{name} - Grade: {grade}, after bonus: {bonus_grade}')

# with open('books.txt') as book_file:
#     for line in book_file:
#         book = line.strip()
#         print(book)

#         parts = line.split()
#         for word in parts:
#             print(word)
#         print(book_file)

# with open("books.txt") as book_file:

#     # Go through each line in the file, one by one
#     for line in book_file:
#         # The .strip() function returns a new line that doesn't have leading
#         # or trailing whitespace. In other words, it strips off the "\n" that
#         # would otherwise be at the end of each line.
#         book = line.strip()

#         # Print the book out to the screen
#         print(book)

# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]

# youngest_age = -1

# for item in people:
#     peoples = item[1]


#     if item < youngest_age:
#         youngest_age = item[1]

#         if price <

# print(f'The youngest is: {youngest_age}')


 


