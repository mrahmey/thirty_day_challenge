# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Maurice Rahmey

# 3.1: NameError: name 'repeat_lyrics' is not defined

# 3.2: It runs and prints the lyrics twice.

# 3.3:
def right_justify(name):
    print (" "*(70-len(name))+name)

right_justify("allen")

# 3.4:

# 2)
	def do_twice(f, v):
	    f(v)
	    f(v)

	def print_spam(spam):
	    print "spam"

	do_twice(print_spam, "spam")

# 3)
	def print_twice(string):
	    print string
	    print string

# 4)
	def do_twice(f, v):
	    f(v)
	    f(v)

	def print_twice(string):
	    print string
	    print string

	do_twice(print_twice, "spam")

# 5)
	def do_twice(f, v):
	    f(v)
	    f(v)

	def print_twice(string):
	    print string
	    print string

	do_twice(print_twice, "spam")
	print ""

	def do_four(f, v):
	    do_twice(f, v)
	    do_twice(f, v)

	do_four(print_twice, "spam")
	print ""