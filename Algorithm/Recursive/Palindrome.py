'''

Palindrome : 앞에서 읽든 뒤에서 읽든 동일한 단어 또는 문장

1. 첫 글자와 마지막 글자를 비교  
2. 대소문자 구분 x
3. 비교하지 않은 글자가 한 글자 이하 -> 회문
4. 첫 글자는 다음 글자로 , 마지막 글자는 그 전 글자로 이동해가며 비교 

'''

# example : k a y a k  -> 2번 이동하면 끝 
# Example : borrow -> 3번 이동하면 끝 

def palindrome(str, start, end): # Arr 문자 n 번째 

    if start <= len(str)//2:
        if str[start] == str[end]:
            palindrome(str,start+1,end-1)
            return print("Palindrome Inner")
        else:            
            return print("Not Palindrome")
    else:        
        return print("Palindrome Outer")

str = "borrob"
start, end = 0, len(str)-1

palindrome(str,start,end)




