import os
import shutil

def remove_files(directory, extension):
    flag = os.path.isabs(directory)
    if flag == False:
        directory = os.path.abspath(directory)
    exists = os.path.isdir(directory)
    if exists:
        for foldername, subfolder, filenames in os.walk(directory):
            pass
            for subf in subfolder:
                pass
            for filename in filenames:
                if filename == "en.vtt":
                    break
                if filename.endswith(("de.vtt","es.vtt","fr.vtt","id.vtt","it.vtt","pl.vtt","pt.vtt","ro.vtt","th.vtt")):
                    filename = os.path.join(foldername, filename)
                    try:
                        if os.path.isfile(filename) or os.path.islink(filename):
                            os.unlink(filename)
                        if filename == "en.vtt":
                            break
                        elif os.path.isdir(filename):
                            shutil.rmtree(filename)
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (filename, e))

# Example usage
file_list = ["de.vtt","es.vtt","fr.vtt","id.vtt","it.vtt","pl.vtt","pt.vtt","ro.vtt","th.vtt"]
remove_files("C:/Users/Yogesh/Downloads/Udemy_Become_a_Probability_and_Statistics_Master/", file_list)