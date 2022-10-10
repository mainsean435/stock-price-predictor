import React from "react";
import { useNavigate } from "react-router-dom"
import { BsFillCaretDownFill, BsFillCaretUpFill } from "react-icons/bs"
import { Tr, Td } from "@chakra-ui/react";

export default function StockItem({ stock }) {
  const navigate = useNavigate()

  const changeColor = (change) => {
    return change > 0 ? "success" : "danger"
  }

  const renderIcon = (change) => {
    return change > 0 ? <BsFillCaretUpFill /> : <BsFillCaretDownFill />
  }

  const handleStockSelect = (ticker) => {
    navigate(`/stock/${ticker}`)
  }

  return (
    <Tr style={{ cursor: "pointer" }} onClick={() => handleStockSelect(stock.ticker)}>
      <Td>{stock.ticker}</Td>
      <Td>{stock.ticker}</Td>
      <Td>{stock.data.last}</Td>
      <Td className={`text-${changeColor(stock.data.change)}`}>{stock.data.change_percent}{renderIcon(stock.data.change)}</Td>
      <Td>{stock.data.high}</Td>
      <Td>{stock.data.low}</Td>
      <Td>{stock.data.open}</Td>
      <Td>{stock.data.previous_close}</Td>
    </Tr>
  )
}
