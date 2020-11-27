def mutate_string(string, position, character):
    inp_string = list(string)
    inp_string[position] = character
    return ''.join(inp_string)
