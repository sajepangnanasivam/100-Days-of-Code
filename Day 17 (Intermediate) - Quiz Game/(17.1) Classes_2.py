class User:

    def __init__(self, user_id, username):
        # Where we create our starting values.
        # Will be called everytime i create an object
        # Passed in values will be set on self
        self.id = user_id
        self.username = username

        # Setting default 0 as the value for followers on all users.
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Creating an object from the User class
user_1 = User("001", "Sajepan")
user_2 = User("002", "Jack")

# User 1 follows User 2
user_1.follow(user_2)
user_1.follow(user_2)

print(f"User 1 Following: \t {user_1.following}")
print(f"User 1 Followers: \t {user_1.followers}")
print(f"User 2 Following: \t {user_2.following}")
print(f"User 2 Followers: \t {user_2.followers}")

