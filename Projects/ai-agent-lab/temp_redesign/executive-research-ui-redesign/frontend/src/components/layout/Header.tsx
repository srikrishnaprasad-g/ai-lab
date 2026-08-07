import React from 'react';

export const Header = () => {
  return (
    <header className="w-full bg-ink text-paper">
      <div className="w-full max-w-[720px] mx-auto px-6 pt-14 pb-10">
        <div className="flex items-center gap-3 mb-6">
          <span className="flex h-6 w-6 items-center justify-center rounded-full border border-brass-dim text-brass-light font-mono text-[10px]">
            ×
          </span>
          <p className="font-mono text-[11px] tracking-[0.22em] uppercase text-brass-light">
            AI Agent Lab &middot; Research Desk
          </p>
        </div>
        <h1 className="font-display text-[2.75rem] leading-[1.05] tracking-tight text-paper">
          Executive Research
        </h1>
        <p className="mt-4 max-w-[46ch] font-body text-[15px] leading-relaxed text-paper/70">
          Put a question to the desk. Receive a structured briefing — summary,
          findings, and a formatted report — assembled by a multi-agent
          research runtime.
        </p>
      </div>
      <div className="h-px w-full bg-gradient-to-r from-transparent via-brass to-transparent" />
    </header>
  );
};
