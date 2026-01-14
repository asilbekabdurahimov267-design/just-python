import time


def time_size(function):
    def wrap(n):
        stat = time.time()
        result = function(n)
        end = time.time()
        umumiy = end - stat
        print(f"Bajarilgan vaqt: {umumiy} sekund")
        return result

    return wrap


@time_size
def create_list(n):
    if n > 100000:
        print("xatolik")
        return []
    lst = [i for i in range(1,n+1)]
    return lst

n = int(input('Son kriting: '))
create_list(n)





file = open('byron.txt')    #fileni chaqirib beradi
content = file.read() #fileni o'qib beradi
print(content)
file.close() #fileni yopib beradi




fike = open('pushkin.txt', mode='r', encoding='UTF-8')
contet = fike.read()
print(contet)
fike.close()






fike = open('temp.txt', mode='a')
texty = 'Qaleson polvon 100\n '
fike.write(texty)
print(fike)
fike.close()











for i in range(100):
    fike = open('temp.txt', mode='a')
    texty = 'Qaleson polvon 100\n '
    fike.write(texty)
    print(fike)
    fike.close()




# r - faylni oqishi kerakligini bildiradi
# a - faylga ma'lumoot qo'shib beradi



with open('romeo.txt', mode='r', encoding='UTF-8') as file:
    content = file.read()
    print(content)
    for i in range(10):
        f = open(f"romeo.txt {i}", mode='w', encoding='utf=8')
        f.write(content)
        f.close()   #faylni ozini ko'paytirib beradi





with open('nature.jpg', mode='rb') as file:
    content = file.read()
    print(content)   #rasmni kod variantini chiqaradi




with open('mbox-short.txt', mode='r', encoding='utf=8') as jild:
    for line in jild:
        if line.startswith('From '):
            lst = line.split(' ')
            print(lst[1])






with open('mbox-short.txt', mode='r', encoding='utf=8') as jild:
    for line in jild:
        if line.startswith('Message-ID'):
            lst = line.split(' ')
            print(lst[1])





# lambda argument: ifoda


add= lambda a , b : a+b
print(add(5,21))
