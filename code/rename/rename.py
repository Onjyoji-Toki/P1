import os

def rename_down(loop,start_time):
    bin_directory_old = r"C:\Users\kyoto\WaveDump"
    bin_directory_new = r"C:\Users\kyoto\WaveDump\down" + str(start_time) 
    old_file_path = os.path.join(bin_directory_old, "wave0.txt")
    new_file_path = os.path.join(bin_directory_new, str(start_time) + "down" + str(loop)+ ".txt")
    os.rename(old_file_path, new_file_path)    

def rename_up(loop,start_time):
    bin_directory_old = r"C:\Users\kyoto\WaveDump"
    bin_directory_new = r"C:\Users\kyoto\WaveDump\up" + str(start_time) 
    old_file_path = os.path.join(bin_directory_old, "wave0.txt")
    new_file_path = os.path.join(bin_directory_new, str(start_time) + "up" + str(loop)+ ".txt")
    os.rename(old_file_path, new_file_path)

def make_file(start_time) :
    right_filepath = r"C:\Users\kyoto\WaveDump\down" + str(start_time) 
    left_filepath = r"C:\Users\kyoto\WaveDump\up" + str(start_time) 
    os.makedirs(right_filepath)
    os.makedirs(left_filepath) 