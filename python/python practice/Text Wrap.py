#Text Wrap
#https://www.hackerrank.com/challenges/text-wrap
def wrap(string, max_width):
    s = textwrap.fill(string, max_width)
    return s
