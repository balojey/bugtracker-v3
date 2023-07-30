import { useState, useEffect } from "react";
import { getProjectBugs } from "@src/utils/projectsUtils";
import { Typography } from "@mui/material";
import DisplayProjectBug from "@src/components/DisplayProjectBug";

export default function ProjectBugs({ projectId }) {
  const [bugs, setBugs] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    async function fetchBugs() {
      const bugsData = await getProjectBugs(projectId);
      setBugs(bugsData);
      setLoading(false);
    }
    fetchBugs();
  }, [projectId]);
  return (
    <>
      {bugs && bugs.length > 0 ? (
        bugs.map((bug) => <DisplayProjectBug key={bug.id} bug={bug} />)
      ) : (
        <Typography variant="body2">No bugs</Typography>
      )}
    </>
  );
}
