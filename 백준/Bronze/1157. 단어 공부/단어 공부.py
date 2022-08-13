word = input().upper() #대문자
only_word = list(set(word))#대표글자

cnt_list =[] #대표글자갯수
for x in only_word:
    cnt = word.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(only_word[max_index])