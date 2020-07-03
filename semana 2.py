print(11%5)
print((10>=5*2)&(10<=5*2))

print(6*7)
print(((2050/5)-32)/9)
def area_triangle(base, height) :
     return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a +area_b
print ("la suma de las base de las areas " + str(sum))

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2 , 30 , 0)
amount_b = get_seconds(0 , 45 , 15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600 ) // 60
    remaining_seconds = seconds - hours * 3600 - minutes *60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


def lucky_number(name):
    number = len(name) * 9
    print("hello" + name + "your luky number is " + str(number))

lucky_number("simon")
lucky_number("sofia")


def greeting(name , department):
    print("welcome," + name)
    print("you are part of " + department)

greeting("simon " , "doctor")
greeting("sofia " , "ingeniers suport" )


def rectangle_area(base,height):
    area = base*height
    base = 5
    height = 6
    return area
    
    print("The area is " + str(area))

def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

print ("cat " == "dog") # == genera una igualdad en este caso es resultado de consola es falso

print(1 != 2) # != genera una diferencia el resultado es true por que 1 y dos son diferentes


#semana 3 loops 
while True:
    do_something_cool()
    if user_requested_to_stop():
        break #esto le indica al loops que debe dejar de funcionar



#ejercicios de semana 3 quiz

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n / 2>= 1:
    n = (n + 1)% 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT



def sum_divisors(n):
    sum=1
    x=int(n**0.5)
    for i in range(2,(x//1)+1):
        if n%i==0:
            sum=sum+i
        if n%i==0 and n/i!=i:
            sum=sum+(n/i)            
    return int(sum)

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114


def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number
		# What is the additional condition to exit out of the loop?
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1


multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

#SECCIÓN 2EJERCICIO
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(1,x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285