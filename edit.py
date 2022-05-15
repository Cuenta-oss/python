
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]


def isYearLeap(year):
    if year % 4 != 4:  # si no es divisible entre 4, NO ES BISIESTO
        return False
    elif year % 4 == 0 and year % 100 != 0:  # divisible entre 4 y no entre 100 o 400, ES BISIESTO
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: # divisible entre 4 y 10 y no entre 400, NO ES BISIESTO
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:  # divisible entre 4, 100 y 400, ES BISIESTO
        return True

for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("error")
