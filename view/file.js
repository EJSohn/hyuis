var lines = ''+'<nav id="gnb" class="navbar navbar-default navbar-fixed-top">'+'<div class="container">'+
			'<div class="navbar-header">'+
				'<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">'+
			        '<span class="sr-only">Toggle navigation</span>'+
			        '<span class="icon-bar"></span>'+
			        '<span class="icon-bar"></span>'+
			        '<span class="icon-bar"></span>'+
			    '</button>'+
				'<a class="navbar-brand" href="main.html">HYUIS</a>'+
			'</div>'+
			'<div id="bs-example-navbar-collapse-1" class="collapse navbar-collapse">'+
				'<ul class="nav navbar-nav navbar-right">'+
					'<li><a href="login.html">로그인</a></li>'+
					'<li><a href="register.html">회원가입</a></li>'+
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