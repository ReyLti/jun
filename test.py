def get_start(string):
    return string.find(" ",string.find(" ")+1)+1

def get_time(string):
    l = line[get_start(string):].split(',')
    chas,min,sec = map(int,l[0].split(':'))
    return chas*3600+min*60+(sec+int(l[1])/(10**(len(l[1])-1)))

file = open("results_RUN.txt","r")
times_start = []
times_finish = []
for line in file:
    if line.split()[1] == "start":
        times_start.append(get_time(line))
    else:
        times_finish.append(get_time(line))
print(times_start)
print(times_finish)