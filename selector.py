# Easy Python project  :P
# Random friend selector to decide who to FaceTime!


import random

friends =[
    'Arnab','Dipankar','Sandeep Sir','Aman','Virat','Pant'
]

selected = random.choice(friends)   #randomly choose a friend
print('Who should I facetime today? ')
print(selected)

# random.randint(1,5) 
# random.choice(friends)