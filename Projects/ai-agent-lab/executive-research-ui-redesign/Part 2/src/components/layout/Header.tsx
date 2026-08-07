'use client';

import React, { useEffect, useState } from 'react';
import { Sun, Moon } from 'lucide-react';

// The header masthead is always dark (ink navy) regardless of light/dark body theme.
// We achieve this by applying fixed colour values directly, not CSS vars.
const HDR_BG   = '#12161f';   // always-dark ink
const HDR_TEXT = '#eae8e2';   // always-light cream
const HDR_SUB  = 'rgba(234,232,226,0.65)';
const HDR_GOLD = '#c9a66b';
const HDR_GOLD_DIM = 'rgba(201,166,107,0.4)';
const HDR_BORDER = 'rgba(234,232,226,0.15)';

export const Header = () => {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const current = document.documentElement.getAttribute('data-theme') as 'light'|'dark'|null;
    const saved   = localStorage.getItem('theme') as 'light'|'dark'|null;
    const sys     = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    setTheme(current ?? saved ?? sys);
  }, []);

  const toggleTheme = () => {
    const next = theme === 'light' ? 'dark' : 'light';
    setTheme(next);
    localStorage.setItem('theme', next);
    document.documentElement.setAttribute('data-theme', next);
  };

  return (
    <header style={{ backgroundColor: HDR_BG, color: HDR_TEXT }} className="w-full">
      <div className="w-full max-w-[720px] mx-auto px-6 pt-10 pb-10">
        {/* Eyebrow row */}
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <span
              className="flex h-6 w-6 items-center justify-center rounded-full font-mono text-[10px]"
              style={{ border: `1px solid ${HDR_GOLD_DIM}`, color: HDR_GOLD }}
            >
              ×
            </span>
            <p
              className="font-mono text-[11px] tracking-[0.22em] uppercase"
              style={{ color: HDR_GOLD }}
            >
              AI Agent Lab &middot; Research Desk
            </p>
          </div>

          {/* Theme toggle — only render client-side to avoid hydration mismatch */}
          {mounted && (
            <button
              onClick={toggleTheme}
              className="flex items-center gap-1.5 rounded-full px-3 py-1.5 font-mono text-[11px] tracking-[0.1em] uppercase transition-colors duration-200"
              style={{ border: `1px solid ${HDR_BORDER}`, color: HDR_SUB }}
              aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} theme`}
            >
              {theme === 'light'
                ? <><Moon className="h-3 w-3" strokeWidth={2} />Dark</>
                : <><Sun  className="h-3 w-3" strokeWidth={2} />Light</>
              }
            </button>
          )}
        </div>

        <h1
          className="font-display text-[2.75rem] leading-[1.05] tracking-tight"
          style={{ color: HDR_TEXT }}
        >
          Executive Research
        </h1>
        <p
          className="mt-4 max-w-[46ch] font-body text-[15px] leading-relaxed"
          style={{ color: HDR_SUB }}
        >
          Put a question to the desk. Receive a structured briefing — summary,
          findings, and a formatted report — assembled by a multi-agent
          research runtime.
        </p>
      </div>

      {/* Brass hairline divider */}
      <div
        className="h-px w-full"
        style={{ background: `linear-gradient(to right, transparent, ${HDR_GOLD}, transparent)` }}
      />
    </header>
  );
};
