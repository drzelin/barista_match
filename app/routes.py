from flask import render_template, flash, redirect
from app import app
from app.forms import RequestForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/barista_request', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        flash('Barista requested for {}'.format(
            form.cafe_name.data))
        print(form.owner_name.data)
        print(form.cafe_name.data)
        print(form.email.data)
        print(form.phone.data)
        return redirect('/')
    return render_template('barista_request.html', title='Submit Request', form=form)
