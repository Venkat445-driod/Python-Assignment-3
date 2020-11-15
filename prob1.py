x='The quick Brown Fox'
y=list(x.upper())
z=list(x.lower())
x=list(x)
#to find uppercase letters
count=0
for i in range(len(x)):
    j=i
    if(x[i]==y[j] and x[i]!=" "):
        count=count+1
print("no. of upper case characters:",count) 

#to find lowercase letters
count=0
for i in range(len(x)):
    k=i
    if(x[i]==z[k] and x[i]!=" "):
        count=count+1
print("no. of lower case characters:",count)