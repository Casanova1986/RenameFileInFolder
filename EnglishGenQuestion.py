import json
import random

# --- NGUỒN DỮ LIỆU ĐỘNG TỪ (CHO CÂU HỎI NHẬN DIỆN) ---
# (V1, V2, V3)
VERB_LIST = [
    ("be", "was/were", "been"), ("begin", "began", "begun"), ("break", "broke", "broken"),
    ("bring", "brought", "brought"), ("buy", "bought", "bought"), ("build", "built", "built"),
    ("choose", "chose", "chosen"), ("come", "came", "come"), ("cost", "cost", "cost"),
    ("cut", "cut", "cut"), ("do", "did", "done"), ("draw", "drew", "drawn"),
    ("drive", "drove", "driven"), ("drink", "drank", "drunk"), ("eat", "ate", "eaten"),
    ("fall", "fell", "fallen"), ("feel", "felt", "felt"), ("find", "found", "found"),
    ("fly", "flew", "flown"), ("forget", "forgot", "forgotten"), ("get", "got", "gotten/got"),
    ("give", "gave", "given"), ("go", "went", "gone"), ("grow", "grew", "grown"),
    ("have", "had", "had"), ("hear", "heard", "heard"), ("hit", "hit", "hit"),
    ("hold", "held", "held"), ("keep", "kept", "kept"), ("know", "knew", "known"),
    ("leave", "left", "left"), ("lead", "led", "led"), ("let", "let", "let"),
    ("lose", "lost", "lost"), ("make", "made", "made"), ("mean", "meant", "meant"),
    ("meet", "met", "met"), ("pay", "paid", "paid"), ("put", "put", "put"),
    ("read", "read", "read"), ("ride", "rode", "ridden"), ("run", "ran", "run"),
    ("say", "said", "said"), ("see", "saw", "seen"), ("sell", "sold", "sold"),
    ("send", "sent", "sent"), ("set", "set", "set"), ("sing", "sang", "sung"),
    ("sit", "sat", "sat"), ("sleep", "slept", "slept"), ("speak", "spoke", "spoken"),
    ("spend", "spent", "spent"), ("stand", "stood", "stood"), ("swim", "swam", "swum"),
    ("take", "took", "taken"), ("teach", "taught", "taught"), ("tell", "told", "told"),
    ("think", "thought", "thought"), ("throw", "threw", "thrown"), ("understand", "understood", "understood"),
    ("wake", "woke", "woken"), ("wear", "wore", "worn"), ("win", "won", "won"),
    ("write", "wrote", "written")
]

