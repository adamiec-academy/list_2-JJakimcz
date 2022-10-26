def remove_parentheses(text):

    x=False
    text2=""

    for i in range(len(text)):

        if text[i] == "(" :
            x = True

        if x==False:
            text2+=text[i]
            
        if text[i] == ")" :
            x = False

remove_parentheses(text)
