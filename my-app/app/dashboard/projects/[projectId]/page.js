import Link from "next/link";
import Bugs from "@/components/Bugs";
import NavBar from "@/components/NavBar";

const status = require("../../../../colorPalette").status;
const projects = require("../../../../dummyData").projects;

export default function ProjectPage({ params }) {
  const project = projects.find((project) => project._id == params.projectId);
  return (
    <div>
      <NavBar />
      <div className="container mx-auto my-4 px-10" style={{}}>
        <div className="mt-4">
          <code
            className="px-2"
            style={{ backgroundColor: `${status[project.status]}` }}
          >
            {project.status}
          </code>
          <h2 className="font-bold text-xl mb-2 mt-4">{project.name}</h2>
          <p>{project.description}</p>
          <ul className="mt-6">
            <li className="">Created by: {project.created_by}</li>
            <li className="ml-auto">Last updated: {project.last_updated}</li>
          </ul>
        </div>
        <div className="divider mt-10">Bugs</div>
        <Bugs projectId={project._id} />
      </div>
    </div>
  );
}
