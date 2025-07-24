def num_of_words(text):
    words = text.split()
    len_words = len(words)
    return len_words

def num_of_each(text):
   letter_count = {} 
   lowered = text.lower()
   for char in lowered:
     if char in letter_count:
        letter_count[char] += 1
     else:
        letter_count[char] = 1    
    
   return letter_count

def sort_on(item):
    return item['nums']


def expanded_dict(old_dict):
    new_list = []
    for item in old_dict:
        if item.isalpha() == True:
            new_list.append({'char': item, 'nums': old_dict[item]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list


    