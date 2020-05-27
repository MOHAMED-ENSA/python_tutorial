#print("this file contain informations about ex handling in python")
#print ("part1")
#a = -5
#if a < 0 : 
 #   raise Exception("this number is less than 0!")

#print("every things i good!")a 
#print("part2")
#try : 
#    a = int(input("enter an integer : "))
#except : 
#    print("the input is not an integer")
#else : 
#    print("good!")
#finally : 
#    print("thank you !")
# we can use multiple except in one try 
#a = 0
#try : 
 #   print(4/a) 
#except ZeroDivisionError : 
 #   print("you can't devide by zero!")
#except TypeError : 
  #  print(f"{a} is not an integer! ")
print("part3")
# ask the user to give the path of a file for open it : 
a = 5 
my_file = None 
while a > 0:
    try : 
        file_path = input("pleas give the absolute path for the file : ").strip()
        my_file = open(file_path,"r") 
        print(my_file.read())
        break
    except : 
        print("please enter a correct path !")
        a -= 1 
    finally :
        if my_file is not None : 
            my_file.close()













