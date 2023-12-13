import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read files content in the app
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

@app.route("/", methods=['GET', 'POST'])
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    if request.method == 'POST':
        # Handle form submission here if needed
        # For example, you can access form data using request.form['input_name']
        pass

    return render_template("index.html")


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)