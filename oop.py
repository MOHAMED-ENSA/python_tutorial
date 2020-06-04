# class/object : 
class students : 
    id = 0 
    def __init__(self ,name,CNE,Class) : 
        self.name = name 
        self.CNE = CNE 
        self.Class = Class
        
        #students.id +=1
    def disp(self) : 
        print(self.name , self.CNE , self.Class ,self.id)

# student1 = students("Mohamed",1314166688,"GTR4")
# student1.disp()
# student2 = students("ali",1314555311,"GTR5") 
# student2.disp()
# student3 = students("Mohamed",1458866688,"GC4") 
# student3.disp()
# student4 = students("Mohamed",1314134688,"GE4") 
# student4.disp()
# how to now the class of any object 
#print(student1.__class__)

# encapsulation : 
# totalement comme celui de java  
# acces modifiers : public /  protected / private 

class humain : 
    def __init__ (self, name = "no name",age = 0 ,sex = "male" ) : # pour pouvoir utiliser le constructeur sans arg il faut avoir une val par defaut pour chaque argument
        self.name = name # public 
        self._age = age  # protected
        self.__sex = sex  # private 
    def getName(self) : 
        return self.name 
    def getAge(self) : 
        return self._age 
    def getSex(self) : 
       return self.__sex 
    def setName(self, name) : 
        self.name  = name 
    def setAge(self, age) : 
        self._age  = age 
    def setSex(self, sex) : 
        self.__sex  = sex
    def disp () : 
        print("name : {getName()} \n age : {getAge} \n sex : {getSex}") 

humain1 = humain(name = 'ahmed')    # we can use dictionary for changing the default value
#print(humain1.name)
#humain1.setAge(22) 
#humain1.setName('Allal')
#print(humain1.getSex())
#print(f" this all info about humain1 : \n name :  {humain1.getName()} \n sex :  {humain1.getSex()} \n age :  {humain1.getAge()}")
#print(humain1._age)
#print(humain1.__sex) # not gonna work because it's private
#print(humain1._humain__sex) # this gonna work 

# inheritence : 

# class teacher(humain) : # c'est pas obligatoire de cree init constractor pour la class fille 
#     def __init__ (self,etab = "S",school = "UMP" ) : 
#          self.etab = etab  
#         self.school = school 

# teacher1 = teacher( name  = "D.Meharraf" , age = 40 , sex = "male" )
# #print(dir(teacher1))

# print(teacher1.getName(),teacher1.getAge(),teacher1.getSex(),teacher1.etab,teacher1.school)
# the keyword super 
# class employee (humain): 
#     def __init__ (self , name = "no name",age = 0 ,sex = "male",salary = 0,city = "") : 
#         super().__init__(name,age,sex) 
#         self.city = city 
#         self.salary = salary
#     def disp(self) : 
#         print(self.disp() , self.city , self.salary)

# em1 = employee(salary = 3500 , city = "oujda" ,name ="Soufian " , sex = "male" , age = 35)
# em1.disp()

# polymorphisme 

# pass an object in parametre : a : className





