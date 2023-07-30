import React from "react";
import ReactDOM from "react-dom";
import { useFormik } from "formik";
import * as yup from "yup";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useSession } from "next-auth/react";
import { useRouter } from "next/router";

const validationSchema = yup.object({
  name: yup.string("Enter project name").required("Project name is required"),
  description: yup
    .string("Enter project's description")
    .required("Project description is required"),
});

export default function CreateProject() {
  const router = useRouter();
  const { data: session } = useSession();
  const formik = useFormik({
    initialValues: {
      name: "",
      description: "",
    },
    validationSchema: validationSchema,
    onSubmit: async (values) => {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/projects`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `${session.user.tokenType} ${session.user.accessToken}`,
          },
          redirect: "follow",
          body: JSON.stringify(values),
        }
      );
      if (response.ok) {
        const data = await response.json();
        console.log(data);
        router.push("/projects");
      } else {
        console.log("Project creation Error");
      }
    },
  });
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "100vh",
        width: "100%",
      }}
    >
      <form onSubmit={formik.handleSubmit}>
        <TextField
          fullWidth
          id="name"
          name="name"
          label="name"
          placeholder="Enter project name"
          value={formik.values.name}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          error={formik.touched.name && Boolean(formik.errors.name)}
          helperText={formik.touched.name && formik.errors.name}
        />
        <TextField
          fullWidth
          id="description"
          name="description"
          label="description"
          multiline
          placeholder="Enter project description"
          value={formik.values.description}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          error={
            formik.touched.description && Boolean(formik.errors.description)
          }
          helperText={formik.touched.description && formik.errors.description}
        />
        <Button
          color="primary"
          variant="contained"
          fullWidth
          type="submit"
          style={{ color: "#000", marginTop: "50px" }}
        >
          Submit
        </Button>
      </form>
    </div>
  );
}
