def average_project() :
    print("This game will take some numbers and print the average")
    print("----------------------------------")

    num_of_num = int(input("Enter how much times do you want to write :"))
    times = 0
    sum = 0

    while times < num_of_num :
        number = int(input(f"Enter the num {times+1} :"))
        sum += number
        times += 1

    average = sum/num_of_num
    print(f"The average is {average}")