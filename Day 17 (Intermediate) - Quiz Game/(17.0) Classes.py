class User:

    def __init__(self, user_id, username):
        # Where we create our starting values.
        # Will be called everytime i create an object
        # Passed in values will be set on self
        self.id = user_id
        self.username = username

        # Setting default 0 as the value for followers on all users.
        self.followers = 0


# Creating an object from the User class
user_1 = User("001", "Sajepan")
print(user_1.id)

# Define attribute like this without class.
# user_1.id = "001"
# user_1.username = "Sajepan"
# print(user_1.username)
