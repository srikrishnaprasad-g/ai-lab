'use client';

import React, { useEffect, useState } from 'react';
import { Sun, Moon, FlaskConical } from 'lucide-react';

const HDR_BG     = '#12161f';
const HDR_TEXT   = '#eae8e2';
const HDR_SUB    = 'rgba(234,232,226,0.72)';
const HDR_GOLD   = '#d4a96a';           // brighter gold — was #c9a66b
const HDR_GOLD_D = 'rgba(212,169,106,0.35)';
const HDR_BORDER = 'rgba(234,232,226,0.18)';

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

        {/* ── Eyebrow row ── */}
        <div className="flex items-center justify-between mb-7">

          {/* Left: flask icon + label — REMOVED the × circle that looked like a close button */}
          <div className="flex items-center gap-2.5">
            <FlaskConical
              className="h-4 w-4 shrink-0"
              style={{ color: HDR_GOLD }}
              strokeWidth={1.75}
            />
            {/* Inter body font, 13px, high-contrast gold — replaces unreadable mono 11px */}
            <span
              className="font-body text-[13px] font-medium tracking-wide"
              style={{ color: HDR_GOLD, letterSpacing: '0.04em' }}
            >
              AI Agent Lab · Research Desk
            </span>
          </div>

          {/* Right: theme toggle */}
          {mounted && (
            <button
              onClick={toggleTheme}
              className="flex items-center gap-1.5 rounded-full px-3.5 py-1.5 font-body text-[13px] font-medium transition-colors duration-200"
              style={{ border: `1px solid ${HDR_BORDER}`, color: HDR_SUB }}
              aria-label={`Switch to ${theme === 'light' ? 'dark' : 'light'} theme`}
            >
              {theme === 'light'
                ? <><Moon className="h-3.5 w-3.5" strokeWidth={2} /> Dark</>
                : <><Sun  className="h-3.5 w-3.5" strokeWidth={2} /> Light</>
              }
            </button>
          )}
        </div>

        {/* ── Main title ── */}
        <h1
          className="font-display text-[2.75rem] leading-[1.05] tracking-tight"
          style={{ color: HDR_TEXT }}
        >
          Executive Research
        </h1>

        {/* ── Subtitle ── */}
        <p
          className="mt-4 max-w-[46ch] font-body text-[16px] leading-relaxed"
          style={{ color: HDR_SUB }}
        >
          Put a question to the desk. Receive a structured briefing — summary,
          findings, and a formatted report — assembled by a multi-agent
          research runtime.
        </p>
      </div>

      <div
        className="h-px w-full"
        style={{ background: `linear-gradient(to right, transparent, ${HDR_GOLD}, transparent)` }}
      />
    </header>
  );
};
