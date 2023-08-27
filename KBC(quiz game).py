print("-----------WELCOME TO KBC(Kaun Banega Crorepati)----------")
name=(input("Please Enter your name: "))
print("Welcome" ,name)
print()
a=(input("Do you want to play this game? ")).lower()
if(a=="yes" or a=="s"):
    x=(input("Type Yes,if you want to read the instructions :"))
    if(x=="yes" or x=="s"):
        print("Here are the instructions")
        print("It consists of total 15 questions")
        print("For each correct answer,you will get some money")
        print("If you answer correctly for 5 questions you will get Rs.10000")
        print("For 10 correct answers you will get Rs.32000")
        print("For total 15 correct answers,you will get 1 crore rupees")
        print("BEST OF LUCK\n")
        print("------Lets Start------\n")
        print()
    else:
        print("------Lets Start------\n")
    questions=[
      [
        "which language is used to create fb?","python","french","javascript","php","none",4
     ],
      [
        "what is the maximum length of a python identifier?",32,16,128,"No fixed length is specified","none",4
     ],
      [
        "How is a code block indicated in python?","brackets","key","paranthesis","indentation","none",4
     ],
      [
        "which of the following concept is not a part of python?","loops","dynamic typing","functions","pointers","none",4
     ],
      [
        "which of the following statements are used in exception handling in python?","try","except","finally","all of these","none",4
     ],
      [
        "which of the following types of loops are not supported in python?","for","if-else","while","do-while","none",4
     ],
      [
        "which of the following function converts date to corresponding time in python?","strftime","time.strftime","both a and b","strptime","none",4
     ],
      [
        "As what datatype are the *args stored,when passed into a function?","list","string","dictionary","tuple","none",4
     ],
      [
        "As what datatype are the *kwargs stored,when passed into a function?","string","tuple","list","dictionary","none",4
     ],
      [
        "which of the following blocks will always be executed whether an exception is encountered or not in a program?","try","except","both a and b","finally","none",4
     ],
      [
        "which keyword is used in python to raise exceptions?","try","goto","except","raise","none",4
     ],
      [
        "which of the following is not a valid set operation in python?","union","intersection","difference","sum","none",4
     ],
      [
        "which of the following modules need to be imported to handle date and time computations in python?","date","time","timedate","datetime","none",4
     ],
      [
        "which of the following are valid string manipulation functions in python?","count()","upper()","strip()","all","none",4
     ],
      [
        "In which language is written?","python","french","javascript","c","none",4
     ],
    ]
    levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000,2560000,6020000,10000000]
    money=0
    for i in range(0,len(questions)):
        question=questions[i]
        print(f"Question for Rs.{levels[i]}")
        print(questions[i][0])
        print(f"a.{question[1]}         b.{question[2]}")
        print(f"c.{question[3]}         d.{question[4]}")
        reply=int(input("Enter your answer(1-4):\n"))
        if (reply==question[-1]):
            print(f"correct answer,you have won Rs.{levels[i]}\n\n")
            if(i==4):
                money=10000
            elif(i==9):
                money=320000
            elif(i==14):
                money=10000000
        else:
            print("wrong answer!")
            break
    print(f"your take home money is {money}\n")
else:
    print("See you next time,Thankyou\n")
print("-----Thank you for Playing-----")
