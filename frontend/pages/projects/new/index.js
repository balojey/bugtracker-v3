import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import Container from "@mui/material/Container";
import CreateProject from "@src/components/CreateProject";

export default function NewProject() {
  return (
    <>
      <ResponsiveAppBar />
      <Container maxWidth="md" sx={{my: "auto", width: "inherit"}}>
        <CreateProject />
      </Container>
    </>
  );
}
