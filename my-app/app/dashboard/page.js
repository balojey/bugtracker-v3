"use client";

import { useContext, useEffect, useState } from "react";
import NavBar from "@/components/NavBar";
import BottomNavigation from "@/components/BottomNavigation";
import Projects from "@/components/Projects";
import Bugs from "@/components/Bugs";
import { useRouter } from "next/navigation";
import AuthContext from "@/auth/context";

export default function DashBoard() {
  const authCtx = useContext(AuthContext);
  const router = useRouter();
  const [activeTab, setActiveTab] = useState("");

  const renderComponent = () => {
    switch (activeTab) {
      case "bugs":
        return <Bugs />;
      case "projects":
        return <Projects />;
      default:
        return <Bugs />;
    }
  };

  if (!authCtx.isLoggedIn) return router.push("/login");
  return (
    <div>
      <NavBar />
      <main className="container mx-auto">{renderComponent()}</main>
      <BottomNavigation activeTab={activeTab} setActiveTab={setActiveTab} />
    </div>
  );
}
