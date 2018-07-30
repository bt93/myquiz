# 1. Statements with fill-in-the-blanks and Numbered
# Stage 0, HTML
easy_statement ="""\n ___1___ is considered the language of the Internet. It is used 
				\nto make the contents of the web page. We can view these web pages
            	\nwith a procedure called ___2___. In ___1___ we create ___3___ that
            	\nwill create elements. A ___4___ can be used to classify elements as
            	\nwell as connect them to a ___5___ file.
             	"""
# Stage 1, CSS
medium_statement ="""\n ___1___ is the language that is used to style a web page.
				\nwe use ___2___ to select an element on an HTML document. ___2___
				\ncan do any thing from changing font-size or giving an element a
				\ncolor. One of the first changes you can make to a ___1___ document
				\nis by adding the ___3___. In order for the ___1___ to be seen on
				\na web page we must ___4___ it to an ___5___ file. 
	            """
# Stage 2, Python
hard_statement ="""\nPython was created by Guido van Rossum. It was created in ___1___.
				\nPython like many programming languages use ___2___ to store data and
				\ninformation. A ___3___ is a data type that contains a sequence of characters
				\nsurrounded by quotation marks. A ___4___ is made in Python by typing out def
				\nfollowed by a name with parenthasis and a colon. A ___4___ is also known as
				\na procedure. An ___5___ is used to find if the conditions of 
				\nsomething is true. It is otherwise known as an Equality comparision.
				"""

# 2. List correct answers for corresponding Statements
easy_answers = ["HTML", "HTTP", "tags", "class", "CSS"]
medium_answers = ["CSS", "selectors", "flex-box", "link", "HTML"]
hard_answers = ["1991", "variables", "string", "function", "if statement"]

# 3. List the number of blank strings
fill_in_the_blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]

# 4. Welcome Message when program begins.
print "Welcome! Ready for a quiz?"

# 5. Ask user which dificulty wanted and return the selected statement and answers.
def level_select():
	user_level = raw_input("What level would you like to try? Type in 'easy', 'medium' or 'hard'. ")
	if user_level == "easy" or user_level == "Easy":
		return start_quiz(easy_statement,easy_answers,fill_in_the_blanks)
	elif user_level == "medium" or user_level == "Medium":
		return start_quiz(medium_statement,medium_answers,fill_in_the_blanks)
	elif user_level == "hard" or user_level == "Hard":
		return start_quiz(hard_statement,hard_answers,fill_in_the_blanks)
	else:
		print "Oops that is not a level. You need to type 'easy', 'medium' or 'hard'. "
		level_select()

# 6. Asks user how many tries the user would like to have and returns the intiger. Found way to check if the user input is an intiger on stackoverflow.
# https://stackoverflow.com/questions/27310631/checking-if-input-is-an-integer
def how_many_times():
	while True:
		try:
			tries_left = int(raw_input("How many tries would you like? "))
			return tries_left
		except ValueError:
			print "That is not a number."

# 7. Prints appropriate statement, loops through each blank and asks the user for the correct answer. If the responce is incorrect,
# subtracts from amount of tries left. If tries left is 0 ends test and prompts user to try again. It it's correct it replaces the blanks
# with the correct answer and prints out the statment. Once all questions are answered correctly test ends and propmts user to try another test.
def start_quiz(statement,answers,blanks):
	tries_left = how_many_times()
	print statement
	for num in range(0,len(blanks)):
		user_input = raw_input("Type in the correct answer" + blanks[num] + " ")
		while user_input != answers[num]:
			if tries_left > 1:
				tries_left -= 1
				print "Incorrect. You have " + str(tries_left) + " tries left. "
				user_input = raw_input("Try again: " + blanks[num] + " ")
			else:
				print "You are out of trys. Maybe try a different quiz."
				level_select()
		if user_input in answers[num]:
			statement = statement.replace(blanks[num],answers[num])
			print "Correct!" + statement
	print "Congrats, You completed the quiz! Why not try a different quiz?"
	level_select()

level_select()