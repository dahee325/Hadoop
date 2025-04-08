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


## 리눅스 환경에서 damf2만 github에 올리기
- `cd ../hadoop` : 하둡으로 위치 이동
- `git init` : branch master로 설정(기본이 master이므로 그냥 냅둬라~~)
- `git add .`
- `git commit -m "hadoop"` -> email, username 설정
- `git config --global user.email 'sally8323@gmail.com'`
- `git config --global user.name 'dahee325'`
- `git commit -m "hadoop"`
- `git remote add origin https://github.com/dahee325/Hadoop.git` -> 실패함 -> 리눅스에 github 계정 알려주는 라이브러리 설치
- `sudo apt-get install gh` : gh 라이브러리 설치
- GitHub.com -> HTTPS -> Yes -> Login with a web browser -> 링크 접속 후 코드 입력, 비밀번호 입력
- `git push origin master`