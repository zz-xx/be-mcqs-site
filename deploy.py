import os
import json
import errno
from werkzeug.utils import secure_filename

from flask import Flask
from flask import Flask, request, render_template, send_from_directory

from helpers import make_subject_html


app = Flask(__name__)
# create folder to save uploads
#os.makedirs(os.path.join(app.instance_path, 'uploads'), exist_ok=True)


# favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'),
                               'favicon.png', mimetype='image/png')


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/index')
def index_page():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit_page():

    if request.method == 'POST':
        # print("post")
        contact_name = request.form["name"]
        contact_email = request.form["email"]
        contact_message = request.form["message"]
        contact_branch = request.form["branch"]
        contact_subject = request.form["subject"]

        print(request.files.getlist('image-file'))

        for uploaded_file in request.files.getlist('image-file'):
            if uploaded_file.filename != '':
                print(os.path.join(app.instance_path, 'uploads',
                                   secure_filename(uploaded_file.filename)))
                #uploaded_file.save(os.path.join(app.instance_path, 'uploads', secure_filename(uploaded_file.filename)))
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


@app.route('/comp')
def computer_engineering_page():
    return render_template('computer-engineering.html')


@app.route('/it')
def it_engineering_page():
    return render_template('it-engineering.html')


@app.route('/entc')
def entc_engineering_page():
    return render_template('ENTC-engineering.html')


@app.route('/civil')
def civil_engineering_page():
    return render_template('civil-engineering.html')


@app.route('/electrical')
def electrical_engineering_page():
    return render_template('electrical-engineering.html')


@app.route('/mech')
def mechanical_engineering_page():
    return render_template('mechanical-engineering.html')


#---comp routes---#

@app.route('/comp/ml')
def comp_engineering_ml():
    make_subject_html.MakeSubjectHTML("comp/ml", "Machine Learning")
    return render_template('_'.join("comp/ml".split('/')) + ".html")


@app.route('/comp/cc')
def comp_engineering_cc():
    make_subject_html.MakeSubjectHTML("comp/cc", "Cloud Computing")
    return render_template('_'.join("comp/cc".split('/')) + ".html")


@app.route('/comp/ertos')
def comp_engineering_ertos():
    make_subject_html.MakeSubjectHTML(
        "comp/ertos", "Embedded & Real-Time Operating Systems")
    return render_template('_'.join("comp/ertos".split('/')) + ".html")


@app.route('/comp/hci')
def comp_engineering_hci():
    make_subject_html.MakeSubjectHTML("comp/hci", "Human Computer Interaction")
    return render_template('_'.join("comp/hci".split('/')) + ".html")


@app.route('/comp/ics')
def comp_engineering_ics():
    make_subject_html.MakeSubjectHTML(
        "comp/ics", "Information & Cyber Security")
    return render_template('_'.join("comp/ics".split('/')) + ".html")


@app.route('/comp/scoa')
def comp_engineering_scoa():
    make_subject_html.MakeSubjectHTML(
        "comp/scoa", "Soft Computing and Optimization Algorithm")
    return render_template('_'.join("comp/scoa".split('/')) + ".html")


@app.route('/comp/Textbooks')
def comp_engineering_Textbooks():
    make_subject_html.MakeSubjectHTML("comp/Textbooks", "Textbooks")
    return render_template('_'.join("comp/Textbooks".split('/')) + ".html")


@app.route('/comp/compiler')
def comp_engineering_compiler():
    make_subject_html.MakeSubjectHTML("comp/compiler", "Compiler")
    return render_template('_'.join("comp/compiler".split('/')) + ".html")
#---civil routes---#


@app.route('/civil/cm')
def civil_engineering_cm():
    make_subject_html.MakeSubjectHTML("civil/cm", "Construction Management")
    return render_template('_'.join("civil/cm".split('/')) + ".html")


@app.route('/civil/qsct')
def civil_engineering_qsct():
    make_subject_html.MakeSubjectHTML(
        "civil/qsct", "Quantity Surveying,Contracts and Tenders")
    return render_template('_'.join("civil/qsct".split('/')) + ".html")

#---electrical routes---#


@app.route('/electrical/ed')
def electrical_engineering_ed():
    make_subject_html.MakeSubjectHTML("electrical/ed", "Electronic Drives")
    return render_template('_'.join("electrical/ed".split('/')) + ".html")


@app.route('/electrical/pecd')
def electrical_engineering_pecd():
    make_subject_html.MakeSubjectHTML(
        "electrical/pecd", "Power Electronic Controlled Drives")
    return render_template('_'.join("electrical/pecd".split('/')) + ".html")


@app.route('/electrical/sgp')
def electrical_engineering_sgp():
    make_subject_html.MakeSubjectHTML(
        "electrical/sgp", "Switchgear and Protection")
    return render_template('_'.join("electrical/sgp".split('/')) + ".html")

#---entc routes---#


