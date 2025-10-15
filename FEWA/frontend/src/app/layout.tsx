import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-geist-sans",
});

const metadata: Metadata = {
  title: "Liftra ApS - Weld Analysis Suite",
  description: "Professional Finite Element Analysis tool for Liftra's welding solutions and engineering simulations",
  keywords: "Liftra, FEA, Finite Element Analysis, Weld Analysis, ANSYS, Engineering, Simulation, Welding",
  authors: [{ name: "Liftra ApS Engineering Team" }],
  viewport: "width=device-width, initial-scale=1",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} antialiased`}>
        {children}
      </body>
    </html>
  );
}
