from flask import Flask,render_template


FAI = Flask(__name__) #FAI is Flask Application Instance



@FAI.route('/firstHtml')
def firstHtml():

    return render_template('firstHtml.html')


@FAI.route('/secondHtml')
def secondHtml():

    return render_template('secondHtml.html',name = 'Narendra Sai')


















if __name__ == '__main__':
    FAI.run(debug=True)