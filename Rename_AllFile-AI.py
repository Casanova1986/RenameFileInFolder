import os

def rename_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if ".atlas.prefab" in file:
                old_path = os.path.join(root, file)
                new_file = file.replace(".atlas.prefab", ".atlas.txt")
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                print(f'Renamed: {old_path} -> {new_path}')
            if ".skel.prefab" in file:
                old_path_ske = os.path.join(root, file)
                new_file_ske = file.replace(".skel.prefab", ".skel.bytes")
                new_path_ske = os.path.join(root, new_file_ske)
                os.rename(old_path_ske, new_path_ske)
                print(f'Renamed: {old_path_ske} -> {new_path_ske}')


if __name__ == "__main__":
    directory = input("Nhập đường dẫn thư mục: ").strip()
    if os.path.isdir(directory):
        rename_files(directory)
        print("Hoàn thành!")
    else:
        print("Thư mục không tồn tại.")
