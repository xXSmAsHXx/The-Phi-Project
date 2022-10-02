
def main():

    VarA = float(input("\nEnter the age : "))
    VarH = int(input("Enter your height in ft. : "))
    VarH2 = float(input("Enter your height in inches. : "))

    if VarH2 >= 12:
        x = VarH2//12
        VarH = x + VarH
        VarH2 = VarH2%12
        print("The extra inches were converted into feet, your new height is ",VarH, "ft. and ",VarH2, "inches")

    totalH = (12*VarH + VarH2) #for comparing average heights

    ages = list(range(1,20))
    dict = {1 : 30 , 2 : 34 , 3 : 37 , 4 : 40, 5 : 42 , 6 : 45 , 7 : 48, 8 : 50 ,
            9 : 52 , 10 : 54 , 11 : 56 , 12 : 58 , 13 : 61 , 14 : 64 , 15 : 66 , 16 : 68 , 17 : 69 , 18 : 69 , 19 : 69}

    if VarA in ages:
        if totalH >= dict[(VarA)]:
            x = totalH-dict[(VarA)]
            print("Your Height is ",x,"inches higher than average!")

        else:
            y = dict[(VarA)]-totalH
            print("Your Height is ",y,"inches lower than average!")

    elif VarA >= 20:
        if totalH >= 69:
            x = totalH - dict[(VarA)]
            print("Your Height is ", x, "inches higher than average!")
        else:
            y = dict[(VarA)] - totalH
            print("Your Height is ", y, "inches lower than average!")


main()

restart = str(input("Do you want to rerun this code? ")).lower()

if "yes" in restart:
    main()
else:
    exit()





