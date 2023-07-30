import React, { useState, useEffect } from "react";
import {
  Container,
  Box,
  Typography,
  List,
  ListItem,
  ListItemText,
  TextField,
  Button,
} from "@mui/material";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import { useRouter } from "next/router";

export default function BugDetails() {
  const [bugData, setBugData] = useState(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const bugId = router.query.bugId;

  useEffect(() => {
    const fetchBugData = async () => {
      try {
        // Fetch the bug data based on the bugId using your API endpoint
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/bugs/${bugId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch bug data');
        }
        const bugData = await response.json();
        setBugData(bugData);
        setLoading(false);
      } catch (error) {
        console.error('Error fetching bug data:', error);
        setLoading(false);
      }
    };

    fetchBugData();
  }, [bugId]);

  const onDeleteBug = async () => {
    // Implement the logic to delete the bug here
    try {
      const response = await fetch(`/api/bugs/${bugId}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error('Failed to delete bug');
      }
      // Handle successful deletion, e.g., redirecting to a different page
    } catch (error) {
      console.error('Error deleting bug:', error);
      // Handle error, e.g., showing an error message to the user
    }
  };
  
  const onAddComment = async (comment) => {
    // Implement the logic to add a comment here
    try {
      const response = await fetch(`/api/bugs/${bugId}/comments`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ comment }),
      });
      if (!response.ok) {
        throw new Error('Failed to add comment');
      }
      // Handle successful comment addition, e.g., updating the bugData state with the new comment
      const newComment = await response.json();
      setBugData((prevData) => ({
        ...prevData,
        comments: [...prevData.comments, newComment],
      }));
    } catch (error) {
      console.error('Error adding comment:', error);
      // Handle error, e.g., showing an error message to the user
    }
  };

  const onAssignDeveloper = async (email) => {
    // Implement the logic to assign the bug to a developer here
    try {
      const response = await fetch(`/api/bugs/${bugId}/assign`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });
      if (!response.ok) {
        throw new Error('Failed to assign the bug');
      }
      // Handle successful assignment, e.g., updating the bugData state with the assigned developer
      const assignedDeveloper = await response.json();
      setBugData((prevData) => ({
        ...prevData,
        assignedDeveloper,
      }));
    } catch (error) {
      console.error('Error assigning bug:', error);
      // Handle error, e.g., showing an error message to the user
    }
  };

  const initialValues = {
    email: "",
    comment: "",
  };

  const commentValidationSchema = Yup.object().shape({
    comment: Yup.string(),
  });

  const assignDeveloperValidationSchema = Yup.object().shape({
    email: Yup.string().email("Invalid email"),
  });

  return (
    <>
      <ResponsiveAppBar />
      <Container maxWidth="md">
        <Box marginBottom={4}>
          <Typography variant="h5" gutterBottom>
            Bug Details
          </Typography>
          <Typography variant="h6" gutterBottom>
            Title: {bugData.title}
          </Typography>
          <Typography variant="body1" gutterBottom>
            Description: {bugData.description}
          </Typography>
          <Typography variant="body1" gutterBottom>
            Steps to Reproduce: {bugData.steps_to_reproduce}
          </Typography>
          <Typography variant="body1" gutterBottom>
            Priority: {bugData.priority}
          </Typography>
          <Typography variant="h6" gutterBottom>
            Files:
          </Typography>
          {/* <List>
            {files.map((file) => (
              <ListItem key={file.filename}>
                <ListItemText primary={file.filename} secondary={file.url} />
              </ListItem>
            ))}
          </List> */}
          <Typography variant="h6" gutterBottom>
            Comments:
          </Typography>
          {/* <List>
            {comments.map((comment, index) => (
              <ListItem key={index}>
                <ListItemText primary={comment} />
              </ListItem>
            ))}
          </List> */}
          {assignedDeveloper && (
            <Typography variant="body1" gutterBottom>
              Assigned Developer: {bugData.assigned_developer}
            </Typography>
          )}
        </Box>
        <Box marginBottom={4}>
          <Typography variant="h6" gutterBottom>
            Assign Bug to a Developer
          </Typography>
          <Formik
            initialValues={initialValues}
            validationSchema={assignDeveloperValidationSchema}
            onSubmit={(values, { resetForm }) => {
              onAssignDeveloper(values.email);
              resetForm();
            }}
          >
            <Form>
              <Field
                as={TextField}
                label="Developer Email"
                name="email"
                variant="outlined"
                fullWidth
              />
              <ErrorMessage
                name="email"
                component="div"
                style={{ color: "red" }}
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ marginTop: 10 }}
              >
                Assign
              </Button>
            </Form>
          </Formik>
        </Box>
        <Box marginBottom={4}>
          <Typography variant="h6" gutterBottom>
            Add a Comment
          </Typography>
          <Formik
            initialValues={initialValues}
            validationSchema={commentValidationSchema}
            onSubmit={(values, { resetForm }) => {
              onAddComment(values.comment);
              resetForm();
            }}
          >
            <Form>
              <Field
                as={TextField}
                label="Comment"
                name="comment"
                variant="outlined"
                fullWidth
                multiline
                rows={4}
              />
              <ErrorMessage
                name="comment"
                component="div"
                style={{ color: "red" }}
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                style={{ marginTop: 10 }}
              >
                Add Comment
              </Button>
            </Form>
          </Formik>
        </Box>
        <Button
          variant="contained"
          color="secondary"
          onClick={() => onDeleteBug()}
        >
          Delete Bug
        </Button>
        <Button
          variant="contained"
          color="primary"
          href={`/bugs/${bugData.id}/edit`}
        >
          Edit Bug
        </Button>
      </Container>
    </>
  );
}
