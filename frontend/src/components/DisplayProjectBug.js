import { Box, Typography } from "@mui/material";

export default function DisplayProjectBug({ bug }) {
  console.log(bug);
  return (
    <Box>
      <Typography variant="h6">{bug.title}</Typography>
      <Typography variant="body1">{bug.description}</Typography>
    </Box>
  );
}
