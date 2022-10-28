### 이상욱님, 신현강님과 함게 개발한 영화리뷰 게시판입니다.

### 핵심목표

- 비동기 처리 활용
- M:N 관계의 기능 구현(좋아요, 팔로우)

# Accounts

### 회원 가입

branch account/signup

앱 App 생성

- 앱 이름 : accounts

모델 Model 작성

- 모델 이름 : User
- Django AbstractUser 모델 상속

폼 Form 작성

- Django 내장폼 UserCreationForm을 상속받은 CustomUserCreationForm 작성

기능 View

- `POST` accounts/signup/
- CustomUserCreationForm 활용
- 회원가입 완료 후 자동으로 로그인 진행

화면 Template

- `GET` accounts/signup/
- 회원가입 폼

---

### 로그인

branch accounts/login

기능 View

- `POST` accounts/signup/
- 내장 폼 AuthenticationForm 활용

화면 Template

- `GET` accounts/signup/
- 로그인 폼
- login_required메서드를 활용하여 로그인 후 접속하려고 했던 페이지로 이동하거나 게시판 메인 페이지로 이동

---

### 로그아웃

branch accounts/logout

기능 View

- `POST` accounts/logout

---

### 마이페이지

기능 View

- accounts/detail.html
- request 정보의 user 객체에 대한 정보를 보여주며, 당연히 로그인이 필요하게 구현.
- user의 이름, 이메일, 아이디, 작성한 글, 작성한 댓글을 명시함.
- 작성한 글 과 작성한 댓글에는 바로 해당 글로 접근할 수 있는 링크를 삽입.
- 회원정보수정과 회원탈퇴 버튼으로 update.html 과 delete view 함수에 접근가능하다.
- 회원탈퇴 버튼은 Modal을 활용하여 한번 더 삭제의사를 물음으로써, 실수로 인한 계정삭제를 방지한다. 

---

### 회원정보

기능 View

- accounts/detail
- 리뷰 작성자 에 링크를 삽입하여 해당 유저의 정보 페이지를 볼 수 있도록 함.
- 유저 정보에는 이름, 이메일, 작성글, 작성댓글 등이 있음.

---

### 내 정보 수정

기능 View

- Django의 기본 ModelForm 인 UserChangeForm을 상속하여 CustomUserChangeForm 생성 및 활용
- 사용자로부터 수정할 정보를 입력받음(이름, 이메일)
- 비밀번호 수정 버튼을 삽입하여 비밀번호 수정 폼으로 이동할 수 있게 함.
  - 비밀번호 수정은 Django 의 PasswordChangeForm을 활용
  - update_session_auth_hash 메서드를 활용하여 비밀번호 변경 후에도 로그인을 유지할 수 있도록 함.
  - 비밀번호 변경 후 마이페이지로 이동
- 수정 후 마이페이지로 이동

---

### 팔로우

기능 view

- 유저 간에 정보를 detail페이지에서 볼 수 있고, 팔로우 할 수 있다. 이 때 팔로우는 로그인하지 않으면 진행되지 않으며, 버튼이 생성되지 않는다.
- 팔로우 버튼을 클릭하게 되면 views.py의 팔로우 함수를 통해 누가 누구를 팔로우하였는지 에 대한 테이블에 생성되며, 팔로우 버튼은 팔로우 취소버튼으로 변경된다. 이 때 모든 과정은 axios의 비동기처리를 통해서 이루어진다.



# Reviews

### 리뷰 작성

모델 Model 생성

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드                | 속성                              |
  | ---------- | ------------- | ------------------- | --------------------------------- |
  | user       | 리뷰 작성자   | Foreignkey          | User 모델 참조, on_delete=CASCADE |
  | title      | 리뷰 제목     | Char                | max_length=20                     |
  | image      | 이미지        | ProcessedImageField | ...                               |
  | content    | 리뷰 내용     | Text                |                                   |
  | movie_name | 영화 이름     | Char                | max_length=20                     |
  | grade      | 영화 평점     |                     | 이모티콘으로 1~5점까지 표현       |
  | created_at | 리뷰 생성시간 | DateTime            | auto_now_add=True                 |
  | updated_at | 리뷰 수정시간 | DateTime            | auto_now = True                   |

기능 View

모델폼, bootstrap form을 활용하여 사용자들의 요청을 받음.

