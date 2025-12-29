import os

def process_files(root_folder):
    # Định nghĩa chuỗi bytes cần tìm và thay thế
    # bytes('61t8', 'ascii') tương đương b'61t8'
    search_pattern = b'61t8'
    replace_pattern = b'61f1'
    
    # Giới hạn đọc 1000 bytes đầu
    chunk_size = 1000
    
    count_modified = 0
    count_errors = 0

    print(f"Đang bắt đầu quét thư mục: {root_folder}...")

    # os.walk giúp duyệt toàn bộ thư mục con
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            try:
                # Mở file ở chế độ đọc/ghi nhị phân ('r+b')
                with open(file_path, 'r+b') as f:
                    # Đọc 300 bytes đầu tiên
                    header_data = f.read(chunk_size)
                    
                    # Kiểm tra xem chuỗi cần tìm có trong 300 bytes này không
                    if search_pattern in header_data:
                        # Thực hiện thay thế trong bộ nhớ
                        new_header_data = header_data.replace(search_pattern, replace_pattern)
                        
                        # Đưa con trỏ file về lại vị trí đầu tiên (0)
                        f.seek(0)
                        
                        # Ghi đè dữ liệu đã sửa vào file
                        f.write(new_header_data)
                        
                        print(f"[Đã sửa]: {file_path}")
                        count_modified += 1
                        
            except Exception as e:
                print(f"[Lỗi] Không thể đọc file {file_path}: {e}")
                count_errors += 1

    print("-" * 30)
    print(f"Hoàn tất! Tổng số file đã sửa: {count_modified}")
    print(f"Số file bị lỗi truy cập: {count_errors}")

if __name__ == "__main__":
    # --- CẤU HÌNH ĐƯỜNG DẪN TẠI ĐÂY ---
    # Hãy thay đổi đường dẫn bên dưới thành thư mục bạn muốn quét
    # Sử dụng r"" để tránh lỗi ký tự đặc biệt trong đường dẫn Windows
    target_directory = r"E:\Assets\Monopoly-TienThiep-taptap\1000144\assets\assetBundle" 
    
    if os.path.exists(target_directory):
        process_files(target_directory)
    else:
        print("Đường dẫn thư mục không tồn tại!")