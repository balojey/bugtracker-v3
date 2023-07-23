import { API_URL } from "@/variables";

export const getCurrentUser = (token) => {
  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  myHeaders.append("accept", "application/json");
  myHeaders.append("Authorization", `Bearer ${token}`);

  const requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow",
  };

  fetch(`${API_URL}/users/me`, requestOptions)
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
      console.log(JSON.stringify(data, null, 2));
      return data;
    })
    .catch((err) => {
      alert(err.message);
    });
};
