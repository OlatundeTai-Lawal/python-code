"""
This piece of code is to write to a file, read from a file and append to another file
"""
with open ('file1.txt', 'w') as f1:
    f1.write('first chapter of Alice in wonderland\n')
    f1.write('Enjoy the story\n')
    f1.write('See you in chaptertwo\n')

def copy(story, story_2):
    with open ('file1.txt', 'r') as f1,  open ('file2.txt', 'a') as f2:
        for line in f1:
            f2.write(line)
            
f1= "file1.txt"
f2 = "file2.txt"
copy(f1, f2) 
