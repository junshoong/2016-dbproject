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


## Git Command
```bash
$ # clone은 프로젝트를 컴퓨터로 받아옵니다. 최초에만 실행합니다.
$ git clone https://gitlab.com/vaporize93/2016_db_project.git
$ git checkout <team_branch>
$ # 이후에는 pull로 해당 프로젝트를 당겨옵니다.
$ git pull
$ # dev로부터 작업내용을 가져옵니다.
$ git merge dev
$ # 개발을 진행합니다.
$ git add -p
$ git commit -v
$ git push
```
[프로젝트페이지](https://gitlab.com/vaporize93/2016_db_project)에 접속해서  상단의 `Merge Requests`를 클릭합니다. source에 <team_branch>를 설정하고 target에 dev를 설정합니다. 충분한 내용을 적어주고 submit 합니다.  

이후에 모든 팀원이 확인이 되면 merge를 진행합니다.


## Member
공원배
김준수
고다경
김미소
