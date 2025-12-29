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

# --- NGUỒN DỮ LIỆU MẪU CÂU (64 ĐỘNG TỪ CUỐI CÙNG) ---
# Cấu trúc: (V1, V2, V3, Câu_V1, Câu_V2, Câu_V3, Hint_V1, Hint_V2, Hint_V3)
SENTENCE_TEMPLATES = [
    ("slide", "slid", "slid", "Be careful not to [BLANK] on the ice.", "He [BLANK] into the base.", "The doors have [BLANK] open.", "Sau 'not to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("sling", "slung", "slung", "Don't [BLANK] your bag on the floor.", "He [BLANK] the backpack over his shoulder.", "His coat was [BLANK] over the chair.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("slink", "slunk", "slunk", "The fox tried to [BLANK] away.", "The cat [BLANK] into the shadows.", "It had [BLANK] off before we arrived.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì quá khứ hoàn thành (had + V3)."),
    ("slit", "slit", "slit", "You must [BLANK] the envelope open.", "He [BLANK] the paper with a knife.", "The bag was [BLANK] open.", "V1, V2, V3 của 'slit' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("smell", "smelt/smelled", "smelt/smelled", "Can you [BLANK] the flowers?", "The food [BLANK] delicious.", "I have [BLANK] this perfume before.", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("sow", "sowed", "sown/sowed", "The farmer needs to [BLANK] the seeds.", "He [BLANK] the seeds in spring.", "The seeds have been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("speak", "spoke", "spoken", "You must [BLANK] clearly.", "She [BLANK] to the manager.", "English is [BLANK] here.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("speed", "sped/speeded", "sped/speeded", "Don't [BLANK] in a school zone.", "The car [BLANK] down the highway.", "He has [BLANK] through his work.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("spell", "spelt/spelled", "spelt/spelled", "How do you [BLANK] your name?", "He [BLANK] the word correctly.", "The word is [BLANK] wrong.", "Câu hỏi hiện tại đơn (Do + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("spend", "spent", "spent", "How much did you [BLANK]?", "I [BLANK] all my money.", "She has [BLANK] hours on this.", "Câu hỏi quá khứ đơn (Did + V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("spill", "spilt/spilled", "spilt/spilled", "Be careful not to [BLANK] the milk.", "He [BLANK] coffee on his shirt.", "The milk has been [BLANK].", "Sau 'not to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("spin", "spun/span", "spun", "The dancer can [BLANK] very fast.", "The car [BLANK] out of control.", "The top has [BLANK] for a minute.", "Sau 'can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("spit", "spat/spit", "spat/spit", "It's rude to [BLANK] in public.", "He [BLANK] out the bad food.", "He has [BLANK] on the ground.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("split", "split", "split", "Let's [BLANK] the bill.", "They [BLANK] the prize money.", "The wood has been [BLANK].", "V1, V2, V3 của 'split' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("spoil", "spoilt/spoiled", "spoilt/spoiled", "Don't [BLANK] the child.", "The rain [BLANK] our picnic.", "The milk has [BLANK].", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("spread", "spread", "spread", "Can you [BLANK] the butter?", "The fire [BLANK] quickly.", "The news has [BLANK] everywhere.", "V1, V2, V3 của 'spread' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("spring", "sprang/sprung", "sprung", "The cat is about to [BLANK].", "He [BLANK] out of bed.", "The trap has [BLANK].", "Sau 'about to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("stand", "stood", "stood", "Please [BLANK] up.", "He [BLANK] in the corner.", "She has [BLANK] there for hours.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("steal", "stole", "stolen", "It is wrong to [BLANK].", "Someone [BLANK] my wallet.", "My bike has been [BLANK].", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("stick", "stuck", "stuck", "You need to [BLANK] a stamp on it.", "He [BLANK] the note to the wall.", "I am [BLANK] on this problem.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (am + V3)."),
    ("sting", "stung", "stung", "A bee might [BLANK] you.", "A wasp [BLANK] me.", "I have been [BLANK] by a jellyfish.", "Sau 'might' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("stink", "stank/stunk", "stunk", "That food will [BLANK] if you leave it.", "The garbage [BLANK] yesterday.", "This room has [BLANK] for days.", "Sau 'will' là động từ nguyên mẫu (V1).", "'yesterday' (quá khứ).", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("strew", "strewed", "strewn/strewed", "Don't [BLANK] your clothes everywhere.", "He [BLANK] flowers on the path.", "Papers were [BLANK] all over the floor.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (were + V3)."),
    ("stride", "strode", "stridden", "He loves to [BLANK] through the park.", "She [BLANK] confidently into the room.", "He has [BLANK] across the stage.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("strike", "struck", "struck/stricken", "The clock is about to [BLANK] twelve.", "Lightning [BLANK] the tree.", "The city was [BLANK] by an earthquake.", "Sau 'about to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("string", "strung", "strung", "You need to [BLANK] the beads.", "She [BLANK] the lights on the tree.", "The guitar has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("strive", "strove/strived", "striven/strived", "We must [BLANK] for excellence.", "He [BLANK] to be the best.", "She has [BLANK] all her life.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("swear", "swore", "sworn", "Do you [BLANK] to tell the truth?", "He [BLANK] he didn't do it.", "He has [BLANK] an oath.", "Câu hỏi hiện tại đơn (Do + V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("sweat", "sweat/sweated", "sweat/sweated", "He began to [BLANK] nervously.", "She [BLANK] a lot during the match.", "I have [BLANK] through my shirt.", "Sau 'began to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("sweep", "swept", "swept", "You need to [BLANK] the floor.", "She [BLANK] the broken glass.", "The floor has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("swell", "swelled", "swollen/swelled", "The injury will [BLANK] up.", "His ankle [BLANK] after the fall.", "My eyes are [BLANK] from crying.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (are + V3)."),
    ("swim", "swam", "swum", "I love to [BLANK] in the ocean.", "He [BLANK] across the lake.", "She has [BLANK] the English Channel.", "Sau 'love to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("swing", "swung", "swung", "The child loves to [BLANK].", "He [BLANK] the bat.", "She has [BLANK] from one opinion to another.", "Sau 'love to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("take", "took", "taken", "Please [BLANK] a seat.", "She [BLANK] the bus to work.", "Has he [BLANK] his medicine?", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (Has + V3)."),
    ("teach", "taught", "taught", "He wants to [BLANK] history.", "She [BLANK] me how to play guitar.", "This method is [BLANK] in all schools.", "Sau 'wants to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (is + V3)."),
    ("tear", "tore", "torn", "Be careful not to [BLANK] the paper.", "He [BLANK] the letter in half.", "The page has been [BLANK] out.", "Sau 'not to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("tell", "told", "told", "Can you [BLANK] me the time?", "He [BLANK] me a secret.", "I have [BLANK] you everything.", "Sau 'Can' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("think", "thought", "thought", "I need to [BLANK] about it.", "I [BLANK] you were at home.", "I have often [BLANK] of moving.", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (have + V3)."),
    ("throw", "threw", "thrown", "Don't [BLANK] stones.", "He [BLANK] the ball to me.", "The keys were [BLANK] on the table.", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (were + V3)."),
    ("thrust", "thrust", "thrust", "He had to [BLANK] the door open.", "He [BLANK] his hands in his pockets.", "The knife was [BLANK] into the wood.", "V1, V2, V3 của 'thrust' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("tread", "trod", "trodden/trod", "Don't [BLANK] on the flowers.", "He [BLANK] carefully on the broken glass.", "The path was well [BLANK].", "Sau 'Don't' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("typeset", "typeset", "typeset", "We need to [BLANK] the document.", "He [BLANK] the entire book.", "The book has been [BLANK].", "V1, V2, V3 của 'typeset' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("undergo", "underwent", "undergone", "The patient must [BLANK] surgery.", "She [BLANK] a major change.", "He has [BLANK] extensive training.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("understand", "understood", "understood", "Did you [BLANK] the question?", "I [BLANK] what he meant.", "His instructions were not [BLANK].", "Câu hỏi quá khứ đơn (Did + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (were + V3)."),
    ("upset", "upset", "upset", "I didn't mean to [BLANK] you.", "The news [BLANK] him.", "She was [BLANK] by his comments.", "V1, V2, V3 của 'upset' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("wake", "woke/waked", "woken/waked", "What time do you [BLANK] up?", "I [BLANK] up early today.", "Have you been [BLANK] long?", "Câu hỏi hiện tại đơn (Do + V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("wear", "wore", "worn", "What should I [BLANK] to the party?", "She [BLANK] a beautiful dress.", "This coat has been [BLANK] a lot.", "Sau 'should' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("weave", "wove/weaved", "woven/weaved", "She knows how to [BLANK] baskets.", "He [BLANK] a complex story.", "The tapestry was [BLANK] by hand.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3)."),
    ("wed", "wed/wedded", "wed/wedded", "They plan to [BLANK] next year.", "They [BLANK] in a small chapel.", "They have been [BLANK] for 10 years.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("weep", "wept", "wept", "She started to [BLANK] uncontrollably.", "He [BLANK] for hours.", "She has [BLANK] tears of joy.", "Sau 'to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("wet", "wet/wetted", "wet/wetted", "Don't [BLANK] the floor.", "He [BLANK] the towel.", "The clothes have been [BLANK] by the rain.", "V1, V2, V3 của 'wet' viết giống nhau.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("win", "won", "won", "Who will [BLANK] the game?", "Our team [BLANK] the championship.", "She has [BLANK] three awards.", "Sau 'will' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là thì hiện tại hoàn thành (has + V3)."),
    ("wind", "wound", "wound", "You need to [BLANK] the clock.", "He [BLANK] the bandage around his arm.", "The clock has been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("withdraw", "withdrew", "withdrawn", "I need to [BLANK] some money.", "He [BLANK] his application.", "The troops have been [BLANK].", "Sau 'need to' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("wring", "wrung", "wrung", "You must [BLANK] out the wet cloth.", "She [BLANK] the towel.", "The cloth has been [BLANK] out.", "Sau 'must' là động từ nguyên mẫu (V1).", "Đây là hành động trong quá khứ.", "Đây là câu bị động (been + V3)."),
    ("write", "wrote", "written", "Please [BLANK] your name here.", "He [BLANK] a letter to his parents.", "The book was [BLANK] in 1990.", "Câu mệnh lệnh/yêu cầu dùng V1.", "Đây là hành động trong quá khứ.", "Đây là câu bị động (was + V3).")
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

print(f"Bắt đầu tạo câu hỏi điền từ (64 động từ cuối, có hint)...")

# --- LẶP QUA 64 MẪU CÂU MỚI (BỎ VÒNG LẶP WHILE) ---
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
output_filename = 'fill_in_the_blank_last_64_with_hints.json'
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"\nHoàn thành! Đã tạo {len(questions)} câu hỏi (không trùng lặp) và lưu vào tệp '{output_filename}'.")