# -*- coding: utf-8 -*-  

import re

# [0]: info, [1]: author
def getinfo(data):
	checkPattern = re.compile(r'content@=(.*)/scope@=/snick@=(.*)/dnick@=')
	checkResult = checkPattern.search(data).groups()
	return checkResult