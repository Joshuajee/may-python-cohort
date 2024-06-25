def calBMI():
    try:
        height = float(input("What is your height: "))
        weight = float(input("What is your weight: "))
        if (weight < 1): raise Exception("Weight most be greater than zero")
        BMI = (weight / (height ** 2)) * 10000
        print("Your BMI is: {}".format(BMI))
    except ValueError:
        print("Incorrect value, please put in only numbers")
        calBMI()
    except ZeroDivisionError:
        print("Height cannot be zero")
        calBMI()
    except:
        print("Weight Most be greater than zero")
        calBMI()
    else:
        print("Done")





calBMI()