import os


class MakeSubjectHTML:

    
    def __init__(self, subject_path:str, subject_name:str):
        self.subject_path = f"./static/mcq_data/{subject_path}"
        self.subject_path_download = f"./mcq_data/{subject_path}"
        self.files_list = os.listdir(self.subject_path)
        self.files_size = [(os.stat(f"{self.subject_path}/{file_name}").st_size)/1048576 for file_name in self.files_list]
        self.html_file_name = '_'.join(subject_path.split('/')) + ".html"
        self.subject_name = subject_name
        #print(self.html_file_name)

        self.initialize_f_string()
        self.content_fstring()
        self.end_fstring()
        self.save_html_text()

    
    def initialize_f_string(self):
        self.html_text = '''

        <!DOCTYPE HTML>

<html>
	<head>
		<title>SPPU BE MCQs</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />
	</head>

	<body class="is-preload homepage">
		<div id="page-wrapper">

			<!-- Header -->
				<div id="header-wrapper">
					<header id="header" class="container">

						<!-- Logo -->
							<div id="logo">
								<h1><a href="{{ url_for('index_page') }}">SPPU BE MCQs</a></h1>
								
							</div>

						<!-- Nav -->
						<nav id="nav">
							<ul>
								<li class="current"><a href="{{ url_for('index_page') }}">Home</a></li>
								<li><a href="{{ url_for('submit_page') }}">Submit</a></li>
							</ul>
						</nav>

     </header>
       </div>

       <!-- Main -->
				<div id="main-wrapper">
					<div class="container">
						<div class="row gtr-200">
							<div class="col-8 col-12-medium">
								<div id="content">
        '''
    
    def content_fstring(self):

        #self.html_text += "test"

        self.html_text += f'''
        <h2>{self.subject_name}</h2>
        '''

        for i in range(0, len(self.files_list)):
            self.html_text += f'''
                <a href="{{{{ url_for('static', filename='{self.subject_path_download}/{self.files_list[i]}') }}}}" class="download_button">
                <div class="downloadicon">
                <div class="cloud"><div class="arrowdown"></div></div>
                </div>
                <div class="filename"><span class="value">{self.files_list[i][:18]}</span></div>
                <div class="filesize">Size : <span class="value">{self.files_size[i]:.2f} MB</span></div>
                </a> 
            '''

    def end_fstring(self):

        self.html_text += '''
        </div>
								</div>
       </div>
      </div>
     </div>
       
       <!-- Footer -->
				<div id="footer-wrapper">
					<footer id="footer" class="container">
						<div class="row">
							<div class="col-12">
								<div id="copyright">
									<ul class="menu">
										<li>Site is not affiliated with Savitribai Phule Pune University (SPPU) in anyway.
										Site owner does not claim copyright to any of the content.</li>
									</ul>
									Designed and created by <a href="http://github.com/zz-xx">zz-xx.</a><br />
									Special thanks to <a href="http://github.com/indranil53">indranil53.</a>
								</div>
							</div>
						</div>
					</footer>
				</div>

			</div>

		<!-- Scripts -->
			<script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
			<script src="{{ url_for('static', filename='js/jquery.dropotron.min.js') }}"></script>
			<script src="{{ url_for('static', filename='js/browser.min.js') }}"></script>
			<script src="{{ url_for('static', filename='js/breakpoints.min.js') }}"></script>
			<script src="{{ url_for('static', filename='js/util.js') }}"></script>
			<script src="{{ url_for('static', filename='js/main.js') }}"></script>
			
	</body>
</html>

        '''
    
    def save_html_text(self):

        fileStream = open(f"./templates/{self.html_file_name}", 'w')
        fileStream.write(self.html_text)