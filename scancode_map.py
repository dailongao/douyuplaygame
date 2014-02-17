
key_code_map = {
	'w' : 0x11,
	's' : 0x1f,
	'a' : 0x1e,
	'd' : 0x20,
	'z' : 0x2c,
	'x' : 0x2d,
	'c' : 0x2e,
	'v' : 0x2f
}

def scancode(key):
	return key_code_map[key];