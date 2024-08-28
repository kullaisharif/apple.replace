str1="apples"
str2=""
for i in str1:
    if i=="a":
       str2+="p"
    elif i=="p":
        str2+="a"
    else:
        str2+=i
print(str2)
