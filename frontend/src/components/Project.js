import * as React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import Link from "@src/Link";
import { projectStatus } from "@src/statuses";

export default function Project({ project }) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {project.name}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {project.description}
        </Typography>
        <Typography variant="subtitle2" color="text.secondary">
          Status: {projectStatus[project.status]}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">
          <Link href={`/projects/${project._id}`}>goto project</Link>
        </Button>
      </CardActions>
    </Card>
  );
}
