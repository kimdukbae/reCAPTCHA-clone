# Uncaptcha



+ 3rd grade 2nd semester Computer Security Project(2019/10/01 ~ 2019/12/05)
+ with : 김태현, 김상현, 박지훈, 박현우



## Introduction

+ 구글에서 컴퓨터와 사람을 구분하기 위하여 개발한 reCAPTCHA 프로그램을 딥러닝 분류 모델을 이용하여 노약자나 몸이 불편한 사람이 해결하기 쉽게 유도하는 프로그램 개발.

![image](https://user-images.githubusercontent.com/62137510/92397263-809b3b00-f161-11ea-87d4-d6671050c294.png)
![image](https://user-images.githubusercontent.com/62137510/92397280-8729b280-f161-11ea-9364-cf4cbb81b828.png)

* Confusion Matrix

![image-20200909164324639](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164324639.png)





## Process

![image-20200909164511031](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164511031.png)





## Usage

1. ![image-20200909164004137](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164004137.png)

'로봇이 아닙니다' 체크박스에 체크 후 아이디, 비밀번호 입력 (실제 로그인하는 환경과 유사하게 구현)





2. ![image-20200909164013374](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164013374.png)

Google reCAPTCHA와 유사하게 만든 HTML 실행





3. ![image-20200909164119738](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164119738.png)





4. Python Model Execution

![image-20200909164240483](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164240483.png)

Image Cropping 과정





5. ![image-20200909164334895](C:\Users\user33\AppData\Roaming\Typora\typora-user-images\image-20200909164334895.png)

The result of finding answer from Python Deep Learning model