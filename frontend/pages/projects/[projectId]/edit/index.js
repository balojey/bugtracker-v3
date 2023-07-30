import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import Container from "@mui/material/Container";
import EditProject from "@src/components/EditProject";

export default function NewProject() {
  return (
    <>
      <ResponsiveAppBar />
      <Container maxWidth="md" sx={{my: "auto", width: "inherit"}}>
        <EditProject />
      </Container>
    </>
  );
}
