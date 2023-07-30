import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import ProTip from "@/src/ProTip";
import Link from "@/src/Link";
import Footer from "@src/components/Footer";
import ResponsiveAppBar from "@/src/components/ResponsiveAppBar";

export default function Index() {
  return (
    <div>
      <ResponsiveAppBar />
      <Container maxWidth="" sx={{ marginTop: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Bug tracker app
        </Typography>
        <Link href="/about" color="secondary">
          Go to the about page
        </Link>
        <ProTip />
      </Container>
    </div>
  );
}
