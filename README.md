# cumputer network first project (develop socket connection)

**_이번 프로젝트 과제_** 는 socket 통신을 구현하여 지정된 기능들을 구현해야한다. Python에서 제공하는 socket 라이브러리를 이용하여 구현하였고, 파일 입출력을 통해 실제로 클라이언트가 request 를 보냈을 때 서버가 동작을 하는것을 보여준다.

## 🚀 과제 목표

~~ 흐름 그림으로 설명 불라불라
1. 서버 : 서버를 구동시킨다 (on listen)
2. 클라리언트 : 구현된 메소드에 request 를 보낸다.
3. 서버 : 적절한 기능을 수행한 뒤 결과를 반환한다.

---

## 🖥 라우트 구성
[Alpha](https://github.com/IcaliaLabs/alpha)
- **123.123.123.123/home**
  - 


---

## 🧚🏻‍♀️ 사용할 라이브러리

<table>
<tbody>
    <tr>
        <td width="60">
            <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/220px-Python-logo-notext.svg.png" alt="python" width="40" height="40"/> </a><br>Python3</br></div>
          <td>
            <div align="center"><a href="https://babeljs.io/" target="_blank"> <img src="https://studygyaan.com/wp-content/uploads/2021/12/Python-Socket-IO.jpg?ezimgfmt=rs:300x150/rscb1/ng:webp/ngcb1" alt="babel" width="40" height="40"/> 
            </a><br>Python Socket</br></div>
        </td>
</tbody>
</table>
---

## 👩‍💻 기능 & 라우트 명세

### - ROUTE
- 111.111.111.111:12345/ : root and request path

### - HTTP METHOD

#### 1. POST
- 200(Success) : 사용자가 보낸 단어를 텍스트 파일에 추가한다.
- 400(Bad request) : 사용자가 보낸 단어가 영문자와 숫자로 이루어지지 않았다면 에러 발생.

#### 2. GET
- 200(Success) : 지금까지 저장된 텍스트 파일을 반환한다. 
- 401(Unauthenticated) : 인가되지 않은 사용자가 요청하면 거부한다.

#### 3. PUT
- 200(Success) : 공백을 기준으로, 첫 번째 단어를 두 번째 단어로 수정한다.
- 400(Bad request) : 수정될 단어가 유효하지 않은 경우 에러 발생.

#### 4. DELETE
- 200(Success) : 사용자가 보낸 단어가 정상적으로 삭제된다.
- 400(Bad request) : 삭제될 단어가 유효하지 않은 경우 에러 발생.

#### + Plus
- 501(interval server error) : 통신 도중 서버 로직의 문제로 에러 발생.
- 504(Gateway timeout) : 비정상적으로 연결이 종료 혹은 타임아웃.
- 404(not found error) : 유효하지 않은 경로로 접근할 시 에러 발생.

---
## 🌠 실행 결과
- 챗봇 페이지 <br>
<table>
	<tbody>
		<tr>
            <td rowspan="6"><div align="center"><img src="https://github.com/osamhack2020/WEB_Meditact_Meditact/blob/main/src/demo.gif" width="40%" height="40%"></a></div></td>
            <td width="33%">NLP를 이용한 진료과 분류</td>
        </tr>
	<tr>
	    <td>버튼기반의 편리한 UI/UX 제공</td>
	</tr>
        <tr>
            <td>병원 예약 기능</td>
        </tr>
        <tr>
            <td>상담 연결 및 군 병원 정보를 출력</td>
        </tr>
    </tbody>
</table>

---
## 💻 클라이언트 필수 조건 안내 

- python3 이상의 버전 지원
- 필요한 라이브러리들의 설치 유무
- 등