import sys

# 파일을 줄별로 쪼개기
for line in sys.stdin:
    line = line.strip()

    # 쉼표를 기준으로 쪼개기
    fields = line.split(',')
    # ['1', '296', '5.0', '1147880044']

    movie_id = fields[1]
    rating = fields[2]

    print(f'{movie_id}\t{rating}')