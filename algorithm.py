import re
import svgwrite

def html_to_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_string = file.read()
            return html_string
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def extract_text_between_tags(html_string):
    # Use regular expressions to extract text between '>' and '<'
    pattern = r'>([^<]+)<'
    matches = re.findall(pattern, html_string)
    return ''.join(matches)

file_path = './input.html'
html_string = html_to_string(file_path)

if html_string:
    output_string = extract_text_between_tags(html_string)
    # Replace '&lt;' with '<' and '&gt;' with '>'
    final_string = output_string.replace('&lt;', '<').replace('&gt;', '>')

    print("Final String (text between '>' and '<' with replacements):")
    print(final_string)
    
    output = open("output.svg", "w")
    output.write(final_string)
    output.close()
    print("SVG file saved as output.svg in the root directory.")