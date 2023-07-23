import Link from "next/link";

const status = require("../colorPalette").status;
const priority = require("../colorPalette").priority;
const bugs = require("../dummyData").bugs;

export default function Project({ props }) {
  const borderColor = status[props.status];
  const bugCount = bugs.filter((bug) => bug.project === props._id).length;
  return (
    <div
      className="card w-96 bg-base-100 shadow-xl rounded-md mx-auto my-4"
      style={{ border: `3px solid ${borderColor}` }}
    >
      <div
        className="badge rounded-none"
        style={{
          border: `3px solid ${borderColor}`,
          backgroundColor: `${borderColor}`,
          color: "#fff",
        }}
      >
        {props.status}
      </div>
      <div className="card-body">
        <Link href={`./dashboard/projects/${props._id}`}>
          <h2 className="card-title mb-4">{props.name}</h2>
          <p>{props.description}</p>
        </Link>
        <ul className="menu menu-horizontal px-1">
          <ul className="menu px-1">
            <li className="">Created by: {props.created_by}</li>
            <li className="">Last updated: {props.last_updated}</li>
          </ul>
          <li className="ml-auto">bugs: {bugCount}</li>
        </ul>
      </div>
    </div>
  );
}
