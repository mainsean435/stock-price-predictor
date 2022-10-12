import React from "react";

import { Tr, Td } from "@chakra-ui/react";

export default function TransactionItem({ transaction }) {
  let date = transaction["time_transacted"]
  date = date.slice(0, date.indexOf('T'))
  return (
    <Tr>
      <Td>{transaction["ticker"]}</Td>
      <Td isNumeric>Ksh {transaction["amount"].toLocaleString()}</Td>
      <Td isNumeric>{transaction["no_of_shares"]}</Td>
      <Td isNumeric>Ksh {transaction["price_purchased_at"].toLocaleString()}</Td>
      <Td>{date}</Td>
    </Tr>
  );
}
