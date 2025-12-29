import json
import random

# --- NGUỒN DỮ LIỆU ĐỘNG TỪ (180+) ---
# Dùng để tạo các phương án nhiễu (distractors)
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
    # ... (phần còn lại của 180+ động từ)
]

# --- NGUỒN DỮ LIỆU MẪU CÂU (60 ĐỘNG TỪ TIẾP THEO) ---
# Cấu trúc: (V1, V2, V3, Câu_V1, Câu_V2, Câu_V3, Hint_V1, Hint_V2, Hint_V3)
SENTENCE_TEMPLATES = [
    ("hide", "hid", "hidden", "You can't [BLANK] from the truth.", "He [BLANK] the money under the bed.", "The key was [BLANK] in a drawer.", "Sau 'can't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("hit", "hit", "hit", "Don't [BLANK] your brother.", "The car [BLANK] the tree.", "He was [BLANK] by a falling rock.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "V1, V2, V3 của 'hit' viết giống nhau.", "Đây là câu bị động (was + V3)."),
    ("hold", "held", "held", "Please [BLANK] my bag for me.", "She [BLANK] the baby in her arms.", "The meeting will be [BLANK] tomorrow.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (be + V3)."),
    ("hurt", "hurt", "hurt", "Be careful not to [BLANK] yourself.", "He [BLANK] his knee playing soccer.", "I have [BLANK] my back.", "V1, V2, V3 của 'hurt' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("keep", "kept", "kept", "You must [BLANK] this a secret.", "She [BLANK] her promise.", "The food is [BLANK] in the fridge.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("kneel", "knelt/kneeled", "knelt/kneeled", "He had to [BLANK] before the king.", "She [BLANK] down to pray.", "He has [BLANK] in front of the altar.", "Sau 'had to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("know", "knew", "known", "Do you [BLANK] the answer?", "I [BLANK] you were right.", "He is [BLANK] for his generosity.", "Câu hỏi hiện tại đơn (Do + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("lay", "laid", "laid", "Please [BLANK] the table for dinner.", "He [BLANK] the book on the desk.", "The foundation has been [BLANK].", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("lead", "led", "led", "Who will [BLANK] the team?", "The general [BLANK] his troops.", "She has [BLANK] a difficult life.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("lean", "leant/leaned", "leant/leaned", "Don't [BLANK] against the wet paint.", "He [BLANK] back in his chair.", "She has [BLANK] on me for support.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("leap", "leapt/leaped", "leapt/leaped", "He is about to [BLANK] over the fence.", "The frog [BLANK] into the pond.", "He has [BLANK] to a new conclusion.", "Sau 'about to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("learn", "learnt/learned", "learnt/learned", "I want to [BLANK] a new language.", "We [BLANK] about history yesterday.", "She has [BLANK] her lesson.", "Sau 'want to' là động từ nguyên mẫu (V1).", "'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("leave", "left", "left", "What time do we [BLANK]?", "He [BLANK] the house at 8.", "She has [BLANK] her keys at home.", "Câu hỏi hiện tại đơn (Do + V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("lend", "lent", "lent", "Can you [BLANK] me your pen?", "He [BLANK] me his car.", "I have [BLANK] him some money.", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("let", "let", "let", "Please [BLANK] me go.", "His mother [BLANK] him stay up late.", "He has [BLANK] me borrow his bike.", "V1, V2, V3 của 'let' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("lie", "lay", "lain", "I want to [BLANK] down.", "He [BLANK] on the sofa all day.", "The book has [BLANK] on the floor for weeks.", "Sau 'want to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("light", "lit/lighted", "lit/lighted", "Can you [BLANK] the candle?", "She [BLANK] the fire.", "The fire has been [BLANK].", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("lose", "lost", "lost", "Don't [BLANK] your keys.", "I [BLANK] my wallet yesterday.", "Have you [BLANK] your mind?", "Sau 'Don't' là động từ nguyên mẫu (V1).", "'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("make", "made", "made", "Did you [BLANK] this cake?", "She [BLANK] a mistake.", "This table was [BLANK] of wood.", "Câu hỏi quá khứ đơn (Did + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("mean", "meant", "meant", "What does this word [BLANK]?", "I'm sorry, I [BLANK] what I said.", "This gift was [BLANK] for you.", "Câu hỏi hiện tại đơn (Does + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("meet", "met", "met", "Nice to [BLANK] you.", "We [BLANK] at a party.", "Have you [BLANK] my new boss?", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("mow", "mowed", "mown/mowed", "You need to [BLANK] the lawn.", "He [BLANK] the grass yesterday.", "The grass has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "'yesterday' (quá khứ).", "Đây là câu bị động (been + V3)."),
    ("offset", "offset", "offset", "We need to [BLANK] the costs.", "The gain [BLANK] the loss.", "The costs have been [BLANK].", "V1, V2, V3 của 'offset' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("overcome", "overcame", "overcome", "You must [BLANK] your fears.", "She [BLANK] her illness.", "He has [BLANK] many obstacles.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "V1 và V3 của 'overcome' viết giống nhau (has + V3)."),
    ("partake", "partook", "partaken", "Did you [BLANK] in the activities?", "He [BLANK] of the meal.", "She has [BLANK] in many ceremonies.", "Câu hỏi quá khứ đơn (Did + V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("pay", "paid", "paid", "You must [BLANK] for your ticket.", "He [BLANK] the bill.", "Have you [BLANK] the rent?", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("plead", "pled/pleaded", "pled/pleaded", "He will [BLANK] not guilty.", "The man [BLANK] for mercy.", "He has [BLANK] with her to stay.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("preset", "preset", "preset", "You can [BLANK] the radio stations.", "He [BLANK] the timer.", "The machine was [BLANK] at the factory.", "V1, V2, V3 của 'preset' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("prove", "proved", "proven/proved", "You must [BLANK] your identity.", "He [BLANK] his point.", "It has been [BLANK] that he is innocent.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("put", "put", "put", "Please [BLANK] the book on the shelf.", "She [BLANK] on her coat.", "Where have you [BLANK] my keys?", "V1, V2, V3 của 'put' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("quit", "quit/quitted", "quit/quitted", "Are you going to [BLANK] your job?", "He [BLANK] smoking last year.", "She has [BLANK] the team.", "Sau 'going to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("read", "read", "read", "I love to [BLANK] books.", "I [BLANK] that book last year.", "Have you [BLANK] 'Hamlet'?", "Phát âm V1 là /ri:d/.", "Phát âm V2 là /red/.", "Phát âm V3 là /red/ (Have + V3)."),
    ("relay", "relaid", "relaid", "We need to [BLANK] the message.", "He [BLANK] the news to his boss.", "The message has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("rid", "rid", "rid", "I want to [BLANK] this old furniture.", "He [BLANK] the company of its debts.", "They have finally [BLANK] themselves of the problem.", "V1, V2, V3 của 'rid' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("ride", "rode", "ridden", "Can you [BLANK] a bike?", "He [BLANK] his horse.", "Have you ever [BLANK] a camel?", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("ring", "rang", "rung", "I will [BLANK] the bell.", "The phone [BLANK] suddenly.", "Has the bell [BLANK] yet?", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Has + V3)."),
    ("rise", "rose", "risen", "The sun will [BLANK] at 6 AM.", "The sun [BLANK] late today.", "The water level has [BLANK].", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("run", "ran", "run", "I like to [BLANK] in the morning.", "He [BLANK] a marathon.", "She has [BLANK] five miles.", "Sau 'like to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "V1 và V3 của 'run' viết giống nhau (has + V3)."),
    ("saw", "sawed", "sawn/sawed", "He needs to [BLANK] the wood.", "He [BLANK] the log in half.", "The wood has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("say", "said", "said", "What did you [BLANK]?", "She [BLANK] goodbye.", "He hasn't [BLANK] anything.", "Câu hỏi quá khứ đơn (Did + V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (hasn't + V3)."),
    ("see", "saw", "seen", "Did you [BLANK] the new movie?", "We [BLANK] your brother last week.", "I have never [BLANK] such a thing.", "Câu hỏi quá khứ đơn (Did + V1).", "'last week' (quá khứ).", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("seek", "sought", "sought", "We must [BLANK] a solution.", "They [BLANK] shelter from the rain.", "He has [BLANK] help from a doctor.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("sell", "sold", "sold", "Are you planning to [BLANK] your car?", "He [BLANK] his house.", "Have you [BLANK] all the tickets?", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("send", "sent", "sent", "I need to [BLANK] an email.", "She [BLANK] me a letter.", "He has [BLANK] the package.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("set", "set", "set", "Let's [BLANK] a date for the meeting.", "He [BLANK] the table.", "She has [BLANK] a new world record.", "V1, V2, V3 của 'set' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("sew", "sewed", "sewn/sewed", "I am learning to [BLANK].", "She [BLANK] a button on his shirt.", "This dress was [BLANK] by hand.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("shake", "shook", "shaken", "You need to [BLANK] the bottle.", "He [BLANK] his head.", "The news has [BLANK] him.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("shave", "shaved", "shaven/shaved", "He needs to [BLANK] every morning.", "He [BLANK] his beard off.", "He has not [BLANK] in days.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("shear", "shore/sheared", "shorn/sheared", "It's time to [BLANK] the sheep.", "The farmer [BLANK] the wool.", "The sheep have been [BLANK].", "Sau 'time to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("shed", "shed", "shed", "The snake will [BLANK] its skin.", "The tree [BLANK] its leaves.", "He has [BLANK] a lot of weight.", "V1, V2, V3 của 'shed' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("shine", "shone", "shone", "The sun will [BLANK] tomorrow.", "The moon [BLANK] brightly.", "He has [BLANK] his shoes.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("shoot", "shot", "shot", "Don't [BLANK]!", "He [BLANK] the target.", "The soldier was [BLANK].", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("show", "showed", "shown/showed", "Can you [BLANK] me the way?", "He [BLANK] me his new watch.", "I have been [BLANK] the new designs.", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("shrink", "shrank/shrunk", "shrunk", "The sweater will [BLANK] in the wash.", "My jeans [BLANK]!", "The shirt has [BLANK].", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("shut", "shut", "shut", "Please [BLANK] the door.", "He [BLANK] the window.", "The shop has [BLANK] for the day.", "V1, V2, V3 của 'shut' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("sing", "sang", "sung", "She loves to [BLANK].", "He [BLANK] a beautiful song.", "Have you ever [BLANK] in public?", "Sau 'loves to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("sink", "sank/sunk", "sunk", "The boat is going to [BLANK].", "The Titanic [BLANK] in 1912.", "The ship has [BLANK].", "Sau 'going to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("sit", "sat", "sat", "Please [BLANK] down.", "He [BLANK] on the chair.", "She has [BLANK] there all day.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("slay", "slew/slained", "slain", "The knight must [BLANK] the dragon.", "St. George [BLANK] the dragon.", "The monster was [BLANK].", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("sleep", "slept", "slept", "I need to [BLANK].", "The baby [BLANK] for hours.", "Have you [BLANK] well?", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3).")
]


# --- CÁC HÀM HỖ TRỢ ---

# 1. Tạo bể từ nhiễu
print("Đang tạo bể từ nhiễu...")
distractor_pool = []
for v1, v2, v3, v1_meaning in VERB_LIST: # Dùng danh sách 180+
    distractor_pool.append(v1)
    distractor_pool.extend(v2.split('/')) 
    distractor_pool.extend(v3.split('/'))
    distractor_pool.append(v1 + "ed") 
    distractor_pool.append(v1 + "s") 
    distractor_pool.append(v1 + "ing")

distractor_pool = list(set(distractor_pool))
print(f"Đã tạo bể từ nhiễu với {len(distractor_pool)} từ duy nhất.")

# 2. Hàm tạo 4 lựa chọn
def get_options(correct_answer, verb_tuple, pool):
    v1, v2, v3 = verb_tuple # Chỉ cần 3 giá trị cho hàm này
    
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

# --- HÀM TẠO CÂU HỎI CHÍNH ---
questions = []
current_id = 1

print(f"Bắt đầu tạo câu hỏi điền từ (60 động từ tiếp theo, có hint)...")

# --- LẶP QUA 60 MẪU CÂU MỚI (BỎ VÒNG LẶP WHILE) ---
for v1, v2, v3, s_v1, s_v2, s_v3, hint_v1, hint_v2, hint_v3 in SENTENCE_TEMPLATES:
    
    verb_tuple = (v1, v2, v3) # Bộ ba (V1,V2,V3)
    
    correct_v2 = random.choice(v2.split('/'))
    correct_v3 = random.choice(v3.split('/'))

    # --- Loại 1: Điền V1 ---
    options_v1, index_v1 = get_options(v1, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id,
        "topic": "fill_in_the_blank_v1",
        "question": s_v1,
        "options": options_v1,
        "answer_index": index_v1,
        "hint": hint_v1 
    })
    current_id += 1

    # --- Loại 2: Điền V2 ---
    options_v2, index_v2 = get_options(correct_v2, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id,
        "topic": "fill_in_the_blank_v2",
        "question": s_v2,
        "options": options_v2,
        "answer_index": index_v2,
        "hint": hint_v2
    })
    current_id += 1

    # --- Loại 3: Điền V3 ---
    options_v3, index_v3 = get_options(correct_v3, verb_tuple, distractor_pool)
    questions.append({
        "id": current_id,
        "topic": "fill_in_the_blank_v3",
        "question": s_v3,
        "options": options_v3,
        "answer_index": index_v3,
        "hint": hint_v3
    })
    current_id += 1

# --- GHI RA TỆP JSON ---
output_filename = 'fill_in_the_blank_60_next_with_hints.json'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"\nHoàn thành! Đã tạo {len(questions)} câu hỏi (không trùng lặp) và lưu vào tệp '{output_filename}'.")