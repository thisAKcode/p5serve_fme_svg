import re
import html
import glob
from html_components import html_beginning, html_ending

"""
This script reads an embedded Python script from an FME file, decodes it, and writes the decoded script to an HTML file.a
Workflow:
    1. Load text from the specified file.
    2. Use a regular expression to extract the encoded Python script from the XML content.
    3. Decode the extracted script by unescaping HTML entities.
    4. Replace placeholder-like markers with actual code characters.
    5. Output the decoded Python script to the console.
    6. Write the decoded script to a new HTML file.
"""


# Load text from file and store it as a variable
# First file with .fmw extension in the actual directory
file_path = glob.glob(r'./*.fmw')[0]
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Regular expression to extract the desired content included between PYTHONSOURCE AND 
matches = re.findall(r'<XFORM_PARM PARM_NAME="PYTHONSOURCE" PARM_VALUE="(.*?)"/>', file_content)
matches_valid = [i for i in matches if '#main_script' in i]
# Extracted encoded Python source as a string
encoded_xml = matches_valid[0]

print('#main_script' in encoded_xml)
# Unescaping the encoded entities
decoded_script = html.unescape(encoded_xml)

# Replacing placeholder-like markers with actual string representations
decoded_script = decoded_script.replace("<space>", " ").replace("<lf>", "\n")
decoded_script = decoded_script.replace("<quote>", "\"").replace("<apos>", "'")
decoded_script = decoded_script.replace("<openparen>", "(").replace("<closeparen>", ")")
decoded_script = decoded_script.replace("<comma>", ",")
decoded_script = decoded_script.replace("<openbracket>", "[").replace("<closebracket>", "]")
decoded_script = decoded_script.replace("<solidus>", "/").replace("<opencurly>", "{")
decoded_script = decoded_script.replace("<closecurly>", "}").replace("<colon>", ":")
decoded_script = decoded_script.replace("<semicolon>", ";").replace("<equals>", "=")
decoded_script = decoded_script.replace("<ampersand>", "&").replace("<percent>", "%")
decoded_script = decoded_script.replace("<dollar>", "$").replace("<hash>", "#")
decoded_script = decoded_script.replace("<at>", "@").replace("<exclamation>", "!")
decoded_script = decoded_script.replace("<question>", "?").replace("<pipe>", "|")
decoded_script = decoded_script.replace("<backslash>", "\\").replace("<caret>", "^")
decoded_script = decoded_script.replace("<tilde>", "~").replace("<underscore>", "_")
decoded_script = decoded_script.replace("<plus>", "+").replace("<minus>", "-")
decoded_script = decoded_script.replace("<asterisk>", "*").replace("<slash>", "/")
decoded_script = decoded_script.replace("<lessthan>", "<").replace("<greaterthan>", ">")
decoded_script = decoded_script.replace("<dot>", ".").replace("<colon>", ":")
decoded_script = decoded_script.replace("<semicolon>", ";").replace("<equals>", "=")

# Output the decoded Python script

# wrap code in tags
actual_code = f""" 
  <code class="language-python" id="code-block">
{decoded_script}
  </code>
"""

complete_index =html_beginning +actual_code + html_ending
# Write the decoded script to a new HTML file
output_file_path = './index.html'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(complete_index)
    
print(f"HTML content written to index.html")