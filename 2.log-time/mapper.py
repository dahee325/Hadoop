import sys
import re # regular expression


time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})') # r':\d{2}' => `:`뒤에 digit이 2개 있어야함, 문자열 뒤에 있는 것은 정규 표현식이라는 것을 알려줌

for line in sys.stdin:
    line = line.strip()

    match = time_pattern.search(line)
    
    if match:
        hour = match.group(1) # `r':(\d{2}):(\d{2}):(\d{2})')`` 에서의 첫번째 괄호 선택
        print(f'{hour}\t1')