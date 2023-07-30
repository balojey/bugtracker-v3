import ResponsiveAppBar from "../../src/components/ResponsiveAppBar";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Footer from "@src/components/Footer";
import LoginForm from "@src/components/LoginForm";

export default function Login() {
  return (
    <div>
      <ResponsiveAppBar />
      <Container maxWidth="" sx={{ marginTop: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Login
        </Typography>
        <LoginForm />
      </Container>
    </div>
  );
}
