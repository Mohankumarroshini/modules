from scenario import dispatcher
from scenario.modules.disable import DisableAbleCommandHandler
from scenario.modules.helper_funcs.alternate import typing_action
from telegram import ParseMode
from telegram.ext import run_async

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "ⓐ",
    "ⓑ",
    "ⓒ",
    "ⓓ",
    "ⓔ",
    "ⓕ",
    "ⓖ",
    "ⓗ",
    "ⓘ",
    "ⓙ",
    "ⓚ",
    "ⓛ",
    "ⓜ",
    "ⓝ",
    "ⓞ",
    "ⓟ",
    "ⓠ",
    "ⓡ",
    "ⓢ",
    "ⓣ",
    "ⓤ",
    "ⓥ",
    "ⓦ",
    "ⓧ",
    "ⓨ",
    "ⓩ",
]
fbubblefont = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
squarefont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
fsquarefont = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
bluefont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
latinfont = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]
linedfont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]
sonic= [
"𝕬",

"𝕭",

"𝕮",

"𝕯",

"𝕰",

"𝕱",

"𝕲",

"𝕳",

"𝕵",

"𝕶",

"𝕷",

"𝕸",

"𝕹",

"𝕺",

"𝕻",

"𝕼",

"𝕽",

"𝖀",

"𝕾",

"𝕿",

"𝖀",

"𝖁",

"𝖂",

"𝖃",

"𝖄",

"𝖅",
         ]
         
  ntini = [
      "ᵃ",
"ᵇ",
"ᶜ",
"ᵈ",
"ᵉ",
"ᶠ",
"ʰ",
"ⁱ",
"ᵏ",
"ˡ",
"ᵐ",
"ⁿ",
"ᵒ",
"ᵖ",
"ᵠ",
"ʳ",
"ˢ",
"ᵗ",
"ᵘ",
"ᵛ",
"ʷ",
"ˣ",
"ʸ",
"ᶻ ",
      ]
      
   cursiv = [
   "Ⓐ︎",
"Ⓑ︎",
"Ⓒ︎",
"Ⓓ︎",
"Ⓔ︎",
"Ⓕ︎",
"Ⓖ︎",
"Ⓗ︎",
"Ⓘ︎",
"Ⓙ︎",
"Ⓚ︎",
"Ⓛ︎",
"Ⓜ︎",
"Ⓝ︎",
"Ⓞ︎",
"Ⓟ︎",
"Ⓠ︎",
"Ⓡ︎",
"Ⓢ︎",
"Ⓣ︎",
"Ⓤ︎",
"Ⓥ︎",
"Ⓦ︎",
"Ⓧ︎",
"Ⓨ︎",
"Ⓩ︎",
        ]
     glow = [
     " a⃠",
" b⃠",
" c⃠",
" d⃠",
" e⃠",
" f⃠",
" g⃠",
" h⃠",
"  i⃠",
"  j⃠",
" k⃠",
"  l⃠",
" m⃠",
" n⃠",
" o⃠",
" p⃠",
" q⃠",
" r⃠",
" s⃠",
" t⃠",
" u⃠",
" v⃠",
"w⃠",
" x⃠",
" y⃠",
" z⃠",
       ]
         
@typing_action
def weebify(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def bubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/bubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def fbubble(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fbubble <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def square(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/square <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def fsquare(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/fsquare <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def blue(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/blue <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bluecharacter = bluefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bluecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def latin(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/latin <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            latincharacter = latinfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, latincharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


@typing_action
def lined(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/lined <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            linedcharacter = linedfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linedcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)

@typing_action
def sonic(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/sonic <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            soniccharacter = sonicfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, soniccharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        
@typing_action
def ntini(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/ntini <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            ntinicharacter = ntinifont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, ntinicharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        
        
@typing_action
def cursive(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/cursive<text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            cursivecharacter = cursivefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, cursivecharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)
        
        
@typing_action
def glow(update, context):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/glow <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            glowcharacter = glowfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, glowcharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)




__mod_name__ = "Styletext"

WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify, run_async=True)
BUBBLE_HANDLER = DisableAbleCommandHandler("bubble", bubble, run_async=True)
FBUBBLE_HANDLER = DisableAbleCommandHandler("fbubble", fbubble, run_async=True)
SQUARE_HANDLER = DisableAbleCommandHandler("square", square, run_async=True)
FSQUARE_HANDLER = DisableAbleCommandHandler("fsquare", fsquare, run_async=True)
BLUE_HANDLER = DisableAbleCommandHandler("blue", blue, run_async=True)
LATIN_HANDLER = DisableAbleCommandHandler("latin", latin, run_async=True)
LINED_HANDLER = DisableAbleCommandHandler("lined", lined, run_async=True)
SONIC_HANDLER = DisableAbleCommandHandler("sonic", sonic, run_async=True)
NTINI_HANDLER = DisableAbleCommandHandler("ntini", ntini, run_async=True)
CURSIVE_HANDLER = DisableAbleCommandHandler("cursive", cursive, run_async=True)
GLOW_HANDLER = DisableAbleCommandHandler("glow", glow, run_async=True)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(BUBBLE_HANDLER)
dispatcher.add_handler(FBUBBLE_HANDLER)
dispatcher.add_handler(SQUARE_HANDLER)
dispatcher.add_handler(FSQUARE_HANDLER)
dispatcher.add_handler(BLUE_HANDLER)
dispatcher.add_handler(LATIN_HANDLER)
dispatcher.add_handler(LINED_HANDLER)
dispatcher.add_handler(SONIC_HANDLER)
dispatcher.add_handler(NTINI_HANDLER)
dispatcher.add_handler(CURSIVE_HANDLER)
dispatcher.add_handler(GLOW_HANDLER)

__command_list__ = ["weebify"]
__command_list__ = ["bubble"]
__command_list__ = ["fbubble"]
__command_list__ = ["square"]
__command_list__ = ["fsquare"]
__command_list__ = ["blue"]
__command_list__ = ["latin"]
__command_list__ = ["lined"]
__command_list__ = ["sonic"]
__command_list__ = ["ntini"]
__command_list__ = ["cursive"]
__command_list__ = ["glow"]
__handlers__ = [WEEBIFY_HANDLER]
__handlers__ = [BUBBLE_HANDLER]
__handlers__ = [FBUBBLE_HANDLER]
__handlers__ = [SQUARE_HANDLER]
__handlers__ = [FSQUARE_HANDLER]
__handlers__ = [BLUE_HANDLER]
__handlers__ = [LATIN_HANDLER]
__handlers__ = [LINED_HANDLER]
__handlers__ = [SONIC_HANDLER]
__handlers__ = [NTINI_HANDLER]
__handlers__ = [CURSIVE_HANDLER]
__handlers__ = [GLOW_HANDLER]
