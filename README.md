# Uncaptcha



+ 3rd grade 2nd semester Computer Security Project(2019/10/01 ~ 2019/12/05)
+ with : 김태현, 김상현, 박지훈, 박현우

<br>

## Introduction

+ 구글에서 컴퓨터와 사람을 구분하기 위하여 개발한 reCAPTCHA 프로그램을 딥러닝 분류 모델을 이용하여 노약자나 몸이 불편한 사람이 해결하기 쉽게 유도하는 프로그램 개발.

![image](https://user-images.githubusercontent.com/62137510/92397263-809b3b00-f161-11ea-87d4-d6671050c294.png)
![image](https://user-images.githubusercontent.com/62137510/92397280-8729b280-f161-11ea-9364-cf4cbb81b828.png)

<br>


## Process

![2](https://user-images.githubusercontent.com/50494545/92570999-8a39b580-f2bd-11ea-99d0-b612453c1136.PNG)


<br>


## Usage

1. 
![3](https://user-images.githubusercontent.com/50494545/92571029-91f95a00-f2bd-11ea-9c17-2ee69c803525.PNG)

'로봇이 아닙니다' 체크박스에 체크 후 아이디, 비밀번호 입력 (실제 로그인하는 환경과 유사하게 구현)

<br>
<br>


2. 
![4](https://user-images.githubusercontent.com/50494545/92571061-9aea2b80-f2bd-11ea-92c4-74ee4cf0eec8.png)

Google reCAPTCHA와 유사하게 만든 HTML 실행

<br>
<br>


3. 
![5](https://user-images.githubusercontent.com/50494545/92571082-a2a9d000-f2bd-11ea-9917-336ab3fe0233.png)

<br>
<br>


4. Python Model Execution

![6](https://user-images.githubusercontent.com/50494545/92571113-accbce80-f2bd-11ea-8146-083c66e814d2.png)

Image Cropping 과정

<br>
<br>


5. 
![7](https://user-images.githubusercontent.com/50494545/92571140-b35a4600-f2bd-11ea-8724-e03ed811630f.png)

The result of finding answer from Python Deep Learning model

<br>
<br>

## Confusion Matrix

![1](https://user-images.githubusercontent.com/50494545/92570976-81e17a80-f2bd-11ea-9a0e-d9cde18e7e6c.PNG)

