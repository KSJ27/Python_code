# name = "강석준"
# number = "000327-3000000"
# gender = ""
# if gender.index(7) == "3":
#     gender = "남자"
# else: 
#     gender = "여자"
# month = number[2:4]
# date = number[4:6]
# print("{0}님은 {1}이며, 생일은 {2}월 {3}일입니다.".format(name,gender,month,date))




# slist = [1,'a',2,3,'b',['apple','banana','peach']]
# print(slist)
# print(slist[3])
# print(slist[4])
# slist[4] = "Hello Python"
# print(slist[4])
# print(slist)
# print(slist[2:5])
# print(slist[5][1])

# evennumber = [2,4,6,8,10]
# oddnumber =  [1,3,5,7,9]
# number = evennumber + oddnumber
# print(number)
# number[4:5] = [99]
# print(number)
# number[2:6] = 'hello'
# print(number)
# number[8] = ['a','b','c']
# print(number)
# number[:] = [1]
# print(number)


# 리스트 함수
# x = 인자
# append(x) 리스트 맨 마지막에 x 인자 추가
# remove(x) 리스트에서 가장 처음 나오는 x 삭제, 만약 x가 없으면 오류 발생
# insert(y,x) y위치에 x 값을 추가
# pop()
# extend(x)
# sort()오름차순 정렬
# reverse()내림차순 정렬

# a = [1, 9, 3, 2, 6, 4, 5]
# a.sort()
# print(a)
# a.pop(6)
# print(a)
# a.append(9)
# print(a)
# a.insert(6,7)
# print(a)
# a.append(10)
# print(a)
# a.reverse()
# print(a)
# a.insert(2,8)
# print(a)


# 딕셔너리
# 딕셔너리이름 = {key1:value1, key2:value2}
# 딕셔너리이름 = dict1(key1:value1)


# nation = {"Kor":"한국", "Jap":"일본", "USA":"미국"}
# print(nation)
# nation["Ger"]="독일"
# print(nation)
# nation["SA"] ="아르헨티나,브라질"
# print(nation)
# print(nation["USA"])

# print(nation.keys())
# print(nation.items())
# print(nation.clear())
# nation = {"Kor":"한국", "Jap":"일본"}
# print(nation)
# print(nation.get("USA"))



# str, list, dict, tuple, set
# str1 = "Hello"
# print(str1)
# list1 = [1,2,3,'a','b','c']
# print(list1)
# dict1 = {"apple" : "사과", "banana" : "바나나", "grape" : "포도", "key1" : "value1" }
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# 리스트(변환 가능) []
# 튜플(immutable)  ()
# 딕셔너리(대응, 변환 가능) {}
# 세트(집합-중복 제거,묶음)

# tuple1 = ("Hello")
# tuple2 = ('a','b',1,2,3)
# tuple3 = 'c,', 'd', 4, 5, 6
# print(tuple3)
# print(tuple2, tuple3[2])

# t1 = (1,2,3,4,5)
# t2 = (2,4,6,8,10)
# t3 = 11, 13, 17, 19, 23

# print(t1[2], t2[1])
# print(t3[:])
# print(t3[0:5])
# print(t1 + (6,))
# print(t1*2)
# print(t1)

# print(id(t1))
# t1 = t1 + (6,)
# print(t1)
# print(id(t1))

# list1 = ['a', 'c', 'd', 'b', 'e']


# list2 = ['This', 'is', 'a', 'book']
# print(" ".join(list2))

# dic1 = {'a':90, 'b':80, 'c':70, 'd':60, 'e':50}
# dic2 = {}
# dic2 = dic1.pop('d')
# print(dic2)

# x = 'world Hello'

# count = 0
# while count != 10:
#     print("count: ", count)
#     count += 1

# while 구구단
# num = 1
# dan = int(input("1부터 9까지 정수를 입력하시오: "))
# while num <= 9:
#     print(dan * num)
#     num += 1

# for 구구단 
# for i in range(1,10):
#     for j in range(1,10):
#         print(i, "*", j, "=", i*j)

# evenlist = [2,4,6,8,10]
#리스트의 크기를 알려주는 함수 len, count
# print(len(evenlist))
# for i in range(len(evenlist)):
#     print(evenlist[i])

# dic1 = {
#     "cat" : "고양이",
#     "dog" : "개", "human" : "사람"}
# evennumber = [2,4,6,8,10]
# oddnumber = [1,3,5,7,9]
# str1 = "Hello Python!"

# for i in str1:
#     print(i, end = ' ')

# i = 1
# for i in range(1,100,2):
#     print(i)

# scorelist = [70,60,88,75,89,90,68,72,85,82]
# print(len(scorelist))
# total = 0
# for score in range(len(scorelist)):
#     print(scorelist[score])
#     total += scorelist[score]
#     print(total)
# aver = total / len(scorelist)
# print(aver)

# year = 0
# money = 1000
# while money<2000:
#     #money += money *0.07
#     money *= 1.03
#     year += 1
# print(year)


