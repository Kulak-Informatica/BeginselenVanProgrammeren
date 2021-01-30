# Apparently, if you make a subclass of a dict and give it a dunder missing function, it does something if you call
# for a key that doesn't exist. Which is awesome. Why did I know this yet?
class specdict(dict):
    def __missing__(self, key):
        return 0


def main():
    new_sdict = specdict()
    new_sdict["a"] += 1
    print(new_sdict)  # prints {"a": 1}


main()
