import React, { useState } from "react";
import {
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalFooter,
  ModalBody,
  ModalCloseButton,
  VStack,
  Button,
  Input,
} from "@chakra-ui/react";

export default function AddModal({ isOpen, onClose }) {
  const [type, setType] = useState("");
  const [name, setName] = useState("");
  const [stock, setSymbol] = useState("");
  const [amount, setAmount] = useState("");
  const [pricePurchasedAt, setPricePurchasedAt] = useState("");
  const [transactionDate, setTransactionDate] = useState("");
  const [numberOfShares, setNumberOfShares] = useState("");

  const addTransaction = () => {
    const payload = JSON.stringify({
      name: name,
      type: type,
      amount: amount * 100,
      stock: stock,
      time_transacted: Date.parse(transactionDate) / 1000,
      time_created: Date.now() / 1000,
      price_purchased_at: pricePurchasedAt,
      no_of_shares: numberOfShares,
    });
    console.log(payload);
    fetch("http://127.0.0.1:5000/transactions/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: payload,
    })
      .then((response) => response.json())
      .then((data) => {
        onClose();
      });
  };

  return (
    <>
      <Modal isOpen={isOpen} onClose={onClose} size="xl">
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Add Transaction</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
            <VStack spacing={8}>
              <Input
                value={type}
                onChange={(e) => setType(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Type [1 = Purchase, 2 = Sell]"
              />
              <Input
                value={name}
                onChange={(e) => setName(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Name"
              />
              <Input
                value={stock}
                onChange={(e) => setSymbol(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Symbol"
              />
              <Input
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Amount"
              />
              <Input
                value={pricePurchasedAt}
                onChange={(e) => setPricePurchasedAt(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Price Purchased At"
              />
              <Input
                value={transactionDate}
                onChange={(e) => setTransactionDate(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Transaction Date (MM-DD-YYYY)"
              />
              <Input
                value={numberOfShares}
                onChange={(e) => setNumberOfShares(e.target.value)}
                focusBorderColor="tomato"
                variant="flushed"
                placeholder="Number of Shares"
              />
            </VStack>
          </ModalBody>
          <ModalFooter>
            <Button
              bg="tomato"
              color="white"
              mr={3}
              size="lg"
              onClick={addTransaction}
            >
              Add Transaction
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  );
}
