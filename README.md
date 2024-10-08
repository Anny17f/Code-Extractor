# HTML Code Extractor

## Overview

The **HTML Code Extractor** is a Python-based script that scans an HTML file containing embedded CSS and JavaScript code, extracts these components, and generates separate external files for the CSS and JavaScript. This process helps streamline your web project by separating concerns and improving maintainability. After running this script, your original HTML file will be modified to link to these new external files, enhancing its readability and organization.

## Features

- **Scans HTML files**: Detects and reads embedded CSS and JavaScript in a given HTML file.
- **Extracts CSS and JavaScript**: Separates CSS and JavaScript into individual external files.
- **Modifies HTML**: Replaces the inline CSS and JavaScript in the HTML file with proper `<link>` and `<script>` tags to reference the new external files.
- **Automated File Generation**: Automatically creates the external `.css` and `.js` files in the specified directory.

## Project Structure

Here’s an overview of the structure after running the script:

project/
│
├── extracted/
│   ├── styles.css       # Contains the extracted CSS
│   ├── scripts.js       # Contains the extracted JavaScript
│
├── modified/
│   └── index.html       # The updated HTML with references to external files
│
└── script/
    └── extractor.py     # The Python script that handles the extraction

## Requirements

This project runs on Python 3.x and does not require any external dependencies. However, you can install libraries such as `beautifulsoup4` for more robust HTML parsing if necessary.

## Installation

1. **Clone the repository**:

   git clone https://github.com/Anny17f/Code-Extractor.git
   cd html-code-extractor

2. **Set up the environment** (optional):
   If you’re using a virtual environment for Python:

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**:
   If you're using BeautifulSoup for parsing (optional):

   pip install beautifulsoup4

## Usage

### Step-by-step guide

1. **Place the HTML file**: Ensure the HTML file containing inline CSS and JavaScript is in the correct directory. The script assumes the file is named `index.html` by default, but you can modify the code to handle different file names.

2. **Run the script**

   python extractor.py <path_to_html_file>

   - If the HTML file is named `index.html`, no additional argument is needed:

     python extractor.py

3. **Output**
   - After running the script, two external files will be generated:
     - `styles.css`: Contains all extracted CSS.
     - `scripts.js`: Contains all extracted JavaScript.
   - The HTML file will be modified to:
     - Replace the embedded `<style>` block with a `<link>` to `styles.css`.
     - Replace the inline `<script>` block with a `<script>` tag referencing `scripts.js`.

### Example

Here’s an example of how the extraction works.

#### Before running the script (index.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Web Page</title>
    <style>
        body {
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <script>
        console.log("Page loaded");
    </script>
</body>
</html>
```

#### After running the script (modified index.html):

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Web Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to My Website</h1>
    <script src="scripts.js"></script>
</body>
</html>
```

#### styles.css:

```css
body {
    background-color: #f0f0f0;
}
h1 {
    color: #333;
}
```

#### scripts.js:
```javascript
console.log("Page loaded");
```

## How It Works

1. **Reading the HTML**: The script reads the provided HTML file and searches for `<style>` and `<script>` tags. These tags are assumed to contain inline CSS and JavaScript.
   
2. **Extracting the Code**:
   - CSS between the `<style>` tags is written to a new `.css` file.
   - JavaScript between the `<script>` tags is written to a new `.js` file.

3. **Modifying the HTML**: The script then removes the inline code from the original HTML and replaces it with links to the external `.css` and `.js` files.

4. **Saving the Changes**: The modified HTML file is saved in the `modified/` folder, while the CSS and JavaScript files are saved in the `extracted/` folder.

## Customization

You can customize the script to:
- Handle multiple HTML files in a directory.
- Use different naming conventions for the external files (e.g., `main.css`, `app.js`).
- Enhance error handling (e.g., when no `<style>` or `<script>` tags are found).
- Automatically prettify or minify the extracted files using additional libraries like `cssbeautifier` or `jsmin`.

## Future Improvements

Some ideas for expanding this project:
- Support for external libraries to better handle complex HTML structures.
- Adding unit tests for improved robustness.
- Configurable options for output paths and file naming conventions.

## Contributing

Contributions are welcome! Feel free to submit pull requests, report bugs, or suggest features.
