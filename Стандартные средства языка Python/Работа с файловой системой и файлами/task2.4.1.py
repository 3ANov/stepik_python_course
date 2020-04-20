stack = []
with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
    for input_line in inp:
        stack.append(input_line.rstrip())
    stack.reverse()
    output_line = "\n".join(stack)
    out.write(output_line)


