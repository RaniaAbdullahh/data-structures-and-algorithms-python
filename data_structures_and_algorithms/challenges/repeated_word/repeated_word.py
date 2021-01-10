import re
def repeated_word(string):
   
    string = re.sub(r'[^\w\s]', '', string)
    all_the_words = {}
    rep_word = ''

    
    for word in string.split():
        
        try:
            all_the_words[word] += 1
            rep_word = rep_word or word
        except:
            all_the_words[word] = 1

    if rep_word:
        return f'"{rep_word}"'
    else:
        return "No repeating words found"



if __name__ == "__main__":
    print(repeated_word('Once upon a time, there was a brave princess who')) 
 
 