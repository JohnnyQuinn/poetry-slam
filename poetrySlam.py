import random
import string

"""
Asks user to choose a way to print out a poem. Options to print the poem are print lines normally, print lines in reverse, print lines in random order,
print only lines containing a word of the user's choosing, and print each line with the line's words randomized
"""

poem_txt = "./poetry slam/poem.txt"
#Poem citation: Chanie Gorkin

#Recieves txt file, opens, returns readlines() of txt, then closes
def get_file_lines(filename):
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close() 
    return lines

def lines_print_normally(lines_list):
    print("\n")
    for lines in lines_list:
        print(f"{lines}", end='')

#Prints txt file's lines backwards along with original line numbers
def lines_printed_backwards(lines_list):
    lines_len = len(lines_list) - 1
    print("\nPoem in reverse:\n----------------")
    for line_num in range(lines_len, -1, -1):
        print(f"{line_num} {lines_list[line_num]}", end='')
    return

#prints poem out with lines in a random order
def lines_printed_random(lines_list):
    print("\nPoem lines printed randomly: \n----------------------------")

    poem = lines_list

    while len(poem) > 0:
        ran_index = random.randint(0, len(poem)-1)
        print(poem[ran_index], end='')
        del poem[ran_index]
    return

#asks user to input a word and it will only print lines containing that word
def lines_printed_custom(lines_list):
    print("------------------------------------------------------------")
    print("Input a word and only lines containing that word will be printed")
    user_word = input("Input a word of your choice:\n")

    #prints out error message if input contains a number
    while any(char.isdigit() for char in user_word):
        print("------------------------------")
        print("ERROR: input contains a number")
        print("------------------------------")
        user_word = input("\nInput a word of your choice:\n")

    print("\n")

    #adds spaces surrounding user_word
    user_word = " " + user_word.lower() + " "
    
    print(f"Lines from the poem containing the word:{user_word}")
    print("-----------------------------------------------------")
    for line in lines_list:
        if user_word in line:
            print(line, end='')

    return

#goes through each line of the poem and prints the line with its words randomized
def randomize_words(lines_list):
    print("\n")
    for line in lines_list:
        word_list = line.split()
        while len(word_list) > 0:
            ran_index = random.randint(0, len(word_list)-1)
            print(word_list[ran_index], end=' ')
            del word_list[ran_index]  
        print("\n")       

#prints menu of options for user to choose
def print_menu():
    print("\nInput a number from the menu below to choose how the poem should be read:")
    print("_________________________________________________________")
    print("| 1 | Print normally ")
    print("| 2 | Print in reverse")
    print("| 3 | Print lines randomly")
    print("| 4 | Print lines only containing a word of your choice")
    print("| 5 | Print poem but each line's words are randomized")
    print("_________________________________________________________\nENTER 'stop' TO EXIT")

def choose_print():
    print("--------------------------------------------")
    print("Let's read 'Worst Day Ever' by Chanie Gorkin")
    print_menu()

    user_choice = input("")

    while user_choice != 'stop':
        if user_choice == '1':
            lines_print_normally(get_file_lines(poem_txt))
        elif user_choice == '2':
            lines_printed_backwards(get_file_lines(poem_txt))
        elif user_choice == '3':
            lines_printed_random(get_file_lines(poem_txt))
        elif user_choice == '4':
            lines_printed_custom(get_file_lines(poem_txt))
        elif user_choice == '5':
            randomize_words(get_file_lines(poem_txt))
        print_menu()
        user_choice = input("")

choose_print()
    