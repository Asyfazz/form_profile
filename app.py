from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form_pendaftaran.html')


@app.route('/myprofile')
def myprofile():
    return render_template('my-profile.html')

@app.route('/update')
def update():
    return render_template('update_profile.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    # Process the data here
    return jsonify({'message': 'Registration successful!'})

if __name__ == '__main__':
    app.run(debug=True)
