# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для 
# изменения и удаления данных/
def read(filename):
    data=[]
    fields=['Фамилия','имя','отчество','номер']
    with open (filename,'r',encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields,line.strip().split(',')))
            data.append(record)
    return printing(data)
def printing(col):
    for i in range(len(col)):
        print(col[i])
def write(filename,str):
    with open (filename,'a') as f:
        f.write(f'{str}')
def search(filename):
    print('поиск по имени-1, поиск по фамилии-2')
    choise=int(input())
    if choise==1:
        print('введите имя')
        key=input()
        # print(key)
        with open (filename,'r',encoding='utf-8') as fin:
            for line in fin:
                rec=list(line.strip().split(','))
                # print(list)
                if rec[1]==key:
                    print(key+': '+rec[3])
    elif choise==2:
        print('введите фамилию')
        key=input()
        # 
        with open (filename,'r',encoding='utf-8') as fin:
            for line in fin:
                rec=list(line.strip().split(','))
                if rec[0]==key:
                    print(key+': '+rec[3])
def rewrite(filename):
    import re
    with open(filename,'r',encoding='utf-8') as fin:
        lines=[]
        for line in fin:
            lines.append(line)
        print('введите фамилию абонента')
        pattern=input()
    with open(filename,'w',encoding='utf-8') as fin:
        for i in range(len(lines)):
             result = re.search(pattern,lines[i])
             if result is None:
                 fin.write(lines[i])
             else:
                rec=list(lines[i].strip().split(','))
                print('введите новый номер')
                rec[3]=input()
                line=",".join(rec)
                fin.write(f'{line}'+'\n')
    fin.close()   
def delete(filename):
    import re
    with open(filename,'r',encoding='utf-8') as fin:
        lines=[]
        for line in fin:
            lines.append(line)
        print('введите фамилию абонента')
        pattern=input()
    with open(filename,'w',encoding='utf-8') as fin:
        for i in range(len(lines)):
             result = re.search(pattern,lines[i])
             if result is None:
                 fin.write(lines[i])
    fin.close()           
print('Выберете операцию: 1. Чтение. 2. Добваить контакт 3. Поиск 4.Изменить номер телефона 5. Удалить контакт')
choise=int(input())
if choise==1:
    print(read('phon.txt'))
elif choise==2:
    print("введите данные в формате:Фамилия,имя,отчество,номер")
    a=input()
    print(write('phon.txt',a))
elif choise==3:
    print(search('phon.txt'))
elif choise==4:
    print(rewrite('phon.txt'))
elif choise==5:
   print(delete('phon.txt'))
# 15