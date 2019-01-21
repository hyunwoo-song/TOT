T = input()

if T.islower():
    print(f'{T}(ASCII: {ord(T)}) => {T.upper()}(ASCII: {ord(T.upper())})')
elif T.isupper():
    print(f'{T}(ASCII: {ord(T)}) => {T.lower()}(ASCII: {ord(T.lower())})')
else:
    print(f'{T}')
