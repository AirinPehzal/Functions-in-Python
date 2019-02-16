#Не бейте за 4 позязя, у меня в тексте просто это не сработает
def ask():
    quest = " "
    while quest[len(quest)-1] != '?':
        quest = input("Введите ваш вопрос ")
    return quest


def lastone(tecst, quest):
    found = quest[0][0]
    check = True
    tecst.reverse()
    for word in tecst:
        a = word[0].lower()
        b = found.lower()
        if a == b:
            print(word)
            check = False
            break
    if check:
        print("42")


def wtf(tecst, quest):
    c = 0
    for word in quest:
        for i in word:
            if (i.lower() == 'а') or (i.lower() == 'к'):
                c = c + 1
    w = len(quest)
    x = c*w
    if x > len(tecst):
        print(tecst[len(tecst)-2])
    else:
        print(tecst[x])


def ymn(sentence, sent):
    kolvo = 0
    newsentence = sentence.split(' ')
    newsent = sent.split(' ')
    for ele in newsent:
        if ele == '':
            newsent.remove('')
    for ele in newsent:
        if ele == '':
            newsent.remove('')
    for word in newsentence:
        for words in newsent:
            if words == word.lower():
                kolvo = kolvo+1
    if kolvo >= 2:
        print("Да")
    if kolvo == 1:
        print("Может быть")
    if kolvo == 0:
        print("Нет")
    lastone(newsent, newsentence)
    wtf(newsent,newsentence)


text = open("text.txt", "r")
sent = ""
for line in text:
    sent = sent + " " + line.replace('\n', '').replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('—', '').replace('«', '').replace('»', '').replace('-', '').replace('…', '').replace('(', '').replace(')', '').replace('  ', ' ')
question = ask()
question = question.replace('?', '')
ymn(question, sent)