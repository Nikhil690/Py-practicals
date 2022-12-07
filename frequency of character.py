r = True
while r == True: 
    userInput = str(input("Enter a string: "))
  
    freq = {}
  
    for i in userInput:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
  
    print ("Count of all characters in", userInput, "is :","\n " +  str(freq))
    r = input("To run the code again just type yes: ")
    if r == "yes":
        r = bool(True)
    else:
        r = bool(False)
