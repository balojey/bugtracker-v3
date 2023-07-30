const { API_URL } = require("@endpoints");

// Get all projects user is a member of
const getProjects = async (user) => {
  const response = await fetch(`${API_URL}/projects`, {
    method: "GET",
    headers: {
      Authorization: `${user.tokenType} ${user.accessToken}`,
      "Content-Type": "application/json",
    },
    redirect: "follow",
  })
    .then((response) => response.json())
    .then((result) => {
      return result;
    })
    .catch((error) =>
      console.log("[getProjects() - projectsUtils.js] Get projects error", error)
    );
  console.log(response);
  return response;
};

const getProject = async (projectId) => {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/projects/${projectId}`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
    }
  )
    .then((response) => response.json())
    .then((result) => {
      return result;
    })
    .catch((error) =>
      console.log("[getProject() - projectsUtils.js] Get project error", error)
    );
  console.log(response);
  return response;
};

const deleteProject = async (projectId, user) => {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/projects/${projectId}`,
    {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `${user.tokenType} ${user.accessToken}`,
      },
      redirect: "follow",
    }
  );
  if (response.status === 204) {
    return true;
  } else if (response.status === 403) {
    console.log("[deleteProject() - projectsUtils.js] Forbidden");
  } else {
    console.log("[deleteProject() - projectsUtils.js] Project delete Error");
  }
};

const getProjectBugs = async (projectId) => {
  const response = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/projects/${projectId}/bugs`,
    {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
    }
  )
    .then((response) => response.json())
    .then((result) => {
      return result;
    })
    .catch((error) =>
      console.log(
        "[getProjectBugs() - projectsUtils.js] Get project bugs error: ",
        error
      )
    );
  console.log(response);
  return response;
};

export { getProjects, getProject, deleteProject, getProjectBugs };
