import React, { useEffect } from 'react';
import {
  isRouteErrorResponse,
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
  type ErrorResponse
} from "react-router";
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import "./styles/global.css";

const CURRENT_APP_VERSION = "v1.0.1"; // Replace with your actual versioning strategy

// Create a client instance
const queryClient = new QueryClient();

export const links = () => [
  { rel: "preconnect", href: "https://fonts.googleapis.com" },
  {
    rel: "preconnect",
    href: "https://fonts.gstatic.com",
    crossOrigin: "anonymous",
  },
  {
    rel: "stylesheet",
    href: "https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap",
  },
];

export function Layout({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    const storedVersion = localStorage.getItem('appVersion');
    if (storedVersion !== CURRENT_APP_VERSION) {
      console.log(`Cache cleared due to version mismatch. Old: ${storedVersion}, New: ${CURRENT_APP_VERSION}`);
      localStorage.setItem('appVersion', CURRENT_APP_VERSION);
      // Optionally clear other sensitive localStorage data here
      // localStorage.removeItem('userToken');
      window.location.reload();
    }
  }, []);

  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" type="image/x-icon" href="/favicon.ico" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Outlet />
    </QueryClientProvider>
  );
}

interface ErrorBoundaryProps {
  error: Error | ErrorResponse | unknown;
}

export function ErrorBoundary({ error }: ErrorBoundaryProps) {
  let message = "Oops!";
  let details = "An unexpected error occurred.";
  let stack: string | undefined;

  if (isRouteErrorResponse(error)) {
    message = error.status === 404 ? "404" : "Error";
    details =
      error.status === 404
        ? "The requested page could not be found."
        : error.statusText || details;
  } else if (error instanceof Error) {
    details = error.message;
    stack = error.stack;
  }

  return (
    <main className="pt-16 p-4 container mx-auto">
      <h1>{message}</h1>
      <p>{details}</p>
      {stack && (
        <pre className="w-full p-4 overflow-x-auto">
          <code>{stack}</code>
        </pre>
      )}
    </main>
  );
} 