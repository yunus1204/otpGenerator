# sum to generate otp on given input ,taken odd places from input and square it up and the ans we get on squaring those number is taken and return first 4 digit
x=input()
j=0
st1=''
for i in x:
    if j%2!=0:
        p=int(i)
        st1+=str(p*p)   
    j=j+1    
print(st1[:4])        
