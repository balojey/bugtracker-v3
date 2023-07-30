import { useRouter } from "next/router";
import { useSession } from "next-auth/react";
import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import { getProjects } from "@/src/utils/projectsUtils";
import { useEffect, useState } from "react";
import Project from "@src/components/Project";
import Container from "@mui/material/Container";
import CreateEntityButton from "@src/components/CreateEntityButton";

export default function Projects() {
  const [projects, setProjects] = useState([]);
  const { data: session } = useSession();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchProjects() {
      const projectsData = await getProjects(session.user);
      setProjects(projectsData);
      setLoading(false);
    }
    fetchProjects();
  }, [session]);

  return (
    <>
      <ResponsiveAppBar />
      <CreateEntityButton linkTo={"projects"} />
      <Container maxWidth="md" style={{}}>
        {loading ? (
          <div>Loading...</div>
        ) : (
          projects.map((project) => (
            <Project key={project._id} project={project} />
          ))
        )}
      </Container>
    </>
  );
}
