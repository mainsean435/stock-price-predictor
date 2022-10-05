from flask_restx import Namespace, Resource, fields
from models import Stock
from flask import request

stock_ns = Namespace('stock', description="""
    A namespace for stocks, contains routes related to stocks, routes to view extra information about a stock such it's historical prices.
     """)

stock_model = stock_ns.model(
    "Stock",
    {
        "id": fields.Integer(),
        "ticker_symbol": fields.String(),
        "company_name": fields.String(),
        "company_logo": fields.String(),
        "industry": fields.String(),
        "company_ceo": fields.String(),
        "company_headquaters": fields.String(),
        "company_website": fields.String(),
        "description": fields.String(),
        "year_founded": fields.Integer()
    }
)

@stock_ns.route('/stocks')
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
            ticker_symbol=data.get("ticker_symbol"),
            company_name=data.get("company_name"),
            description=data.get("description"),
            company_ceo=data.get("company_ceo"),
            company_headquaters=data.get("company_headquaters"),
            year_founded=data.get("year_founded"),
            industry=data.get("industry"),
            company_logo=data.get("company_logo"),
            company_website=data.get("company_website")
        )
        new_stocks.save()

        return new_stocks, 201


@stock_ns.route('/stocks/<int:id>')
class Stocks(Resource):

    @stock_ns.marshal_with(stock_model)
    def get(self, id):
        stock = Stock.query.get_or_404(id)
        return stock

    @stock_ns.marshal_with(stock_model)
    def put(self, id):
        stock_to_update = Stock.query.get_or_404(id)
        data = request.get_json()

        stock_to_update.update(ticker_symbol=data.get("ticker_symbol"),
                               company_name=data.get("company_name"),
                               description=data.get("description"),
                               company_ceo=data.get("company_ceo"),
                               company_headquaters=data.get("company_headquaters"),
                               year_founded=data.get("year_founded"),
                               industry=data.get("industry"),
                               company_logo=data.get("company_logo"),
                               company_website=data.get("company_website"))
        return stock_to_update

    @stock_ns.marshal_with(stock_model)
    def delete(self, id):
        stock_to_delete = Stock.query.get_or_404(id)
        stock_to_delete.delete()
        return stock_to_delete

