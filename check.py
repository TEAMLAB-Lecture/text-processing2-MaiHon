strings = [""]#, "     ", ".....", "__EXAMPLE_NAME__", "alreadyCarmel", "_____"]

for s in strings:
    print(s)

    replaced = s.split("_")
    
    if len(replaced) == 0: 
        print("")
    elif len(replaced) == 1:
        print(replaced[0])
    else:
        replaced = ' '.join(' '.join(replaced).split())
        replaced = replaced.split()
        if len(replaced) >= 1:
            replaced[0] = replaced[0].lower()
            replaced[1:] = [string.capitalize() for string in replaced[1:]]
            print(''.join(replaced))
    print()
    
    # extracted = replaced.split()
    # print(extracted)