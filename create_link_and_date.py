###TRANSLATES YOUR "watch-history.html" into more readable txt, to be analysed.
###RUN this first...

#example
from html.parser import HTMLParser
from html.entities import name2codepoint



example = """
<a href="https://www.youtube.com/watch?v=Q-4vRXzRpkM">Joji - plastic taste</a><br><a href="https://www.youtube.com/channel/UCpSWIHakX5BDV9eClaSUYog">Catie</a><br>May 4, 2019, 2:46:42 PM AEDT</div>
"""
filename = "watch-history.html"

f = open(filename, "r")

global just_saw_link
just_saw_link = False
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        to_return = ""
        if tag == 'a':
            for attr in attrs:
                if "watch?v" in attr[1]:
                    link = attr[1]
                    just_saw_link = True
                    to_return = link
                    print(link)
    def handle_data(self, data):
        if "AEDT" in data:
            print(data)

parser = MyHTMLParser()
parser.feed(example) 
parser.handle_starttag('a', [('href', 'https://www.youtube.com/')])
for line in f:
    parser.feed(line)
