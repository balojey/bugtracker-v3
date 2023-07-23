"use client";

import Comment from "./Comment";

const comments = require("../dummyData").comments;

export default function Comments({ bugId }) {
  const cmnts = comments.filter((cmnt) => cmnt.bug === bugId);
  return (
    <div>
      <div className="flex justify-end">
        {/* You can open the modal using ID.showModal() method */}
        <button
          className="btn btn-primary rounded-none"
          onClick={() => window.my_modal_3.showModal()}
        >
          Write a comment
        </button>
        <dialog id="my_modal_3" className="modal">
          <form method="dialog" className="modal-box">
            <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">
              ✕
            </button>
            <h3 className="font-bold text-lg mb-6">Make a comment</h3>
            <textarea
              className="textarea textarea-primary textarea-lg w-full max-w-full rounded-none mb-6"
              placeholder="Write here..."
            ></textarea>
            <button
              type="submit"
              className="btn btn-primary rounded-none w-full"
            >Save</button>
          </form>
        </dialog>
      </div>
      <div className="grid grid-cols-1 gap-4 mt-4">
        {cmnts.map((cmnt) => (
          <Comment key={cmnt._id} props={cmnt} />
        ))}
      </div>
    </div>
  );
}
