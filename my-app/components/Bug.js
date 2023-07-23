import Link from "next/link";

const status = require("../colorPalette").status;
const priority = require("../colorPalette").priority;
const bugs = require("../dummyData").bugs;

export default function Bug({ props }) {
  const borderColor = status[props.status];
  const badgeColor = priority[props.priority];
  return (
    <div
      className="card w-96 bg-base-100 rounded-md mx-auto my-4 shadow-xl"
      style={{}}
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
      <div
        className="badge badge-primary badge-xs ml-auto mr-4 tooltip"
        data-tip={props.priority}
        style={{
          backgroundColor: `${badgeColor}`,
          borderColor: `${badgeColor}`,
        }}
      ></div>
      <div className="card-body">
        <Link href={`/dashboard/bug/${props._id}`}>
          <h2 className="card-title mb-2">{props.title}</h2>
          <p>{props.description}</p>
        </Link>
        <ul className="menu menu-horizontal px-1">
          <ul className="menu menu-horizontal px-1 min-w-full">
            <li className="">Reported by: {props.reporter}</li>
            <li className="ml-auto">Last updated: {props.last_updated}</li>
          </ul>
        </ul>
      </div>
    </div>
  );
}
