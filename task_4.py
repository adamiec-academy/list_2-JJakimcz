def multiplication_table(x1, x2, y1, y2):
    max_spaces = len(str(x2*y2))+1
    i=y1

    print(" " * (max_spaces+1) +"|",end="")

    for y in range(y1, y2 + 1):
        print(f"{y : {max_spaces}}",end="")
    
    print("")
    print("-" * ((max_spaces * abs(y2-y1)) + max_spaces+abs(y2-y1))   ,end="")

    for x in range( x1, (x2-2) + x1):
 
        print("")
        print(f"{x : {max_spaces}}" + " " + "|" + "",end="" )

        for y in range(y1, y2 + 1):

            print(f"{x * y : {max_spaces}}",end="")
