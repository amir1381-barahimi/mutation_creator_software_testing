import difflib


def find_code_diff(original_code, mutated_code):

    original_lines = original_code.splitlines()
    mutated_lines = mutated_code.splitlines()

    differ = difflib.Differ()

    diff = list(differ.compare(original_lines, mutated_lines))

    for line in diff:
        prefix = line[:2]
        content = line[2:]
        if prefix == '  ':
            print(f'   {content}')
        elif prefix == '- ':
            print(f'-  {content}')
        elif prefix == '+ ':
            print(f'+  {content}')

    return diff
