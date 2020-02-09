from datetime import date
class Employee:
                
        def __init__(self, name, age, salary, employment_year):
                self.name = name
                self.age = age
                self.salary = salary
                self.employment_year = employment_year
                
               
                
        def get_data(self):
                return 'Name: '+self.name+', Age:'+str(self.age)+', Salary: '+str(self.salary)+', Working Years: '+str(self.get_working_years())
                
        def get_working_years(self):
                start_year=self.employment_year
                p=(date.today().year - start_year)
                return(p)
                
                       
                        
                 
       
           

class Manager(Employee):
               
        def __init__(self, name, age, salary, employment_year,  tbonus_percentage):
                
                super().__init__(name, age, salary, employment_year)
                self.bonus_percentage = tbonus_percentage
                
        

        def get_data(self):
               
                bonus=self.bonus_percentage
                init_salay=self.salary
                s=bonus*init_salay
                start_year=self.employment_year
                p=(date.today().year - start_year)
                return "Name: "+self.name+", Age:"+str(self.age)+", Salary: "+str(self.salary)+", Working Years: "+str(self.get_working_years())+", Bonus: " +str(self.get_bonus)
                      
                
       
     
                 


        def get_bonus(self):
              
                bonus=self.bonus_percentage
                init_salay=self.salary
                s=bonus*init_salay   
                return s
                
                        
            
                
def main():
        Employee1=[]
        Manager1=[]
        
       
       
       
        options=["Show Employees","Show Managers","Add An Employee","Add A Manager", "Exit"]
        for n,m in enumerate(options,1):
                print(n,".",m)
        
        
                
        option_num=0
        while  option_num!=5:
                option_num=int(input("What would you like to do?"))
                
                if option_num == 1:
                        for v in Employee1:
                                print (v)
                                
                       
                       

                elif option_num == 2:
                        for u in Manager1:
                                print (u)
                        

                                

                elif option_num == 3:
                        a=input("Name:")
                        b=int(input("Age:"))
                        c=float(input("Salary:"))
                        d=int(input("Employement year:"))
                        Employee1.append(a)
                        Employee1.append(b)
                        Employee1.append(c)
                        Employee1.append(d)
                       
                        
                        E=Employee(a,b,c,d)
                        print("Employee added succesfully")
                                
                                

                elif option_num == 4:
                        
                        a=input("Name:")
                        b=int(input("Age:"))
                        c=float(input("Salary:"))
                        d=int(input("Employement year:"))
                        e=float(input("bonus_percentage:"))
                        Manager1.append(a)
                        Manager1.append(b)
                        Manager1.append(c)
                        Manager1.append(d)
                        Manager1.append(e)
                        
                        M=Manager(a,b,c,d,e)
                        
                        print("Manager added succesfully")
                                

              

if __name__ == '__main__':
	main()
