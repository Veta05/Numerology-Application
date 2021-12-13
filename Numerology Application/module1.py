def read_from_file(file:str)->list:
    file=open(file,"r", encoding="UTF-8-sig")
    mas=[]
    for line in file:
        mas.append(line.strip())
    file.close()
    return mas

#def first(name,lbl3):
#    text = list(name)
#    lbl3.configure(text=text)
#    return

def name_number(l:list,n:list,name:str,lbl3):
    name=list(name)
    numbers_index=int()
    for i in name:
        letters_index=l.index(i)
        numbers_index+=int(n[letters_index])
    if numbers_index <10:
        text=f"Твоё число имени - {numbers_index}"
    elif numbers_index>=10:
        first=numbers_index//10
        second=numbers_index%10
        numbers_index=first+second
        text=f"Твоё число имени - {numbers_index}"
    if numbers_index>=10:
        first=numbers_index//10
        second=numbers_index%10
        numbers_index=first+second
        text=f"Твоё число имени - {numbers_index}"
    if numbers_index==1:
        file = open('one.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==2:
        file = open('two.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==3:
        file = open('three.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==4:
        file = open('four.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==5:
        file = open('five.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==6:
        file = open('six.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==7:
        file = open('seven.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==8:
        file = open('eight.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    elif numbers_index==9:
        file = open('nine.txt', 'r', encoding='UTF-8-sig')
        f=file.read()
    lbl3.configure(text = f)
    return numbers_index
