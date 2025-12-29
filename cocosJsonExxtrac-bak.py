import json
import os
from PIL import Image

# --- CẤU HÌNH ĐƯỜNG DẪN ---
IMPORT_DIR = './assets/import'   # Thư mục chứa các file JSON (.json)
NATIVE_DIR = './assets/native'   # Thư mục chứa ảnh (.png, .jpg...)
OUTPUT_DIR = './extracted_all'   # Thư mục lưu kết quả

def find_texture_path(uuid):
    """Tìm đường dẫn ảnh dựa trên UUID (2 ký tự đầu là tên thư mục)"""
    sub_folder = uuid[:2]
    for ext in ['.png', '.jpg', '.webp', '.jpeg']:
        path = os.path.join(NATIVE_DIR, sub_folder, uuid + ext)
        if os.path.exists(path):
            return path
    return None

def process_single_json(json_path):
    """Đọc và trích xuất ảnh từ một file JSON đơn lẻ"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Kiểm tra xem có đúng định dạng Cocos SpriteFrame không
        # data[3] thường chứa ["cc.SpriteFrame"]
        if len(data) < 6 or "cc.SpriteFrame" not in str(data[3]):
            return

        texture_uuids = data[1]
        sprites_info = data[5]
        mapping = data[6]

        for i, info in enumerate(sprites_info):
            uuid_idx = mapping[i]
            target_uuid = texture_uuids[uuid_idx]
            
            img_path = find_texture_path(target_uuid)
            if not img_path:
                continue

            # Xử lý hình ảnh bằng Pillow
            atlas = Image.open(img_path).convert("RGBA")
            name = info['name']
            rect = info['rect']          # [x, y, w, h]
            offset = info['offset']      # [ox, oy]
            orig_size = info['originalSize'] # [w, h]

            # 1. Cắt ảnh
            crop_box = (rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3])
            sprite_crop = atlas.crop(crop_box)

            # 2. Tạo khung ảnh gốc (Canvas)
            new_img = Image.new("RGBA", (orig_size[0], orig_size[1]), (0, 0, 0, 0))

            # 3. Tính tọa độ dán (Cocos Offset logic)
            paste_x = int((orig_size[0] - rect[2]) / 2 + offset[0])
            paste_y = int((orig_size[1] - rect[3]) / 2 - offset[1])

            new_img.paste(sprite_crop, (paste_x, paste_y))

            # 4. Lưu file
            # Tạo thư mục con theo tên file JSON để tránh trùng lặp
            folder_name = os.path.basename(json_path).split('.')[0]
            save_path = os.path.join(OUTPUT_DIR, folder_name)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            new_img.save(os.path.join(save_path, f"{name}.png"))
            return True # Đã xử lý thành công
    except Exception as e:
        print(f"Lỗi khi xử lý {json_path}: {e}")
    return False

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    count = 0
    print("--- Bắt đầu trích xuất hàng loạt ---")
    
    # Duyệt toàn bộ file trong thư mục import và các thư mục con của nó
    for root, dirs, files in os.walk(IMPORT_DIR):
        for file in files:
            if file.endswith('.json'):
                json_full_path = os.path.join(root, file)
                if process_single_json(json_full_path):
                    count += 1
                    if count % 10 == 0:
                        print(f"Đã xử lý xong {count} file...")

    print(f"--- Hoàn tất! Đã trích xuất thành công {count} SpriteFrames ---")
    print(f"Kết quả lưu tại: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()