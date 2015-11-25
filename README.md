# audit-reqs
The online degree audit tool lists a bunch of links to course descriptions but it's impossible to tell what classes they are unless you click every single link. This tool turns the list of links into a list of course names.

![example](/art/screenshot.png?raw=true "Example")

## How to use
1. Download courses.py to somewhere on your computer.
2. Replace the first line in courses.py with your list of requirements from the degree audit. Make sure that each requirement is separated by a single space.
3. Open Terminal and make sure you have Python installed (Linux and Mac users have python installed by default).
4. Navigate to where you downloaded courses.py
5. Type "python courses.py output", change "output" to whatever file you want to save the list of courses to. 
6. Wait while it does its thing. There's even a nice progress bar and everything.
7. Once it's done, you can open up the output file and see your list of classes.
