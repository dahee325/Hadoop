#!/usr/bin/env python3

import sys

# apple 1 -> line1
# apple 1 -> line2
# hello 1
# hello 1
# hello 1
# ....

last_word = None # 글자가 바뀌는 시점
total_count = 0

for line in sys.stdin: 
    word, value = line.split('\t') # 탭을 기준으로 쪼개기
    value = int(value) # 모든 데이터는 문자이므로 정수로 유형 바꿈

    if last_word == word:
        total_count += value
    else:
        if last_word is not None: 
        # None인 경우는 맨 처음, None이 아닌 경우는 단어에서 단어로 이어질 때
            print(f'{last_word}\t{total_count}')
        last_word = word # 글자가 바뀜
        total_count = value # 글자가 바꼈으니까 total_count 값 초기화

if last_word == word:
    print(f'{last_word}\t{total_count}')