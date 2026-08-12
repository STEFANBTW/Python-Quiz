import json
import re

questions = [
    {
        "id": 1,
        "question": "What is the correct way to write a single-line comment in Python?",
        "options": {
            "A": "// This is a comment",
            "B": "/* This is a comment */",
            "C": "# This is a comment",
            "D": "-- This is a comment"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. This is used in C++, Java, and JavaScript.",
            "B": "Incorrect. This is a multi-line comment in C-style languages.",
            "C": "Correct. Python uses the hash symbol (#) for single-line comments.",
            "D": "Incorrect. This is used in SQL."
        }
    },
    {
        "id": 2,
        "question": "Which of the following data types is immutable in Python?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Set",
            "D": "Tuple"
        },
        "correct": "D",
        "explanations": {
            "A": "Incorrect. Lists can be modified after creation.",
            "B": "Incorrect. Dictionaries can be modified.",
            "C": "Incorrect. Sets can be modified.",
            "D": "Correct. Tuples are immutable, meaning their elements cannot be changed once assigned."
        }
    }
]

# I'll just dynamically generate 48 more questions that are variations of basic python topics.
topics = [
    ("What does the `type()` function do?", "Returns the type of an object", "Converts a type", "Prints the object", "Deletes the object", "A"),
    ("Which keyword is used to define a function?", "def", "function", "fun", "define", "A"),
    ("What is the output of `2 ** 3`?", "8", "6", "9", "5", "A"),
    ("How do you start a while loop in Python?", "while x > 0:", "while (x > 0)", "while x > 0 {", "loop while x > 0:", "A"),
    ("Which of the following is a valid variable name?", "my_var", "2myvar", "my-var", "my var", "A"),
    ("What is the result of `3 // 2` in Python 3?", "1", "1.5", "2", "1.0", "A"),
    ("Which operator is used to check if two values are equal?", "==", "=", "===", "=>", "A"),
    ("How do you get the length of a list?", "len(my_list)", "my_list.length()", "size(my_list)", "length(my_list)", "A"),
    ("What does the `range()` function return?", "A sequence of numbers", "A list of strings", "A single number", "A boolean", "A"),
    ("Which data structure uses key-value pairs?", "Dictionary", "List", "Tuple", "Set", "A"),
    ("How do you import a module named `math`?", "import math", "include math", "require math", "using math", "A"),
    ("What is the boolean representation of an empty string `''`?", "False", "True", "None", "Error", "A"),
    ("Which method adds an item to the end of a list?", ".append()", ".insert()", ".add()", ".push()", "A"),
    ("What does `break` do in a loop?", "Exits the loop completely", "Skips to the next iteration", "Pauses the loop", "Restarts the loop", "A"),
    ("What is the output of `'a' + 'b'`?", "'ab'", "'a b'", "Error", "'a+b'", "A"),
    ("Which keyword is used for exception handling?", "except", "catch", "handle", "error", "A"),
    ("What is `None` in Python?", "A special constant representing the absence of a value", "Zero", "An empty string", "False", "A"),
    ("How do you open a file for reading?", "open('file.txt', 'r')", "open('file.txt')", "read('file.txt')", "Both A and B", "D"),
    ("Which logical operator returns True if both conditions are True?", "and", "or", "not", "&&", "A"),
    ("What does the `in` operator do?", "Checks if a value exists in a sequence", "Converts a string to integer", "Loops through a list", "None of the above", "A"),
    ("How do you convert the string `'5'` to an integer?", "int('5')", "integer('5')", "num('5')", "convert('5')", "A"),
    ("Which symbol is used for string formatting (f-strings)?", "f", "format", "str", "$", "A"),
    ("What is the output of `bool(0)`?", "False", "True", "None", "Error", "A"),
    ("Which function reads input from the user?", "input()", "read()", "get()", "scan()", "A"),
    ("What is a correct way to create an empty list?", "[]", "list()", "Both A and B", "None", "C"),
    ("Which function returns the absolute value of a number?", "abs()", "absolute()", "math.abs()", "val()", "A"),
    ("What does `continue` do in a loop?", "Skips the rest of the current iteration and goes to the next", "Exits the loop", "Pauses the program", "Returns a value", "A"),
    ("How can you make a string completely uppercase?", "s.upper()", "s.capitalize()", "s.uppercase()", "upper(s)", "A"),
    ("What is the result of `10 % 3`?", "1", "3", "3.33", "0", "A"),
    ("Which index refers to the first element in a list?", "0", "1", "-1", "First", "A"),
    ("How do you check the data type of `x`?", "type(x)", "typeof(x)", "x.type()", "class(x)", "A"),
    ("What is a class in Python?", "A blueprint for creating objects", "A built-in data type", "A function", "A module", "A"),
    ("How do you instantiate an object of class `Car`?", "Car()", "new Car()", "create Car", "Car.new()", "A"),
    ("What is the purpose of `__init__` in a class?", "It initializes a newly created object", "It creates the class", "It deletes the object", "It prints the object", "A"),
    ("Which keyword refers to the current instance of a class?", "self", "this", "me", "current", "A"),
    ("How do you access the value associated with key 'k' in dict 'd'?", "d['k']", "d.get('k')", "Both A and B", "None", "C"),
    ("What does the `strip()` method do?", "Removes leading and trailing whitespace", "Removes all spaces", "Splits the string", "Joins strings", "A"),
    ("Which of these is a Python web framework?", "Django", "React", "Spring", "Laravel", "A"),
    ("What is a lambda function?", "An anonymous inline function", "A complex class method", "A built-in mathematical function", "A type of loop", "A"),
    ("How do you write 'Not equal' in Python?", "!=", "<>", "not=", "!==", "A"),
    ("Which function is used to sort a list in-place?", "list.sort()", "sorted(list)", "sort(list)", "order(list)", "A"),
    ("What does `pass` do?", "Does nothing, acts as a placeholder", "Skips to the next iteration", "Exits the function", "Returns None", "A"),
    ("What is a tuple?", "An ordered, immutable collection of elements", "An unordered collection", "A mutable list", "A dictionary", "A"),
    ("How do you declare a global variable inside a function?", "global var_name", "var_name = global", "global(var_name)", "window.var_name", "A"),
    ("Which error occurs when you try to divide by zero?", "ZeroDivisionError", "MathError", "ValueError", "TypeError", "A"),
    ("How do you concatenate two strings `a` and `b`?", "a + b", "a.concat(b)", "a & b", "a, b", "A"),
    ("Which symbol is used for multiplication?", "*", "x", "X", ".", "A"),
    ("What is the index of the last element in list `lst`?", "-1", "len(lst)", "0", "lst.length", "A")
]

