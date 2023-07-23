import Link from "next/link";
import Comments from "@/components/Comments";
import NavBar from "@/components/NavBar";

const status = require("../../../../colorPalette").status;
const priority = require("../../../../colorPalette").priority;
const bugs = require("../../../../dummyData").bugs;

export default function BugPage({ params }) {
  const bug = bugs.find((bug) => bug._id == params.bugId);
  const borderColor = status[bug.status];
  const badgeColor = priority[bug.priority];
  return (
    <div>
      <NavBar />
      <div className="container mx-auto my-4 px-10" style={{}}>
        <div className="flex justify-between items-center">
          <div
            className="badge rounded-none"
            style={{
              border: `3px solid ${borderColor}`,
              backgroundColor: `${borderColor}`,
              color: "#fff",
            }}
          >
            {bug.status}
          </div>
          <div
            className="badge badge-xs tooltip"
            data-tip={bug.priority}
            style={{
              backgroundColor: `${badgeColor}`,
              borderColor: `${badgeColor}`,
            }}
          ></div>
        </div>
        <div className="mt-4">
          <h2 className="font-bold text-xl mb-2">{bug.title}</h2>
          <p>{bug.description}</p>
          <ul className="mt-6">
            <li className="">Reported by: {bug.reporter}</li>
            <li className="ml-auto">Last updated: {bug.last_updated}</li>
          </ul>
        </div>
        <div className="divider mt-10">Comments</div>
        <Comments bugId={bug._id} />
      </div>
    </div>
  );
}
