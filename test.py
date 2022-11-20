import json

def get_start(string:str)->int:
    return string.find(" ",string.find(" ")+1)+1

def get_time(string:str)->float:
    l = string[get_start(string):].split(',')
    chas,min,sec = map(int,l[0].split(':'))
    return chas*3600+min*60+(sec+int(l[1])/(10**(len(l[1])-1)))

def get_difference(string:str)->list:
    times_start = []
    times_finish = []
    array_numbers=[] #номера участников
    for line in open(string):
        if line.split()[1] == "start":
            times_start.append(get_time(line))
            array_numbers.append(line.split()[0])
        else:
            times_finish.append(get_time(line))
    y=0
    array_times = [] #массив с разницей между финишем и стартом
    while y!=len(times_start):
        array_times.append(times_finish[y]-times_start[y])
        y+=1
    dictoinary = dict()
    dictoinary = dict.fromkeys(array_times)
    z=0
    for i in dictoinary:
        dictoinary[i]=array_numbers[z]
        z+=1
    return dictoinary,array_times

def read_json(string:str)->dict:
    with open(string, newline='', encoding="utf-8") as file:
        return json.load(file) 

def convert(sec:int)->str:
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600 
    min = sec // 60 
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec)

def search_time(string:str,number:str)->str:
    file = open(string)
    for line in file:
        l = line.split()
        if l[0]==number: 
            if l[1] == "start": 
                start = l[2].split(',')[0]
            else:
                finish = l[2].split(',')[0]
    chas,min,sec = map(int,finish.split(':'))
    a = chas*3600+min*60 + sec # итоговое время в секундах для финиша
    chas,min,sec = map(int,start.split(':'))
    a = a - (chas*3600+min*60 + sec)
    return convert(a)
dictonary,array_times = get_difference("results_RUN.txt")
array_times.sort()
prizes = []
for i in range(4):
    prizes.append(dictonary[array_times[i]])

print("| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |\n| --- | --- | --- | --- | --- |")
d = read_json('competitors2.json')
for i in range(0,4):
    print(f"| {i+1} | {prizes[i]} |" + " | " + d[prizes[i]]["Name"] + " | "+d[prizes[i]]["Surname"] + " | " + search_time("results_RUN.txt",prizes[i]))
