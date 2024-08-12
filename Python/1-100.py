
nums = []
negativenum = []  # creates a list containing numbers from 1 to 50

for x in range(1,202):
    if  1 <= x < 100 :
        nums.append(x)
    else:
       nums.append(200-x) 

    print(nums)


for x in range (-1, 100):
    if -1 <= x <= 100:
        negativenum.append(x)

    print(negativenum)

numbers = list(range(-1, -2, 100)) 


#print(numbers)

#def Reverse(lst):
    #return lst[::-1]

#combined_list = [i for i in range(-1,101, 100, 0, -1)]

#print(Reverse(combined_list))





