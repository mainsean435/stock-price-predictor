from config import DevConfig as cfg
from flask_restx import Namespace, Resource, fields
from models import Transaction, User
from flask import request, jsonify
from datetime import datetime
from collections import defaultdict
from sqlalchemy import create_engine
from flask_jwt_extended import jwt_required, get_jwt_identity

from stocks_data.stocks_data import get_live_price


transaction_ns = Namespace('transactions', description="""
    A namespace for transactions, contains routes related to transactions, routes to add information about a ticker purchase.
     """)

transaction_model = transaction_ns.model(
    "Transaction",
    {
        "id": fields.Integer(),
        "type": fields.String(),
        "amount": fields.Float(),
        "ticker": fields.String(),
        "time_transacted": fields.DateTime(),
        "time_created": fields.DateTime(),
        "price_purchased_at": fields.Float(),
        "no_of_shares": fields.Float()
    }
)


@transaction_ns.route('/')
class Transactions(Resource):

    @transaction_ns.marshal_list_with(transaction_model)
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first_or_404()
        transactions = user.transactions
        transactions.sort(key=lambda x: x.time_transacted, reverse=True)
        return transactions

    @transaction_ns.marshal_with(transaction_model)
    @transaction_ns.expect(transaction_model)
    @jwt_required()
    def post(self):
        data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first_or_404()
        new_transaction = Transaction(
            user_id=user.id,
            type=data.get("type"),
            amount=data.get("amount"),
            ticker=data.get("ticker"),
            time_transacted=datetime.fromtimestamp(
                int(data.get("time_transacted"))),
            time_created=datetime.fromtimestamp(int(data.get("time_created"))),
            price_purchased_at=data.get("price_purchased_at"),
            no_of_shares=data.get("no_of_shares"))
        new_transaction.save()
        return new_transaction, 201


@transaction_ns.route('/rollups_by_stock')
class Transactions(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first_or_404()
        portfolio = defaultdict(
            lambda: {
                "shares": 0,
                "total_cost": 0,
                "total_equity": 0,
                "live_price": 0
            }
        )

        engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI)
        with engine.connect() as con:
            cur = con.execute(
                f"SELECT ticker, type, SUM(amount)/100 AS total_amount, SUM(no_of_shares) AS total_shares FROM transactions WHERE user_id={user.id} GROUP BY ticker, type")
            rows = cur.fetchall()
        for row in rows:
            ticker = row[0]
            transaction_type = row[1]
            transaction_amount = row[2]
            transaction_shares = row[3]

            if transaction_type == 'BOUGHT':
                portfolio[ticker]['total_cost'] += transaction_amount
                portfolio[ticker]['shares'] += transaction_shares
            else:
                portfolio[ticker]['total_cost'] -= transaction_amount
                portfolio[ticker]['shares'] -= transaction_shares

        response = []
        for ticker in portfolio:
            live_price = get_live_price(ticker)
            portfolio[ticker]['live_price'] = live_price
            portfolio[ticker]['total_equity'] = portfolio[ticker]['shares'] * live_price

            response.append({
                "ticker": ticker,
                "live_price": portfolio[ticker]['live_price'],
                "total_equity": portfolio[ticker]['total_equity'],
                "shares": portfolio[ticker]['shares'],
                "total_cost": portfolio[ticker]["total_cost"]
            })

        return jsonify(response)
