import random

poem_txt = "./poetry slam/poem.txt"
#Citation: Chanie Gorkin

#Recieves txt file, opens, returns readlines() of txt, then closes
def get_file_lines(filename):
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close() 
    return lines

#Prints txt file's lines backwards along with original line numbers
def lines_printed_backwards(lines_list):
    lines_len = len(lines_list) - 1
    print("\nPoem in reverse:\n----------------")
    for line_num in range(lines_len, 0, -1):
        if line_num >= lines_len:
            print(f"{line_num} {lines_list[line_num]}")
        else:
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

def lines_printed_custom(lines_list):
    global user_word
    print("\nYou've chosen to print the poem using the custom function!\n")
    print("Input a word and only lines containing that word will be printed")
    user_word = input("Input a word of your choice:\n")

    #prints out error message if input contains a number
    while any(char.isdigit() for char in user_word):
        print("------------------------------")
        print("ERROR: input contains a number")
        user_word = input("\nInput a word of your choice:\n")



# lines_printed_backwards(get_file_lines(poem_file))
# lines_printed_random(get_file_lines(poem_txt))
lines_printed_custom(get_file_lines(poem_txt))