def find(s, i):
    j = i + 1
    print(s[i], s[j], j)

    while '0' <= s[j] <= '9' and j < len(s) - 1:
        j += 1
    print(s[i + 1:j])
    print()



file = open('filename.txt', 'r')
s = file.readline()


list = []
count = -1

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        list.append([s[i]])
        count += 1
    elif 'A' <= s[i] <= 'Z':
        list.append([s[i]])
        count += 1
    elif '0' <= s[i] <= '9':
        list[count].append(s[i])


for i in range(len(list)):
    str2 = ''
    for j in list[i][1::]:
        str2 = str2 + j
    print(list[i][0]*int(str2), end='')
print()
















