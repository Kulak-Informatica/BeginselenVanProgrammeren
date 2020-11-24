# PLAYGROUND! Here I test some random shit I find online and wanna try out.
# If you find anything interesting that helps in your programming, you're welcome, I guess?
# --------------------------------------------------------------------------------------------------------------
# Here, I'm testing self-defined exceptions. You know when your program doesn't work and it gives that red text?
# That's an exception, and you can make 'em yourself.
# First idea I thought of: Test if a string contains characters that can't be in a name. Raise an exception if it aint.
class NotANameError(Exception):
    """Exception raised when given string is sure to not be a name

    Attributes:
        name -- given string which caused the error
        message -- explanation of the error
    """
    def __init__(self, name, message="string is not a name"):
        self.name = name
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.name} -> {self.message}"


def main():
    name = input("Give a name\n> ")
    from string import ascii_letters
    for char in name:
        if char not in ascii_letters + " ":
            raise NotANameError(name)
    print(name, "might be a proper name.")


main()