# --- NGUỒN DỮ LIỆU MẪU CÂU (ĐÃ BỔ SUNG THÊM) ---
# Cấu trúc: (V1, V2, V3, Câu_V1, Câu_V2, Câu_V3)
SENTENCE_TEMPLATES = [
    # Bộ gốc
    ("go", "went", "gone", "You must [BLANK] now.", "She [BLANK] to the cinema yesterday.", "He has [BLANK] to Japan."),
    ("eat", "ate", "eaten", "What time do you [BLANK] dinner?", "I [BLANK] a big breakfast.", "Have you [BLANK] all the cookies?"),
    ("see", "saw", "seen", "Did you [BLANK] the new movie?", "We [BLANK] your brother last week.", "I have never [BLANK] such a thing."),
    ("do", "did", "done", "I have to [BLANK] my homework.", "He [BLANK] a great job.", "What have you [BLANK] today?"),
    ("take", "took", "taken", "Please [BLANK] a seat.", "She [BLANK] the bus to work.", "The photo was [BLANK] by a professional."),
    ("write", "wrote", "written", "Don't forget to [BLANK] a thank-you note.", "He [BLANK] a famous novel.", "This book was [BLANK] in 1990."),
    ("begin", "began", "begun", "The show will [BLANK] at 8 PM.", "It [BLANK] to rain.", "The race has already [BLANK]."),
    ("break", "broke", "broken", "Be careful not to [BLANK] the glass.", "He [BLANK] his leg playing football.", "The window is [BLANK]."),
    ("buy", "bought", "bought", "I need to [BLANK] some milk.", "My father [BLANK] me a new bike.", "We have [BLANK] a new house."),
    ("come", "came", "come", "Can you [BLANK] to my party?", "They [BLANK] home very late.", "Has the mail [BLANK] yet?"),
    ("drink", "drank", "drunk", "What would you like to [BLANK]?", "She [BLANK] all the juice.", "He had [BLANK] too much coffee."),
    ("drive", "drove", "driven", "I am learning to [BLANK] a car.", "He [BLANK] me to the airport.", "Have you ever [BLANK] a sports car?"),
    ("find", "found", "found", "I can't [BLANK] my keys.", "She [BLANK] a wallet on the street.", "The lost dog has been [BLANK]."),
    ("give", "gave", "given", "What did you [BLANK] him for his birthday?", "She [BLANK] me a book.", "I have [BLANK] it a lot of thought."),
    ("know", "knew", "known", "Do you [BLANK] the answer?", "I [BLANK] you were hiding something.", "She has [BLANK] him for ten years."),
    
    # *** BỘ MỚI BỔ SUNG ***
    ("bring", "brought", "brought", "Please [BLANK] your book tomorrow.", "He [BLANK] flowers to the party.", "She has [BLANK] her kids with her."),
    ("build", "built", "built", "They want to [BLANK] a new house.", "The Romans [BLANK] this bridge.", "The nest was [BLANK] by birds."),
    ("choose", "chose", "chosen", "You must [BLANK] one option.", "She [BLANK] the red dress.", "He was [BLANK] as team captain."),
    ("draw", "drew", "drawn", "Can you [BLANK] a picture of a cat?", "He [BLANK] a beautiful landscape.", "The curtains were [BLANK] closed."),
    ("fall", "fell", "fallen", "Be careful not to [BLANK].", "He [BLANK] off his bike.", "The leaves have [BLANK] from the tree."),
    ("feel", "felt", "felt", "How do you [BLANK] today?", "I [BLANK] a sharp pain.", "I haven't [BLANK] this good in years."),
    ("fly", "flew", "flown", "I wish I could [BLANK].", "The bird [BLANK] away.", "He has [BLANK] all over the world."),
    ("forget", "forgot", "forgotten", "Don't [BLANK] your keys.", "I [BLANK] his name.", "The rules are easily [BLANK]."),
    ("get", "got", "gotten/got", "I need to [BLANK] some sleep.", "She [BLANK] a new job.", "Have you [BLANK] your ticket yet?"),
    ("grow", "grew", "grown", "Tomatoes [BLANK] well in the sun.", "The tree [BLANK] very tall.", "You have [BLANK] so much!"),
    ("hear", "heard", "heard", "Can you [BLANK] that noise?", "I [BLANK] a strange sound.", "Have you [BLANK] the news?"),
    ("keep", "kept", "kept", "Please [BLANK] the door closed.", "He [BLANK] his promise.", "I have [BLANK] all your letters."),
    ("leave", "left", "left", "What time do we [BLANK]?", "He [BLANK] the room angrily.", "She has [BLANK] her phone at home."),
    ("lose", "lost", "lost", "Don't [BLANK] your passport.", "We [BLANK] the match.", "I think I have [BLANK] my wallet."),
    ("make", "made", "made", "Do you want to [BLANK] a cake?", "She [BLANK] a cup of tea.", "This table is [BLANK] of wood."),
    ("meet", "met", "met", "Nice to [BLANK] you.", "I [BLANK] an old friend yesterday.", "Have you [BLANK] my new boss?"),
    ("pay", "paid", "paid", "You can [BLANK] at the counter.", "He [BLANK] the bill.", "Have you [BLANK] for the tickets?"),
    ("read", "read", "read", "I love to [BLANK] books.", "I [BLANK] that book last year.", "Have you [BLANK] 'Hamlet'?"),
    ("run", "ran", "run", "I like to [BLANK] in the morning.", "He [BLANK] a marathon.", "She has [BLANK] five miles."),
    ("say", "said", "said", "What did you [BLANK]?", "She [BLANK] goodbye.", "He hasn't [BLANK] anything."),
    ("sing", "sang", "sung", "She loves to [BLANK] in the shower.", "He [BLANK] a beautiful song.", "Have you ever [BLANK] in a choir?"),
    ("sleep", "slept", "slept", "I need to [BLANK] for eight hours.", "The baby [BLANK] all night.", "I haven't [BLANK] well."),
    ("speak", "spoke", "spoken", "You must [BLANK] clearly.", "We [BLANK] for hours.", "English is [BLANK] here."),
    ("swim", "swam", "swum", "Let's go [BLANK] in the lake.", "She [BLANK] across the river.", "He has [BLANK] the English Channel."),
    ("teach", "taught", "taught", "He wants to [BLANK] history.", "She [BLANK] me how to play guitar.", "This method is [BLANK] in all schools."),
    ("tell", "told", "told", "Can you [BLANK] me the time?", "He [BLANK] me a secret.", "I have [BLANK] you everything."),
    ("think", "thought", "thought", "I need to [BLANK] about it.", "I [BLANK] you were at home.", "I have often [BLANK] of moving."),
    ("wear", "wore", "worn", "What are you going to [BLANK]?", "She [BLANK] a blue dress.", "This coat has been [BLANK] a lot."),
    ("win", "won", "won", "Everyone wants to [BLANK].", "Our team [BLANK] the game.", "She has [BLANK] three gold medals.")
]


