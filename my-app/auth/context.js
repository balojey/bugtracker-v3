"use client";

import { createContext, useContext, useState, useEffect } from "react";

let logoutTimer;
let initialToken;
let initialAdminToken;

const AuthContext = createContext({
  token: "",
  admintoken: "",
  isLoggedIn: false,
  isAdmin: false,
  login: (token) => {},
  adminAccess: (admintoken) => {},
  logout: () => {},
});

const calcTimeRemaining = (expirationTime) => {
  const currentTime = new Date().getTime();
  const adjExpireTime = new Date(expirationTime).getTime();
  const remaingDuration = adjExpireTime - currentTime;

  return remaingDuration;
};

export function AuthContextProvider(props) {
  const authCtx = useContext(AuthContext);
  const isAdmin = authCtx.isAdmin;

  const [token, setToken] = useState(initialToken);
  const [admintoken, setAdminToken] = useState(initialAdminToken);

  const userIsLoggedIn = !!token;
  const userHasAdmin = !!admintoken;

  useEffect(() => {
    initialToken = localStorage.getItem("token");
    initialAdminToken = localStorage.getItem("admintoken");
    if (initialAdminToken !== initialToken) {
      setToken(initialToken);
    } else {
      setToken(initialToken);
      setAdminToken(initialAdminToken);
    }
  }, [initialToken, initialAdminToken]);

  const logoutHandler = () => {
    setToken(null);
    setAdminToken(null);
    localStorage.removeItem("token");
    localStorage.removeItem("admintoken");
  };

  const loginHandler = (token) => {
    if (admintoken == null) {
      setToken(token);

      localStorage.setItem("token", token);
    } else {
      setToken(token);
      localStorage.setItem("token", token);
      setAdminToken(token);
      localStorage.setItem("admintoken", token);
    }
    // const remainingTime = calcTimeRemaining(expirationTime);
    setTimeout(logoutHandler, 300000);
  };

  const adminTokenHandler = (admintoken) => {
    setAdminToken(admintoken);
    localStorage.setItem("admintoken", admintoken);
  };

  const contextValue = {
    token: token,
    admintoken: admintoken,
    isAdmin: userHasAdmin,
    isLoggedIn: userIsLoggedIn,
    adminAccess: adminTokenHandler,
    login: loginHandler,
    logout: logoutHandler,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {props.children}
    </AuthContext.Provider>
  );
}

export default AuthContext;
