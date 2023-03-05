import os

# specify the folder directory containing text files
folder_path = '/path/to/folder'

# specify the desired words to search for
desired_words = ['word1', 'word2', 'word3']

# iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # read the contents of the file
        with open(file_path, 'r') as f:
            file_contents = f.read()
            
        # check if the desired words are present in the file contents
        for word in desired_words:
            if word in file_contents:
                print(f"{word} found in {filename}")
