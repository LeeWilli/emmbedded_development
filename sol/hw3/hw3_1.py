prompt_text = "Enter a number: "

try:
    user_in = input(prompt_text)
    user_num = int(user_in)
except NameError:
    print("please input a number!")

for i in range(1,10):
    print(i, " times ", user_num, " is ", i*user_num)
    even = (user_num % 2) == 0
    if even:
        print(user_num, " is even")
    else:
        print(user_num, " is odd")
