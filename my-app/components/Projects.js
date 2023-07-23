import AuthContext from "@/auth/context";
import Project from "./Project";
import { useFormik } from "formik";
import { useContext, useState } from "react";
import * as Yup from "yup";
import { API_URL } from "@/variables";
import { getCurrentUser } from "@/utils/users";
import { getProjects } from "@/utils/projects";

// const projects = require("../dummyData").projects;

export default function Projects() {
  const authCtx = useContext(AuthContext);
  const projects = getProjects();
  const [showSuccessAlert, setShowSuccessAlert] = useState(false);
  const formik = useFormik({
    initialValues: {
      name: "",
      description: "",
    },
    validationSchema: Yup.object({
      name: Yup.string().required("Project name required!"),
      description: Yup.string(),
    }),
    onSubmit: (values) => {
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      myHeaders.append("accept", "application/json");
      myHeaders.append("Authorization", `Bearer ${authCtx.token}`);

      const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: JSON.stringify(values),
        redirect: "follow",
      };

      fetch(`${API_URL}/projects`, requestOptions)
        .then(async (res) => {
          if (res.ok) {
            return res.json();
          } else {
            const data = await res.json();
            let errorMessage = "Unable to create project";
            throw new Error(errorMessage);
          }
        })
        .then((data) => {
          console.log(JSON.stringify(data, null, 2));
          setTimeout(() => {
            setShowSuccessAlert(true);
          }, 2000);
        })
        .catch((err) => {
          alert(err.message);
        });
    },
  });
  const handleAlertClose = () => {
    setShowSuccessAlert(false);
  };
  console.log("Projects: ", JSON.stringify(projects, null, 2));
  return (
    <div>
      <div className="flex justify-end">
        {/* You can open the modal using ID.showModal() method */}
        <button
          className="btn btn-primary mr-4 rounded-none"
          onClick={() => window.my_modal_2.showModal()}
        >
          Create a project
        </button>
        <dialog id="my_modal_2" className="modal">
          {showSuccessAlert && (
            <div className="fixed inset-0 flex items-end justify-center bg-gray-900 bg-opacity-50">
              <div className="bg-primary p-4 rounded w-80">
                <h2 className="text-xl font-bold mb-4 text-base-100">
                  Project Created
                </h2>
                <p className="mb-4 text-base-100">
                  Your project has been created successfully!
                </p>
                <button
                  type="button"
                  className="bg-base-100 text-white rounded py-2 px-4"
                  onClick={handleAlertClose}
                >
                  Close
                </button>
              </div>
            </div>
          )}
          <form
            method="dialog"
            className="modal-box"
            onSubmit={formik.handleSubmit}
          >
            <h3 className="font-semibold text-3xl my-7">Create a project</h3>
            <label htmlFor="name" className="mb-4">
              Project's Name
            </label>
            <input
              id="name"
              name="name"
              type="text"
              {...formik.getFieldProps("name")}
              placeholder="Enter project's name"
              className="input input-bordered input-primary w-full max-w-full rounded-none mb-1"
            />
            {formik.touched.name && formik.errors.name ? (
              <div className="mb-6 text-red-600">{formik.errors.name}</div>
            ) : null}
            <label htmlFor="description" className="mb-4">
              Project's Description
            </label>
            <textarea
              id="description"
              name="description"
              {...formik.getFieldProps("description")}
              className="textarea textarea-primary textarea-lg w-full max-w-full rounded-none mb-1"
              placeholder="Enter project's description"
            ></textarea>
            {formik.touched.description && formik.errors.description ? (
              <div className="mb-6 text-red-600">
                {formik.errors.description}
              </div>
            ) : null}
            <button
              type="submit"
              className="btn btn-primary rounded-none w-full"
            >
              Create
            </button>
          </form>
          <form method="dialog" className="modal-backdrop">
            <button>close</button>
          </form>
        </dialog>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {projects ? (
          projects.map((project) => (
            <Project key={project._id} props={project} />
          ))
        ) : (
          <p>No projects available</p>
        )}
      </div>
    </div>
  );
}
