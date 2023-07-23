"use client";

// import { createAvatar } from "@dicebear/core";
// import { adventurer } from "@dicebear/collection";

import AuthContext from "@/auth/context";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useContext } from "react";

export default function NavBar() {
  const router = useRouter();
  const authCtx = useContext(AuthContext);

  const handleLogout = () => {
    authCtx.logout();
    // return router.replace("/");
  };
  //   const avatar = createAvatar(adventurer, {
  //     seed: "Oscar",
  //   });

  //   const svg = avatar.toString();

  return (
    <header>
      <div className="navbar bg-base-100">
        <div className="flex-1">
          <Link
            className="btn btn-ghost normal-case text-xl rounded-none"
            href="/"
          >
            bugtracker
          </Link>
        </div>
        <div className="flex-none">
          <div className="dropdown dropdown-end">
            <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
              <div className="w-10 rounded-full">
                <img
                  src="https://api.dicebear.com/6.x/adventurer/svg?seed=Oscar"
                  alt="avatar"
                />
              </div>
            </label>
            <ul
              tabIndex={0}
              className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52"
            >
              <li>
                <Link className="justify-between" href="./">
                  Profile
                  <span className="badge">New</span>
                </Link>
              </li>
              <li>
                <Link href="./">Settings</Link>
              </li>
              <li>
                <button onClick={handleLogout}>Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </header>
  );
}
