import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Button from "@mui/material/Button";
import Link from "@src/Link";
import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import { getProject, deleteProject } from "@src/utils/projectsUtils";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Divider from "@mui/material/Divider";
import { projectStatus } from "@src/statuses";
import { useSession } from "next-auth/react";
import ProjectBugs from "@src/components/ProjectBugs";

export default function Project() {
  const router = useRouter();
  const { data: session } = useSession();
  const [project, setProject] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    async function fetchProject() {
      const projectData = await getProject(router.query.projectId);
      setProject(projectData);
      setLoading(false);
    }
    fetchProject();
  }, [router.query.projectId]);
  const handleDelete = async () => {
    if (await deleteProject(router.query.projectId, session.user)) {
      router.push("/projects");
    }
  };
  return (
    <>
      <ResponsiveAppBar />
      <Button size="body1">
        <Link href={`/projects/${project._id}/edit`}>Edit</Link>
      </Button>
      <Button size="body1" onClick={handleDelete}>
        delete
      </Button>
      <Container maxWidth="md">
        <Typography variant="h4">{project.name}</Typography>
        <Typography variant="subtitle1">{project.description}</Typography>
        <Typography variant="subtitle2">
          Status: {projectStatus[project.status]}
        </Typography>
        <Typography variant="caption">
          {/* Created by: {project.created_by.first_name}{" "}
          {project.created_by.last_name} */}
        </Typography>
      </Container>
      <Divider />
      <Container maxWidth="md">
        <ProjectBugs projectId={project._id} />
      </Container>
    </>
  );
}
