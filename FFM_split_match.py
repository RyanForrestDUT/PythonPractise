
########################################################################
# Author: Ryan
# Date: Oct 17
# Note: Forward Maximum Matching Segmentation
########################################################################

def load_dict(filename):
	word_dict = set()
	max_len = 1
	f = open(filename, "r", encoding="utf-8")
	for line in f:
#		word = unicode(line.strip(), "utf-8")
		word = str(line.strip())
		word_dict.add(word)
		if(len(word) > max_len):
			max_len = len(word)
			
	return max_len, word_dict


def fm_word_seg(sent, max_len, word_dict):
	begin = 0
	words = []
	sent = str(sent)
	
	while begin < len(sent):
		for end in range(begin+max_len, begin, -1):
			if sent[begin: end] in word_dict:
				words.append(sent[begin:end])
		
		begin = end
		
	return words


max_len, word_dict = load_dict("lexincon.dic")
sent = input("please input a sentence: ")
words = fm_word_seg(sent, max_len, word_dict)
for word in words:
	print(word)
