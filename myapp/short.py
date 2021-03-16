import pyshorteners

link = input('enter link: ')
shortener = pyshorteners.Shortener()
short = shortener.tinyurl.short(link)

print(short)