import json
import random

# --- NGUỒN DỮ LIỆU ĐỘNG TỪ (180+ ĐỘNG TỪ KÈM NGHĨA) ---
VERB_LIST = [
    ("arise", "arose", "arisen", "phát sinh"), ("awake", "awoke", "awoken", "thức giấc"),
    ("be", "was/were", "been", "thì, là, ở"), ("bear", "bore", "born/borne", "mang, chịu đựng"),
    ("beat", "beat", "beaten", "đánh, đập"), ("become", "became", "become", "trở nên"),
    ("begin", "began", "begun", "bắt đầu"), ("bend", "bent", "bent", "uốn cong"),
    ("bet", "bet", "bet", "cá cược"), ("bid", "bid/bade", "bid/bidden", "trả giá, ra lệnh"),
    ("bind", "bound", "bound", "buộc, trói"), ("bite", "bit", "bitten", "cắn"),
    ("bleed", "bled", "bled", "chảy máu"), ("blow", "blew", "blown", "thổi"),
    ("break", "broke", "broken", "làm vỡ"), ("breed", "bred", "bred", "nuôi, gây giống"),
    ("bring", "brought", "brought", "mang lại"), ("broadcast", "broadcast", "broadcast", "phát sóng"),
    ("build", "built", "built", "xây dựng"), ("burn", "burnt/burned", "burnt/burned", "đốt, cháy"),
    ("burst", "burst", "burst", "nổ tung"), ("buy", "bought", "bought", "mua"),
    ("cast", "cast", "cast", "ném, quăng"), ("catch", "caught", "caught", "bắt, chụp"),
    ("choose", "chose", "chosen", "chọn"), ("cling", "clung", "clung", "bám vào"),
    ("come", "came", "come", "đến"), ("cost", "cost", "cost", "có giá"),
    ("creep", "crept", "crept", "bò, trườn"), ("cut", "cut", "cut", "cắt"),
    ("deal", "dealt", "dealt", "giao dịch, xử lý"), ("dig", "dug", "dug", "đào"),
    ("do", "did", "done", "làm"), ("draw", "drew", "drawn", "vẽ"),
    ("dream", "dreamt/dreamed", "dreamt/dreamed", "mơ"), ("drink", "drank", "drunk", "uống"),
    ("drive", "drove", "driven", "lái xe"), ("dwell", "dwelt/dwelled", "dwelt/dwelled", "trú ngụ"),
    ("eat", "ate", "eaten", "ăn"), ("fall", "fell", "fallen", "ngã, rơi"),
    ("feed", "fed", "fed", "cho ăn"), ("feel", "felt", "felt", "cảm thấy"),
    ("fight", "fought", "fought", "chiến đấu"), ("find", "found", "found", "tìm thấy"),
    ("flee", "fled", "fled", "chạy trốn"), ("fling", "flung", "flung", "quăng, ném"),
    ("fly", "flew", "flown", "bay"), ("forbid", "forbade/forbad", "forbidden", "cấm"),
    ("forecast", "forecast", "forecast", "dự báo"), ("forget", "forgot", "forgotten", "quên"),
    ("forgive", "forgave", "forgiven", "tha thứ"), ("freeze", "froze", "frozen", "đóng băng"),
    ("get", "got", "gotten/got", "nhận được"), ("give", "gave", "given", "cho, đưa"),
    ("go", "went", "gone", "đi"), ("grind", "ground", "ground", "nghiền"),
    ("grow", "grew", "grown", "phát triển, trồng"), ("hang", "hung", "hung", "treo"),
    ("have", "had", "had", "có"), ("hear", "heard", "heard", "nghe"),
    ("hide", "hid", "hidden", "ẩn, trốn"), ("hit", "hit", "hit", "đánh, đụng"),
    ("hold", "held", "held", "cầm, giữ"), ("hurt", "hurt", "hurt", "làm đau"),
    ("keep", "kept", "kept", "giữ"), ("kneel", "knelt/kneeled", "knelt/kneeled", "quỳ"),
    ("know", "knew", "known", "biết"), ("lay", "laid", "laid", "đặt, để"),
    ("lead", "led", "led", "dẫn dắt"), ("lean", "leant/leaned", "leant/leaned", "dựa, nghiêng"),
    ("leap", "leapt/leaped", "leapt/leaped", "nhảy"), ("learn", "learnt/learned", "learnt/learned", "học"),
    ("leave", "left", "left", "rời đi"), ("lend", "lent", "lent", "cho vay"),
    ("let", "let", "let", "để, cho phép"), ("lie", "lay", "lain", "nằm"),
    ("light", "lit/lighted", "lit/lighted", "thắp sáng"), ("lose", "lost", "lost", "mất, thua"),
    ("make", "made", "made", "làm, chế tạo"), ("mean", "meant", "meant", "có nghĩa là"),
    ("meet", "met", "met", "gặp"), ("mow", "mowed", "mown/mowed", "cắt cỏ"),
    ("offset", "offset", "offset", "bù đắp"), ("overcome", "overcame", "overcome", "vượt qua"),
    ("partake", "partook", "partaken", "tham gia"), ("pay", "paid", "paid", "trả tiền"),
    ("plead", "pled/pleaded", "pled/pleaded", "bào chữa"), ("preset", "preset", "preset", "cài đặt sẵn"),
    ("prove", "proved", "proven/proved", "chứng minh"), ("put", "put", "put", "đặt, để"),
    ("quit", "quit/quitted", "quit/quitted", "từ bỏ"), ("read", "read", "read", "đọc"),
    ("relay", "relaid", "relaid", "chuyển tiếp"), ("rid", "rid", "rid", "thoát khỏi"),
    ("ride", "rode", "ridden", "cưỡi"), ("ring", "rang", "rung", "rung chuông"),
    ("rise", "rose", "risen", "mọc, tăng lên"), ("run", "ran", "run", "chạy"),
    ("saw", "sawed", "sawn/sawed", "cưa"), ("say", "said", "said", "nói"),
    ("see", "saw", "seen", "nhìn, thấy"), ("seek", "sought", "sought", "tìm kiếm"),
    ("sell", "sold", "sold", "bán"), ("send", "sent", "sent", "gửi"),
    ("set", "set", "set", "thiết lập"), ("sew", "sewed", "sewn/sewed", "may, khâu"),
    ("shake", "shook", "shaken", "lắc, rung"), ("shave", "shaved", "shaven/shaved", "cạo râu"),
    ("shear", "shore/sheared", "shorn/sheared", "xén lông cừu"), ("shed", "shed", "shed", "rụng lá, lột da"),
    ("shine", "shone", "shone", "chiếu sáng"), ("shoot", "shot", "shot", "bắn"),
    ("show", "showed", "shown/showed", "cho xem"), ("shrink", "shrank/shrunk", "shrunk", "co lại"),
    ("shut", "shut", "shut", "đóng"), ("sing", "sang", "sung", "hát"),
    ("sink", "sank/sunk", "sunk", "chìm"), ("sit", "sat", "sat", "ngồi"),
    ("slay", "slew/slained", "slain", "sát hại"), ("sleep", "slept", "slept", "ngủ"),
    ("slide", "slid", "slid", "trượt"), ("sling", "slung", "slung", "ném mạnh"),
    ("slink", "slunk", "slunk", "lẻn đi"), ("slit", "slit", "slit", "rạch, xẻ"),
    ("smell", "smelt/smelled", "smelt/smelled", "ngửi"), ("sow", "sowed", "sown/sowed", "gieo hạt"),
    ("speak", "spoke", "spoken", "nói"), ("speed", "sped/speeded", "sped/speeded", "tăng tốc"),
    ("spell", "spelt/spelled", "spelt/spelled", "đánh vần"), ("spend", "spent", "spent", "tiêu xài"),
    ("spill", "spilt/spilled", "spilt/spilled", "làm tràn"), ("spin", "spun/span", "spun", "quay"),
    ("spit", "spat/spit", "spat/spit", "khạc, nhổ"), ("split", "split", "split", "chia, tách"),
    ("spoil", "spoilt/spoiled", "spoilt/spoiled", "làm hỏng"), ("spread", "spread", "spread", "trải ra, lan truyền"),
    ("spring", "sprang/sprung", "sprung", "nhảy"), ("stand", "stood", "stood", "đứng"),
    ("steal", "stole", "stolen", "ăn cắp"), ("stick", "stuck", "stuck", "dán, dính"),
    ("sting", "stung", "stung", "chích, đốt"), ("stink", "stank/stunk", "stunk", "bốc mùi hôi"),
    ("strew", "strewed", "strewn/strewed", "rải, rắc"), ("stride", "strode", "stridden", "sải bước"),
    ("strike", "struck", "struck/stricken", "đánh, đình công"), ("string", "strung", "strung", "xâu dây"),
    ("strive", "strove/strived", "striven/strived", "phấn đấu"), ("swear", "swore", "sworn", "thề"),
    ("sweat", "sweat/sweated", "sweat/sweated", "đổ mồ hôi"), ("sweep", "swept", "swept", "quét"),
    ("swell", "swelled", "swollen/swelled", "sưng, phồng"), ("swim", "swam", "swum", "bơi"),
    ("swing", "swung", "swung", "đu, lắc"), ("take", "took", "taken", "lấy, cầm"),
    ("teach", "taught", "taught", "dạy"), ("tear", "tore", "torn", "xé rách"),
    ("tell", "told", "told", "kể, bảo"), ("think", "thought", "thought", "suy nghĩ"),
    ("throw", "threw", "thrown", "ném"), ("thrust", "thrust", "thrust", "đẩy mạnh"),
    ("tread", "trod", "trodden/trod", "giẫm, đạp"), ("typeset", "typeset", "typeset", "sắp chữ"),
    ("undergo", "underwent", "undergone", "trải qua"), ("understand", "understood", "understood", "hiểu"),
    ("upset", "upset", "upset", "làm buồn, lật đổ"), ("wake", "woke/waked", "woken/waked", "thức dậy"),
    ("wear", "wore", "worn", "mặc"), ("weave", "wove/weaved", "woven/weaved", "dệt"),
    ("wed", "wed/wedded", "wed/wedded", "kết hôn"), ("weep", "wept", "wept", "khóc"),
    ("wet", "wet/wetted", "wet/wetted", "làm ướt"), ("win", "won", "won", "thắng"),
    ("wind", "wound", "wound", "quấn, lên dây cót"), ("withdraw", "withdrew", "withdrawn", "rút lui, rút tiền"),
    ("wring", "wrung", "wrung", "vắt, siết"), ("write", "wrote", "written", "viết")
]

