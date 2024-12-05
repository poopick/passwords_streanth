import re
import math

# Step 1: Password strength checker
def check_password_strength(password):
    #password = str(password)
    # Analyze total_chars, diversity of characters, and patterns
    # Return a strength score
    total_chars = len(password)
    
    char_types = []
    char_types.append (len(re.findall(r'[a-z]',password))) # lowecase
    char_types.append ( len(re.findall(r'[A-Z]',password))) # upercase
    char_types.append ( len(re.findall(r'[0-9]',password))) # numbers 
    char_types.append (total_chars - (char_types[0] + char_types[1] + char_types[2])) # spetial chars
    for i in range(len(char_types)):
        char_types[i] = char_types[i] / total_chars
    

    total_sequential_chars = 0
    
    for i in range(total_chars):
        if i == 0:
            continue
        if ord(password[i]) - 1 == ord(password[i -1]) or ord(password[i]) + 1 == ord(password[i -1]):
            total_sequential_chars += 1
    
    
    total_repeting_chars = 0
    for i in range(total_chars):
        
        if password.find(password[i], i + 1) != -1 :
            total_repeting_chars += 1
    

    score = 100

    # score reduction based on length
    if   8 < total_chars < 12 :
        score -= 5 * (12 - total_chars )   #  penalty for total_charss 8-11
    if 5 < total_chars <= 8:
        score -= 15 * ( 8 - total_chars ) #  penalty for total_charss 5-8
    if 0 < total_chars <= 5 :
        score -= 35 * (5 -total_chars)    #  penalty for total_charss 0-5

    # score reduction based on char compasition
    binay_compas = math.ceil(char_types[0]) + math.ceil(char_types[1]) + math.ceil(char_types[2]) + math.ceil(char_types[3]) # a if a char type exist [lowercase,upercase,number,other]
    if binay_compas == 3 :
        score -= 5
    elif binay_compas == 2 :
        score -= 15
    elif binay_compas == 1 :
        score -= 25

    binay_compas = 0 # used here to find how many low compasiton char types 0-4
    for i in range(4):
        if char_types[i] < 0.1 :
            binay_compas += 1

    score -= binay_compas * 5

    # score reduction based on sequential chars
    score -= (total_sequential_chars * 10) / (total_chars) # penalty shall be reduced for longer passwords

    # score reduction based on repeting chars
    score -= (total_repeting_chars * 10) / (total_chars) # penalty shall be reduced for longer passwords

    
    print("password length : ", total_chars)
    print("\n\n")

    print("compasition of chars :")
    print(char_types,"\n\n")

    print("total sequential chars: ",total_sequential_chars)
    print("\n\n")

    print("total repeting chars: ",total_repeting_chars)
    print("\n\n")

    print("your score is : ",score)
    
    return score
    




# Step 2: Brute force time estimation
def brute_force_estimation(password):
    # Calculate the time to brute force based on character space and total_chars
    # Simulate cracking speed (1k, 10k, 1M attempts/sec)
    pass
# Step 3: Dictionary attack
def dictionary_attack(password, dictionary_file="common_passwords.txt"):
    # Check if the password exists in the dictionary
    # Return result
    pass

# Step 4: Hashing demonstration
def hash_password(password, algorithm='sha256'):
    # Hash the password with the chosen algorithm
    # Return the hash
    pass

# Main function to tie everything together
def main():
    # Get user input
    # Call the functions above and display results
    password = input("enter a password for me to judge\n" )
    check_password_strength(password)

if __name__ == "__main__":
    main()
