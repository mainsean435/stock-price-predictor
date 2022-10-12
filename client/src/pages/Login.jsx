import { Button } from "@chakra-ui/button"
import { Heading, VStack } from "@chakra-ui/layout"
import { Formik } from "formik"
import * as Yup from "yup"
import TextField from "../components/TextField"

import React from 'react'
import {useNavigate} from 'react-router-dom'
import { login } from '../auth'

export default function SignUpPage() {

    const navigate = useNavigate()

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
            })}
            onSubmit={(values, actions) => {

                const options={
                    method:"POST",
                    headers:{
                        'content-type':'application/json'
                    },
                    body:JSON.stringify(values)
                }
             
                fetch('http://localhost:5000/auth/login',options)
                .then(res=>res.json())
                .then(data=>{
                    console.log(data.access_token)
                    
                    if (data){
                     login(data.access_token)
                     navigate('/portfolio')
                    }
                    else{
                        alert('Invalid username or password')
                    }
         
         
                })
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
                    <Heading>Sign In</Heading>

                    <TextField name="username"
                        placeholder="enter username"
                    />

                    <TextField
                        name="password"
                        type="password"
                        placeholder="enter password"
                    />

                    <Button type="submit" variant="outline" colorScheme="teal">
                        Sign In
                    </Button>
                </VStack>
            )}
        </Formik>
    )
}