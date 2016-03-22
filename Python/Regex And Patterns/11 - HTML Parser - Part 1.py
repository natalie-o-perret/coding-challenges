from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print("Start :", tag)
		for arg0, arg1 in attrs:
			print("->", arg0, ">", arg1)

	def handle_endtag(self, tag):
		print("End   :", tag)

	def handle_startendtag(self, tag, attrs):
		print("Empty :", tag)
		for arg0, arg1 in attrs:
			print("->", arg0, ">", arg1)


N = int(input())
S = ""
for _ in range(N):
	S += input()

parser = MyHTMLParser()
parser.feed(S)
