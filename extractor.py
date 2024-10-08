from bs4 import BeautifulSoup
import os
import re
import uuid

# Function to generate a new unique class name
def generate_unique_class_name(original_name):
    return f"{original_name}_{uuid.uuid4().hex[:6]}"

# Load your HTML file
input_file = 'src/index.html'
output_css_file = 'dist/extracted.css'
output_js_file = 'dist/extracted.js'

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()  # Read the entire file

# Create BeautifulSoup object
soup = BeautifulSoup(content, 'html.parser')

css_contents = []
js_contents = []

# Find and extract all <style> and <script> tags
for style_tag in soup.find_all('style'):
    css_contents.append(style_tag.string)
    style_tag.decompose()  # Remove the <style> tag from the HTML

for script_tag in soup.find_all('script'):
    js_contents.append(script_tag.string)
    script_tag.decompose()  # Remove the <script> tag from the HTML

# Process inline styles and update classes
for tag in soup.find_all(True):  # Find all tags
    # Process inline styles
    inline_styles = tag.get('style')
    if inline_styles:
        # Generate a new class name
        new_class_name = generate_unique_class_name('inline')
        css_contents.append(f".{new_class_name} {{{inline_styles}}}")
        tag['class'] = tag.get('class', []) + [new_class_name]  # Add new class to the tag
        del tag['style']  # Remove the inline style

    # Rename other classes
    if tag.get('class'):
        for i, class_name in enumerate(tag['class']):
            tag['class'][i] = generate_unique_class_name(class_name)

# Write extracted CSS to file
os.makedirs('dist', exist_ok=True)  # Create dist directory if it doesn't exist
if css_contents:
    with open(output_css_file, 'w', encoding='utf-8') as css_file:
        for css in css_contents:
            css_file.write(css + '\n')
    print(f'CSS extracted to {output_css_file}')
else:
    print('No CSS found to extract.')

# Write extracted JavaScript to file
if js_contents:
    with open(output_js_file, 'w', encoding='utf-8') as js_file:
        for js in js_contents:
            js_file.write(js + '\n')
    print(f'JavaScript extracted to {output_js_file}')
else:
    print('No JavaScript found to extract.')

# Write the modified HTML back to the file
with open(input_file, 'w', encoding='utf-8') as file:
    file.write(str(soup))
print(f'Inline styles and <style>/<script> tags have been removed from {input_file}.')
