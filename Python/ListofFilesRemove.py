import os
import shutil

def remove_files(directory, extension):
    for filename in os.listdir(directory):
        if filename == "en.vtt":
            break
        if filename.endswith(("de.vtt","es.vtt","fr.vtt","id.vtt","it.vtt","pl.vtt","pt.vtt","ro.vtt","th.vtt")):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                if filename == "en.vtt":
                    break
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

# Example usage
file_list = ["de.vtt","es.vtt","fr.vtt","id.vtt","it.vtt","pl.vtt","pt.vtt","ro.vtt","th.vtt"]
remove_files("C:/Users/Yogesh/Downloads/Udemy_Become_a_Probability_and_Statistics_Master/09_Regression/", file_list)