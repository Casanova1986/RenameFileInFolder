import json
import os
from PIL import Image
import rectpack

# ================= CẤU HÌNH ĐƯỜNG DẪN =================
IMPORT_DIR = './assets/import'   # Thư mục chứa JSON
NATIVE_DIR = './assets/native'   # Thư mục chứa ảnh gốc (thư mục 00, 0a, 1b...)
OUTPUT_DIR = './spine_output'    # Thư mục xuất kết quả
OUTPUT_NAME = 'hero_atlas'       # Tên file atlas xuất ra
MAX_ATLAS_SIZE = 2048            # Kích thước tối đa của tấm ảnh mới
# =======================================================

def find_image_by_uuid(uuid):
    """Tìm đường dẫn ảnh dựa trên cấu trúc thư mục 2 ký tự của Cocos."""
    sub = uuid[:2]
    for ext in ['.png', '.jpg', '.webp', '.jpeg']:
        path = os.path.join(NATIVE_DIR, sub, uuid + ext)
        if os.path.exists(path):
            return path
    return None

def extract_all_sprites():
    """Quét JSON và cắt ảnh."""
    print("--- Giai đoạn 1: Đang trích xuất sprite từ JSON ---")
    all_sprites = []
    
    for root, _, files in os.walk(IMPORT_DIR):
        for file in files:
            if not file.endswith('.json'): continue
            
            try:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Kiểm tra định dạng cc.SpriteFrame
                if len(data) < 6 or "cc.SpriteFrame" not in str(data[3]): continue

                uuids = data[1]
                info_list = data[5]
                map_idx = data[6]

                for i, info in enumerate(info_list):
                    target_uuid = uuids[map_idx[i]]
                    img_path = find_image_by_uuid(target_uuid)
                    if not img_path: continue

                    # Thông số kỹ thuật
                    name = info['name']
                    rect = info['rect']         # [x, y, w, h] trong atlas cũ
                    offset = info['offset']     # [ox, oy]
                    orig_size = info['originalSize']
                    is_rotated = info.get('rotated', False) or info.get('rotated') == 1

                    # Cắt và xử lý xoay
                    with Image.open(img_path) as atlas_old:
                        atlas_old = atlas_old.convert("RGBA")
                        # Pillow crop: (left, top, right, bottom)
                        sprite_img = atlas_old.crop((rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3]))
                        
                        if is_rotated:
                            # Xoay lại 90 độ theo chiều kim đồng hồ để về trạng thái thẳng
                            sprite_img = sprite_img.transpose(Image.ROTATE_270)
                        
                        all_sprites.append({
                            'name': name,
                            'img': sprite_img,
                            'orig_size': orig_size,
                            'cocos_offset': offset
                        })
            except Exception as e:
                print(f"Bỏ qua file {file} do lỗi: {e}")
                
    print(f"Thành công: Thu thập được {len(all_sprites)} sprite.")
    return all_sprites

def pack_to_spine(sprites):
    """Đóng gói và tạo file .atlas.txt"""
    if not sprites: return

    print("--- Giai đoạn 2: Đóng gói (Packing) ---")
    
    # SỬA LỖI VALUEERROR: Sử dụng tham số mặc định ổn định nhất
    packer = rectpack.newPacker(rotation=False) 

    for i, s in enumerate(sprites):
        w, h = s['img'].size
        packer.add_rect(w, h, rid=i)

    packer.add_bin(MAX_ATLAS_SIZE, MAX_ATLAS_SIZE)
    packer.pack()

    # Tạo canvas mới
    new_atlas = Image.new("RGBA", (MAX_ATLAS_SIZE, MAX_ATLAS_SIZE), (0, 0, 0, 0))
    
    # Chuẩn bị nội dung file .atlas theo chuẩn Spine
    atlas_lines = [
        f"\n{OUTPUT_NAME}.png",
        f"size: {MAX_ATLAS_SIZE},{MAX_ATLAS_SIZE}",
        "format: RGBA8888",
        "filter: Linear,Linear",
        "repeat: none"
    ]

    for rect in packer.rect_list():
        b, x, y, w, h, rid = rect
        s = sprites[rid]
        
        # Pillow dán ảnh (y tính từ trên xuống)
        paste_y = MAX_ATLAS_SIZE - y - h
        new_atlas.paste(s['img'], (x, paste_y))

        # Tính Offset cho Spine
        # Spine offset: từ góc dưới-trái ảnh gốc đến góc dưới-trái ảnh cắt
        full_w, full_h = s['orig_size']
        ox, oy = s['cocos_offset']
        
        spine_ox = (full_w - w) / 2 + ox
        spine_oy = (full_h - h) / 2 + oy

        # Ghi dữ liệu vào file text
        atlas_lines.append(s['name'])
        atlas_lines.append("  rotate: false")
        atlas_lines.append(f"  xy: {x}, {paste_y}")
        atlas_lines.append(f"  size: {w}, {h}")
        atlas_lines.append(f"  orig: {full_w}, {full_h}")
        atlas_lines.append(f"  offset: {spine_ox:.1f}, {spine_oy:.1f}")
        atlas_lines.append("  index: -1")

    # Lưu kết quả
    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)
    
    new_atlas.save(os.path.join(OUTPUT_DIR, f"{OUTPUT_NAME}.png"))
    with open(os.path.join(OUTPUT_DIR, f"{OUTPUT_NAME}.atlas.txt"), 'w', encoding='utf-8') as f:
        f.write("\n".join(atlas_lines))

    print(f"--- HOÀN TẤT ---")
    print(f"File lưu tại: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    data = extract_all_sprites()
    pack_to_spine(data)