def cipher(text, shift):
    result=""

    for letter in text:
        if letter.isupper()==True: # liczby wielkie
            if (ord(letter) + shift)>90:
                x = ((ord(letter)) + shift) - 90
                x=64+x
                result+=chr(x)

            elif (ord(letter)+shift)<65:
                x = ((ord(letter)) + shift) - 65
                x=91-abs(x)
                result+=chr(x)
                
        elif letter==" ":
            result+=" "
            
            else:
                result+=(chr(ord(letter) + shift))

        else: # liczby małe
            if (ord(letter) + shift)>122:
                x = ((ord(letter)) + shift) - 122
                x=96+x
                result+=chr(x)
                
        elif letter==" ":
            result+=" "
            
            elif (ord(letter)+shift)<97:
                x = ((ord(letter)) + shift) - 97
                x=123-abs(x)
                result+=chr(x)

            else:
                result+=(chr(ord(letter) + shift))
    return result

def decipher(text, shift):
    result=""

    for letter in text:
        if letter.isupper()==True: # liczby wielkie
            if (ord(letter) - shift)>90:
                x = ((ord(letter)) - shift) - 90
                x=64+x
                result+=chr(x)

            elif (ord(letter) - shift)<65:
                x = ((ord(letter)) - shift) - 65
                x=91-abs(x)
                result+=chr(x)

            else:
                result+=(chr(ord(letter) - shift))

        else: # liczby małe
            if (ord(letter) - shift)>122:
                x = ((ord(letter)) - shift) - 122
                x=96+x
                result+=chr(x)

            elif (ord(letter) - shift)<97:
                x = ((ord(letter)) - shift) - 97
                x=123-abs(x)
                result+=chr(x)

            else:
                result+=(chr(ord(letter) - shift))
    return result
