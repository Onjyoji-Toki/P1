import os
def main(loop):
    #測定前にaaaの部分に日付などを入力
    bin_directory = r'C:\Program Files\CAEN\Digitizers\WaveDump'
    old_file_path = os.path.join(bin_directory, "wave2.txt")
    new_file_path = os.path.join(bin_directory, 'aaa_right' + str(loop) + '.txt')
    os.rename(old_file_path, new_file_path)

    if __name__ == '__main__':
    main()