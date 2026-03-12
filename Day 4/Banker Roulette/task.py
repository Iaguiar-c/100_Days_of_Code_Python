import random


# 1st option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_friends = random.choice(friends)
print(random_friends)

# 2nd option
randon_index = random.randint(0, 4)
print(friends[randon_index])