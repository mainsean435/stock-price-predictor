import React, { useState } from 'react'
import {useNavigate} from 'react-router-dom'
import {Alert} from 'react-bootstrap'



import { Button } from "@chakra-ui/button"
import { Heading, VStack } from "@chakra-ui/layout"
import { Formik } from "formik"
import * as Yup from "yup"
import TextField from "../components/TextField"

export default function SignUpPage() {
    const navigate = useNavigate()
    const [serverResponse,setServerResponse]=useState('')
    const [show,setShow]=useState(false)

    return (
        <Formik
            initialValues={{ username: "", password: "" }}
            validationSchema={Yup.object({
                username: Yup.string()
                    .required("Username required")
                    .min(3, "Username is too short"),
                password: Yup.string()
                    .required("Password required")
                    .min(8, "Password is too short"),
                email: Yup.string().email("invalid email").required("email required"),
            })}
            onSubmit={(values, actions) => {

                const body = {
                    username: values.username,
                    email: values.email,
                    password: values.password
                }
    
                const options = {
                    method: "POST",
                    headers: {
                        'content-type': 'application/json'
                    },
                    body: JSON.stringify(body)
                }
    
                fetch('http://localhost:5000/auth/signup', options)
                    .then(res => res.json())
                    .then(data =>{
                        console.log(data)
                        setServerResponse(data.message)
                        setShow(true)
                        alert(serverResponse)
                        navigate('/login')
                    })
                    .catch(err => console.log(err))
                actions.resetForm()

            }}
        >
            {formik => (
                <VStack
                    spacing={35}
                    as="form"
                    mx="auto"
                    w={{ base: "90%", md: 500 }}
                    h="100vh"
                    justifyContent="center"
                    onSubmit={formik.handleSubmit}
                >
                    {show?
                    <>
                    <Alert variant="success" onClose={() => {setShow(false)
                        }} dismissible>
                    <p>
                        {serverResponse}
                    </p>
                    </Alert>

                    <Heading>Sign Up</Heading>
                
                    </>
                    :
                    <Heading>Sign Up</Heading>
               
               }

                    {/* <Heading>Sign Up</Heading> */}

                    <TextField name="username"
                        placeholder="enter username"
                    />

                    <TextField
                        name="email"
                        placeholder="enter email"
                        type="email"
                    />

                    <TextField
                        name="password"
                        type="password"
                        placeholder="enter password"
                    />

                    <Button type="submit" variant="outline" colorScheme="teal">
                        Create Account
                    </Button>
                </VStack>
            )}
        </Formik>
    )
}