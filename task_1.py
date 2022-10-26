def remove_parentheses(text):

    x=False
    chuj=False
    text2=""

    for i in range(len(text)):

        if chuj==True and text[i]==" ":
            continue

        if text[i] == "(" :
            x = True

        if x==False:
            text2+=text[i]
        
        if (x==True) and (text[i] == ")"):
            chuj=True

        if text[i] == ")" :
            x = False

remove_parentheses(text)
