import ast


def read_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            python_code = file.read()
        return python_code
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def mutate_arithmetic_replacement(code):
    mutant = []
    for node in ast.walk(code):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            # Replace the arithmetic operator with a new one
            old_operator = ast.Add()
            new_operator = ast.Sub()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator

        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
            # Replace the arithmetic operator with a new one
            new_operator = ast.Add()
            old_operator = ast.Sub()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator

        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
            # Replace the arithmetic operator with a new one
            new_operator = ast.Div()
            old_operator = ast.Mult()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator

        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            # Replace the arithmetic operator with a new one
            old_operator = ast.Div()
            new_operator = ast.Mult()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator

        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
            # Replace the arithmetic operator with a new one
            old_operator = ast.Mod()
            new_operator = ast.Mult()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator
    return mutant


def mutate_conditional_replacement(code):
    mutant = []
    for node in ast.walk(code):
        if isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.GtE):
            # Randomly select a comparison to replace
            node.ops[0] = ast.Gt()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.GtE()

        elif isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.LtE):
            # Randomly select a comparison to replace
            node.ops[0] = ast.Lt()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.LtE()

        elif isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.Lt):
            # Randomly select a comparison to replace
            node.ops[0] = ast.LtE()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.Lt()

        elif isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.Gt):
            # Randomly select a comparison to replace
            node.ops[0] = ast.GtE()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.Gt()

        elif isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.Eq):
            # Randomly select a comparison to replace
            node.ops[0] = ast.NotEq()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.Eq()

        elif isinstance(node, ast.Compare) and isinstance(node.ops[0], ast.NotEq):
            # Randomly select a comparison to replace
            node.ops[0] = ast.Eq()
            mutant.append(ast.unparse(code))
            node.ops[0] = ast.NotEq()
    return mutant


def mutate_change_if(code):
    mutant = []
    prev_code = code
    for node in ast.walk(code):
        if isinstance(node, ast.If):
            # Change "if" to "if not"
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            mutant.append(ast.unparse(code))
            node.test = ast.UnaryOp(op=ast.Not(), operand=node.test)
            code = prev_code
    return mutant

def mutate_logical_replacement(code):
    mutant = []
    for node in ast.walk(code):
        if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
            # Replace the logical operator with a new one
            new_operator = ast.Or()
            old_operator = ast.And()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator

        elif isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
            # Replace the logical operator with a new one
            new_operator = ast.And()
            old_operator = ast.Or()
            node.op = new_operator
            mutant.append(ast.unparse(code))
            node.op = old_operator
    return mutant

def mutate_shift_operator_replacement(code):
    mutant = []
    for node in ast.walk(code):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.RShift):
            # Replace a shift operator with a new one
            node.op = ast.LShift()
            mutant.append(ast.unparse(code))
            node.op = ast.RShift()

        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.LShift):
            # Replace a shift operator with a new one
            node.op = ast.RShift()
            mutant.append(ast.unparse(code))
            node.op = ast.LShift()
    return mutant






