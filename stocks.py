from flask_restx import Namespace, Resource, fields
from models import Stock
from flask import request
from predictor import get_predictions

from stocks_data.stocks_data import get_all_data


stock_ns = Namespace('stocks', description="""
    A namespace for stocks, contains routes related to stocks, routes to view extra information about a stock such it's historical prices.
     """)

stock_model = stock_ns.model(
    "Stock",
    {
        "id": fields.Integer(),
        "symbol": fields.String(),
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
            symbol=data.get("symbol"),
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


@stock_ns.route('/<string:symbol>/info')
class Stocks(Resource):

    @stock_ns.marshal_with(stock_model)
    def get(self, symbol):
        stock = Stock.query.filter_by(symbol=symbol).first_or_404()
        return stock

@stock_ns.route('/<string:symbol>')
class Stocks(Resource):
    @stock_ns.marshal_with(stock_model)
    def put(self, symbol):
        stock = Stock.query.filter_by(symbol=symbol).first_or_404()
        data = request.get_json()

        stock.update(symbol=data.get("symbol"),
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
    def delete(self, symbol):
        stock = Stock.query.filter_by(symbol=symbol).first_or_404()
        stock.delete()
        return stock

@stock_ns.route('/<string:symbol>/data')
class Stocks(Resource):

    def get(self, symbol):
        return get_all_data(symbol)

@stock_ns.route('/<string:symbol>/summary')
class Stocks(Resource):

    def get(self, symbol):
        data = get_all_data(symbol)
        return {
            "name": symbol,
            "change": data['change'],
            "change_percent": data['change_percent'],
            "high": data["high"][-1][1],
            "low": data["low"][-1][-1],
            "open": data["open"][-1][1],
            "previous_close": data["previous_close"]
        }

@stock_ns.route('/<string:symbol>/predictions')
class Stocks(Resource):

    def get(self, symbol):
        return get_predictions(symbol)
