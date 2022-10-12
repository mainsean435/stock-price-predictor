import React from "react";
import {
  Heading,
  VStack,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  TableContainer,
} from "@chakra-ui/react";
import StockItem from "./StockItem";

export default function StocksTable({ stocks }) {
  return (
    <VStack>
      <Heading size='md' margin='0px'>Available stocks</Heading>
      <TableContainer>
      <Table variant='simple'>
        <Thead>
          <Tr>
            <Th>Stock</Th>
            <Th>Name</Th>
            <Th isNumeric>Last</Th>
            <Th isNumeric>Change</Th>
            <Th isNumeric>High</Th>
            <Th isNumeric>Low</Th>
            <Th isNumeric>Open</Th>
            <Th isNumeric>Prev Close</Th>
          </Tr>
        </Thead>
        <Tbody>
          {stocks.map((stock, index) => {
            return (
              <StockItem key={index} stock={stock}></StockItem>
            );
          })}
        </Tbody>
      </Table>
      </TableContainer>
    </VStack>
  );
}
