const getFiles = async (user, bugId) => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/bugs/${bugId}/attachments`, {
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
        console.log("[getFiles() - filesUtils.js] Get projects error", error)
      );
    console.log(response);
    return response;
  };