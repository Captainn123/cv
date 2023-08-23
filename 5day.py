# student_heights=int("Enter the heights of students").split()
# for i in range(0, len(student_heights)):
#     student_heights[i]=int(student_heights[i])
# print(student_heights)
# sum_student_heights=0
# for height in student_heights:
#     sum_student_heights=sum_student_heights+height
# student_number=0
# for number in student_heights:
#     student_number=student_number+1
# average_height=float(sum_student_heights/student_number)
# print(average_height)

# student_score=input("Enter the score of students").split()
# for i in range(0, len(student_score)):
#     student_score[i]=int(student_score[i])
# print(student_score)
# highets_score=0
# for score in student_score:
#     if score>highets_score:
#         highets_score=score
# print(highets_score)

# total=0
# for num in range(0,101):
#     if num%2==0:
#         total=total+num
#     else:
#         continue
# print(total)

# total=0
# for num in range(0,101):
#     if num%3==0 and num%5==0:
#         print("FizzBuzz")
#     elif num%3==0:
#         print("Fizz")
        
#     elif num%5==0:
#         print("Buzz")
#     else:
#         print(num)
import random
letters=("a", "b", "c")
numbers=("1", "2", "3")
symbols=("#", "$", "%")
letters_num=int(input("Enter how many letters you want"))
symbols_num=int(input("Enter how many symbol you want"))
numbers_num=int(input("Enter how many numbers you want"))
password_list= []
for i in range(1,letters_num+1):
    password_list.append(random.choice(letters))

for i in range(1,symbols_num+1):
    password_list.append(random.choice(symbols))

for i in range(1,numbers_num+1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)

password=""
for i in password_list:
    password=password+i
print(password)
