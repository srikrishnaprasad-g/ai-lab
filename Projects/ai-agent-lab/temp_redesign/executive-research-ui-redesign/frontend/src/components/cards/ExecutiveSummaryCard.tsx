import React from 'react';
import { Card } from '../common/Card';

interface ExecutiveSummaryCardProps {
  summary: string;
  isVisible: boolean;
}

export const ExecutiveSummaryCard = ({ summary, isVisible }: ExecutiveSummaryCardProps) => {
  if (!isVisible) return null;

  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
  });

  return (
    <Card className="animate-rise-in mt-8">
      <div className="mb-5 flex items-center justify-between border-b border-hairline pb-4">
        <span className="font-mono text-[11px] tracking-[0.16em] uppercase text-brass">
          Executive Summary
        </span>
        <span className="font-mono text-[11px] text-slate-soft">{today}</span>
      </div>
      <p className="font-display text-[19px] italic leading-relaxed text-ink-soft">
        {summary}
      </p>
    </Card>
  );
};
