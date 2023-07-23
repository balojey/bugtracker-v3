"use client";

import AuthContext from "@/auth/context";
import LoginForm from "@/components/LoginForm";
import { useRouter } from "next/navigation";
import { useContext } from "react";

export default function LoginPage() {
  const authCtx = useContext(AuthContext);
  const router = useRouter();
  if (authCtx.isLoggedIn) {
    return router.replace("/dashboard");
  }
  return (
    <div className="">
      <main className="">
        <LoginForm />
      </main>
    </div>
  );
}