# scorelist = [70,60,55,75,95,80,82,79,68,73]

# for score in range(len(scorelist)):
#     if scorelist[score]<60 :
#         print("F")
#     elif scorelist[score]<70 :
#         print("D")
#     elif scorelist[score] <80 :
#         print("C")
#     elif scorelist[score] <90 :
#         print("B")
#     else: print("A")
#     score += 1

# list1 = ['a', 'b', 'c']
# for index in list1:
#     print(index)
# num1 = 5
# for n in range(num1):
#     print(n,'번째 숫자입니다')

# num1 = int(input("정수를 입력하세요: "))
# result = 1
# for k in range(1, num1 + 1):
#     result *= k 
# print(k, '!','=', result)

# for k in range(1,10):
#     print(3, '*', k, '=',3*k)

# x = int(input("첫번째 숫자 입력:"))
# y = int(input("두번째 숫자 입력:"))

# if x<y:
#     print(x,'가',y,'보다 작습니다')
# elif x==y:
#     print(x,'와',y,'는 같습니다')
# else:
#     print(x,'가',y,'보다 큽니다')


# A = [1,2,3,4,5,6,73,8,10,54]

# odd = 0
# even = 0

# #홀수와 짝수의 개수 세기

# for k in A:
#     if k%2 ==0:
#         even += 1
#     else:
#         odd += 1
# print(even, odd)

# for number1 in range(1,10):
#     if number1%3 == 0:
#         print('짝')
#     else:
#         print(number1)
# for number2 in range(10,100):
#     strnum = str(number2)
#     x = int(strnum[0])
#     y = int(strnum[1])
#     if x%3 ==0 and y%3 ==0:
#         print('짝짝')
#     elif x%3 !=0 and y%3 ==0:
#         print('짝')
#     elif x%3 ==0 and y%3 !=0:
#         print('짝')
#     else:
#         print(number2)
# # y = 0 일때도 y % 3 = 0

# for i in range(1,1000):
#     str1 = str(i)
#     list1 = list(str1)
#     print(list1)
#     for j in str1:
#         if (j == '3' or j == '6' or j =='9'):
#              print('clap')

# for i in range(1,100):
#     str1 = str(i)
#     list1 = list(str1)
#     print(list1)
#     for j in str1:
#         if (j == '3' or j == '6' or j == '9'):
#             print('짝!')

# 함수 def = define  definition
# 매개변수 -> 기능 -> 결과, 반환값
"""매개변수는 함수에 입력으로 전달된 값을 받는 변수를 의미하고 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
def add(a, b):  # a, b는 매개변수
    return a+b
 print(add(3, 4))  # 3, 4는 인수"""
# return c 는 replace 값을 반환함

# def myfunction(a,b): #인자
#     c = a*b          #기능      #반환
#     return c
# print(myfunction(3,6))

#생년원일 입력시 띠를 출력하는 프로그램 만들기

# def birth_func(year):
#     year = input('생년:')
#     index = year % 12
#     print('띠')
# birth = int(input("생년:"))
# birthlist = ['원숭이','닭','쥐','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
# index = birth % 12
# print(birthlist[index])

# 매개변수 o 반환값 o
# 매개변수 o 반환값 x
# 매개변수 x 반환값 o 
# 매개변수 x 반환값 x

#아이디넘버, 나이, 띠, 남자 여자

# id_number = str(input("주민등록번호를 입력해주세요:"))
# nn = int(id_number[7])
# yr1 = int(id_number[0])
# yr2 = int(id_number[1])
# year = 0
# if nn == 1 or nn== 2:
#     year = 10*yr1 + yr2 +1900
# else:
#     year = 10*yr1 + yr2 +2000
# this_year = 2019
# age = this_year - year + 1
# print("나이는",age)
# def DDi_func(y):
#     index = y % 12
#     birthlist = ['원숭이','닭','쥐','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']  
#     return(print("띠는",birthlist[index]),"띠")    
# DDi_func(year)
# if nn == 1 or nn == 3:
#     print("성별은 남자")
# elif nn == 2 or nn == 4:
#     print("성별은 여자")

# 반복문, 조건문, 함수를 활용하여 주어진 정수 리스트의 최댓값을 출력하는 함수
# 주어진 함수는 리스트 A의 입력값 
# if문의 조건이 최댓값을 비교하는 조건
# 리스트의 값이 max 보다 클 때 max를 그 리스트의 max로 바꿈

# numList = [1,3,5,6,73,8,10,54,68]
# maxNumber = 0
# def maxFunc():
#     for value in numList:
#         if value >= maxNumber :
#             maxNumber = value
#     print((maxNumber,value))
#     return(maxNumber)
# a = 6
# def plust(a):
#     a += 3
#     return a
# print(plust(a))
# print(a)
# a = 8
# print(plust(a))
# print(a)


number = 7
def mulNum(a) : 
    a *= number 
    return a

def subNum(a) :
    a -= number
    return a

res = mulNum(4)
print(res)