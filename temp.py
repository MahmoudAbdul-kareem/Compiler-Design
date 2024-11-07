import re
import argparse
regular_exprisions = [
    ('COMMENT',  r'//.*|/\*.*?\*/'),   # Comments (single-line and multi-line)
    ('NUMBER',   r'\d+(\.\d*)?'),      # Integer or float
    ('KEYWORD',  r'\b(main|const|int|if|else|return)\b'),  # Keywords
    ('ID',       r'[A-Za-z_]\w*'),     # Identifiers (variable names)
    ('OPERATOR', r'[+\-*/=<>!&|^%]'),  # Operators
    ('PUNCTUATION', r'[;,\{\}\(\)\[\]]'), # Punctuation marks
    ('WHITESPACE', r'\s+'),            # Spaces, tabs, newlines
    ('MISMATCH', r'.')                 # Any other character (used for errors) 
]

lexem_pattern = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in regular_exprisions)

def Lexical_analyzer(code):
    
    for mo in re.finditer(lexem_pattern, code):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'WHITESPACE':
            continue
        if kind == 'COMMENT':
            value = value[2:]
        
        yield (kind, value)

def main(): 
    parser = argparse.ArgumentParser(description='Lexical Analyzer for C code.') 
    parser.add_argument('filename', type=str, help='The code file') 
    args = parser.parse_args() 
    with open(args.filename, 'r') as file: code = file.read()
    for token in Lexical_analyzer(code): 
        print(f'TOKEN TYPE: {token[0]}, TOKEN VALUE: {token[1]}') 
if __name__ == "__main__": 
    main()