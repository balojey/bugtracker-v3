import {
  Card,
  CardContent,
  Typography,
  CardActions,
  Button,
} from "@mui/material";
import { bugStatus } from "@src/statuses";
import Link from "@src/Link";

export default function Bug({ bug }) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {bug.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {bug.description}
        </Typography>
        <Typography variant="subtitle2" color="text.secondary">
          Status: {bugStatus[bug.status]}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">
          <Link href={`/bugs/${bug._id}`}>goto bug</Link>
        </Button>
        <Button size="small">
          <Link href={`/projects/${bug.project._id}`}>goto project</Link>
        </Button>
      </CardActions>
    </Card>
  );
}