# Tạo một "bể" các từ để làm phương án nhiễu
distractor_pool = []
for v1, v2, v3 in VERB_LIST:
    distractor_pool.append(v1)
    distractor_pool.extend(v2.split('/')) 
    distractor_pool.extend(v3.split('/'))
    distractor_pool.append(v1 + "ed") 
    distractor_pool.append(v1 + "s") # Thêm dạng -s sai
    distractor_pool.append(v1 + "ing") # Thêm dạng -ing sai

distractor_pool = list(set(distractor_pool))

def get_options(correct_answer, verb_tuple, pool):
    """Tạo 4 phương án lựa chọn (1 đúng, 3 nhiễu) và xáo trộn chúng."""
    v1, v2, v3 = verb_tuple
    
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
TARGET_COUNT = 1000

print(f"Bắt đầu tạo {TARGET_COUNT} câu hỏi từ bộ mẫu câu mở rộng...")

while current_id <= TARGET_COUNT:
    
    # --- VÒNG LẶP 1: CÂU HỎI NHẬN DIỆN (3 LOẠI CŨ) ---
    # Lặp qua danh sách động từ ngắn hơn để ưu tiên câu điền từ
    for verb_tuple in random.sample(VERB_LIST, len(VERB_LIST) // 2):
        if current_id > TARGET_COUNT: break
        v1, v2, v3 = verb_tuple
        correct_v2 = random.choice(v2.split('/'))
        correct_v3 = random.choice(v3.split('/'))

        # Loại 1: Tìm V2
        options, answer_index = get_options(correct_v2, verb_tuple, distractor_pool)
        questions.append({
            "id": current_id, "topic": "v2_identification",
            "question": f"What is the past simple (V2) of '{v1}'?",
            "options": options, "answer_index": answer_index
        })
        current_id += 1
        if current_id > TARGET_COUNT: break

        # Loại 2: Tìm V3
        options, answer_index = get_options(correct_v3, verb_tuple, distractor_pool)
        questions.append({
            "id": current_id, "topic": "v3_identification",
            "question": f"What is the past participle (V3) of '{v1}'?",
            "options": options, "answer_index": answer_index
        })
        current_id += 1
        if current_id > TARGET_COUNT: break
        
    if current_id > TARGET_COUNT: break

    # --- VÒNG LẶP 2: CÂU HỎI ĐIỀN TỪ (3 LOẠI MỚI) ---
    # Lặp qua toàn bộ danh sách mẫu câu
    for v1, v2, v3, s_v1, s_v2, s_v3 in SENTENCE_TEMPLATES:
        if current_id > TARGET_COUNT: break
        verb_tuple = (v1, v2, v3)
        correct_v2 = random.choice(v2.split('/'))
        correct_v3 = random.choice(v3.split('/'))

        # Loại 4: Điền V1
        options, answer_index = get_options(v1, verb_tuple, distractor_pool)
        questions.append({
            "id": current_id, "topic": "fill_in_the_blank_v1",
            "question": s_v1, "options": options, "answer_index": answer_index
        })
        current_id += 1
        if current_id > TARGET_COUNT: break

        # Loại 5: Điền V2
        options, answer_index = get_options(correct_v2, verb_tuple, distractor_pool)
        questions.append({
            "id": current_id, "topic": "fill_in_the_blank_v2",
            "question": s_v2, "options": options, "answer_index": answer_index
        })
        current_id += 1
        if current_id > TARGET_COUNT: break

        # Loại 6: Điền V3
        options, answer_index = get_options(correct_v3, verb_tuple, distractor_pool)
        questions.append({
            "id": current_id, "topic": "fill_in_the_blank_v3",
            "question": s_v3, "options": options, "answer_index": answer_index
        })
        current_id += 1
        if current_id > TARGET_COUNT: break

# --- GHI RA TỆP JSON ---
output_filename = 'irregular_verbs_1000_mixed_expanded.json'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Hoàn thành! Đã tạo {len(questions)} câu hỏi và lưu vào tệp '{output_filename}'.")