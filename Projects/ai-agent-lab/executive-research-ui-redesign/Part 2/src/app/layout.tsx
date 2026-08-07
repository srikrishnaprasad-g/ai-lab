import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Executive Research — AI Agent Lab",
  description: "Commission an executive-ready research briefing.",
};

const themeScript = `
(function() {
  try {
    var saved = localStorage.getItem('theme');
    var prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var theme = saved || (prefersDark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
  } catch(e) {}
})();
`;

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className="h-full antialiased preview-fonts" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeScript }} />
      </head>
      <body className="min-h-full flex flex-col transition-colors duration-200" suppressHydrationWarning>
        {children}
      </body>
    </html>
  );
}
