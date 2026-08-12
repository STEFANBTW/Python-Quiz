import json
import re
import os

questions = [
    {
        "id": 1,
        "question": "Which of the following data types is immutable in Python?",
        "options": {
            "A": "List",
            "B": "Dictionary",
            "C": "Tuple",
            "D": "Set"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. Lists are mutable; their elements can be changed after creation.",
            "B": "Incorrect. Dictionaries are mutable; you can add, remove, or modify key-value pairs.",
            "C": "Correct! Tuples are immutable, meaning their elements cannot be changed after they are created.",
            "D": "Incorrect. Sets are mutable; you can add and remove elements."
        }
    },
    {
        "id": 2,
        "question": "How do you insert an element at a specific index in a list?",
        "options": {
            "A": "list.add(index, item)",
            "B": "list.insert(index, item)",
            "C": "list.append(index, item)",
            "D": "list.push(index, item)"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Python lists do not have an add() method.",
            "B": "Correct! The insert() method takes the index as the first argument and the item as the second.",
            "C": "Incorrect. append() only adds an item to the end of the list and takes exactly one argument.",
            "D": "Incorrect. push() is not a list method in Python."
        }
    },
    {
        "id": 3,
        "question": "What is the result of 9 // 2 in Python?",
        "options": {
            "A": "4.5",
            "B": "4",
            "C": "5",
            "D": "1"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. 4.5 is the result of standard division (9 / 2).",
            "B": "Correct! The // operator performs floor division, rounding down to the nearest whole integer.",
            "C": "Incorrect. The result is not rounded up.",
            "D": "Incorrect. 1 is the remainder, which would be the result of the modulo operator (9 % 2)."
        }
    },
    {
        "id": 4,
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "func",
            "B": "function",
            "C": "def",
            "D": "define"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. Python does not use 'func' for function definitions.",
            "B": "Incorrect. 'function' is used in languages like JavaScript, but not Python.",
            "C": "Correct! The 'def' keyword is used to define a function in Python.",
            "D": "Incorrect. 'define' is not a valid Python keyword."
        }
    },
    {
        "id": 5,
        "question": "What will print(type([])) output?",
        "options": {
            "A": "<class 'list'>",
            "B": "<class 'tuple'>",
            "C": "<class 'array'>",
            "D": "<class 'dict'>"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! Square brackets [] create a list in Python, so the type is list.",
            "B": "Incorrect. Tuples are created using parentheses ().",
            "C": "Incorrect. While similar to arrays in other languages, Python calls them lists.",
            "D": "Incorrect. Dictionaries are created using curly braces {}."
        }
    },
    {
        "id": 6,
        "question": "How do you start a single-line comment in Python?",
        "options": {
            "A": "// comment",
            "B": "/* comment",
            "C": "<!-- comment",
            "D": "# comment"
        },
        "correct": "D",
        "explanations": {
            "A": "Incorrect. This is used in C++, Java, and JavaScript.",
            "B": "Incorrect. This starts a multi-line comment in C-like languages.",
            "C": "Incorrect. This is an HTML comment.",
            "D": "Correct! The hash symbol (#) is used for single-line comments in Python."
        }
    },
    {
        "id": 7,
        "question": "What is the correct way to get the length of a string named 'text'?",
        "options": {
            "A": "text.length()",
            "B": "length(text)",
            "C": "len(text)",
            "D": "text.size"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. This syntax is used in Java or JavaScript, not Python.",
            "B": "Incorrect. The function is named 'len', not 'length'.",
            "C": "Correct! Python's built-in len() function returns the number of items in an object.",
            "D": "Incorrect. Python strings do not have a 'size' attribute."
        }
    },
    {
        "id": 8,
        "question": "Which operator is used to check if two values are equal?",
        "options": {
            "A": "=",
            "B": "==",
            "C": "===",
            "D": "equals"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. A single equals sign is the assignment operator.",
            "B": "Correct! The double equals sign (==) is the equality operator.",
            "C": "Incorrect. Python does not have a strict equality operator (===) like JavaScript does.",
            "D": "Incorrect. 'equals' is not a valid operator in Python."
        }
    },
    {
        "id": 9,
        "question": "What will be the output of: print(3 ** 2)?",
        "options": {
            "A": "6",
            "B": "9",
            "C": "5",
            "D": "32"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This would be the result of 3 * 2.",
            "B": "Correct! The ** operator performs exponentiation, so 3 ** 2 means 3 squared, which is 9.",
            "C": "Incorrect. This would be the result of 3 + 2.",
            "D": "Incorrect. The numbers are not concatenated."
        }
    },
    {
        "id": 10,
        "question": "How do you access the last element of a list named 'items'?",
        "options": {
            "A": "items[-1]",
            "B": "items.last()",
            "C": "items[len(items)]",
            "D": "items[0]"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! Python supports negative indexing, and -1 refers to the last element.",
            "B": "Incorrect. Lists do not have a 'last()' method.",
            "C": "Incorrect. This will raise an IndexError because list indices start at 0, so the last valid index is len(items) - 1.",
            "D": "Incorrect. This accesses the first element."
        }
    },
    {
        "id": 11,
        "question": "Which statement is used to exit a loop prematurely?",
        "options": {
            "A": "stop",
            "B": "exit",
            "C": "break",
            "D": "return"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. 'stop' is not a Python keyword.",
            "B": "Incorrect. 'exit()' terminates the entire program, not just the loop.",
            "C": "Correct! The 'break' statement terminates the current loop and resumes execution at the next statement.",
            "D": "Incorrect. 'return' exits a function, which may implicitly exit a loop if it's inside one, but its primary purpose is returning from functions."
        }
    },
    {
        "id": 12,
        "question": "What is the output of bool(\"\") in Python?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "None",
            "D": "Error"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Non-empty strings evaluate to True.",
            "B": "Correct! An empty string is considered 'falsy' in Python, so bool(\"\") evaluates to False.",
            "C": "Incorrect. The bool() function always returns a boolean value.",
            "D": "Incorrect. bool() can safely evaluate strings."
        }
    },
    {
        "id": 13,
        "question": "How do you convert a string '123' to an integer?",
        "options": {
            "A": "Integer('123')",
            "B": "int('123')",
            "C": "parse_int('123')",
            "D": "to_int('123')"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. The built-in function is lowercase 'int'.",
            "B": "Correct! The int() built-in function converts a number or string to an integer.",
            "C": "Incorrect. This looks like JavaScript's parseInt, which Python does not use.",
            "D": "Incorrect. This function does not exist in standard Python."
        }
    },
    {
        "id": 14,
        "question": "Which of the following will create an empty set?",
        "options": {
            "A": "set()",
            "B": "{}",
            "C": "[]",
            "D": "()"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! Calling set() without arguments creates an empty set.",
            "B": "Incorrect. {} creates an empty dictionary, not an empty set.",
            "C": "Incorrect. [] creates an empty list.",
            "D": "Incorrect. () creates an empty tuple."
        }
    },
    {
        "id": 15,
        "question": "What does the 'continue' statement do in a loop?",
        "options": {
            "A": "Exits the loop entirely.",
            "B": "Skips the rest of the current iteration and moves to the next.",
            "C": "Pauses the loop execution.",
            "D": "Restarts the loop from the beginning."
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This describes the 'break' statement.",
            "B": "Correct! 'continue' skips the remaining code in the current iteration and jumps to the loop's condition/next item.",
            "C": "Incorrect. Python does not have a built-in 'pause' statement for loops like this.",
            "D": "Incorrect. It moves to the next iteration, not the first iteration."
        }
    },
    {
        "id": 16,
        "question": "What is the correct syntax for a dictionary?",
        "options": {
            "A": "d = ['key' : 'value']",
            "B": "d = ('key' => 'value')",
            "C": "d = {'key': 'value'}",
            "D": "d = {key = 'value'}"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. Square brackets are for lists.",
            "B": "Incorrect. Parentheses are for tuples, and => is not used in Python.",
            "C": "Correct! Dictionaries use curly braces and separate keys and values with a colon.",
            "D": "Incorrect. The equals sign is not used for key-value assignment within a dictionary literal."
        }
    },
    {
        "id": 17,
        "question": "How do you check if a key exists in a dictionary named 'my_dict'?",
        "options": {
            "A": "if 'key' in my_dict:",
            "B": "if my_dict.has('key'):",
            "C": "if 'key' exists my_dict:",
            "D": "if my_dict.contains('key'):"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! The 'in' operator checks if the specified key exists in the dictionary.",
            "B": "Incorrect. Python dictionaries don't have a has() method (though Python 2 had has_key()).",
            "C": "Incorrect. 'exists' is not a valid Python keyword.",
            "D": "Incorrect. Dictionaries do not have a contains() method."
        }
    },
    {
        "id": 18,
        "question": "Which of these functions will read input from the user?",
        "options": {
            "A": "get_input()",
            "B": "read()",
            "C": "scan()",
            "D": "input()"
        },
        "correct": "D",
        "explanations": {
            "A": "Incorrect. No such built-in function exists.",
            "B": "Incorrect. read() is typically used for reading from files.",
            "C": "Incorrect. scan() is used in languages like C (scanf) or Go.",
            "D": "Correct! The input() function reads a line of text from the user via the console."
        }
    },
    {
        "id": 19,
        "question": "What is the result of 'a' + 'b' in Python?",
        "options": {
            "A": "ab",
            "B": "a b",
            "C": "Error",
            "D": "9798"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! The + operator concatenates (joins) strings together without adding any spaces.",
            "B": "Incorrect. No space is automatically inserted.",
            "C": "Incorrect. String concatenation is a valid operation.",
            "D": "Incorrect. Python does not implicitly convert characters to their ASCII values during addition."
        }
    },
    {
        "id": 20,
        "question": "How do you define a block of code in Python?",
        "options": {
            "A": "Using curly braces {}",
            "B": "Using parentheses ()",
            "C": "Using indentation",
            "D": "Using square brackets []"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. C, Java, and JS use {}, but Python does not.",
            "B": "Incorrect. Parentheses are for function calls and tuples.",
            "C": "Correct! Python strictly uses whitespace indentation to define code blocks (e.g., inside loops or functions).",
            "D": "Incorrect. Square brackets are for lists."
        }
    },
    {
        "id": 21,
        "question": "Which sequence of numbers is generated by range(3)?",
        "options": {
            "A": "1, 2, 3",
            "B": "0, 1, 2",
            "C": "0, 1, 2, 3",
            "D": "1, 2"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. range() starts at 0 by default.",
            "B": "Correct! range(n) generates numbers from 0 up to, but not including, n.",
            "C": "Incorrect. The end value is exclusive, so 3 is not included.",
            "D": "Incorrect. It starts from 0."
        }
    },
    {
        "id": 22,
        "question": "What is the purpose of the 'pass' statement in Python?",
        "options": {
            "A": "To terminate a program.",
            "B": "To skip an iteration in a loop.",
            "C": "To act as a null operation (placeholder).",
            "D": "To return from a function."
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. sys.exit() or raising an exception terminates a program.",
            "B": "Incorrect. That is the job of 'continue'.",
            "C": "Correct! 'pass' does nothing. It's often used as a placeholder where syntax requires a statement but no action is needed.",
            "D": "Incorrect. 'return' handles this."
        }
    },
    {
        "id": 23,
        "question": "What happens if you try to add a string and an integer (e.g., 'Age: ' + 25)?",
        "options": {
            "A": "It outputs 'Age: 25'",
            "B": "It throws a TypeError",
            "C": "It converts the string to an integer",
            "D": "It outputs 'Age: '"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Python does not implicitly convert integers to strings for concatenation.",
            "B": "Correct! Python is strongly typed and will raise a TypeError because it doesn't know how to add str and int directly.",
            "C": "Incorrect. 'Age: ' cannot be cast to an integer.",
            "D": "Incorrect. The operation halts with an error."
        }
    },
    {
        "id": 24,
        "question": "How do you format a string to include a variable 'x' easily in Python 3.6+?",
        "options": {
            "A": "f\"Value: {x}\"",
            "B": "\"Value: {x}\".format()",
            "C": "\"Value: %x\"",
            "D": "\"Value: \" & x"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! f-strings (formatted string literals) provide a concise and convenient way to embed expressions.",
            "B": "Incorrect. format() requires passing the variable: format(x=x) or similar.",
            "C": "Incorrect. % formatting exists, but %x is for hexadecimal, and %s is for string, plus it requires % x at the end.",
            "D": "Incorrect. The ampersand is not used for concatenation in Python."
        }
    },
    {
        "id": 25,
        "question": "Which symbol is used for the modulo operation (finding the remainder)?",
        "options": {
            "A": "//",
            "B": "/",
            "C": "%",
            "D": "**"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. // is for floor division.",
            "B": "Incorrect. / is for standard division.",
            "C": "Correct! The percent sign (%) is the modulo operator, returning the remainder of division.",
            "D": "Incorrect. ** is for exponentiation."
        }
    },
    {
        "id": 26,
        "question": "What is the output of 'hello'.upper()?",
        "options": {
            "A": "HELLO",
            "B": "Hello",
            "C": "hello",
            "D": "Error"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! The upper() method returns a new string where all lowercase characters are converted to uppercase.",
            "B": "Incorrect. This would be the result of 'hello'.capitalize().",
            "C": "Incorrect. The string is modified to uppercase.",
            "D": "Incorrect. This is a valid string method."
        }
    },
    {
        "id": 27,
        "question": "What data type is the result of 10 / 2?",
        "options": {
            "A": "int",
            "B": "float",
            "C": "string",
            "D": "list"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. While the mathematical result is a whole number, standard division (/) always returns a float.",
            "B": "Correct! In Python 3, standard division (/) always results in a float (5.0).",
            "C": "Incorrect. Math operations don't return strings.",
            "D": "Incorrect. Math operations don't return lists."
        }
    },
    {
        "id": 28,
        "question": "How do you remove a specific item from a list by its value?",
        "options": {
            "A": "list.delete('value')",
            "B": "list.remove('value')",
            "C": "list.pop('value')",
            "D": "list.discard('value')"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Lists do not have a delete() method.",
            "B": "Correct! The remove() method finds the first occurrence of the specified value and removes it.",
            "C": "Incorrect. pop() removes an item by its index, not its value.",
            "D": "Incorrect. discard() is a method used for sets, not lists."
        }
    },
    {
        "id": 29,
        "question": "Which of the following is NOT a valid Python keyword?",
        "options": {
            "A": "global",
            "B": "lambda",
            "C": "yield",
            "D": "foreach"
        },
        "correct": "D",
        "explanations": {
            "A": "Incorrect. 'global' is a keyword used to declare global variables inside functions.",
            "B": "Incorrect. 'lambda' is used for anonymous functions.",
            "C": "Incorrect. 'yield' is used in generator functions.",
            "D": "Correct! 'foreach' is not a keyword in Python (Python uses 'for x in y' syntax instead)."
        }
    },
    {
        "id": 30,
        "question": "What is the result of list('abc')?",
        "options": {
            "A": "['a', 'b', 'c']",
            "B": "['abc']",
            "C": "Error",
            "D": "(a, b, c)"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! The list() constructor iterates over the string, creating a list of its individual characters.",
            "B": "Incorrect. This would be created by ['abc'].",
            "C": "Incorrect. It's perfectly valid to pass an iterable like a string to list().",
            "D": "Incorrect. This resembles a tuple representation."
        }
    },
    {
        "id": 31,
        "question": "Which operator is used for logical 'NOT' in Python?",
        "options": {
            "A": "!",
            "B": "not",
            "C": "~",
            "D": "none"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. The exclamation mark is used in languages like C or Java.",
            "B": "Correct! The keyword 'not' is Python's logical negation operator.",
            "C": "Incorrect. The tilde (~) is the bitwise NOT operator.",
            "D": "Incorrect. 'none' is a value (None), not an operator."
        }
    },
    {
        "id": 32,
        "question": "What is the boolean evaluation of the number 0?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "None",
            "D": "Error"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Non-zero numbers evaluate to True.",
            "B": "Correct! In Python, numeric zero of any type (0, 0.0) is considered False in boolean contexts.",
            "C": "Incorrect. It evaluates to a boolean.",
            "D": "Incorrect. Python easily converts numbers to booleans."
        }
    },
    {
        "id": 33,
        "question": "How do you define a dictionary with a key 'name' and value 'Alice'?",
        "options": {
            "A": "{'name' = 'Alice'}",
            "B": "{'name': 'Alice'}",
            "C": "['name': 'Alice']",
            "D": "('name' => 'Alice')"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Dictionaries use colons to separate keys and values, not equals signs.",
            "B": "Correct! Curly braces and colons are the standard syntax for dictionaries.",
            "C": "Incorrect. Square brackets are for lists.",
            "D": "Incorrect. Parentheses are for tuples."
        }
    },
    {
        "id": 34,
        "question": "Which method is used to remove whitespace from the beginning and end of a string?",
        "options": {
            "A": "trim()",
            "B": "strip()",
            "C": "clean()",
            "D": "remove_space()"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This method is common in JavaScript and Java, but not standard Python.",
            "B": "Correct! The strip() method removes leading and trailing whitespace.",
            "C": "Incorrect. clean() is not a built-in string method.",
            "D": "Incorrect. This method does not exist."
        }
    },
    {
        "id": 35,
        "question": "What is the slice syntax to get the first three elements of a list 'my_list'?",
        "options": {
            "A": "my_list[1:3]",
            "B": "my_list[0:2]",
            "C": "my_list[:3]",
            "D": "my_list[3:]"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. This gets elements at index 1 and 2, missing the first element (index 0).",
            "B": "Incorrect. This gets elements at index 0 and 1 (only two elements).",
            "C": "Correct! Omitting the start index implies 0, and slicing up to 3 gets indices 0, 1, and 2.",
            "D": "Incorrect. This gets everything from index 3 to the end of the list."
        }
    },
    {
        "id": 36,
        "question": "What will 3 == '3' evaluate to in Python?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "Error",
            "D": "None"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Unlike JavaScript, Python does not coerce types for equality checks.",
            "B": "Correct! An integer and a string are strictly of different types, so they are never equal in Python.",
            "C": "Incorrect. Checking equality between different types is valid, it just returns False.",
            "D": "Incorrect. Equality operators always return a boolean."
        }
    },
    {
        "id": 37,
        "question": "What is the correct way to import the 'math' module?",
        "options": {
            "A": "include math",
            "B": "import math",
            "C": "using math",
            "D": "require math"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This is used in C/C++.",
            "B": "Correct! 'import' is the keyword used to bring modules into your Python script.",
            "C": "Incorrect. This is used in C#.",
            "D": "Incorrect. This is used in Node.js/Ruby."
        }
    },
    {
        "id": 38,
        "question": "Which of these is a valid multi-line string literal in Python?",
        "options": {
            "A": "/* Multi-line */",
            "B": "'''Multi-line'''",
            "C": "// Multi-line //",
            "D": "-- Multi-line --"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This is a comment in C/Java.",
            "B": "Correct! Triple quotes (either single ''' or double \"\"\") are used for multi-line strings in Python.",
            "C": "Incorrect. This is not valid syntax.",
            "D": "Incorrect. This is not valid syntax (resembles SQL comments)."
        }
    },
    {
        "id": 39,
        "question": "If x = [1, 2, 3], what does x.pop() return?",
        "options": {
            "A": "1",
            "B": "2",
            "C": "3",
            "D": "[1, 2]"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. pop(0) would return 1.",
            "B": "Incorrect. pop(1) would return 2.",
            "C": "Correct! By default, pop() removes and returns the last item in the list.",
            "D": "Incorrect. That is what the list 'x' looks like after the operation, but pop() returns the removed element itself."
        }
    },
    {
        "id": 40,
        "question": "What does the method string.replace('a', 'b') do?",
        "options": {
            "A": "Replaces the first 'a' with 'b'",
            "B": "Replaces all occurrences of 'a' with 'b'",
            "C": "Throws an error if 'a' is not found",
            "D": "Replaces 'b' with 'a'"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. By default, it replaces all occurrences. You would need a third argument like replace('a', 'b', 1) to replace only the first.",
            "B": "Correct! Unless specified otherwise, replace() swaps every instance of the old substring with the new one.",
            "C": "Incorrect. If 'a' is not found, it simply returns the original string unchanged.",
            "D": "Incorrect. The first argument is the target to be replaced."
        }
    },
    {
        "id": 41,
        "question": "Which function finds the largest number in a list?",
        "options": {
            "A": "largest()",
            "B": "maximum()",
            "C": "max()",
            "D": "top()"
        },
        "correct": "C",
        "explanations": {
            "A": "Incorrect. This function doesn't exist.",
            "B": "Incorrect. It's abbreviated in Python.",
            "C": "Correct! The built-in max() function returns the largest item in an iterable.",
            "D": "Incorrect. This is not a standard built-in function."
        }
    },
    {
        "id": 42,
        "question": "What is the output of 'Hello' * 3?",
        "options": {
            "A": "Hello Hello Hello",
            "B": "HelloHelloHello",
            "C": "Error",
            "D": "Hello3"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. The multiplication operator does not automatically add spaces.",
            "B": "Correct! Using the multiplication operator on a string repeats it that many times consecutively.",
            "C": "Incorrect. String multiplication by an integer is fully supported.",
            "D": "Incorrect. It doesn't concatenate the number."
        }
    },
    {
        "id": 43,
        "question": "How do you add a new key-value pair to an existing dictionary 'd'?",
        "options": {
            "A": "d.add('key', 'value')",
            "B": "d['key'] = 'value'",
            "C": "d.insert('key', 'value')",
            "D": "d.push('key', 'value')"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. Sets have an add() method, but dictionaries do not.",
            "B": "Correct! Assigning a value to a new key directly creates the key-value pair in the dictionary.",
            "C": "Incorrect. Lists have insert(), not dictionaries.",
            "D": "Incorrect. push() is not a Python dictionary method."
        }
    },
    {
        "id": 44,
        "question": "Which statement correctly creates a function named 'greet' that takes a parameter 'name'?",
        "options": {
            "A": "def greet(name):",
            "B": "function greet(name):",
            "C": "create greet(name):",
            "D": "def greet name:"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! You use the 'def' keyword, followed by the function name, parameters in parentheses, and a colon.",
            "B": "Incorrect. Python uses 'def', not 'function'.",
            "C": "Incorrect. 'create' is not a keyword.",
            "D": "Incorrect. Parentheses are required around parameters."
        }
    },
    {
        "id": 45,
        "question": "What will round(3.14159, 2) output?",
        "options": {
            "A": "3.1",
            "B": "3.14",
            "C": "3.15",
            "D": "3"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. That would be rounding to 1 decimal place.",
            "B": "Correct! The round() function rounds the number to the specified number of decimal places (2 in this case).",
            "C": "Incorrect. The third decimal digit is 1, so it rounds down, keeping the 4 as is.",
            "D": "Incorrect. That would be rounding to 0 decimal places."
        }
    },
    {
        "id": 46,
        "question": "Which operator is used to test if a value is NOT in a list?",
        "options": {
            "A": "not in",
            "B": "out of",
            "C": "not_in",
            "D": "!in"
        },
        "correct": "A",
        "explanations": {
            "A": "Correct! 'not in' is the standard membership operator to check if a value is absent from a sequence.",
            "B": "Incorrect. This is not valid syntax.",
            "C": "Incorrect. There is no underscore.",
            "D": "Incorrect. Python uses English words for these operators."
        }
    },
    {
        "id": 47,
        "question": "What does a dictionary's keys() method return?",
        "options": {
            "A": "A list of values",
            "B": "A view object containing all the keys",
            "C": "A tuple of key-value pairs",
            "D": "The number of keys"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. The values() method does this.",
            "B": "Correct! It returns a dict_keys object, which is a view of all the keys in the dictionary.",
            "C": "Incorrect. The items() method returns pairs.",
            "D": "Incorrect. The len() function gives the number of keys."
        }
    },
    {
        "id": 48,
        "question": "Which of these is used to handle exceptions (errors) in Python?",
        "options": {
            "A": "try...catch",
            "B": "try...except",
            "C": "do...except",
            "D": "catch...finally"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. This syntax is used in JavaScript, Java, and C++.",
            "B": "Correct! Python uses 'try' blocks to test code and 'except' blocks to handle any errors that occur.",
            "C": "Incorrect. This is not valid syntax.",
            "D": "Incorrect. It must start with a 'try' block."
        }
    },
    {
        "id": 49,
        "question": "What is the output of bool(1)?",
        "options": {
            "A": "False",
            "B": "True",
            "C": "None",
            "D": "1"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. 0 evaluates to False.",
            "B": "Correct! Any non-zero number evaluates to True in Python.",
            "C": "Incorrect. bool() always returns a boolean.",
            "D": "Incorrect. The type is cast to a boolean."
        }
    },
    {
        "id": 50,
        "question": "How do you check the type of a variable 'x'?",
        "options": {
            "A": "typeof(x)",
            "B": "type(x)",
            "C": "type_of(x)",
            "D": "check_type(x)"
        },
        "correct": "B",
        "explanations": {
            "A": "Incorrect. 'typeof' is used in JavaScript.",
            "B": "Correct! The built-in type() function returns the type of the given object.",
            "C": "Incorrect. This function does not exist.",
            "D": "Incorrect. This function does not exist."
        }
    }
]

def main():
    path_in = "C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-easy-quiz-v3.html"
    path_out = "C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-easy-quiz-batch1.html"

    with open(path_in, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title in <title> and <div class="quiz-title">
    # The title inside <title> might be: <title>Python Basics - Easy Quiz (v3)</title>
    content = re.sub(r'<title>.*?</title>', '<title>Python Basics: Easy Quiz (Batch 1)</title>', content)
    
    # The div title might be: <span>🐍</span> Python Basics: Easy Quiz (Version 3)
    # Let's just find and replace "Python Basics: Easy Quiz (Version 3)" or "Python Basics - Easy Quiz (v3)"
    # A robust regex for the div:
    content = re.sub(r'(<div class="quiz-title">[\s\S]*?<span>.*?</span>)\s*.*?(?=\n\s*</div>)', r'\1 Python Basics: Easy Quiz (Batch 1)', content)

    # 2. Replace the questions array
    # Look for "const questions = [" or something similar.
    # The original array is: const questions = \uFEFF[ ... ];
    # We can split on "const questions = " and then find the next ";"
    match = re.search(r'const questions\s*=\s*(.*?\])\s*;', content, re.DOTALL)
    if not match:
        # try without strict ending just in case
        match = re.search(r'const questions\s*=\s*\uFEFF?\[.*?\]\s*;', content, re.DOTALL)
        
    if match:
        json_str = json.dumps(questions, indent=4)
        new_js = f"const questions = {json_str};"
        # we can replace the entire matched string
        content = content.replace(match.group(0), new_js)
    else:
        print("Could not find questions array with regex, trying manual split")
        parts = content.split("const questions =")
        if len(parts) > 1:
            part2 = parts[1]
            end_idx = part2.find(";")
            json_str = json.dumps(questions, indent=4)
            new_part2 = f" {json_str};\n" + part2[end_idx+1:]
            content = parts[0] + "const questions =" + new_part2
        else:
            print("Failed to replace questions!")

    with open(path_out, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Created {path_out} successfully with {len(questions)} questions.")

if __name__ == "__main__":
    main()
