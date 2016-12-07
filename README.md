# 데이터베이스 프로젝트
## 주제
성공회대학교 동문회 프로그램 개발


## 내용
동문회 프로그램 개발


## 작업도구
- Django
- MariaDB
- Mysql Workbench
- Slack
- git (with gitlab)


## Process
- 각자의 Branch나 팀의 Branch에서 작업을 진행합니다.
- 팀 Branch에서 기능이 작성되면 개발 Branch로 병합합니다.
- Main Branch는 기능이 완성되는 경우 검토 후 병합합니다.
- Main Branch에서는 구현된 모든 기능이 항상 동작하여야 합니다.

위 프로세스는 팀별로 의논 후 변동가능 합니다. 하지만 기본적으로 서로 코드리뷰는 진행하도록 합니다.


## 초기 작업 

### 가상환경 설정

```bash
$ # 가상환경 설정을 해줍니다. virtualenv, virtualenvwrapper가 설치되어 있어야합니다.
$ mkvirtualenv dbp
$ echo "cd ~/dbp" >> ./bin/postactivate
$ cd ~
```

### git을 사용해서 프로젝트 받아오기 

```bash
$ # clone은 프로젝트를 컴퓨터로 받아옵니다. 최초에만 실행합니다.
$ # 이후에는 git pull로 해당 프로젝트를 당겨옵니다.
$ git clone https://gitlab.com/vaporize93/2016_db_project.git dbp
$ cd dbp
$ git checkout dev
$ git checkout kims
$ git merge dev
```

### 패키지를 설치

```bash
$ pip install -r requirements.txt
```

### mysql 작업

테이블과 사용자를 만들고 권한을 부여 합니다.
<user>와 <password> 부분은 꺽쇠를 제외하고 작성하세요.
```sql
CREATE DATABASE skhualumni CHARACTER SET UTF8;
CREATE USER <user>@localhost IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON skhualumni.* TO <user>@localhost;
FLUSH PRIVILEGES;
```

### 설정파일 작성

`skhualumni/my.cnf` 를 작성합니다.
`<user>`, `<password>` 부분은 위에서 작성한 내용을 적어 줍니다.

```
[client]
database=skhualumni
user=<user>
password=<password>
default-character-set=utf8
```

### Django 시작

```bash
$ cd skhualumni
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```

### 기존 DB와 crash가 나는경우

```bash
$ ./manage.py migrate --fake <app_name> zero
$ ./manage.py migrate
```

[프로젝트페이지](https://gitlab.com/vaporize93/2016_db_project)에 접속해서  상단의 `Merge Requests`를 클릭합니다. source에 <team_branch>를 설정하고 target에 dev를 설정합니다. 충분한 내용을 적어주고 submit 합니다.  

이후에 모든 팀원이 확인이 되면 merge를 진행합니다.

### Deploy

배포 관련내용 입니다.
```bash
apt install docker.io git
git clone https://gitlab.com/vaporize93/2016_db_project
cd 2016_db_project

docker pull mysql
docker run --name db -e MYSQL_ROOT_PASSWORD=qq1234 -d mysql
docker exec -it db bash
# mysql -uroot -p
> CREATE DATABASE skhualumni CHARACTER SET UTF8;
> exit;
# exit

docker build -t harvey/dbp .
docker run --name=skhudbp \
    --publish=80:80 \
    --link db:db \
    --env="DJANGO_SETTINGS_MODULE=skhualumni.production_settings" \
    --env="MYSQL_ROOT_PASSWORD=qq1234" \
    --env="PYTHONIOENCODING=UTF-8" \
    -d harvey/dbp

docker exec -it skhudbp bash
# python3 manage.py createsuperuser
# exit
```


## Member
공원배
김준수
고다경
김미소