# Tạo một "bể" các từ để làm phương án nhiễu
print("Đang tạo bể từ nhiễu...")
distractor_pool = []
for v1, v2, v3, v1_meaning in VERB_LIST:
    distractor_pool.append(v1)
    distractor_pool.extend(v2.split('/')) 
    distractor_pool.extend(v3.split('/'))
    distractor_pool.append(v1 + "ed") 
    distractor_pool.append(v1 + "s") 
    distractor_pool.append(v1 + "ing")

distractor_pool = list(set(distractor_pool))
print(f"Đã tạo bể từ nhiễu với {len(distractor_pool)} từ duy nhất.")

def get_options(correct_answer, verb_tuple, pool):
    """Tạo 4 phương án lựa chọn (1 đúng, 3 nhiễu) và xáo trộn chúng."""
    v1, v2, v3, v1_meaning = verb_tuple
    
    potential_distractors = [v1]
    potential_distractors.extend(v2.split('/'))
    potential_distractors.extend(v3.split('/'))
    potential_distractors.append(v1 + "ed")
    potential_distractors.append(v1 + "s")
    potential_distractors.append(v1 + "ing")
    
    potential_distractors.extend(random.sample(pool, 5))
    
    final_distractors = []
    for d in potential_distractors:
        if d != correct_answer and d not in final_distractors:
            final_distractors.append(d)
        if len(final_distractors) == 3:
            break
            
    while len(final_distractors) < 3:
        d = random.choice(pool)
        if d != correct_answer and d not in final_distractors:
            final_distractors.append(d)

    options = final_distractors + [correct_answer]
    random.shuffle(options)
    answer_index = options.index(correct_answer)
    
    return options, answer_index

