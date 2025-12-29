import json
import os
import shutil
from PIL import Image

# ================= CẤU HÌNH ĐƯỜNG DẪN =================
IMPORT_DIR = './assets/import'   # Thư mục chứa JSON
NATIVE_DIR = './assets/native'   # Thư mục chứa ảnh gốc
EXPORT_DIR = './atlas_clean_name' # Thư mục xuất kết quả
# =======================================================

def get_image_info(uuid):
    """Tìm đường dẫn ảnh và lấy kích thước thực tế (W, H)."""
    sub = uuid[:2]
    for ext in ['.png', '.jpg', '.webp', '.jpeg']:
        path = os.path.join(NATIVE_DIR, sub, uuid + ext)
        if os.path.exists(path):
            try:
                with Image.open(path) as img:
                    return path, img.size
            except:
                return path, (0, 0)
    return None, (0, 0)

def clean_name(name):
    """Bỏ phần số sau ký tự '_' cuối cùng."""
    if '_' in name:
        # rsplit('_', 1) sẽ chia chuỗi từ bên phải qua, tối đa 1 lần
        return name.rsplit('_', 1)[0]
    return name

def generate_atlas_clean_name():
    if os.path.exists(EXPORT_DIR):
        shutil.rmtree(EXPORT_DIR)
    os.makedirs(EXPORT_DIR)

    # Dictionary gom nhóm: { uuid: { "atlas_name": str, "sprites": [] } }
    uuid_groups = {}

    print("--- Đang quét và xử lý tên Sprite ---")

    # BƯỚC 1: QUÉT VÀ PHÂN LOẠI
    for root, _, files in os.walk(IMPORT_DIR):
        for file in files:
            if not file.endswith('.json'): continue
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if len(data) < 6 or "cc.SpriteFrame" not in str(data[3]): continue

                texture_uuid = data[1][data[6][0]] 
                sprite_data = data[5][0]
                
                # Xử lý tên: role_3401112_14 -> role_3401112
                original_name = sprite_data['name']
                base_name = clean_name(original_name)

                if texture_uuid not in uuid_groups:
                    uuid_groups[texture_uuid] = {
                        "atlas_name": base_name,
                        "sprites": []
                    }
                
                uuid_groups[texture_uuid]["sprites"].append(sprite_data)
            except Exception as e:
                print(f"Lỗi đọc file {file}: {e}")

    # BƯỚC 2: XUẤT FILE ATLAS
    print(f"Tìm thấy {len(uuid_groups)} bộ Atlas. Đang khởi tạo file...")

    for uuid, group in uuid_groups.items():
        img_path, (img_w, img_h) = get_image_info(uuid)
        atlas_name = group["atlas_name"]
        sprites = group["sprites"]

        if not img_path:
            print(f"X Cảnh báo: Không tìm thấy ảnh gốc cho {atlas_name} (UUID: {uuid})")
            continue

        # Tạo thư mục theo tên đã rút gọn
        target_folder = os.path.join(EXPORT_DIR, atlas_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        # Copy ảnh và đặt tên theo atlas_name
        shutil.copy(img_path, os.path.join(target_folder, f"{atlas_name}.png"))

        # Nội dung file .atlas.txt
        atlas_lines = [
            f"\n{atlas_name}.png",
            f"size: {img_w},{img_h}",
            "format: RGBA8888",
            "filter: Linear,Linear",
            "repeat: none"
        ]

        for s in sprites:
            name = s['name']
            rect = s['rect']
            offset = s['offset']
            orig = s['originalSize']
            rotated = "true" if (s.get('rotated', False) or s.get('rotated') == 1) else "false"

            # Tính toán Offset Spine
            sw, sh = (rect[2], rect[3])
            spine_ox = (orig[0] - sw) / 2 + offset[0]
            spine_oy = (orig[1] - sh) / 2 + offset[1]

            atlas_lines.extend([
                name,
                f"  rotate: {rotated}",
                f"  xy: {rect[0]}, {rect[1]}",
                f"  size: {rect[2]}, {rect[3]}",
                f"  orig: {orig[0]}, {orig[1]}",
                f"  offset: {spine_ox:.1f}, {spine_oy:.1f}",
                "  index: -1"
            ])

        # Lưu file .atlas.txt
        with open(os.path.join(target_folder, f"{atlas_name}.atlas.txt"), 'w', encoding='utf-8') as f:
            f.write("\n".join(atlas_lines))
        
        print(f"√ Export thành công: {atlas_name}")

    print(f"\n--- HOÀN TẤT ---")
    print(f"Kết quả lưu tại: {os.path.abspath(EXPORT_DIR)}")

if __name__ == "__main__":
    generate_atlas_clean_name()