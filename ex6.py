types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False 

joke_evaluation = "Isn't that joke so funny?! {}" # 

print(joke_evaluation.format(hilarious)) # Syntax: {}.format(value)   Syntax:{}{}.formate(value1, value2)

test_format_use="*Two Sentences: 1) {} 2) {} *" #  extra line
print(test_format_use.format(x,y))
w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)

