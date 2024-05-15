def filter_messages(messages):
    filtered_messages = []
    count_of_words = []
    filtered_word = "dang"
    for i in range(0,len(messages)):
        count = 0
        not_bad_words = []
        message_split = messages[i].split()

        for word in message_split:
            if word == filtered_word:
                count += 1
            else:
                not_bad_words.append(word)
        
        filtered_messages.append(" ".join(not_bad_words))
        count_of_words.append(count)
    return filtered_messages,count_of_words