import React from 'react';
import { Card } from '../common/Card';

interface ExecutiveSummaryCardProps {
  summary: string;
  isVisible: boolean;
}

export const ExecutiveSummaryCard = ({ summary, isVisible }: ExecutiveSummaryCardProps) => {
  if (!isVisible) return null;

  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric', month: 'short', day: '2-digit',
  });

  return (
    <Card className="animate-rise-in mt-8">
      <div className="mb-5 flex items-center justify-between border-b border-hairline pb-4">
        {/* section label: body 13px semibold brass — was mono 11px */}
        <span className="font-body text-[13px] font-semibold tracking-wide text-brass">
          Executive Summary
        </span>
        <span className="font-body text-[13px] text-slate">{today}</span>
      </div>
      {/* summary text bumped to 20px for comfortable reading */}
      <p className="font-display text-[20px] italic leading-[1.65] text-ink-soft">
        {summary}
      </p>
    </Card>
  );
};
