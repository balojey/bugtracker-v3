import React from "react";
import ReactDOM from "react-dom";
import { useFormik } from "formik";
import * as yup from "yup";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { useSession } from "next-auth/react";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import { getProject } from "@src/utils/projectsUtils";

const validationSchema = yup.object({
  name: yup.string("Enter project name").required("Project name is required"),
  description: yup
    .string("Enter project's description")
    .required("Project description is required"),
});

export default function CreateProject() {
  const router = useRouter();
  const [project, setProject] = useState([]);
  const [loading, setLoading] = useState(true);
  const { data: session } = useSession();
  const formik = useFormik({
    initialValues: {
      name: "",
      description: "",
    },
    validationSchema: validationSchema,
    onSubmit: async (values) => {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/projects/${router.query.projectId}`,
        {
          method: "PATCH",
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
        router.push(`/projects/${router.query.projectId}/`);
      } else {
        console.log("[EditProject.js] Project update Error");
      }
    },
  });
  useEffect(() => {
    async function fetchProject() {
      const projectData = await getProject(router.query.projectId);
      setProject(projectData);
      setLoading(false);
    }
    fetchProject();
  }, [router.query.projectId]);
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
        //   label="name"
          placeholder="Enter project name"
          value={formik.values.name || project.name}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          error={formik.touched.name && Boolean(formik.errors.name)}
          helperText={formik.touched.name && formik.errors.name}
        />
        <TextField
          fullWidth
          id="description"
          name="description"
        //   label="description"
          placeholder="Enter project description"
          value={formik.values.description || project.description}
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
