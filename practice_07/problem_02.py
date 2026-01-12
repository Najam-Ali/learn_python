# WAP to greet all the person names stored in a list L1 and which starts with the letter 'S'.
li = ['Sam', 'John', 'Sara', 'Mike', 'Sophie', 'David']
for name in li:
    if name.startswith('S'):
        print(f"Hello, {name}!")