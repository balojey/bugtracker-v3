import { API_URL } from "@/variables";

export const getProjects = (token) => {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  myHeaders.append("accept", "application/json");
  myHeaders.append("Authorization", `Bearer ${token}`);

  const requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };

  const response = fetch(`${API_URL}/projects`, requestOptions)
    .then(async (res) => {
      if (res.ok) {
        return res.json();
      } else {
        const data = await res.json();
        let errorMessage = "Could not get user";
        throw new Error(errorMessage);
      }
    })
    .then((data) => {
      // console.log("data: ", data);
      return data;
    })
    .catch((err) => {
      alert(err.message);
    });
  console.log("response: ", response.values);
  // let retVal;

  // fetch(`${API_URL}/projects`, requestOptions)
  //   .then(async (res) => {
  //     if (res.ok) {
  //       return res.json();
  //     } else {
  //       const data = await res.json();
  //       let errorMessage = "Could not get user";
  //       throw new Error(errorMessage);
  //     }
  //   })
  //   .then((data) => {
  //     console.log("data: ", data);
  //     retVal = data;
  //   })
  //   .catch((err) => {
  //     alert(err.message);
  //   });
  // return retVal;
};
