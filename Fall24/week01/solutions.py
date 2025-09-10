## Q1


print("Hello there! I'm the CS101 Study Bot. What's your name?")
username = input()

print("Great to meet you, " + username + "! How many semesters have you been studying Computer Science?")
semesters = input()

print('Ah, "' + semesters + '" semesters, nice! I\'m still learning myself. What are you working on right now?')
current_topic = input()

print('"' + current_topic + '", huh? That\'s a challenging topic! I can\'t say I know all the algorithms yet, but maybe we can figure it out together? Need help with something specific?')
specific_help = input()

print('I wish I could, but I\'m just a simple chatbot for now. Maybe check out the lecture notes or ask your instructor for more details. I\'m here for small talk though! Anything else?')
more_info = input()

print('Well, I was programmed by "' + username + '" in a few lines of code for CS101. My job is to chat and keep you company while you study. Have fun with your course, and let\'s talk again soon!')



## Q2

# You are expected to display each one of the following messages on a new line
# "Cmpe150 requires regular practice"
# "The more I study, the easier it will become"
#
# After these two messages, you should define a function calculate_f to calculate
# and display the result of f = m * a for the given m and a arguments.
# Then you should define getWidth function to return the width of a triangle as explained
# in the question description


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

print("Cmpe150 requires regular practice.")
print("The more I study, the easier it will become.")

def calculate_f(m, a):
    print(m*a)

def getWidth(height):
    return 2 * height - 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

m = int(input())
a = int(input())
calculate_f(m, a)

triangle_height = int(input())
triangle_width = getWidth(triangle_height)
print(triangle_width)


