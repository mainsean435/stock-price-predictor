import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import { BsFillCaretDownFill, BsFillCaretUpFill } from "react-icons/bs"


const AllStocksPage = () => {
  const [stocks, setStocks] = useState([])
  const navigate = useNavigate()

  const changeColor = (change) => {
    return change > 0 ? "success" : "danger"
  }

  const renderIcon = (change) => {
    return change > 0 ? <BsFillCaretUpFill /> : <BsFillCaretDownFill />
  }

  useEffect(() => {
    const fetchData = async () => {
      try {
        fetch("http://127.0.0.1:5000/stocks/")
          .then((response) => response.json())
          .then((data) => {
            setStocks(data);
          });
      } catch (err) {
        console.log(err);
      }
    }
    fetchData()
  }, [])

  const handleStockSelect = (ticker) => {
    navigate(`/stock/${ticker}`)
  }


  return (<div>
    <div className="text-center">
      <table className="table hover mt-5">
        <thead style={{ color: "rgb(79,89,102)" }}>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Last</th>
            <th scope="col">Chg</th>
            <th scope="col">Chg%</th>
            <th scope="col">High</th>
            <th scope="col">Low</th>
            <th scope="col">Open</th>
            <th scope="col">Pclose</th>
          </tr>
        </thead>
        <tbody>
          {stocks.map((stockData) => {
            return (
              <tr style={{ cursor: "pointer" }} onClick={() => handleStockSelect(stockData.ticker)} className="table-row" key={stockData.ticker}>
                <th scope="row">{stockData.ticker}</th>
                {/* <td>{stockData.change}</td> */}
                <td className={`text-${changeColor(stockData.d)}`}>{stockData.change} {renderIcon(stockData.d)}</td>
                {/* <td>{stockData.perchange}</td> */}
                <td className={`text-${changeColor(stockData.d)}`}>{stockData.perchange} {renderIcon(stockData.d)} </td>
                <td>{stockData.high}</td>
                <td>{stockData.low}</td>
                <td>{stockData.open}</td>
                <td>{stockData.prevclose}</td>
              </tr>
            )
          })}
        </tbody>
      </table>
    </div>
  </div>
  )
}

export default AllStocksPage