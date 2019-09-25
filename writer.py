from bs4 import BeautifulSoup as BS
import datetime
with open('C:\\Users\\adity\\Documents\\Desktop\\Misc\\not blind\\index.html') as fp:
    soup = BS(fp, features="html.parser")
now = datetime.datetime.now()
rules = '''
The Technology Club | notblind development team
HOW TO USE NotBlindWriter(R)
When prompted with 'Write here>', write down the text of your article.
After pressing 'return', you will be asked for the 'command>' prompt.
Enter 'exit' to exit the article.
Enter 'image' to insert an image.
Enter 'newline' to go to the next line.
Enter 'link' to insert a link.

NOTE: THIS SOFTWARE IS STILL IN BETA!!!
'''
print(rules)
head = input('Enter title>')
original_tag = soup.body
new_tag = soup.new_tag("div", id="blogpost")
original_tag.append(new_tag)
h = soup.new_tag('h1')
h.string = head
new_tag.append(h)
date = soup.new_tag('p')
date.string = now.strftime("%Y-%m-%d %H:%M")
new_tag.append(date)
while True:
    inp = input('Write here>')
    if inp != '':
        par = soup.new_tag('p')
        new_tag.append(par)
        par.string = inp
    else:
        pass
    command = input('command>')
    if command == 'exit':
        break
    elif command == 'newline':
        pass
    elif command == 'image':
        src = input('imgsrc>')
        ty = input('type (small "info" or big "major")>')
        if ty == 'info':
            image = soup.new_tag('img', src=src, height="30%", width="30%")
        elif ty == 'major':
            image = soup.new_tag('img', src=src, height="30%", width="100%")
        new_tag.append(image)
    elif command == 'link':
        link = input('Enter link URL')
        text = input('Enter link text')
        linktag = soup.new_tag('a', href=link)
        linktag.string = text
        soup.append(linktag)


    else:
        print('Invalid command! Moving to newline!!')
with open('C:\\Users\\adity\\Documents\\Desktop\\Misc\\not blind\\index.html','w') as outf:
    outf.write((soup.prettify()))
    input('Your changes have been published! Press return to exit.')