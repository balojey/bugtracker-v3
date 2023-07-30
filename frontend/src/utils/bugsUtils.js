const getBugs = async (user, projectId) => {
  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/projects/${projectId}/bugs`, {
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
      console.log("[getBugs() - bugsUtils.js] Get projects error", error)
    );
  console.log(response);
  return response;
};

const getBug = async (user, bugId) => {
  
}

export { getBugs };
