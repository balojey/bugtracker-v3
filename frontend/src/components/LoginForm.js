import { useState } from "react";
import { signIn, getCsrfToken } from "next-auth/react";
import { Formik, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import { useRouter } from "next/router";

export default function SignIn({ csrfToken }) {
  const router = useRouter();
  const [error, setError] = useState(null);

  return (
    <>
      <Formik
        initialValues={{ email: "", password: "", tenantKey: "" }}
        validationSchema={Yup.object({
          email: Yup.string()
            .max(30, "Must be 30 characters or less")
            .email("Invalid email address")
            .required("Please enter your email"),
          password: Yup.string().required("Please enter your password"),
        })}
        onSubmit={async (values, { setSubmitting }) => {
          const res = await signIn("credentials", {
            redirect: false,
            email: values.email,
            password: values.password,
            callbackUrl: `${window.location.origin}`,
          });
          if (res?.error) {
            setError(res.error);
          } else {
            setError(null);
          }
          if (res.url) router.push(res.url);
          setSubmitting(false);
        }}
      >
        {(formik) => (
          <form onSubmit={formik.handleSubmit}>
            <div
              className="bg-red-400 flex flex-col items-center 
            justify-center min-h-screen py-2 shadow-lg"
              style={{
                backgroundColor: "#F87171", // bg-red-400
                display: "flex", // flex
                flexDirection: "column", // flex-col
                alignItems: "center", // items-center
                justifyContent: "center", // justify-center
                minHeight: "100vh", // min-h-screen
                paddingTop: "0.5rem", // py-2
                boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", // shadow-lg
              }}
            >
              <div
                className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4"
                style={{
                  backgroundColor: "#ffffff", // bg-white
                  boxShadow:
                    "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)", // shadow-md
                  borderRadius: "0.375rem", // rounded
                  padding: "0.875rem", // px-8
                  paddingTop: "1.5rem", // pt-6
                  paddingBottom: "2rem", // pb-8
                  marginBottom: "1rem", // mb-4
                }}
              >
                <input
                  name="csrfToken"
                  type="hidden"
                  defaultValue={csrfToken}
                />

                <div
                  className="text-red-400 text-md text-center rounded p-2"
                  style={{
                    color: "#EF4444", // text-red-400
                    fontSize: "1rem", // text-md
                    textAlign: "center", // text-center
                    borderRadius: "0.25rem", // rounded
                    padding: "0.5rem", // p-2
                  }}
                >
                  {error}
                </div>
                <div className="mb-4" style={{ marginBottom: "1rem" }}>
                  <label
                    htmlFor="email"
                    className="uppercase text-sm text-gray-600 font-bold"
                    style={{
                      textTransform: "uppercase", // uppercase
                      fontSize: "0.875rem", // text-sm
                      color: "#4B5563", // text-gray-600
                      fontWeight: "bold", // font-bold
                    }}
                  >
                    Email
                    <Field
                      name="email"
                      aria-label="enter your email"
                      aria-required="true"
                      type="text"
                      className="w-full bg-gray-300 text-gray-900 mt-2 p-3"
                      style={{
                        width: "100%",
                        backgroundColor: "#d1d5db",
                        color: "#111827",
                        marginTop: "0.5rem",
                        padding: "0.75rem",
                      }}
                    />
                  </label>

                  <div
                    className="text-red-600 text-sm"
                    style={{
                      color: "#DC2626", // text-red-600
                      fontSize: "0.875rem", // text-sm
                    }}
                  >
                    <ErrorMessage name="email" />
                  </div>
                </div>
                <div className="mb-6" style={{ marginBottom: "1.5rem" }}>
                  <label
                    htmlFor="password"
                    className="uppercase text-sm text-gray-600 font-bold"
                    style={{
                      textTransform: "uppercase", // uppercase
                      fontSize: "0.875rem", // text-sm
                      color: "#4B5563", // text-gray-600
                      fontWeight: "bold", // font-bold
                    }}
                  >
                    password
                    <Field
                      name="password"
                      aria-label="enter your password"
                      aria-required="true"
                      type="password"
                      className="w-full bg-gray-300 text-gray-900 mt-2 p-3"
                      style={{
                        width: "100%",
                        backgroundColor: "#d1d5db",
                        color: "#111827",
                        marginTop: "0.5rem",
                        padding: "0.75rem",
                      }}
                    />
                  </label>

                  <div
                    className="text-red-600 text-sm"
                    style={{
                      color: "#DC2626", // text-red-600
                      fontSize: "0.875rem", // text-sm
                    }}
                  >
                    <ErrorMessage name="password" />
                  </div>
                </div>
                <div
                  className="flex items-center justify-center"
                  style={{
                    display: "flex", // flex
                    alignItems: "center", // items-center
                    justifyContent: "center", // justify-center
                  }}
                >
                  <button
                    type="submit"
                    className="bg-green-400 text-gray-100 p-3 rounded-lg w-full"
                    style={{
                      backgroundColor: "#34D399", // bg-green-400
                      color: "#F3F4F6", // text-gray-100
                      padding: "0.75rem", // p-3
                      borderRadius: "0.375rem", // rounded-lg
                      width: "100%", // w-full
                    }}
                  >
                    {formik.isSubmitting ? "Please wait..." : "Sign In"}
                  </button>
                </div>
              </div>
            </div>
          </form>
        )}
      </Formik>
    </>
  );
}

// This is the recommended way for Next.js 9.3 or newer
export async function getServerSideProps(context) {
  return {
    props: {
      csrfToken: await getCsrfToken(context),
    },
  };
}
