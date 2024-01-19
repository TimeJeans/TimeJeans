import random

upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H,', 'I', 'J', 'K,', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specialCharacters = ['!', '?', '#', ',', '.', '$', '%', '£']

def passwordGenerator():

    Password = (random.choice(upperCase) + random.choice(lowerCase) + random.choice(numbers)
                + random.choice(specialCharacters) + random.choice(lowerCase)
                + random.choice(upperCase) + random.choice(numbers)
                + random.choice(specialCharacters) + random.choice(upperCase)
                + random.choice(lowerCase) + random.choice(numbers)
                + random.choice(specialCharacters) + random.choice(lowerCase)
                + random.choice(upperCase) + random.choice(numbers)
                + random.choice(specialCharacters))


    return Password

#print(passwordGenerator())