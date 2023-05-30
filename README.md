# LikeLion


## 영남대학교 멋쟁이사자처럼 11기 
## 과제업로드 및 수행과정
## 공통트랙 HTML/CSS 실습
  ### - Week1 학생 관리 프로그램
  ### - 1) Week1 과제파일
  ### - 2) Week1 코드리뷰
  ### - Week2 Django 블로그 모델링 
  ### - 1) Week2 과제파일 models.py

  ### - 2) Week2 코드리뷰 
  #### - Blog의 _str__
  #### Blog 안에 str 메소드의 리턴값이 잘못 지정됨.def str은 해당 객체를 print()로 찍어서 확인할 때, 반환할 문자열 데이터를 리턴하는데, 나의 코드에는 blog필드가 존재하지 않는데 return self.blog가 사용되어있다. 따라서 return.self.title로 수정해야 함.
  #### - Post 클래스의 content_img와 content_file
  #### Post 클래스에서 content_img = models.ImageField() , content_file 두개의 기본값이 null로 지정되어야할 것 같음. post의 content 내용 및 제목이면 몰라도, 파일이랑 이미지가 없으면 게시글을 올릴수 없는 부분이 좀 어색한것 같음. 
  ''' content_img = models.ImageField(null=True)
      content_file = models.FileField(null=True)
  '''
  #### - class Neighbor
  #### 이웃추가 개념을 설계한 부분이 좋았음. 그런데 팔로워, 팔로잉이 누구의 정보인지 설계되어 있지 않는 것 같음. 그리고 date_added가 새로운 이웃이 추가될 때마다 datetime이 기록되는 걸 설계한 것 같은데 객체의 user를 참조하는 새로운 테이블을 만드는 방법으로 해야하지 않는지 ?