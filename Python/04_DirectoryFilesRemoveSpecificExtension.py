import os
import shutil

def remove_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(".vtt"):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

# Example usage
remove_files("C:/Users/Yogesh/Downloads/Udemy_Become_a_Probability_and_Statistics_Master/03_Analyzing data/", ".vtt")
