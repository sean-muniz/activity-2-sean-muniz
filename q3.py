def wordCount(t):
    try: 
        with open(t, 'r') as file:
            names = file.readlines() 
            for i in range(0, len(names)): 
                names[i] = names[i].strip()
            name_dictionary = {key: 0 for key in names} 
            for key in name_dictionary: 
                for name in names: 
                    if key == name:
                        name_dictionary[key] += 1
        return name_dictionary
    except FileNotFoundError: 
        print("cannot find file")

print(wordCount('dictionary.txt')); 

