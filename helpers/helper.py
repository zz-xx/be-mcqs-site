import os

branch_names = [x for x in next(os.walk("./static/mcq_data"))[1]]

print(branch_names)

'''
@app.route('/comp/ml')
def computer_engineering_ml():
    return render_template("ml.html")
'''

fileStream = open('routes.txt', 'w')

for branch in branch_names:

    branch_folder_path = f"./static/mcq_data/{branch}"

    branch_folders_list = [x for x in next(os.walk(branch_folder_path))[1]]
    print(branch_folders_list)

    for subject in branch_folders_list:
        text = f'''
            @app.route('/{branch}/{subject}')
            def {branch}_engineering_{subject}():
                subjects = "test"
                return render_template("subject-template.html", subjects)
        '''

        print(text)
        fileStream.write(text)
