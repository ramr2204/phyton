#Basic Structures Introduction
def double_word(word):
    return  word * 2 + str(len(word * 2)) 
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#The Parts of a String
name = "raul" 
print (name[1])#python inicia de 0 por eso cuando indicamos [1] el nos muestra la letra a

print (name[0])# a qui se muestra la latra r

print (name[3])#ultima letra
#print(name[4])#se observa el error

#example
def first_and_last(message):
    if not message:
        return True
    elif (message[0] == message[-1]):
            return True
    elif (message[0] != message[-1]):
            return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

fruit = "guayabamanzana"
print (fruit[:5])#es realizar un rango desde el inicio del caracter hasta el caracter 5 
print (fruit[5:])#toma el rango desde el caracter 5 hacia el final de nuestra fruta

pets = "Cats & Dogs"
print(pets.index("&"))

print(pets.index("C"))

print(pets.index("Dog"))

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

print("Dragons" in pets)

print("Cats" in pets)
print ("Dogs" in pets)

print("Mountains".upper())
print("Mountains".lower())

print(" yes ".strip())

print(" yes ".lstrip())

print(" yes ".rstrip())

#"Forest".isnumeric()

#"12345".isnumeric()

print(int("12345") + int("54321"))#porque el resultado es 66666 se que el int lo combierte en numero real

print(" ".join(["this", "is", "a", "phrase", "joined", "by ", "spaces"]))

print(" ".join(["this", "is", "a", "phrase", "joined", "by ", "spaces"]))#observar que cuando se imprime en el inicio hay dos comillas con espacio esto hace separar las palabras si no se deja el espacio entre comillas pues no hay espacios
print("...".join(["this", "is", "a", "phrase", "joined", "by ", "dots"]))

name = "Manny"
number = len(name) * 3
print("hello {}, your lucky number is {}" .format(name, number))

print("your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

"""def student_grade(name, grade):
	return ""

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))no pude resolver esto video Cadenas de formato"""


price = 7.5
with_tax = price * 1.09
print (price, with_tax)

def to_celsius(x):
    return(x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C" .format(x, to_celsius(x)))

#quiz semana 4
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.strip():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if letter != ' ':
			new_string = new_string+letter
			reverse_string = letter+reverse_string
	# Compare the strings
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

#pregunta 2
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#pregunta 4
def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

#pregunta 5 pedir explicación o buscarla
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	if sentence.endswith(old):
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = sentence.rfind(old)
		new_sentence = sentence[:i]+new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"



