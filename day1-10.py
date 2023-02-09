def modify_string(s):
    result = []
    for char in s:
        freq = s.count(char)
        char_ascii = ord(char)
        print(char_ascii)
        new_char_ascii = char_ascii +freq
        print(new_char_ascii)
        print(freq)
        if new_char_ascii > ord('z'):
            new_char_ascii = ord('a') +(new_char_ascii - ord('z') - 1)
        result.append(chr(new_char_ascii))
    return ''.join(result)

s = "ghee"
print(modify_string(s))

s = "elephant"
print(modify_string(s))

s = "apple"
print(modify_string(s))

s = "orange"
print(modify_string(s))

s = "lion"
print(modify_string(s))
