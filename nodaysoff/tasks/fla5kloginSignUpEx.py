@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        if signup_form.validate():
            # Get Form Fields
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            website = request.form.get('website')
            existing_user = User.query.filter_by(email=email).first()
            if existing_user is None:
                user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | Flask-Login Tutorial.',
                           form=SignupForm(),
                           template='signup-page',
                           body="Sign up for a user account.")