@app.route('/entc/AVE')
def entc_engineering_AVE():
    make_subject_html.MakeSubjectHTML("entc/AVE", "Audio Video Engineering")
    return render_template('_'.join("entc/AVE".split('/')) + ".html")


@app.route('/entc/BCS')
def entc_engineering_BCS():
    make_subject_html.MakeSubjectHTML(
        "entc/BCS", "Broadband Communication Systems")
    return render_template('_'.join("entc/BCS".split('/')) + ".html")


@app.route('/entc/MC')
def entc_engineering_MC():
    make_subject_html.MakeSubjectHTML("entc/MC", "Mobile Communication")
    return render_template('_'.join("entc/MC".split('/')) + ".html")


@app.route('/entc/MCOM')
def entc_engineering_MCOM():
    make_subject_html.MakeSubjectHTML("entc/MCOM", "Mobile Communication")
    return render_template('_'.join("entc/MCOM".split('/')) + ".html")


@app.route('/entc/WSN')
def entc_engineering_WSN():
    make_subject_html.MakeSubjectHTML("entc/WSN", "Wireless Networks")
    return render_template('_'.join("entc/WSN".split('/')) + ".html")


@app.route('/entc/VLSI')
def entc_engineering_VLSI():
    make_subject_html.MakeSubjectHTML(
        "entc/VLSI", "Very-Large-Scale Integration")
    return render_template('_'.join("entc/VLSI".split('/')) + ".html")

#---it routes---#


@app.route('/it/DCS')
def it_engineering_DCS():
    make_subject_html.MakeSubjectHTML("it/DCS", "Distributed System")
    return render_template('_'.join("it/DCS".split('/')) + ".html")


@app.route('/it/IOT')
def it_engineering_IOT():
    make_subject_html.MakeSubjectHTML("it/IOT", "Internet of Things")
    return render_template('_'.join("it/IOT".split('/')) + ".html")


@app.route('/it/SMA')
def it_engineering_SMA():
    make_subject_html.MakeSubjectHTML("it/SMA", "Social Media Analytics")
    return render_template('_'.join("it/SMA".split('/')) + ".html")


@app.route('/it/UC')
def it_engineering_UC():
    make_subject_html.MakeSubjectHTML("it/UC", "Ubquitous Computing")
    return render_template('_'.join("it/UC".split('/')) + ".html")

#---mech routes---#


@app.route('/mech/amp')
def mech_engineering_amp():
    make_subject_html.MakeSubjectHTML(
        "mech/amp", "Advanced Manufacturing Processes")
    return render_template('_'.join("mech/amp".split('/')) + ".html")


@app.route('/mech/ee')
def mech_engineering_ee():
    make_subject_html.MakeSubjectHTML("mech/ee", "Energy Engineering")
    return render_template('_'.join("mech/ee".split('/')) + ".html")


@app.route('/mech/ie')
def mech_engineering_ie():
    make_subject_html.MakeSubjectHTML("mech/ie", "Industrial Engineering")
    return render_template('_'.join("mech/ie".split('/')) + ".html")


@app.route('/mech/msd')
def mech_engineering_msd():
    make_subject_html.MakeSubjectHTML("mech/msd", "Mechanical System Design")
    return render_template('_'.join("mech/msd".split('/')) + ".html")


@app.route('/mech/pdd')
def mech_engineering_pdd():
    make_subject_html.MakeSubjectHTML(
        "mech/pdd", "Product Design and Development")
    return render_template('_'.join("mech/pdd".split('/')) + ".html")


@app.route('/mech/tribology')
def mech_engineering_tribology():
    make_subject_html.MakeSubjectHTML("mech/tribology", "Tribology")
    return render_template('_'.join("mech/tribology".split('/')) + ".html")


@app.route('/mech_test/')
def mech_engineering_test():

    branch = "comp"

    branch_folder_path = f"./static/mcq_data/{branch}"

    branch_folders_list = [x for x in next(os.walk(branch_folder_path))[1]]
    print(branch_folders_list)

    subjects_dict = {}

    for subject in branch_folders_list:
        subject_folder_path = f"./static/mcq_data/{branch}/{subject}"
        subject_files_list = os.listdir(subject_folder_path)
        subject_files_size = [round((os.stat(
            f"{subject_folder_path}/{file_name}").st_size)/1048576, 2) for file_name in subject_files_list]

        subjects_dict[subject] = {
            "files_list": subject_files_list,
            "files_size": subject_files_size
        }

    os.makedirs(f"./templates/subject templates/{branch}", exist_ok=True)

    for subject in branch_folders_list:
        output_from_parsed_template = render_template(
            'engineering-subject.html', subject_dict=subjects_dict[subject], branch=branch, subject_folder=subject)
        with open(f"./templates/subject templates/{branch}/{branch}_{subject}.html", "w") as f:
            f.write(output_from_parsed_template)

    return output_from_parsed_template
    print(subjects_dict)

    return render_template("engineering-branch.html", test="test")


if __name__ == '__main__':
    app.run()
