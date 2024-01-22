from mutate import *
import subprocess
import os
import shutil
import re
from getdiff import find_code_diff


def calculate_mutation_score(num_mutaion_total , num_mutaion_kill):
    return f"total number of mutant : {num_mutaion_total} \n kill mutant number : {num_mutaion_kill} \n mutant score without equivalent : {(100*num_mutaion_kill/num_mutaion_total)}"


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


def append_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        with open(file2_path, 'a') as file2:
            file2.write("\n\n\n")
            shutil.copyfileobj(file1, file2)


def run_tests_on_mutant(mutant_test_filename):
    try:
        # result = subprocess.run(['git', '--version'], capture_output=True)
        result = subprocess.run(f"pytest tests/{mutant_test_filename}",
                                capture_output=True,
                                text=True,
                                shell=True)
    except FileNotFoundError as e:
        raise RuntimeError(e)

    failed_matches = re.findall(r'\b(\d+) failed\b', result.stdout)
    passed_matches = re.findall(r'\b(\d+) passed\b', result.stdout)

    # Get the counts or default to 0 if not found
    failed_count = int(failed_matches[0]) if failed_matches else 0
    passed_count = int(passed_matches[0]) if passed_matches else 0

    return passed_count, failed_count

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


original_code = read_python_file("isPrime.py")

mutants = []

code = ast.parse(original_code)

mutants = mutate_arithmetic_replacement(code)
mutants += mutate_conditional_replacement(code)
mutants += mutate_change_if(code)
mutants += mutate_logical_replacement(code)
mutants += mutate_shift_operator_replacement(code)

i = 1
for mutant in mutants:
    with open(f"mutants/mutant{i}.py", "w+") as f:
        f.write(mutant)
    f.close()
    i += 1

mutants_directory = "mutants"

mutant_files = [file for file in os.listdir(mutants_directory) if file.endswith(".py")]

i = 1
for file_name in mutant_files:
    shutil.copy(f"mutants/{file_name}", f"tests/test_mutant{i}.py")
    i += 1

mutant_test_files = [file for file in os.listdir("tests") if file.endswith(".py")]

i = 1
while i <= len(mutant_test_files):
    append_files("test_isPrime.py", f"tests/test_mutant{i}.py")
    i += 1

original_code = read_python_file("isPrime.py")

number_of_mutaion_total = len(mutant_test_files)
number_of_mutaion_kill = 0

for mutant, mutant_test in zip(mutant_files, mutant_test_files):
    mutated_code = read_python_file(f"mutants/{mutant}")
    find_code_diff(original_code, mutated_code)

    print("____________________________________________________________")

    passed_tests, failed_tests = run_tests_on_mutant(mutant_test)

    print(f"{failed_tests} failed test(s)")
    print(f"{passed_tests} passed test(s)")


    if failed_tests > 0:
        number_of_mutaion_kill = number_of_mutaion_kill + 1
        print("********** mutation was killed **********")
    else:
        print("********** mutation is alive **********")
    print("____________________________________________________________")


# print(f"****************** mutaion score : {calculate_mutation_score(number_of_mutaion_total,number_of_mutaion_kill)} % *******************")
print(calculate_mutation_score(number_of_mutaion_total,number_of_mutaion_kill))