# Q5. Create a Login System: (4 Marks)
# • Private variable __password = 'python@123'
# • Private variable __attempts = 3
# • Method login(password):
# → Wrong password: attempts -= 1, show remaining → If attempts == 0: raise AccountLockedError
# → Correct: print 'Login successful!'
# • Handle AccountLockedError with finally block.
# Date: June 2025 Batch: ___________
from abc import ABC, abstractmethod

# Custom Exception
class AccountLockedError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.__password = "python@123"
        self.__attempts = 3

    def login(self, password):
        if self.__attempts == 0:
            raise AccountLockedError("Account Locked!")

        if password == self.__password:
            print("Login successful!")
        else:
            self.__attempts -= 1
            print("Wrong password!")
            print("Remaining Attempts:", self.__attempts)

            if self.__attempts == 0:
                raise AccountLockedError("Account Locked!")


# Main Program
user = LoginSystem()

try:
    user.login("java123")
    user.login("c++123")
    user.login("python")
    user.login("python@123")

except AccountLockedError as e:
    print(e)

finally:
    print("Login process completed.")