import sys

# '296\t5.0'
currunt_movie_id = None
currunt_sum = 0
currunt_count = 0

for line in sys.stdin:
    line = line.strip()
    movie_id, rating = line.split()

    try: # 에러가 발생할 수도 있는 코드
        rating = float(rating)
    except: # 실행을 하다가 문제가 발생한다면
        continue # 실행중인 for문을 무시하고 다음 for문을 실행

    if currunt_movie_id == movie_id:
        currunt_count += 1
        currunt_sum += rating
    else:
        if currunt_movie_id is not None:
            currunt_avg = currunt_sum/currunt_count
            print(f'{currunt_movie_id}\t{currunt_avg}')

        currunt_movie_id = movie_id
        currunt_count = 1
        currunt_sum = rating

currunt_avg = currunt_sum/currunt_count
print(f'{currunt_movie_id}\t{currunt_avg}')