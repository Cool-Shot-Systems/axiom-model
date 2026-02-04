import type { Metadata } from "next";

import "../styles/globals.css";

export const metadata: Metadata = {
  title: "AXIOM",
  description: "AXIOM is an AI model developed and operated by Cool Shot Systems.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
