"use client";
import { useState } from "react";
import Bug from "./Bug";

export default function Bugs({ projectId }) {
  const bugs = require("../dummyData").bugs;
  let bgs;
  // console.log("projectId: ", projectId);
  if (projectId) {
    bgs = bugs.filter((bug) => bug.project == projectId);
  } else {
    bgs = bugs;
  }
  const [bs, setBugs] = useState(bgs);
  const [requestedPriority, setRequestedPriority] = useState("");
  const sortByPriority = (priority) => {
    setRequestedPriority(priority);
  };
  const filteredBugs = requestedPriority
    ? bgs.filter((bug) => bug.priority === requestedPriority)
    : bgs;

  const priorityOptions = [
    { label: "Show All Bugs", value: "" },
    { label: "Sort by Low Priority", value: "LOW" },
    { label: "Sort by Medium Priority", value: "MEDIUM" },
    { label: "Sort by High Priority", value: "HIGH" },
    { label: "Sort by Urgent Priority", value: "URGENT" },
    { label: "Sort by Immediate Priority", value: "IMMEDIATE" },
    { label: "Sort by Critical Priority", value: "CRITICAL" },
    { label: "Sort by Blocker Priority", value: "BLOCKER" },
  ];
  return (
    <div>
      <div className="flex justify-between mb-4">
        <select
          value={requestedPriority}
          onChange={(e) => sortByPriority(e.target.value)}
          className="ml-4"
        >
          <option value="">Sort By Priority</option>
          {priorityOptions.map((option) => (
            <option key={option.value} value={option.value}>
              {option.label}
            </option>
          ))}
        </select>
        {/* You can open the modal using ID.showModal() method */}
        <button
          className="btn btn-primary mr-4 rounded-none"
          onClick={() => window.my_modal_3.showModal()}
        >
          Report a bug
        </button>
        <dialog id="my_modal_3" className="modal">
          <form method="dialog" className="modal-box">
            <div className="flex justify-between my-7">
              <h3 className="font-semibold text-3xl">Report a bug</h3>
              <select className="select w-50 max-w-xs rounded-none border-primary">
                <option disabled selected>
                  Priority
                </option>
                <option>LOW</option>
                <option>MEDIUM</option>
                <option>HIGH</option>
                <option>URGENT</option>
                <option>IMMEDIATE</option>
                <option>CRITICAL</option>
                <option>BLOCKER</option>
              </select>
            </div>
            <input
              type="text"
              placeholder="Enter bug title"
              className="input input-bordered input-primary w-full max-w-full rounded-none mb-6"
            />
            <textarea
              className="textarea textarea-primary textarea-lg w-full max-w-full rounded-none mb-6"
              placeholder="Enter bug description"
            ></textarea>
            <textarea
              className="textarea textarea-primary textarea-lg w-full max-w-full rounded-none mb-6"
              placeholder="State the steps to reproduce bug (Optional)"
            ></textarea>
            <input
              type="file"
              className="file-input file-input-bordered file-input-primary w-full max-w-full mb-6"
            />
            <button
              type="submit"
              className="btn btn-primary rounded-none w-full"
            >
              Report
            </button>

            <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">
              ✕
            </button>
          </form>
        </dialog>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredBugs.map((bug) => (
          <Bug key={bug._id} props={bug} />
        ))}
      </div>
    </div>
  );
}
