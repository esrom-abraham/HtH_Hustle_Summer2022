# Welcome to your last Pair Programming Class!
# We're so glad to be part of your coding journey!
# Today will be a light day. 

# Priorities for today:
# 1. Exit Ticket: Fill out the Post-Survey Form
# 2. Finish your previous Replit assignments. If you commented out tasks from your previous Replit assignments, then go back to those and actually finish them.
# 3. Pick the Replit assignment you struggled with most & obtain feedback from your TA AKA PP Instructor.
# 4. Try out this short intro on functions.
# 5. If you feel like you wanna do more coding, GREAT! Sign up for Build!! You will do more coding & actually have an exploratory data analysis project on a dataset of your choice.
# CONGRATS on finishing Hustle!

# Defining a function
# This is a simple function that says you're the best called greet_user()
def greet_user():
  """Display a simple greeting"""
  print("Hello, you're the best!")
  
greet_user()

# Now let's play a li'l bit more with this. Let's modify our function so it can obtain your name
def greet_user(username):
  """Display a simple greeting with your name"""
  print(f"Hello, {username}!")
greet_user('Kiyomi')

# Let's create a function with a dictionary
def build_person(first_name, last_name):
  """Return a dictionary about a person"""
  person = {'first': first_name, 'last': last_name}
  return person
musician = build_person('jimi', 'hendrix')
print(musician)

# Now make a fun function of your favorite album with your favorite songs