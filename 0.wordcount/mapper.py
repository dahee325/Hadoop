#!/usr/bin/env python3

import sys # system

# 파일을 줄별로 쪼개기
for line in sys.stdin: # stdin(standardinput) : 파일 전체
    line = line.strip() # 좌우 공백 없애기
    words = line.split() # 띄어쓰기를 기준으로 단어 쪼개기
    # words에는 리스트의 형태로 ['apple', 'hello', 'world'] 저장되어있음
    
    for word in words:
        print(f'{word}\t1') # \t : 탭(간격두기)