print('PRIME NUMBERS')
print('CS112 PRE-FINAL EXAM'); print()

print('GUIDELINES:')
print('[1] If [start range] is a negative number. The program will prompt a message: "Enter a non-negative number"')
print('[2] If [end range] is less than [start range]. The program will prompt a message: "Enter a number greater than [start range]"')
print('[3] If the user enters the number "0", the program will terminate.'); print()

while True:
    num = int(input('Enter a Number [start range]: '))

    if num < 0:
        print("Enter a non-negative number."); print()
    
    elif num == 0:
        print("Program terminated"); print()
        break

    elif num > 0:
        num2 = int(input('Enter a Number [end range]: '))

        if num < 0:
            print("Enter a non-negative number."); print()

        elif num2 == 0:
            print("Program Terminated"); print()
            break

        elif num2 < num:
            print("Enter a number greater than", num); print()
        
        elif num2 > num:
            print ('Prime numbers between the range', num, 'and', num2, 'are: ')

            for prime in range(num, num2 + 1):
                
                if prime > 1:

                    for i in range (2, prime):  

                        if (prime % i) == 0:  
                            break  
                        
                    else:  
                        print(prime, end=' ')

    else:
        print('Error!')
        
    print()
    print('----------------------------------') 