import Button from "@mui/material/Button";
import Link from "@src/Link";

export default function CreateEntityButton({ linkTo }) {
  return (
    <Button size="body1">
      <Link
        href={linkTo === "projects" ? `/${linkTo}/new` : `/${linkTo}/report`}
      >
        {linkTo === "projects" ? "Create Project" : "Report Bug"}
      </Link>
    </Button>
  );
}
