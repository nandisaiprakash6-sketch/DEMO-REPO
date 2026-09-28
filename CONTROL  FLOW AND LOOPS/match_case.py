# What is Match-Case?
# Match-case is a new feature introduced in Python 3.10 for pattern matching.
# It simplifies complex conditional logic.

a = int(input("enter your luck number  "))

match a :
    
    case 20:
        print(" you fuckker")

    case 40:
        print( " good boy")
    case 10:
        print("nothing to say about you")

    case _:
        print(" this is default when the value is not matched")            
    

