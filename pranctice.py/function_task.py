def calculate_gross_salary(basic_salary,benefits):
    gross_salary=(basic_salary+benefits)
    return gross_salary
basic_salary=float(input("enter basic salary:"))
benefits=float(input("enter benefits:"))
Gross_salary=calculate_gross_salary(basic_salary,benefits)
print(f"gross salary amount is {Gross_salary}")

def calculate_nhif(Gross_salary):
        if Gross_salary<=5999:
              results=150
        elif Gross_salary>=6000 and Gross_salary<=7999:
              results=300
        elif Gross_salary>=8000 and Gross_salary<=11999:
              results=400
        elif Gross_salary>=12000 and Gross_salary<=14999:
              results=500
        elif Gross_salary>=15000 and Gross_salary<=19999:
              results=600
        elif Gross_salary>=20000 and Gross_salary<=24999:
              results=750
        elif Gross_salary>=25000 and Gross_salary<=29999:
              results=850
        elif Gross_salary>=30000 and Gross_salary<=34999:
              results=900
        elif Gross_salary>=35000 and Gross_salary<=39999:
              results=950
        elif Gross_salary>=40000 and Gross_salary<=44999:
              results=1000
        elif Gross_salary>=45000 and Gross_salary<=49999:
              results=1100                           
        elif Gross_salary>=50000 and Gross_salary<=59999:
              results=1200
        elif Gross_salary>=60000 and Gross_salary<=69999:
              results=1300
        elif Gross_salary>=70000 and Gross_salary<=79999:
              results=1400
        elif Gross_salary>=80000 and Gross_salary<=89999:
              results=1500
        elif Gross_salary>=90000 and Gross_salary<=99999:
              results=1600
        else:
              results=1700
        return(results)            
      
Gross_salary=Gross_salary
NHIF=calculate_nhif(Gross_salary)
print(f"NHIF amount is {NHIF}")

#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.
def calculate_NSSF(Gross_salary):
      if Gross_salary<18000:
            results=(f"{Gross_salary} is below minimum requirement")
      else:
            results=(6/100*(Gross_salary))
      return(results)  
Gross_salary=Gross_salary
NSSF=calculate_NSSF(Gross_salary)          
print(f"NSSF is {NSSF}")


#Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015


def calculate_NHDF(Gross_salary):
      NHDF=(Gross_salary*0.015)
      return(NHDF)
NHDF=calculate_NHDF(Gross_salary)
print(f"NHDF amount is {NHDF}")


#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF + NHIF)
def calculate_taxable_income(Gross_salary,NSSF,NHDF,NHIF):
      taxable_income=(Gross_salary-(NHDF+NSSF+NHIF))
      return(taxable_income)
taxable_income=calculate_taxable_income(Gross_salary,NSSF,NHIF,NHIF)
print(f"taxable income is {taxable_income}")


def calculate_PAYEE(taxable_income):
      if taxable_income<24001:
            results=(f"{taxable_income} is below minimum requirement")
      else:
            if taxable_income>24001:
                  results(taxable_income*10/1000)
                  new=taxable_income-24000
            elif new<8333:
                  results((taxable_income*10/1000)+(new*25/100))   
            elif new>=8333:
                  results=((taxable_income*10/100)+(8333*25/100))
                  anew=new-8333
            elif anew<467667:
                  results=((taxable_income*10/100)+(8333*25/100)+(anew*30/100))
            elif anew>467667:
                  results=()   
                         

              





# Using Python or PHP or Java or Ruby or JavaScript
#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  
# #the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK: 