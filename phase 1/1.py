def count_words(sentence):
    
    if not sentence.strip():  
        return 0
    words = sentence.split()  
    return len(words)

if __name__ == "__main__":
    print("Word Counting in a sentence")
    user_input = input("Type a sentence: ")
    word_count = count_words(user_input)
    print(f"\n Number of words: {word_count}")                                        