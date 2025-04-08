# hadoop command

- `ls`
    - `hdfs dfs -ls /`
    - `hdfs dfs -ls <확인하고싶은 경로>`

- `mkdir`
    - `hdfs dfs -mkdir /input`
    - `hdfs dfs -mkdir <생성하고싶은 폴더 이름>`

- `put`
    - `hdfs dfs -put ml-25m/movies.csv /input`
    - `hdfs dfs -put <업로드할 파일 경로> <업로드할 위치>`

- `cat`
    - `hdfs dfs -cat /input/movies.csv`
    - `hdfs dfs -cat <출력하고싶은 파일 경로>`

- `head`, `tail`
    - `hdfs dfs -head /input/movies.csv`
    - `hdfs dfs -head <출력하고싶은 파일 경로>`
    - `hdfs dfs -tail /input/movies.csv`
    - `hdfs dfs -tail <출력하고싶은 파일 경로>`
- `rm`
    - `hdfs dfs -rm /ratings.csv`
    - `hdfs dfs -rm <지울 파일 경로>`
    - 폴더를 삭제할 경우 `-r` 옵션 추가
    - `hdfs dfs -rm -r /input`