import stripe
from airtable import *
from flask import Flask, render_template, redirect, url_for, request, session, escape, abort

from funcs import *

app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
app.config['STRIPE_SECRET_KEY'] = STRIPE_SECRET_KEY

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@app.route('/')
def home():
    urls = []
    courses = []
    description = []
    for page in maintable.get_iter(sort='id'):
        for record in page:
            if record['fields']['visible'] == 'true':
                value = record['fields']['Portada'][0]['url']
                urls.append(value)
                value = record['fields']['Name']
                courses.append(value)
                value = record['fields']['miniDescription']
                description.append(value)

    length = len(courses)
    return render_template('home.html', name=falsename(), logo=get_logo(), logow=get_logo_white(),
        length=length, urls=urls, courses=courses, description=description, l=['active', '', ''])

@app.route('/home')
def to_home():
    return redirect(url_for('home'))

@app.route('/aboutme/<lang>')
def about_me(lang):
    for page in datatable.get_iter(sort='id'):
        for record in page:
            photo = record['fields']['Fotos'][1]['url']
            print(photo)
            return render_template('about.html', name=falsename(), logo=get_logo(), logow=get_logo_white(), photo=photo, l=['', 'active', ''], lang=lang.lower())

@app.route('/aboutme')
def to_about():
    return redirect(url_for('about_me', lang='es'))

@app.route('/portfolio')
def portfolio():
    dic = {}
    for page in proyectstable.get_iter(sort='id'):
        for record in page:
            record = record['fields']
            dic[record['id']] = [record['Images'][0]['url'], record['Name'], record['Title'], record['Description'], record['Link']]
    
    skills = {}
    for page in skillstable.get_iter(sort='id'):
        for record in page:
            record = record['fields']
            skills[record['Data']] = [record['Data'], record['icons'][0]['url']]
    
    return render_template('portfolio.html', name=falsename(), logo=get_logo(), logow=get_logo_white(), dic=dic, skills=skills, l=['', '', 'active'])

@app.route('/legalnote/<lang>')
def legalnote(lang):
    if lang.lower() == 'es':
        return render_template('legalnote.html', name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])
    elif lang.lower() == 'en':
        return render_template('error.html', title='Not translation yet', 
                error='Sorry so much we don\'t have translated the legal note to English yet, We\'re working on it', 
                name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])
    else:
        abort(404)

@app.route('/course')
@app.route('/course/')
def return_home():
    return redirect(url_for('home'))

@app.route('/course/<course>')
@app.route('/course/<course>/')
def courses(course):
    try:
        for page in maintable.get_iter(sort='id'):
            for record in page:
                value = record['fields']['Name'].lower()
                if value == course.lower():
                    value = record['fields']['Title']
                    alpha = record['fields']['Description']
                    try:
                        portada_ = record['fields']['Portada']
                        portada = portada_[0]['url']
                    except:
                        portada = ''
                    try:
                        pdf_ = record['fields']['PDF']
                        pdf = pdf_[0]['url']
                    except:
                        pdf = False
                    temas = {}
                    urls = []
                    length = 0
                    for page2 in anytable.get_iter(sort='id'):
                        for record2 in page2:
                            try:
                                beta = record2['fields']['Name']
                                delta = beta[0]
                            except:
                                delta = 'Nope'
                            if delta.lower() == course.lower():
                                gamma = record2['fields']['Tema']
                                try:
                                    temas[gamma] = [record2['fields']['Classname'], record2['fields']['Dropmenu']]
                                except:
                                    temas[gamma] = ['']
                            try:
                                if record['fields']['List'] == True:
                                    lista = True
                                    requisitos_ = record['fields']['Requisitos']
                                    requisitos = requisitos_.split(',')
                            except:
                                lista = False
                                requisitos = []
                        
                        return render_template('course.html', name=falsename(), logo=get_logo(), course=course, title=value, description=alpha, temas=temas,
                            portada=portada, lista=lista, requisitos=requisitos, pdf=pdf, logow=get_logo_white(), l=['', '', ''])
            return render_template('error.html', error='Lo sentimos mucho pero el curso que busca no existe',
                title='Course Not Found', name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])
    except Exception as error:
        return render_template('error.html', error=error, title=error, name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])

@app.route('/course/<course>/<leasson>')
def leassons(course, leasson):
    for page in maintable.get_iter(sort='id'):
        for record in page:
            value = record['fields']['Name'].lower()
            if value == course.lower():
                video = ''
                title = ''
                for page2 in leassontable.get_iter(sort='id'):
                    try:
                        for record2 in page2:
                            hash = record2['fields']['Hash']
                            if leasson == hash:
                                id_leasson = record2['fields']['id']
                                try:
                                    video = record2['fields']['Video']
                                    video = video[0]['url']
                                except:
                                    video = ':C'
                                title = record2['fields']['Classname']
                                next_class = record2['fields']['Next Leasson']
                                return render_template('leasson.html', name=falsename(), logo=get_logo(), video=video, next=next_class, title=title, logow=get_logo_white(), course=course, l=['', '', ''])
                    except Exception as error:
                        print(error)
                        return render_template('error.html', error='Class Not Found: The requested class was not found on the server. If you entered the URL manually please check your spelling and try again.', 
                            title='Class Not Found', name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])  
    
    return render_template('error.html', error='Class Not Found: The requested class was not found on the server. If you entered the URL manually please check your spelling and try again.', 
        title='Class Not Found', name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])

# Stripe Test
@app.route('/stripetest')
def stripetest():
    if 'username' in login_:
        user_login = True
        if 'Python' in test_users[escape(login_["username"])]:
            return f'Hola {escape(login_["username"])} tu ya compraste este producto'
    else:
        user_login = False

    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [
            {
                'price': 'price_1IFluMCIFOmYJz0KR54CjgSQ',
                'quantity': 1,
            }
        ],
        mode = 'payment',
        success_url = url_for('thankstest', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url = url_for('stripetest', _external=True),
    )

    return render_template(
        'stripe_test.html', 
        checkout_session_id=session['id'], 
        checkout_public_key=app.config['STRIPE_PUBLIC_KEY'],
        user_login=user_login
    )

@app.route('/nologinstripetest')
def no_login():
    return 'You have to be logged to purchase a product'

@app.route('/thanks')
def thankstest():
    test_users[escape(login_["username"])].append('Python')
    return render_template('stripe_thanks.html')

@app.errorhandler(404)
def error_404(error):
    return render_template('error.html', error=error, title='404 Page Not Found', name=falsename(), logo=get_logo(), logow=get_logo_white(), l=['', '', ''])

if __name__ == "__main__":
    app.run(debug = True, port=5000)