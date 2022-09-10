"""
Usually when you buy something, 
you're asked whether your credit card number,
phone number or answer to your most secret 
question is still correct. However, 
since someone could look over your shoulder, 
you don't want that shown on your screen. Instead, we mask it.
"""
import re
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
def maskify(cc):
    # confirm that the entry is more than four characters
    # if more than four rall all first indexes after -4 with #
    # Slice the string entry into a new string without the last four charcaters
    print(cc)
    x = cc[:-4]
    print(x)
    # y = response = re.sub(r"([[a-zA-Z0-9.!#$%&\"`*+/\\=?;:^_{|}~-])+|\s+[+]]","#",x)
    y = response = re.sub(r"[\d\D\w\W]","#",x)
    print(y)
    z =cc[-4:] 
    print(z)
    return(y+z)

#  input your card number / phone number / secret to phone
credential = input("Input either your card number/ phone number/ most secret :  ")
print(maskify(credential))