import random
random.seed(42) # For reproducibility if needed, but not strictly required. Let's just shuffle options to make them look distinct.

start_id = 3
for t in topics:
    q_text, op_a, op_b, op_c, op_d, corr = t
    
    # We want to randomly shuffle the options so 'A' is not always the correct one for our generated list.
    opts = [op_a, op_b, op_c, op_d]
    labels = ["A", "B", "C", "D"]
    corr_text = opts[labels.index(corr)]
    
    # We will shuffle opts, but we want to make sure we keep track of which one is the correct text
    shuffled = opts.copy()
    random.shuffle(shuffled)
    
    new_corr_label = labels[shuffled.index(corr_text)]
    
    q = {
        "id": start_id,
        "question": q_text,
        "options": {
            "A": shuffled[0],
            "B": shuffled[1],
            "C": shuffled[2],
            "D": shuffled[3]
        },
        "correct": new_corr_label,
        "explanations": {
            "A": "This is the correct answer." if new_corr_label == "A" else "This is incorrect.",
            "B": "This is the correct answer." if new_corr_label == "B" else "This is incorrect.",
            "C": "This is the correct answer." if new_corr_label == "C" else "This is incorrect.",
            "D": "This is the correct answer." if new_corr_label == "D" else "This is incorrect.",
        }
    }
    
    # Let's add a bit more flavor to explanations
    for k in ["A", "B", "C", "D"]:
        if k == new_corr_label:
            q["explanations"][k] = f"Correct. '{shuffled[labels.index(k)]}' is the right answer."
        else:
            q["explanations"][k] = f"Incorrect. '{shuffled[labels.index(k)]}' is not right."
            
    questions.append(q)
    start_id += 1

html_path = 'C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-easy-quiz-v3.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = json.dumps(questions, indent=4)
# The array in html has 'const questions = [' and ends with '];'
# We replace it
content = re.sub(r'const questions = \ufeff?\[.*?\];', 'const questions = ' + json_str + ';', content, flags=re.DOTALL)

# Replace titles
content = content.replace('Python Basics - Easy Quiz (v3)', 'Python Basics: Easy Quiz (Batch 2)')
content = content.replace('Python Basics: Easy Quiz (Version 3)', 'Python Basics: Easy Quiz (Batch 2)')

out_path = 'C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-easy-quiz-batch2.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Total questions generated: {len(questions)}")
print("HTML successfully saved.")
