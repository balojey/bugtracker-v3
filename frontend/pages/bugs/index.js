import CreateEntityButton from "@src/components/CreateEntityButton";
import ResponsiveAppBar from "@src/components/ResponsiveAppBar";
import Bug from "@src/components/ui/Bug";
import { getBugs } from "@src/utils/bugsUtils";
import { getProjects } from "@src/utils/projectsUtils";
import { useSession } from "next-auth/react";
import { Container } from "@mui/material";
import { useEffect, useState } from "react";

export default function BugsPage() {
  const { data: session } = useSession();
  const [bugs, setBugs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchBugs() {
      try {
        const projects = await getProjects(session.user);
        console.log(projects);

        const allBug = [];
        for (const project of projects) {
          const bgs = await getBugs(session.user, project._id);
          allBug.push(...bgs);
        }

        setBugs(allBug);
        setLoading(false);
      } catch (error) {
        // Handle any errors that might occur during data fetching
        console.error("Error fetching bugs:", error);
        setLoading(false);
      }
    }

    fetchBugs();
  }, [session.user]);
  return (
    <>
      <ResponsiveAppBar />
      <CreateEntityButton linkTo={"bugs"} />
      <Container maxWidth="md">
        {loading ? (
          <div>Loading Bugs...</div>
        ) : bugs ? (
          bugs.map((bug) => <Bug key={bug._id} bug={bug} />)
        ) : (
          <div>No Bugs</div>
        )}
      </Container>
    </>
  );
}
