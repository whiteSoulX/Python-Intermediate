def uppercase(func):
    def warpper():
        ori_message = func()
        modified_message = ori_message.upper()
        return modified_message
    return warpper

@uppercase
def greet():
    return "welcome"
print(greet())
