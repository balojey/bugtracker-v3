import React, { useState, useEffect } from "react";
import {
  TextField,
  Button,
  Container,
  Box,
  Typography,
  MenuItem,
  FormControl,
  InputLabel,
  Select,
} from "@mui/material";
import {
  Formik,
  Form,
  Field,
  ErrorMessage,
  useFormikContext,
  useField,
} from "formik";
import * as Yup from "yup";
import { useSession } from "next-auth/react";
import { getProjects } from "@src/utils/projectsUtils";

export default function ReportBugForm() {
  const { data: session } = useSession();
  const [projects, setProjects] = useState();
  const [loading, setLoading] = useState(true);
  const MyTextField = ({ name, ...props }) => {
    const { errors, touched } = useFormikContext();
    return (
      <>
        <Field
          as={TextField}
          fullWidth
          name={name}
          variant="outlined"
          {...props}
          error={Boolean(errors[name] && touched[name])}
          helperText={<ErrorMessage name={name} />}
        />
      </>
    );
  };

  const MySelectField = ({ name, ...props }) => {
    const { errors, touched } = useFormikContext();
    return (
      <>
        <FormControl
          fullWidth
          variant="outlined"
          error={Boolean(errors[name] && touched[name])}
        >
          <InputLabel htmlFor={name}>Priority</InputLabel>
          <Field
            as={Select}
            label="Priority"
            name={name}
            labelId={name}
            {...props}
          >
            {priorityOptions.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </Field>
          <ErrorMessage name={name} />
        </FormControl>
      </>
    );
  };

  const MyProjectSelectField = ({ name, projects, ...props }) => {
    const { errors, touched } = useFormikContext();
    return (
      <>
        <FormControl
          fullWidth
          variant="outlined"
          error={Boolean(errors[name] && touched[name])}
        >
          <InputLabel htmlFor={name}>Project</InputLabel>
          <Field
            as={Select}
            label="Project"
            name={name}
            labelId={name}
            {...props}
          >
            {projects.map((project) => (
              <MenuItem key={project._id} value={project.name}>
                {project.name}
              </MenuItem>
            ))}
          </Field>
          <ErrorMessage name={name} />
        </FormControl>
      </>
    );
  };

  const MyFileInput = ({ name, ...props }) => {
    const { setFieldValue } = useFormikContext();
    const [field, meta] = useField(name);

    return (
      <>
        <input
          type="file"
          {...field}
          {...props}
          onChange={(event) => {
            const { files } = event.target;
            const uploadedFiles = [];
            for (const file of files) {
              uploadedFiles.push({
                filename: file.name,
                url: URL.createObjectURL(file),
              });
            }
            setFieldValue(name, uploadedFiles);
          }}
        />
        {meta.touched && meta.error && (
          <div style={{ color: "red" }}>{meta.error}</div>
        )}
      </>
    );
  };

  const initialValues = {
    projectId: "",
    title: "",
    description: "",
    steps_to_reproduce: "",
    priority: "",
    files: [],
  };

  const validationSchema = Yup.object().shape({
    title: Yup.string().required("Title is required").required("Required"),
    description: Yup.string()
      .required("Description is required")
      .required("Required"),
    steps_to_reproduce: Yup.string(), //.required("Steps to reproduce is required"),
    priority: Yup.string(), //.required("Priority is required"),
  });

  const priorityOptions = [
    { value: "low", label: "Low" },
    { value: "medium", label: "Medium" },
    { value: "high", label: "High" },
  ];

  const handleSubmit = async (values) => {
    try {
      const { projectId, ...bugData } = values; // Destructure projectId from values
      // Make a POST request to the backend endpoint with the form values
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/projects/${projectId}/bugs`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(bugData),
        }
      );

      if (!response.ok) {
        // Handle the error here if needed
        console.error("Error submitting the form:", response.statusText);
      } else {
        // Handle successful submission here, if required
        console.log("Form submitted successfully!");
      }
    } catch (error) {
      // Handle any network or other errors here
      console.error("Error submitting the form:", error);
    }
  };

  useEffect(() => {
    async function fetchProjects() {
      const projectsData = await getProjects(session.user);
      setProjects(projectsData);
      setLoading(false);
    }
    fetchProjects();
  }, [session]);

  return (
    <Container maxWidth="md">
      <Typography variant="h5" gutterBottom>
        Report a Bug
      </Typography>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ setFieldValue }) => (
          <Form>
            <MyTextField label="Title" name="title" />
            <MyTextField
              label="Description"
              name="description"
              multiline
              rows={4}
            />
            <MyTextField
              label="Steps to reproduce"
              name="steps_to_reproduce"
              multiline
              rows={4}
            />
            <MySelectField label="Priority" name="priority" />
            <MyProjectSelectField
              label="Project"
              name="projectId"
              projects={projects}
              required
            />
            {/* For handling file uploads, you can use an input with type="file" */}
            <MyFileInput name="files" multiple />
            <Button type="submit" variant="contained" color="primary">
              Submit
            </Button>
          </Form>
        )}
      </Formik>
    </Container>
  );
}
