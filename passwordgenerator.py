import string
import random





def ask():
	number_char = input('how many charachters is your pasword? it must be between 6 and 30')
	return number_char


def validate(number_char):
	if int(number_char)>5 and int(number_char)<31:
		return int(number_char)
	else:
		return None
		

def main():
	number_char = ask()
	# validate(number_char)
	if validate(number_char) is None:
		print('change the length')
	while validate(number_char) is None:
		number_char = ask()
		print('change the length')

	print('thats a valid password length')
	x = validate(number_char)
	return x

# x = main()
	



# y = id_generator()
# print(y)



# get the random numbers between 6 and 30 to be generated automatically ...
# This is the testing phaze



# • At least 1 digit (0-9)
# • At least 1 lower-case character (a-z)
# • At least 1 upper-case character (A-Z)
# • At least 1 special character (eg. !, @, #, $, %, ^, _, ...)
# • Once there is at least 1 of each, the rest of the password should be composed of more characters
# from the above-mentioned groups.

# this project could be braught to use for checking passwords for login sites

digits = ['0','1','2','3','4','5','6','7','8','9']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special = ['!','@','$','%','^','_','.']


def test():
	n=1
	while n<101:
		x=random.randint(6,31)
		print(x)
		def id_generator(size=x, chars=string.ascii_uppercase + string.digits +string.ascii_lowercase+string.punctuation):
				return ''.join(random.choice(chars) for _ in range(size))
		y = id_generator()
		print(y)
		print(digits)
		for i in y:
			if i in digits:
				print('there are digits')
				a = True
				break
			else:
				a = None
		for j in y:
			if j in lower:
				print('there is lower case')
				b= True
				break
			else:
				b = None
		for k in y:
			if k in upper:
				print('there is upper case')
				c = True
				break
			else:
				c = None
		for m in y:
			if m in special:
				print('there is special case')
				d = True
				break
			else:
				d = None
		the_check_list = [a,b,c,d]
		if None in the_check_list:
			print('Not all of the charachters are present!')
		else:
			print('Perfect password!')
		n+=1



			

test()

# test shows that this algorithm does not generate perfect passwords all of the time..







