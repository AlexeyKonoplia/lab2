#Метод деления

def division(s):
    news = []
    for i in s:
        news += [ord(i)]
    key = ord('я') + 1
    for i in range(len(news)):
        news[i] = hex(key % news[i])[2:].zfill(2)
    return ''.join(news)
if __name__ == '__main__':
    s = input('input: ') # test
    print('hash', division(s)) # 749d77bb
