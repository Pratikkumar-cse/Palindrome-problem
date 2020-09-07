# cook your dish here
st=str(input())
inputstr=[]
for i in range(len(st)):
    inputstr.append(st[i])
def isPalindrome(s): 
    return s == s[::-1]
i=0
j=i+1
c=0
while i<len(inputstr)-2:
    x=[]
    y=[]
    z=[]
    for k in range(j+1,len(inputstr)):
        x.append(inputstr[k])
    if isPalindrome(x):
        y=inputstr[i+1:j+1]
        if isPalindrome(y):
            z=inputstr[0:i+1]
            if isPalindrome(z):
                c=1
                break
            else:
                i+=1
                j=i+1
        else:
            j+=1
    else:
        j+=1
    if j>len(inputstr)-1:
        i+=1
        j=i+1
if c==0:
    print("Impossible")
else:
    str1=''
    print(str1.join(z))
    str1=''
    print(str1.join(y))
    str1=''
    print(str1.join(x))
