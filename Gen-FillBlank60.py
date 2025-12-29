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

# --- NGUỒN DỮ LIỆU MẪU CÂU (ĐÃ BỔ SUNG HINT) ---
# Cấu trúc: (V1, V2, V3, Câu_V1, Câu_V2, Câu_V3, Hint_V1, Hint_V2, Hint_V3)
SENTENCE_TEMPLATES = [
    ("arise", "arose", "arisen", "Problems will [BLANK] if we don't act.", "A new issue [BLANK] during the meeting.", "No complications have [BLANK] so far.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("awake", "awoke", "awoken", "Please [BLANK] me at 7 AM.", "He [BLANK] in the middle of the night.", "I was [BLANK] by a loud noise.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("be", "was/were", "been", "You must [BLANK] quiet.", "She [BLANK] happy yesterday.", "He has [BLANK] to Paris.", "Sau 'must' là động từ nguyên mẫu (V1).", "Chủ ngữ 'She' + 'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("bear", "bore", "born/borne", "I cannot [BLANK] this pain.", "She [BLANK] three children.", "He has [BLANK] this burden for years.", "Sau 'cannot' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("beat", "beat", "beaten", "Can you [BLANK] him in a race?", "Our team [BLANK] them 3-0.", "He has never been [BLANK].", "Sau 'Can' là động từ nguyên mẫu (V1).", "V1, V2 của 'beat' viết giống nhau.", "Đây là câu bị động (been + V3)."),
    ("become", "became", "become", "He wants to [BLANK] a doctor.", "She [BLANK] famous overnight.", "They have [BLANK] good friends.", "Sau 'wants to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "V1 và V3 của 'become' viết giống nhau (have + V3)."),
    ("begin", "began", "begun", "The show will [BLANK] at 8.", "It [BLANK] to rain.", "The race has already [BLANK].", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("bend", "bent", "bent", "Don't [BLANK] the rules.", "He [BLANK] down to tie his shoe.", "The spoon was [BLANK].", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("bet", "bet", "bet", "I [BLANK] you can't do it.", "He [BLANK] all his money on that horse.", "I have [BLANK] on the wrong team.", "V1, V2, V3 của 'bet' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("bid", "bid/bade", "bid/bidden", "I will [BLANK] $100 for the painting.", "She [BLANK] $50 at the auction.", "He was [BLANK] to leave.", "Sau 'will' là động từ nguyên mẫu (V1).", "V1 và V2 của 'bid' có thể giống nhau.", "Đây là câu bị động (was + V3)."),
    ("bind", "bound", "bound", "They will [BLANK] his hands.", "He [BLANK] the papers together.", "She was [BLANK] by the contract.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("bite", "bit", "bitten", "Does your dog [BLANK]?", "The mosquito [BLANK] me.", "He was [BLANK] by a snake.", "Sau 'Does' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("bleed", "bled", "bled", "The cut will [BLANK] for a minute.", "His nose [BLANK] after the fall.", "The patient has [BLANK] a lot.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("blow", "blew", "blown", "The wind will [BLANK] hard today.", "He [BLANK] out the candles.", "The roof was [BLANK] off in the storm.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("break", "broke", "broken", "Be careful not to [BLANK] the vase.", "She [BLANK] her arm.", "The window is [BLANK].", "Sau 'not to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động / V3 làm tính từ (is + V3)."),
    ("breed", "bred", "bred", "They [BLANK] horses on their farm.", "Đây là thói quen (hiện tại đơn).", "This dog was [BLANK] for racing.", "Đây là thói quen (hiện tại đơn, V1).", "Đây là hành động trong quá khứ (V2).", "Đây là câu bị động (was + V3)."),
    ("bring", "brought", "brought", "Please [BLANK] me a glass of water.", "She [BLANK] a cake to the party.", "Have you [BLANK] your homework?", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("broadcast", "broadcast", "broadcast", "They will [BLANK] the news at 6.", "The station [BLANK] the match live.", "The event was [BLANK] worldwide.", "V1, V2, V3 của 'broadcast' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("build", "built", "built", "Let's [BLANK] a sandcastle.", "The Romans [BLANK] this aqueduct.", "The house was [BLANK] in 1950.", "Sau 'Let's' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("burn", "burnt/burned", "burnt/burned", "Don't [BLANK] the toast.", "He [BLANK] the old letters.", "She has [BLANK] her hand.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("burst", "burst", "burst", "The balloon is going to [BLANK].", "The pipe [BLANK] suddenly.", "He has [BLANK] into the room.", "V1, V2, V3 của 'burst' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("buy", "bought", "bought", "I need to [BLANK] some milk.", "He [BLANK] a new car.", "She has [BLANK] a gift for him.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("cast", "cast", "cast", "Let's [BLANK] the fishing line.", "He [BLANK] a shadow on the wall.", "The spell has been [BLANK].", "V1, V2, V3 của 'cast' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("catch", "caught", "caught", "Try to [BLANK] the ball.", "The police [BLANK] the thief.", "I have [BLANK] a cold.", "Sau 'Try to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("choose", "chose", "chosen", "You must [BLANK] one.", "She [BLANK] the blue dress.", "He was [BLANK] as the leader.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("cling", "clung", "clung", "The baby likes to [BLANK] to its mother.", "He [BLANK] to the rope.", "The mud has [BLANK] to my shoes.", "Sau 'likes to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("come", "came", "come", "Can you [BLANK] to the party?", "He [BLANK] home late.", "Has the mail [BLANK] yet?", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "V1 và V3 của 'come' viết giống nhau (Has + V3)."),
    ("cost", "cost", "cost", "How much does this [BLANK]?", "It [BLANK] me $50.", "This mistake has [BLANK] us dearly.", "V1, V2, V3 của 'cost' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("creep", "crept", "crept", "He tried to [BLANK] past the guard.", "The cat [BLANK] silently.", "The feeling has [BLANK] up on me.", "Sau 'tried to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("cut", "cut", "cut", "Be careful when you [BLANK] the onion.", "She [BLANK] her finger.", "I have [BLANK] the price.", "V1, V2, V3 của 'cut' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("deal", "dealt", "dealt", "Who will [BLANK] the cards?", "He [BLANK] with the problem.", "We have [BLANK] with this company before.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("dig", "dug", "dug", "The dog loves to [BLANK] holes.", "They [BLANK] a well.", "He has [BLANK] his own grave.", "Sau 'loves to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("do", "did", "done", "You must [BLANK] your homework.", "He [BLANK] a great job.", "What have you [BLANK]?", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("draw", "drew", "drawn", "Can you [BLANK] a house?", "She [BLANK] a beautiful picture.", "The curtains were [BLANK].", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (were + V3)."),
    ("dream", "dreamt/dreamed", "dreamt/dreamed", "I sometimes [BLANK] of flying.", "I [BLANK] I was famous.", "He had [BLANK] of this moment.", "Đây là thói quen (hiện tại đơn, V1).", "Đây là hành động trong quá khứ.", "Đây là thì quá khứ hoàn thành (had + V3)."),
    ("drink", "drank", "drunk", "What do you want to [BLANK]?", "He [BLANK] all the milk.", "She has [BLANK] too much coffee.", "Sau 'want to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("drive", "drove", "driven", "I am learning to [BLANK] a car.", "He [BLANK] me to the airport.", "Have you ever [BLANK] a truck?", "Sau 'learning to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("dwell", "dwelt/dwelled", "dwelt/dwelled", "Do not [BLANK] on the past.", "They [BLANK] in a small cabin.", "He has [BLANK] on this topic for hours.", "Sau 'Do not' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("eat", "ate", "eaten", "Let's [BLANK] lunch.", "I [BLANK] a sandwich.", "Have you [BLANK] yet?", "Sau 'Let's' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("fall", "fell", "fallen", "Be careful not to [BLANK].", "He [BLANK] off the ladder.", "The leaves have [BLANK].", "Sau 'not to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("feed", "fed", "fed", "It's time to [BLANK] the dog.", "She [BLANK] the baby.", "Have you [BLANK] the cats?", "Sau 'time to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("feel", "felt", "felt", "How do you [BLANK]?", "I [BLANK] sick yesterday.", "I have [BLANK] this way before.", "Câu hỏi hiện tại đơn (Do + V1).", "'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("fight", "fought", "fought", "Don't [BLANK] with your brother.", "They [BLANK] bravely.", "He has [BLANK] for his country.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("find", "found", "found", "I can't [BLANK] my keys.", "She [BLANK] a gold coin.", "Have you [BLANK] what you were looking for?", "Sau 'can't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("flee", "fled", "fled", "The prisoner will try to [BLANK].", "The family [BLANK] the country.", "They have [BLANK] to safety.", "Sau 'try to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("fling", "flung", "flung", "Don't [BLANK] your clothes on the floor.", "He [BLANK] the door open.", "The book was [BLANK] aside.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("fly", "flew", "flown", "Birds can [BLANK] high.", "The plane [BLANK] over the mountains.", "He has [BLANK] all over the world.", "Sau 'can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("forbid", "forbade/forbad", "forbidden", "I [BLANK] you to go.", "His father [BLANK] him to smoke.", "Smoking is [BLANK] here.", "Đây là câu hiện tại đơn (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("forecast", "forecast", "forecast", "They [BLANK] rain for tomorrow.", "The expert [BLANK] a rise in prices.", "The weather was [BLANK] correctly.", "V1, V2, V3 của 'forecast' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("forget", "forgot", "forgotten", "Don't [BLANK] to call me.", "I [BLANK] his name.", "I have [BLANK] my password.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("forgive", "forgave", "forgiven", "Please [BLANK] me.", "She [BLANK] him for his mistake.", "He has been [BLANK].", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("freeze", "froze", "frozen", "The water will [BLANK] at 0°C.", "The lake [BLANK] solid.", "The food is [BLANK].", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động / V3 làm tính từ (is + V3)."),
    ("get", "got", "gotten/got", "You need to [BLANK] permission.", "She [BLANK] a new job.", "Have you [BLANK] the email?", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3)."),
    ("give", "gave", "given", "Please [BLANK] me the book.", "He [BLANK] her a gift.", "I have [BLANK] him the keys.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("go", "went", "gone", "We must [BLANK] now.", "She [BLANK] to the store.", "He has [BLANK] home.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("grind", "ground", "ground", "We need to [BLANK] the coffee beans.", "He [BLANK] the pepper.", "The wheat is [BLANK] into flour.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("grow", "grew", "grown", "Plants need light to [BLANK].", "He [BLANK] tomatoes in his garden.", "You have [BLANK] so tall.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("hang", "hung", "hung", "Please [BLANK] your coat here.", "She [BLANK] the painting on the wall.", "He has [BLANK] up the phone.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("have", "had", "had", "I [BLANK] a cat.", "We [BLANK] a good time yesterday.", "I have [BLANK] enough.", "Đây là câu hiện tại đơn (V1).", "'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("hear", "heard", "heard", "Can you [BLANK] that noise?", "I [BLANK] a strange sound.", "Have you [BLANK] the news?", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Have + V3).")
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

print(f"Bắt đầu tạo câu hỏi điền từ (60 động từ, không trùng lặp, có hint)...")

# --- LẶP QUA 60 MẪU CÂU (BỎ VÒNG LẶP WHILE) ---
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
        "hint": hint_v1 # <<< THÊM HINT
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
        "hint": hint_v2 # <<< THÊM HINT
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
        "hint": hint_v3 # <<< THÊM HINT
    })
    current_id += 1

# --- GHI RA TỆP JSON ---
output_filename = 'fill_in_the_blank_180_with_hints.json'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"\nHoàn thành! Đã tạo {len(questions)} câu hỏi (có hint, không trùng lặp) và lưu vào tệp '{output_filename}'.")