import sys
from stats import num_of_words
from stats import num_of_each
from stats import expanded_dict





def get_book_contents(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)




def main():
    
    
    text = get_book_contents(sys.argv[1])
    num_words = num_of_words(text)
    chars_dict = num_of_each(text)
    #print(num_words)
    #print(chars_dict)
    flattened_dict = expanded_dict(chars_dict)
    #print(flattened_dict)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {sys.argv[1]}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
   
    for dict in flattened_dict:
        #print(dict)
        #print(dict['char'])
        #print(dict['nums'])
        charaters = dict['char']
        numbers = dict['nums']
        final_dict = f"{charaters}: {numbers}"
        print(final_dict)

    
    
    #print(get_book_contents('books/frankenstein.txt'))
    #print(num_of_words(get_book_contents('books/frankenstein.txt')))
    #print(num_of_each(get_book_contents('books/frankenstein.txt')))
    #print(expanded_dict(num_of_each(get_book_contents('books/frankenstein.txt'))))
    
    

main()
