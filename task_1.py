def remove_parentheses(text):

    x=False
    chuj=False
    text2=""

    for i in range(len(text)):

        if chuj==True:
            chuj=False
            continue

        if text[i] == "(" :
            x = True

        if x==False:
            text2+=text[i]
        
        if text[i] == ")" :
            x = False
            chuj = True
            
    return text2:
