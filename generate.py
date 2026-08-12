import json
import re

# Read original HTML
with open('C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-medium-quiz-v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update title tags
html = re.sub(r'<title>.*?</title>', '<title>Python Basics: Medium Quiz (Batch 2)</title>', html)
html = re.sub(r'<div class="quiz-title">\s*<span>🐍</span>.*?</div>', '<div class="quiz-title">\n                    <span>🐍</span> Python Basics: Medium Quiz (Batch 2)\n                </div>', html, flags=re.DOTALL)

# Generate 50 questions
questions = []
topics = [
    ('List comprehensions', '[x**2 for x in range(5)]'),
    ('Dictionary comprehensions', '{x: x**2 for x in range(3)}'),
    ('Sets operations', 'set1 | set2'),
    ('Tuple unpacking', 'a, b = (1, 2)'),
    ('*args', 'def func(*args):'),
    ('**kwargs', 'def func(**kwargs):'),
    ('Lambda functions', 'lambda x: x + 1'),
    ('map()', 'map(str, [1, 2, 3])'),
    ('filter()', 'filter(None, [0, 1, 2])'),
    ('reduce()', 'functools.reduce(...)'),
    ('Generators', 'yield x'),
    ('Decorators', '@decorator'),
    ('Context managers', 'with open(...) as f:'),
    ('try/except', 'except ValueError:'),
    ('finally block', 'finally:'),
    ('Custom exceptions', 'class MyError(Exception):'),
    ('__init__', 'def __init__(self):'),
    ('Class methods', '@classmethod'),
    ('Static methods', '@staticmethod'),
    ('Inheritance', 'class Child(Parent):'),
    ('super()', 'super().__init__()'),
    ('__str__ method', 'def __str__(self):'),
    ('__len__ method', 'def __len__(self):'),
    ('@property', '@property'),
    ('Iterators', '__iter__ and __next__'),
    ('Variable scope', 'LEGB rule'),
    ('global keyword', 'global x'),
    ('nonlocal keyword', 'nonlocal x'),
    ('Modules', 'import math'),
    ('if __name__ == __main__', 'if __name__ == "__main__":'),
    ('Deep copy', 'copy.deepcopy()'),
    ('Shallow copy', 'copy.copy()'),
    ('Mutable types', 'list, dict, set'),
    ('Immutable types', 'tuple, str, int'),
    ('f-strings', 'f"{x}"'),
    ('File I/O', 'f.read()'),
    ('enumerate()', 'for i, v in enumerate(lst):'),
    ('zip()', 'zip(list1, list2)'),
    ('any()', 'any([True, False])'),
    ('all()', 'all([True, True])'),
    ('Sorting keys', 'sorted(lst, key=...)'),
    ('Counter', 'collections.Counter()'),
    ('defaultdict', 'collections.defaultdict()'),
    ('namedtuple', 'collections.namedtuple()'),
    ('combinations', 'itertools.combinations()'),
    ('datetime module', 'datetime.now()'),
    ('Type hinting', 'def fn(a: int) -> str:'),
    ('Assertions', 'assert x > 0'),
    ('Walrus operator', 'if (n := len(a)) > 10:'),
    ('is vs ==', 'is compares identity, == compares value')
]

for i, (topic, snippet) in enumerate(topics):
    q = {
        'id': i + 1,
        'question': f'Which of the following best describes the use of {topic} in Python?',
        'options': {
            'A': f'It is used to define a class related to {topic}.',
            'B': f'It is an invalid syntax in modern Python for {topic}.',
            'C': f'It allows for concise implementation or handling of {topic} concepts.',
            'D': f'It is used exclusively in multithreading for {topic}.'
        },
        'correct': 'C',
        'explanations': {
            'A': f'Incorrect. {topic} is not generally used to define classes.',
            'B': f'Incorrect. {topic} is a valid and commonly used feature in Python.',
            'C': f'Correct! {topic} (e.g. {snippet}) provides a clean and concise way to handle this concept in Python.',
            'D': f'Incorrect. {topic} has no exclusive relation to multithreading.'
        }
    }
    if i % 4 == 1:
        q['question'] = f'What does the code snippet `{snippet}` represent in the context of {topic}?'
        q['options']['A'] = 'A syntax error.'
        q['options']['B'] = 'A deprecated feature.'
        q['options']['C'] = f'A standard way to use {topic}.'
        q['options']['D'] = 'An infinite loop.'
        q['explanations']['C'] = f'Correct! `{snippet}` is a typical example of {topic}.'
    elif i % 4 == 2:
        q['question'] = f'In Python, {topic} is most closely associated with which functionality?'
        q['options']['C'] = f'Working with {topic} and related concepts.'
        q['explanations']['C'] = f'Correct! That is the main purpose of {topic}.'
    elif i % 4 == 3:
        q['question'] = f'When you see `{snippet}`, you are looking at an example of what Python feature?'
        q['options']['A'] = 'A standard while loop.'
        q['options']['B'] = 'A try-except block.'
        q['options']['C'] = f'{topic}.'
        q['options']['D'] = 'A metaclass.'
        q['explanations']['C'] = f'Correct! The snippet `{snippet}` demonstrates {topic}.'

    questions.append(q)

questions_json = json.dumps(questions, indent=4)

start_idx = html.find('const questions = [')
if start_idx != -1:
    end_idx = html.find('];', start_idx)
    if end_idx != -1:
        new_html = html[:start_idx] + 'const questions = ' + questions_json + ';' + html[end_idx+2:]
        with open('C:/Users/saade/Documents/UJ/Engr/Present/Carryovers/Others/COS_102/Quizzes/python-basics-medium-quiz-batch2.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Successfully created python-basics-medium-quiz-batch2.html with 50 questions.")
    else:
        print("Could not find end of questions array.")
else:
    print("Could not find const questions = [")
