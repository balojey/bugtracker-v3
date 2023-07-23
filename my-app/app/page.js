"use client"

import Link from "next/link";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  return (
    <div>
      {/* Home navbar begins */}
      <header className="navbar bg-base-100">
        <div className="flex-1">
          <Link
            href="./"
            className="btn btn-ghost normal-case text-xl rounded-none"
          >
            bugtracker
          </Link>
        </div>
        <nav className="flex-none">
          <ul className="menu menu-horizontal px-1">
            <li>
              <Link href="./" className="rounded-none">
                Sign Up
              </Link>
            </li>
            <li>
              <Link href="/login" className="font-semibold rounded-none">
                Login
              </Link>
            </li>
          </ul>
        </nav>
      </header>
      {/* Home navbar ends */}

      {/* Home hero section begins */}
      <section
        className="hero min-h-screen"
        style={{
          backgroundImage: "url(../public/hero-banner.png)",
        }}
      >
        <div className="hero-overlay bg-opacity-60"></div>
        <div className="hero-content text-center text-neutral-content">
          <div className="max-w-md">
            <h1 className="mb-5 text-5xl font-bold">
              Keep track of bugs, seamlessly!
            </h1>
            <p className="mb-5">
              Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda
              excepturi exercitationem quasi. In deleniti eaque aut repudiandae
              et a id nisi.
            </p>
            <button
              className="btn btn-primary rounded-none w-48"
              onClick={() => router.push("./dashboard")}
            >
              Get Started
            </button>
          </div>
        </div>
      </section>
      {/* Home hero section ends */}
    </div>
  );
}
