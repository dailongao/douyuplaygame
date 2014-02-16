
key_code_map = {
	'`':0,
	'1':0,
	'2':0,
	'3':0,
	'4':0,
	'5':0,
	'6':0,
	'7':0,
	'8':0,
	'9':0,
	'0':0,
	'-':0,
	'=':0,
	'backspace':0,
	'tab':0,
	'q':0,
	'w':0,
	'e':0,
	'r':0,
	't':0,
	'y':0,
	'u':0,
	'i':0,
	'o':0,
	'p':0,
	'[':0,
	']':0,
	'capslock':0,
	'a':0,
	's':0,
	'd':0,
	'f':0,
	'g':0,
	'h':0,
	'j':0,
	'k':0,
	'l':0,
	';':0,
	'':0,
	'enter':0,
	'leftshift':0,
	'z':0,
	'x':0,
	'c':0,
	'v':0,
	'b':0,
	'n':0,
	'm':0,
	',':0,
	'.':0,
	'/':0,
	'rightshift':0,
	'leftctrl':0,
	'leftalt':0,
	'spacebar':0,
	'rightalt':0,
	'rightctrl':0,
	'insert':0,
	'delete':0,
	'leftarrow':0,
	'home':0,
	'end':0,
	'uparrow':0,
	'downarrow':0,
	'pageup':0,
	'pagedown':0,
	'rightarrow':0,
	'numlock':0,
	'keypad7':0,
	'keypad4':0,
	'keypad1':0,
	'keypad/':0,
	'keypad8':0,
	'keypad5':0,
	'keypad2':0,
	'keypad0':0,
	'keypad*':0,
	'keypad9':0,
	'keypad6':0,
	'keypad3':0,
	'keypad.':0,
	'keypad-':0,
	'keypad+':0,
	'keypadenter':0,
	'esc':0,
	'f1':0,
	'f2':0,
	'f3':0,
	'f4':0,
	'f5':0,
	'f6':0,
	'f7':0,
	'f8':0,
	'f9':0,
	'f10':0,
	'f11':0,
	'f12':0,
	'printscreen':0,
	'scrolllock':0,
	'pausebreak':0,
	'\\':0
}

def scancode(key):
	return key_code_map[key.lower()];

if __name__ == '__main__':
	print key_code_map