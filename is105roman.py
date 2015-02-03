roman_nums = (('M', 1000),
			  ('CM', 900),
			  ('D', 500),
			  ('CD', 400),
			  ('C', 100),
			  ('XC', 90),
			  ('L', 50),
			  ('XL', 40),
			  ('X', 10),
			  ('IX', 9),
			  ('V', 5),
			  ('IV', 4),
			  ('I', 1))

def substitute_subtractives(roman):
	pass
	
def int_to_roman(num):
	result = ""
	for roman, integer in roman_nums:
		while num >= integer:
			result += roman
			num -= integer
	return result
	
# Have to start with the highest number
def roman_to_int(roman_num):
	result = 0
	index = 0
	for roman, integer in roman_nums:
		while roman_num[index:index+len(roman)] == roman:
			result += integer
			index += len(roman)
	return result
	
def add_roman(num1, num2):
	num1_uncompacted = ""
	result = num1 + num2
	
	return result

def subtract_roman(num1, num2):
	pass

def multiply_roman(num1, num2):
	pass
	
print int_to_roman(1043)
print roman_to_int('MLXLIIV')

print add_roman('IX', 'V')