import { useState, useEffect} from "react"
import { useParams } from "react-router-dom"
import StockChart from "./StockChart"


const StockInfoPage = ({title}) => {
  const [stockData, setStockData] = useState({})
  const { ticker } = useParams()
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch(`http://127.0.0.1:5000/stocks/${ticker}/historical_data`)
          .then((response) => response.json())
          .then((data) => {
            setStockData(state => {
              return {
                ...state,
                closing_prices: data.close
              }
            });
          })
          fetch(`http://127.0.0.1:5000/stocks/${ticker}/predictions`)
          .then((response) => response.json())
          .then((data) => {
            setStockData(state => {
              return {
                ...state,
                predictions: data
              }
            });
          });
      } catch (err) {
        console.log(err);
      }
    }
    fetchData()
  }, [ticker])

    return (
      <>
        {/* <StockChart
          title={`${ticker} Historical Prices`}
          data={stockData.closing_prices}
        /> */}
        <StockChart
          title={`${ticker} Predicted Prices`}
          data={stockData.predictions}
        />
      </>
    )
  
}




export default StockInfoPage

