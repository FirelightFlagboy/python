#codinf:utf-8

def brainfuck(text):
	ms = []
	for i in range(0,1000):
		ms.append(0)
	i = 0
	ptr = 0
	nel = len(text)
	while i < nel:
		c = text[i]
		if c == '>':
			ptr += 1
		elif c == '<':
			ptr -= 1
		elif c == '+':
			ms[ptr] += 1
		elif c == '-':
			ms[ptr] -= 1
		elif c == '.':
			print(chr(ms[ptr]), end="")
		elif c == '[' and ms[ptr] == 0:
			continue
		elif c == ']' and ms[ptr] != 0:
			loop = 1
			while loop > 0:
				i -= 1
				c = text[i]
				if c == '[':
					loop -= 1
				elif c == ']':
					loop += 1
		i += 1

def main():
	r = input("enter texte to decode in brainfuck :\n")
	brainfuck(r)

if __name__ == '__main__':
	main()
