import {
  Center,
  Heading,
  Divider,
  VStack,
  Button,
  useDisclosure,
} from "@chakra-ui/react";

import { useState, useEffect } from "react";
import TransactionsTable from "../components/TransactionsTable";
import { ChakraProvider } from "@chakra-ui/react";
import Summary from "../components/Summary";
import Visualization from "../components/Visualization";
import AddModal from "../components/AddModal";

export default function PortfolioPage(){
  const [transactions, setTransactions] = useState([]);
  const [portfolioCost, setPortfolioCost] = useState(0);
  const [portfolioValue, setPortfolioValue] = useState(0);
  const [absoluteGain, setAbsoluteGain] = useState(0);
  const [totalGainPercent, setTotalGainPercent] = useState(0);
  const [rollups, setRollups] = useState([]);
  const { isOpen, onOpen, onClose } = useDisclosure();

  useEffect(() => {
    fetch("http://127.0.0.1:5000/transactions/rollups_by_stock")
      .then((response) => response.json())
      .then((data) => {
        setRollups(data);
        let costAccumulator = 0;
        let valueAccumulator = 0;
        data.forEach((item) => {
          costAccumulator += item["total_cost"];
          valueAccumulator += item["total_equity"];
        });
        let absoluteGain = valueAccumulator - costAccumulator;

        setPortfolioCost(costAccumulator);
        setPortfolioValue(valueAccumulator);
        setAbsoluteGain(absoluteGain);
        setTotalGainPercent((absoluteGain / costAccumulator) * 100);
      });
    fetch("http://127.0.0.1:5000/transactions")
      .then((response) => response.json())
      .then((data) => {
        setTransactions(data);
      });
  }, [isOpen]);

  return (
    <ChakraProvider>
      <AddModal isOpen={isOpen} onOpen={onOpen} onClose={onClose}></AddModal>
      <Center bg="black" color="white" padding={8}>
        <VStack spacing={5}>
          <Divider orientation="horizontal"/>
          <Heading size='md' margin='0px'>This is the current state of your portfolio</Heading>
          <Summary
            portfolioCost={portfolioCost}
            portfolioValue={portfolioValue}
            absoluteGain={absoluteGain}
            totalGainPercent={totalGainPercent}
          ></Summary>
          <Visualization rollups={rollups}></Visualization>
          <Divider orientation="horizontal"/>
          <TransactionsTable transactions={transactions}></TransactionsTable>
          <Button size="lg" colorScheme="teal" onClick={onOpen}>
            Add Transaction
          </Button>
        </VStack>
      </Center>
    </ChakraProvider>
  );
}
