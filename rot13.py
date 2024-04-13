def rot13(message):
    msg_list = list(message)
    for i, letter in enumerate(msg_list):
        msg_list[i] = shift_letter(letter)
    return ''.join(msg_list)

def shift_letter(buf: str) -> str:
    current_state = ord(buf)
    if current_state in range(65, 91):
        current_state += 13
        if current_state > 90: current_state -= 26
    elif current_state in range(97, 123):
        current_state += 13
        if current_state > 122: current_state -= 26
    return chr(current_state)

print(rot13('!@#$%^&*+?~()_-+=:;'))