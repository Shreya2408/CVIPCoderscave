import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.punctuation
    s4 = string.digits
    
print("------------Password Generator-------------")
pas = int(input("Enter the length of the password : "))

s = []      
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)  #used to shuffle the list elements

print("Your Password is : ", "".join(s[0:pas]))  # join is used to join the elements removing the quotes

