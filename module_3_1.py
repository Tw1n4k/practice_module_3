def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    a = [len(string), string.upper(), string.lower()]
    count_calls(1)
    return a


def is_contains(string_info, is_contains):
    string_info.lower()
    new_is_contains = []
    count_calls(1)
    for i in is_contains:
        new_is_contains.append(i.lower())
    return string_info.lower() in new_is_contains


calls = 0
print(string_info('banana'))
print(string_info('potato'))
print(is_contains('banana', ['ban', 'ana', 'ananab']))
print(is_contains('potato', ['pot', 'tato', 'otatop']))
print(calls)