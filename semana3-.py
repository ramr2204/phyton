
for x in range(1, 10, 3):
    print(x)

for x in range(10):
    for y in range(x):
        print(y)
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()

print(host_addresses)

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

teams = ['wolves', 'dragons',' pandas', 'unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

def greet_friends (firends):
    for friend in firends:
        print(" hi " + friend)

greet_friends(['sofia', 'Mario','luisa', 'simon'])

greet_friends(['raul'])

threes = list(range(3, 101, 3))

for number in threes:
    print(number)


#quiz semana 3 lopps seccion for
#Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))

#Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.
cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
    
#Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.
threes = list(range(0, 101,7))

for number in threes:
    print(number)

#The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts. Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")
    

#retry(create_user, 3)
#retry(stop_service, 5)
#end quiz

#recursividad
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result)+ "for factorial of " + str(n))
    return result

factorial(10)