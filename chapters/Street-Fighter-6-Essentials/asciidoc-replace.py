import re
import sys

def parse_asciidoc(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace('[!info]', '**Info**')
    content = content.replace('[!warning]', '**Warning**')
    content = content.replace('[!tip]', '**Tip**')
    content = content.replace('[!note]', '**Note**')
    content = content.replace('[!caution]', '**Caution**')
    content = content.replace('[!cite]', ':')


    example_pattern = r'____\n\[!example\] ([^\n]+)\n((?:(?!____)[\s\S])+?)\n____'
    example_replacement = r'.\1\n====\n\2\n===='

    content = re.sub(example_pattern, example_replacement, content)

    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parse_asciidoc.py <asciidoc_file_path>")
    else:
        file_path = sys.argv[1]
        parse_asciidoc(file_path)
