from pygame import font

def write_score(s1, s2):
	file_path = "score.txt"
	s1 = str(s1)
	s2 = str(s2)
	score = s1 + " " + s2
	with open(file_path, "w", encoding="utf-8") as f:
		f.write(score)


def read_score():
	file_path = "score.txt"
	with open(file_path, "r") as f:
		score = f.read().split()
	return int(score[0]), int(score[1])

def create_font(size_font, color):
	s1, s2 = read_score()

	f1 = font.Font(None, size_font)
	text_in_font1 = f1.render(str(s1), True, color)

	f2 = font.Font(None, size_font)
	text_in_font2 = f2.render(str(s2), True, color)

	return text_in_font1, text_in_font2