모델폼의 구성으로는 title, content, movie_name, grade, image 가 있음. image는 Django 패키지인 imagekit과 파이썬 패키지인 pillow를 활용하여 사용자로부터 이미지파일을 받아 기준에 맞게 가공 후 저장하고, DB에는 그 저장경로만 입력하고 있음.

user를 외래키로 accounts 앱의 User 객체를 참조하고, views.py에서 요청을 보낸 user 객체를 review를 작성한 user에 넣는 로직을 구현.

글 목록을 제외한 모든 html 페이지는 로그인을 해야 접근가능하도록 구현.

------

### 리뷰 목록 조회

branch reviews/index

**기능 View**

- `GET` reviews/
- 모든 리뷰를 id, 글제목, 영화이름, 평점으로 표현
- 각 객체에는 detail로 이동할 수 있는 자세히보기 버튼이 있음
- 검색기능을 추가하여 글 제목과 영화제목을 검색할 수 있음.

**화면 Template**

- `GET` reviews/

------

### 리뷰 정보 조회

branch reviews/detail

**기능 View**

- `GET` reviews/\<int:pk>/

**화면 Template**

- `GET` reviews/\<int:pk>/
- 별점은 5점을 만점으로 1점당 별 1개씩 부여하며 나머지는 빈 별로 대체한다.
- 리뷰 수정 / 삭제 버튼
  - 수정 / 삭제 버튼은 해당 리뷰 작성자에게만 출력.
- 댓글 목록
  - 댓글을 추가할 때마다 페이지를 새로고침하는 것이 아닌, 비동기 방식으로 db의 댓글에만 다시 접근하여 댓글 목록만 재구성하게 구현.
  - 댓글 삭제 버튼은 댓글 작성자에게만 출력.
- 댓글 작성 폼
  - 댓글 작성 폼은 로그인 사용자에게만 출력.
- 좋아요 기능
  - 리뷰 객체에 유저를 참조하여 좋아요 기능을 구현.
  - 빈 하트 버튼을 누르면 DB에 그 관계가 저장되고, 좋아요를 이미 누른, 꽉찬 하트모양으로 변경.
  - 하트 옆에는 그 리뷰가 얼마나 많은 좋아요를 받았는지 개수를 카운트 하여 출력.
  - 모든 과정은 비동기처리를 통해 이루어짐.(페이지 새로고침이 되지 않음)

------

### 리뷰 정보 수정

branch reviews/update

**기능 View**

- `POST` reviews/\<int:pk>/update/
- 데이터를 생성한 사용자만 수정할 수 있습니다.
- 리뷰 수정 후 수정 된 페이지(detail.html)로 이동

**화면 Template**

- `GET` reviews/\<int:pk>/update/
- 리뷰 수정 폼

------

### 리뷰 삭제

branch reviews/delete

**기능 View**

- `POST` reviews/\<int:pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.
- 리뷰 삭제 후 리뷰 목록으로 이동

------

### 댓글 작성

branch comments/create

모델 Model 생성

모델 이름 : Comment

- 모델 필드

  | 이름       | 역할        | 필드       | 속성                                            |
  | ---------- | ----------- | ---------- | ----------------------------------------------- |
  | review     | 참조 리뷰   | Foreignkey | reviews 의 Review 모델 참조 on_delete = CASCADE |
  | user       | 댓글 작성자 | Foreignkey | accounts 의 User 모델 참조 on_delete = CASCADE  |
  | content    | 댓글 내용   | Char       | max_length=100                                  |
  | created_at | 작성 일자   | DateTime   | auto_now_add=True                               |

기능 View

- `POST` reviews/\<int:pk>/comment_create/
- 로그인한 사용자만 댓글작성 가능

- 리뷰 정보 조회 페이지 하단에 댓글 작성 폼 출력
- 리뷰 정보 조회 페이지 하단에 댓글 목록 출력
- 댓글 작성 후 현재 페이지(detail.html)유지

------

### 댓글 삭제

branch comments/delete

기능 View

- `POST` reviews/\<int:review_pk>/comments/\<int:comment_pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

- 각 댓글에 리뷰 삭제 버튼 추가
  - 삭제 버튼은 해당 댓글 작성자에게만 출력합니다
- 댓글 삭제 후 현재 위치(detail.html) 그대로 유지

