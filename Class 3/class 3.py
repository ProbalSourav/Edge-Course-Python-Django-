"""
#                                          //Factorial//

def fact(x):
  ans=1
   # factorial using loop
  for i in range (1,x+1):
     ans*=i  #calculate (1*2*3*.....n)
  return ans
    

n=int(input("Enter a number: "))
print("Factorial of the number: ",fact(n))

"""



"""
#                                          //Module//
import module
celsius=float(input("Enter value in celsius:"))
print(f"Farhenheit value of {celsius} degree celsius is: ",module.celsius_to_farhenheit(celsius))
radius=float(input("Enter the value of radius:"))
print("Area of the circle",module.area_of_circle(radius))
"""


"""
#                                           //List//

array=[6,4,7,4,2,5,6,3]

def calculate(array):
    sum=0
    avg=0
    cmin=array[0]
    cmax=array[0]
    for i in array:
        if cmax<i:
            cmax=i
        if cmin>i:
            cmin=i
        sum+=i
    avg=sum/len(array)
    return sum,cmax,cmin,avg

result=calculate(array)
print("Sum of all numbers:",result[0])
print("Largest number:",result[1])
print("Smallest number:",result[2])
print("Average:",result[3])

"""

"""
#                                             //Tuple//
array=(6,4,7,4,2)
def calculate(array):
    array[0]=3
    sum=0
    for i in array:
        sum+=i # sum of all values
    
    return sum

result=calculate(array)
print("Sum of all numbers:",result)

"""

"""
#                                         	 //Set//

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection
intersection_result = set1.intersection(set2)
print("Intersection:", intersection_result)  # Output: {3, 4}

# Difference
difference_result = set1.difference(set2)
print("Difference (set1 - set2):", difference_result)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_result = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_result)  # Output: {1, 2, 5, 6}


# Using operators
intersection_result_operator = set1 & set2
difference_result_operator = set1 - set2
symmetric_difference_result_operator = set1 ^ set2

print("Intersection using '&':", intersection_result_operator)  # Output: {3, 4}
print("Difference using '-':", difference_result_operator)  # Output: {1, 2}
print("Symmetric Difference using '^':", symmetric_difference_result_operator)  # Output: {1, 2, 5, 6}
"""

"""
#                                             //Dictionary//
# Create a dictionary to store student scores
students_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88
}

def calculate_scores(scores):
    total = sum(scores.values())  # Calculate total score
    highest = max(scores.values())  # Find highest score
    lowest = min(scores.values())    # Find lowest score
    average = total / len(scores)    # Calculate average score
    
    return average, highest, lowest

# Calculate average, highest, and lowest scores
average_score, highest_score, lowest_score = calculate_scores(students_scores)

# Print the results
print(f"Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
"""

"""
#                           //List Comprehension && Lamda Function//

even_number=[x for x in range(1,51) if x%2==0] #even number from (1-50)
print(even_number)

multiplied_number=[(lambda x: x*3)(x) for x in even_number] #multiply all even number by 3
print(multiplied_number)
"""