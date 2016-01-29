var lines = ''+'<nav id="gnb" class="navbar navbar-default navbar-fixed-top">'+'<div class="container">'+
			'<div class="navbar-header">'+
				'<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">'+
			        '<span class="sr-only">Toggle navigation</span>'+
			        '<span class="icon-bar"></span>'+
			        '<span class="icon-bar"></span>'+
			        '<span class="icon-bar"></span>'+
			    '</button>'+
				'<a class="navbar-brand" href="index.html">HYUIS</a>'+
			'</div>'+
			'<div id="bs-example-navbar-collapse-1" class="collapse navbar-collapse">'+
				'<ul class="nav navbar-nav navbar-right">'+
					'<li class="dropdown">'+
						'<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">로그인</a>'+
			          '<ul id="login-menu" class="dropdown-menu" role="menu">'+
			            '<li><form class="form-inline" action="/authen/login" method="POST">{% csrf_token %}'+
						  '<div class="form-group">'+
						    '<label class="sr-only">ID</label>'+
						    '<input type="text" id="user_id" placeholder="ID">'+
						  '</div>'+
						  '<div class="form-group">'+
						    '<label class="sr-only">Password</label>'+
						    '<input type="password"  id="password" placeholder="Password"></div>'+
						    '<button type="submit" id="login-btn" class="btn btn-default" >Sign in</button></form>'+
						    '<p class="login-alpa"><a href="#">아이디/비밀번호 찾기</a> | <a href="http://localhost:8000/authen/register">회원가입</a></p></li>'+
			          '</ul>'+
			        '</li>'+
					'<li class="dropdown">'+
			          '<a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">연관사이트 <span class="caret"></span></a>'+
			          '<ul class="dropdown-menu" role="menu">'+
			            '<li><a href="http://www.hanyang.ac.kr/">한양대학교</a></li>'+
			            '<li><a href="https://portal.hanyang.ac.kr/sso/lgin.do">Hy-in</a></li>'+
			            '<li><a href="http://www.hanyang.ac.kr/code_html/H3HADE/">정보시스템학과</a></li>'+
			            '<li class="divider"></li>'+
			            '<li><a href="http://ak.hanyang.ac.kr/">쿷찡 사이트</a></li>'+
			          '</ul>'+
			        '</li>'+
				'</ul>'+
			'</div>'+
		'</div>'+
		'</nav>';
document.write(lines);