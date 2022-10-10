from exts import db

"""
class Stock:
    id:int primary key
    ticker: string
    company_ceo: string
    company_name: string
    company_logo: string
    industry: string
    description: string
    year_founded: integer
"""


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer(), primary_key=True)
    ticker = db.Column(db.String(10), nullable=False, unique=True)
    company_name = db.Column(db.String(100), nullable=False)
    company_logo = db.Column(db.Text(), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    company_ceo = db.Column(db.String(100), nullable=False)
    company_headquaters = db.Column(db.String(100), nullable=False)
    company_website = db.Column(db.Text(), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    year_founded = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"<Stock {self.company_name} >"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **kwargs):
        self.ticker = kwargs.get('ticker') or self.ticker
        self.company_name = kwargs.get('company_name') or self.company_name
        self.company_logo = kwargs.get('company_logo') or self.company_logo
        self.industry = kwargs.get('industry') or self.industry
        self.company_ceo = kwargs.get('company_ceo') or self.company_ceo
        self.company_headquaters = kwargs.get(
            'company_headquaters') or self.company_headquaters
        self.company_website = kwargs.get(
            'company_website') or self.company_website
        self.description = kwargs.get('description') or self.description
        self.year_founded = kwargs.get('year_founded') or self.year_founded
        db.session.commit()


"""
class User:
    id:integer
    username:string
    email:string
    password:string
"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    transactions = db.relationship('Transaction', backref='user')

    def __repr__(self):
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()


"""
class Transactions:
    id: integer
    name: string
    type: string
    amount: float
    ticker: string
    time_transacted: datetime
    time_created: datetime
    price_purchased_at: float
    no_of_shares: float
"""


class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), nullable=False)
    type = db.Column(db.String(10))
    amount = db.Column(db.Float)
    time_transacted = db.Column(db.DateTime)
    time_created = db.Column(db.DateTime)
    price_purchased_at = db.Column(db.Float)
    no_of_shares = db.Column(db.Float)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
