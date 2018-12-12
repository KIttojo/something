m = open('input.txt')
f = open('outtext.txt','w')
words = m.read()
key = len(words)
res = ""
for message in words:
	res += str(ord(message) ^ key) +'\n'
f.write(res)
f.close()
m.close()