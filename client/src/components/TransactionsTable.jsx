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
import TransactionItem from "./TransactionItem";

export default function TransactionsTable({ transactions }) {
  return (
    <VStack>
      <Heading size='md' margin='0px'>Recent Transactions</Heading>
      <TableContainer>
      <Table variant='simple'>
        <Thead>
          <Tr>
            <Th>Stock</Th>
            <Th isNumeric>Amount</Th>
            <Th isNumeric>No. of Shares</Th>
            <Th isNumeric>Purchased At</Th>
            <Th>Date</Th>
          </Tr>
        </Thead>
        <Tbody>
          {transactions.slice(0, 10).map((tran, index) => {
            return (
              <TransactionItem key={index} transaction={tran}></TransactionItem>
            );
          })}
        </Tbody>
      </Table>
      </TableContainer>
    </VStack>
  );
}
