import errno
import json
import os
from werkzeug.utils import secure_filename

from flask import Flask, request, render_template, send_from_directory, make_response


mcq_data_dict = None
app = Flask(__name__)


# favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.png', mimetype='image/png')


@app.route('/')
def home_page():
    mcq_data_folder_path = f"./static/mcq_data/"
    mcq_data_branch_list = [x for x in next(os.walk(mcq_data_folder_path))[1]]
    branch_long_names = [mcq_data_dict[branch_folder]["full_name"]
                         if branch_folder in mcq_data_dict else branch_folder for branch_folder in mcq_data_branch_list]
    branch_short_names = [mcq_data_dict[branch_folder]["short_name"]
                          if branch_folder in mcq_data_dict else branch_folder for branch_folder in mcq_data_branch_list]
    return render_template('index.html', mcq_data_branch_list=mcq_data_branch_list,
                           branch_long_names_list=branch_long_names, branch_short_names_list=branch_short_names)


@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit_page():

    if request.method == 'POST':
        contact_name = request.form["name"]
        contact_email = request.form["email"]
        contact_message = request.form["message"]
        contact_branch = request.form["branch"]
        contact_subject = request.form["subject"]

        for uploaded_file in request.files.getlist('image-file'):
            if uploaded_file.filename != '':
                uploaded_file.save(
                    f"./static/uploads/{uploaded_file.filename}")

        upload_metadata = {"name": contact_name,
                           "email": contact_email,
                           "message": contact_message,
                           "branch": contact_branch,
                           "subject": contact_subject}

        with open("./static/uploads/" + request.files.getlist('image-file')[0].filename + ".json", "w") as outfile:
            json.dump(upload_metadata, outfile)

    return render_template('submit.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/<branch>/<subject>')
@app.route('/<branch>/', defaults={'subject': None})
def main_route(branch, subject):
	try:
		if subject is None:
			branch_folder_path = f"./static/mcq_data/{branch}"
			branch_subjects_folders_list = [
				x for x in next(os.walk(branch_folder_path))[1]]
			subject_long_names = [mcq_data_dict[branch]["subjects"][subject_folder]["full_name"] if subject_folder in mcq_data_dict[branch]
								  ["subjects"] else subject_folder for subject_folder in branch_subjects_folders_list]
			subject_short_names = [mcq_data_dict[branch]["subjects"][subject_folder]["short_name"]
								   if subject_folder in mcq_data_dict[branch]["subjects"] else subject_folder for subject_folder in branch_subjects_folders_list]
			return render_template("engineering-branch.html", branch=branch, subjects_list=branch_subjects_folders_list,
								   subject_long_names_list=subject_long_names, subject_short_names_list=subject_short_names)

		else:
			subject_folder_path = f"./static/mcq_data/{branch}/{subject}"
			subject_files_list = os.listdir(subject_folder_path)
			subject_files_size = [round((os.stat(
				f"{subject_folder_path}/{file_name}").st_size)/1048576, 2) for file_name in subject_files_list]
			subject_dict = {
				"files_list": subject_files_list,
				"files_size": subject_files_size
			}
			subject_full_name = mcq_data_dict[branch]["subjects"][subject][
				"full_name"] if subject in mcq_data_dict[branch]["subjects"] else subject
			output_from_parsed_template = render_template(
				'engineering-subject.html', subject_dict=subject_dict, branch=branch, subject_folder=subject, subject_full_name=subject_full_name)
			return output_from_parsed_template
	except:
		return make_response(page_not_found(404))


def read_mcq_data():
    global mcq_data_dict
    with open("./static/mcq_data/mcq_data.json") as json_file:
        mcq_data_dict = json.load(json_file)


if __name__ == '__main__':
    read_mcq_data()
    app.run()
