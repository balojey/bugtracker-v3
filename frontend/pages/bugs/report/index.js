import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import Container from "@mui/material/Container";
import ReportBugForm from "@src/components/ReportBugForm";

export default function ReportBug() {
  return (
    <>
      <ResponsiveAppBar />
      <Container maxWidth="md" sx={{my: "auto", width: "inherit"}}>
        <ReportBugForm />
      </Container>
    </>
  );
}
