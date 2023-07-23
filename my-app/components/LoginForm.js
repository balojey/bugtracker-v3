"use client";

import React, { useContext } from "react";
import { useRouter } from "next/navigation";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import AuthContext from "@/auth/context";
import { API_URL } from "@/variables";

const LoginForm = () => {
  const authCtx = useContext(AuthContext);
  const router = useRouter();
  const initialValues = {
    email: "",
    password: "",
  };

  const validationSchema = Yup.object({
    email: Yup.string()
      .email("Invalid email address")
      .required("Email is required"),
    password: Yup.string().required("Password is required"),
  });

  const handleSubmit = (values) => {
    console.log(values); // Perform login logic here

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");

    var urlencoded = new URLSearchParams();
    urlencoded.append("username", values.email);
    urlencoded.append("password", values.password);

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: urlencoded,
      redirect: "follow",
    };

    fetch(`${API_URL}/auth/jwt/login`, requestOptions)
      .then(async (res) => {
        if (res.ok) {
          return res.json();
        } else {
          const data = await res.json();
          let errorMessage = "Authentication failed!";
          throw new Error(errorMessage);
        }
      })
      .then((data) => {
        authCtx.login(data.access_token);
        router.replace("/dashboard");
        const processedData = JSON.stringify(data);
        for (let i = 0; i < processedData.length; i++) {
          if (processedData.includes("ROLE_SUPER_ADMIN")) {
            console.log("Found Admin");
            authCtx.adminAccess(data.access_token);
          } else {
            console.log("Found User");
            authCtx.adminAccess(null);
          }
        }
      })
      .catch((err) => {
        alert(err.message);
      });
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form className="max-w-md mx-auto p-8 border border-primary rounded-none shadow-md mt-10">
        <div className="mb-4">
          <label htmlFor="email" className="block mb-2 font-medium">
            Email
          </label>
          <Field
            type="email"
            id="email"
            name="email"
            className="border border-primary rounded-none px-4 py-2 w-full focus:outline-none focus:border-blue-500"
          />
          <ErrorMessage
            name="email"
            component="div"
            className="text-red-500 mt-2"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="password" className="block mb-2 font-medium">
            Password
          </label>
          <Field
            type="password"
            id="password"
            name="password"
            className="border border-primary rounded-none px-4 py-2 w-full focus:outline-none focus:border-blue-500"
          />
          <ErrorMessage
            name="password"
            component="div"
            className="text-red-500 mt-2"
          />
        </div>
        <button
          type="submit"
          className="btn btn-primary rounded-none w-full mt-8"
        >
          Login
        </button>
      </Form>
    </Formik>
  );
};

export default LoginForm;
