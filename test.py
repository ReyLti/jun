def get_start(string):
    return string.find(" ",string.find(" ")+1)+1

def get_time(string):
    l = line[get_start(string):].split(',')
    chas,min,sec = map(int,l[0].split(':'))
    return chas*3600+min*60+(sec+int(l[1])/(10**(len(l[1])-1)))

file = open("results_RUN.txt","r")
time: float = 61200
for line in file:
    if get_time(line)<time:
        first:str = line.split()[0]
print(first)