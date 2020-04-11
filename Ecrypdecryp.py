import string, random
random.seed(1234)
letter = list(string.ascii_letters) + list(string.digits + ' ')

num = len(letter) #52
num_list = list(range(num))

random.shuffle(num_list)
dic = dict()

for i in range(num):
    dic[letter[i]] = num_list[i]
  
code = 'secret message'

enc = [] 
for l in code:
    enc.append(dic[l])

ip = input('Enter Secret Code\n')

if ip == '1234':
    rev_dic = dict()
    for k, v in dic.items():
        rev_dic[v] = k
else:
    print('Itna galat kese ho skte ho bhai')    

dec = ''
for i in enc:
    dec += rev_dic[i]

print('Message after decryption:\n',dec)