# --- HÀM TẠO CÂU HỎI ---
questions = []
current_id = 1

print("Bắt đầu tạo câu hỏi nhận diện (4 loại, không trùng lặp)...")

# --- CHỈ LẶP QUA DANH SÁCH 1 LẦN (BỎ VÒNG LẶP WHILE) ---
for verb_tuple in VERB_LIST:
    v1, v2, v3, v1_meaning = verb_tuple 
    
    correct_v2 = random.choice(v2.split('/'))
    correct_v3 = random.choice(v3.split('/'))

    # Loại 1: Tìm V2 (từ V1)
    question_v2 = f"What is the past simple of '{v1}' ({v1_meaning})?"
    options_v2, index_v2 = get_options(correct_v2, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id, "topic": "v2_identification",
        "question": question_v2,
        "options": options_v2, "answer_index": index_v2
    })
    current_id += 1

    # Loại 2: Tìm V3 (từ V1)
    question_v3 = f"What is the past participle of '{v1}' ({v1_meaning})?"
    options_v3, index_v3 = get_options(correct_v3, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id, "topic": "v3_identification",
        "question": question_v3,
        "options": options_v3, "answer_index": index_v3
    })
    current_id += 1
    
    # Loại 3: Tìm V1 (từ V2)
    question_v1_from_v2 = f"What is the base form of '{correct_v2}'?"
    options_v1a, index_v1a = get_options(v1, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id, "topic": "base_form_identification",
        "question": question_v1_from_v2,
        "options": options_v1a, "answer_index": index_v1a
    })
    current_id += 1
    
    # === BỔ SUNG MỚI ===
    # Loại 4: Tìm V1 (từ V3)
    question_v1_from_v3 = f"What is the base form of '{correct_v3}'?"
    options_v1b, index_v1b = get_options(v1, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id, "topic": "base_form_identification",
        "question": question_v1_from_v3,
        "options": options_v1b, "answer_index": index_v1b
    })
    current_id += 1

# --- GHI RA TỆP JSON ---
output_filename = 'identification_all_4_types_unique.json' # <<< THAY ĐỔI TÊN TỆP
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"\nHoàn thành! Đã tạo {len(questions)} câu hỏi (không trùng lặp) và lưu vào tệp '{output_filename}'.")