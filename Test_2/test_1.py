#补充缺失的代码
def print_directory_contents(s_path):
    import os
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path,s_child)
        #print(s_child_path)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)

if __name__ == '__main__':
    print_directory_contents(r'C:\Users\hp\Desktop\project')