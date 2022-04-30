# cumputer network first project (develop socket connection)

**_이번 프로젝트 과제_** 는 socket 통신을 구현하여 지정된 기능들을 구현해야한다. Python에서 제공하는 socket 라이브러리를 이용하여 구현하였고, 파일 입출력을 통해 실제로 클라이언트가 request 를 보냈을 때 서버가 동작을 하는것을 보여준다.

## 🚀 과제 목표
1. Server side : 유저 정보를 저장하고 유저의 권한에 따라 다른 정보를 제공할 수 있는 API가 구현 되어야 한다.
2. Client side : API를 요청할 수 있는 기능(fetch)이 구현되어야 한다.

## 📈 순서도
![FlowChart](./media/sunsu.jpeg)

---

## 🖥 동작환경
<table>
<tbody>
    <tr>
        <td>
            <div align="center">
                <a href="https://www.python.org/" target="_blank"> 
                    <img src="https://w.namu.la/s/bb31da51908612e116718c9ae59e1cf987ec41fac823c06b89a3d8a4e878f0bbba19b238dbd457495f64331f66d1bd8a188b2bf9db5625f805559a79b3151b37b73ea84b425cea0d6c89677b1174145f265a07d1f83c20719d5aa62cf25f14c3" alt="python" width="40" height="40"/> 
                </a>
                <br>server : mac os</br></div>
        </td>
        <td>
            <div align="center">
                <a href="https://babeljs.io/" target="_blank"> <img src="https://e-wiseweb.com/blog/6/6_1.jpg" alt="babel" width="40" height="40"/> 
                </a>
                <br>client : windows10</br>
            </div>
        </td>
</tbody>
</table>

---

## 🧚🏻‍♀️ 핵심 모듈

<table>
<tbody>
    <tr>
        <td width="60">
            <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/220px-Python-logo-notext.svg.png" alt="python" width="40" height="40"/> </a><br>Python3</br></div>
        </td>
        <td>
            <div align="center"><a href="https://babeljs.io/" target="_blank"> <img src="https://studygyaan.com/wp-content/uploads/2021/12/Python-Socket-IO.jpg?ezimgfmt=rs:300x150/rscb1/ng:webp/ngcb1" alt="babel" width="40" height="40"/> 
            </a><br>Python Socket</br></div>
        </td>
        <td>
            <div align="center"><a href="https://docs.python.org/ko/3/library/json.html" target="_blank"> <img src="https://velog.velcdn.com/images/swhan9404/post/c43940fd-06ab-4fe6-b905-df695506ce8c/d2f1b26783.png" alt="babel" width="40" height="40"/> 
            </a><br>Python Json</br></div>
        </td>
</tbody>
</table>

---

## 👩‍💻 기능 & 라우트 명세

### - ROUTE
- 127.0.0.1 : root and request path

### - HTTP METHOD

#### 1. POST
- 200(login Success) : 사용자의 아이디와 비밀번호를 받아 로그인 성공 정보와 권한 정보를 반환한다. (권한 정보 : 1. 관리자 / 2. 일반 유저)
- 401(login Fail) : 등록되지 않은 유저정보로 로그인을 시도할 경우 401을 반환한다.

#### 2. GET
- 200 (Success) 권한이 관리자일 경우 : 지금까지 저장된 회원 정보를 반환한다. 
- 200 (Success) 권한이 일반 유저일 경우 : 본인의 정보만 반환한다. 
- 403(Forbidden) : 로그인이 되지 않은 클라이언트가 요청할 시 403을 반환한다..

#### 3. PUT
- 201 (Create Success) : 새로운 유저 정보를 생성한다.
- 400 (Bad request) : 이메일 혹은 패스워드의 길이가 1이하일 경우 400을 반환한다.

#### 4. HEAD
- 200(Success) : server의 현재 상태를 반환한다.

---

## 🌠 실행 결과

- POST (login) <br>
<table>
	<tbody>
		<tr>
            <td rowspan="6"><div align="center"><img src="https://primer.dynamobim.org/ko/10_Custom-Nodes/images/10-4/Exercise/Revit/Images/RevitPython%20-%2006.png" width="40%" height="40%"></a></div></td>
            <td width="33%"></td>
        </tr>
        <tr>
            <td>로그인 기능</td>
        </tr>
        <tr>
            <td>전송된 이메일에 따라 admin인지 user인지 판별</td>
        </tr>
    </tbody>
</table>

- GET (get user data) <br>
<table>
	<tbody>
		<tr>
            <td rowspan="6"><div align="center"><img src="https://primer.dynamobim.org/ko/10_Custom-Nodes/images/10-4/Exercise/Revit/Images/RevitPython%20-%2006.png" width="40%" height="40%"></a></div></td>
            <td width="33%"></td>
        </tr>
	<tr>
	    <td>유저 정보 반환 기능</td>
	</tr>
        <tr>
            <td>if admin : return all user data</td>
        </tr>
        <tr>
            <td>if user : return only client's data</td>
        </tr>
    </tbody>
</table>

- PUT (insert new user data) <br>
<table>
	<tbody>
		<tr>
            <td rowspan="6"><div align="center"><img src="https://primer.dynamobim.org/ko/10_Custom-Nodes/images/10-4/Exercise/Revit/Images/RevitPython%20-%2006.png" width="40%" height="40%"></a></div></td>
            <td width="33%"></td>
        </tr>
	<tr>
	    <td>유저 정보 삽입기능</td>
	</tr>
    </tbody>
</table>

- HEAD (return only header(aka, server status)) <br>
<table>
	<tbody>
		<tr>
            <td rowspan="6"><div align="center"><img src="https://primer.dynamobim.org/ko/10_Custom-Nodes/images/10-4/Exercise/Revit/Images/RevitPython%20-%2006.png" width="40%" height="40%"></a></div></td>
            <td width="33%"></td>
        </tr>
	<tr>
	    <td>서버 상태 반환기능</td>
	</tr>
    </tbody>
</table>

---
## 💻 클라이언트 필수 조건 안내 

- python3 이상의 버전 지원
- 필요한 라이브러리들의 설치 유무
- 등