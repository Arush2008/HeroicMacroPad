import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

COL_PINS = [board.GP26, board.GP27, board.GP28, board.GP29]  # 4 columns
ROW_PINS = [board.GP4, board.GP2]  # 2 rows

ENC1_A = board.GP3
ENC1_B = board.GP0

ENC2_A = board.GP5
ENC2_B = board.GP1

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    columns=COL_PINS,
    rows=ROW_PINS,
)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
    (ENC1_A, ENC1_B),  # Encoder 1
    (ENC2_A, ENC2_B),  # Encoder 2
)

encoder_handler.map = [
    (KC.VOLD, KC.VOLU),   # Encoder 1: volume down/up
    (KC.LEFT, KC.RIGHT),  # Encoder 2: horizontal nav
]

macros = Macros()
keyboard.modules.append(macros)

keyboard.keymap = [
    [
        KC.MUTE, KC.N1, KC.N2, KC.N3,   # ROW 0: COL0 to COL3
        KC.N4,   KC.N5, KC.N6, KC.N7,   # ROW 1: COL0 to COL3
    ]
]

if __name__ == '__main__':
    keyboard.go()

