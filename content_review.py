import os
import html_components # import constant_footer, constant_header


names_to_skip = ['xyz123','xyz123_offline']
file_path = 'C:/p5serve_fme_svg/index.html' 
with open(file_path, 'r') as file:
    content = file.read()

my_directory = f'c:/p5serve_fme_svg/sketches' 
entries = os.listdir(my_directory)
relevant_entries = [i for i in entries if not i in names_to_skip]

links_to_index = '\n'.join([f'        <div id="item"><a href="sketches/{i}/index.html"> {i}</a></div>' 
                            for i in relevant_entries
                            ]
                           )
main_div = f'''
<section id="content" class="body">
    <div id="container">
{links_to_index}
    </div>
</section>
'''

result_html_content = f'''
{html_components.constant_header}
{main_div}
{html_components.constant_footer}
'''

# Define the file name you want to write to
file_name = "index.html"

# Open the file in write mode and write the HTML content
with open(file_name, "w") as file:
    file.write(result_html_content)

print(f"HTML content written to {file_name}")