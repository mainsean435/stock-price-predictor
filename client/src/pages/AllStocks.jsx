import { useState, useEffect } from "react"
import StocksTable from "../components/StocksTable"

export default function AllStocksPage() {
  const [stocks, setStocks] = useState([])

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

  return (
    <StocksTable stocks={stocks}></StocksTable>
  )
}
