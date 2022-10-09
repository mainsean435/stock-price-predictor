from flask_restx import Namespace, Resource, fields
from models import Stock
from flask import request

from stocks_data.stocks_data import get_historical_data, get_predictions


stock_ns = Namespace('stocks', description="""
    A namespace for stocks, contains routes related to stocks, routes to view extra information about a stock such it's historical prices.
     """)

stock_model = stock_ns.model(
    "Stock",
    {
        "id": fields.Integer(),
        "ticker": fields.String(),
        "company_name": fields.String(),
        "company_logo": fields.String(),
        "industry": fields.String(),
        "company_ceo": fields.String(),
        "company_headquaters": fields.String(),
        "company_website": fields.String(),
        "description": fields.String(),
        "year_founded": fields.Integer(),
        "data": fields.String()
    }
)


@stock_ns.route('/')
class Stocks(Resource):

    @stock_ns.marshal_list_with(stock_model)
    def get(self):
        stocks = Stock.query.all()
        return stocks

    @stock_ns.marshal_with(stock_model)
    @stock_ns.expect(stock_model)
    def post(self):

        data = request.get_json()
        new_stocks = Stock(
            ticker=data.get("ticker"),
            company_name=data.get("company_name"),
            company_logo=data.get("company_logo"),
            industry=data.get("industry"),
            company_ceo=data.get("company_ceo"),
            company_headquaters=data.get("company_headquaters"),
            company_website=data.get("company_website"),
            description=data.get("description"),
            year_founded=data.get("year_founded"))
        new_stocks.save()
        return new_stocks, 201


@stock_ns.route('/<string:ticker>/info')
class Stocks(Resource):

    @stock_ns.marshal_with(stock_model)
    def get(self, ticker):
        stock = Stock.query.filter_by(ticker=ticker).first_or_404()
        return stock

@stock_ns.route('/<string:ticker>')
class Stocks(Resource):
    @stock_ns.marshal_with(stock_model)
    def put(self, ticker):
        stock = Stock.query.filter_by(ticker=ticker).first_or_404()
        data = request.get_json()

        stock.update(ticker=data.get("ticker"),
                     company_name=data.get("company_name"),
                     company_logo=data.get("company_logo"),
                     industry=data.get("industry"),
                     company_ceo=data.get("company_ceo"),
                     company_headquaters=data.get(
            "company_headquaters"),
            company_website=data.get("company_website"),
            description=data.get("description"),
            year_founded=data.get("year_founded"))
        return stock

    @stock_ns.marshal_with(stock_model)
    def delete(self, ticker):
        stock = Stock.query.filter_by(ticker=ticker).first_or_404()
        stock.delete()
        return stock

@stock_ns.route('/<string:ticker>/data')
class Stocks(Resource):

    def get(self, ticker):
        return get_historical_data(ticker)

@stock_ns.route('/<string:ticker>/summary')
class Stocks(Resource):

    def get(self, ticker):
        data = get_historical_data(ticker)
        return {
            "ticker": ticker,
            "change": data['change'],
            "change_percent": data['change_percent'],
            "high": data["high"][-1][1],
            "low": data["low"][-1][-1],
            "open": data["open"][-1][1],
            "previous_close": data["previous_close"]
        }

@stock_ns.route('/<string:ticker>/predictions')
class Stocks(Resource):

    def get(self, ticker):
        return get_predictions(ticker)
