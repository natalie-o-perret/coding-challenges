from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print(tag)
		for arg0, arg1 in attrs:
			print("->", arg0, ">", arg1)

N = int(input())
S = ""
for _ in range(N):
	S += input()

parser = MyHTMLParser()
parser.feed(S)
