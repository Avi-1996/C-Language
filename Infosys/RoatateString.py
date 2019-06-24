'''
given a string in comma seperated values with some number 
do the following things 
1 - find the sum of square of all digit in a number
2 - if the sum is odd the rotate left the string two time
3 - if not the roate right the string one time

for example input will contain like

avi:22,path:41


Explanation -:
sume of sqaure of digit 22 is 8 which is even so we left rotate avi by one character

sume of sqaure of digit 41 is 17 which is odd so we Right rotate path by one character two times

OUTPUT
iavo,thpa
'''
def SumOfSquare(number):
    return sum( [int(x) * int(x) for x in number ] ) 
def RRotate(string):
    return (string[-1] + string[:len(string) - 1])
def LRotate(string):
    return (string[1::] + string[0])
ans = []
s =list(input().split(','))
for i in s:
    string,number = i.split(':')
    if SumOfSquare(number) % 2 == 0:
        string = RRotate(string)
    else: 
        string = LRotate(string)
        string = LRotate(string)
    ans.append(string)
print(','.join(ans))
