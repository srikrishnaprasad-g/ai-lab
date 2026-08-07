import React from 'react';
import { clsx } from 'clsx';
import { Card } from '../common/Card';

interface KeyInsight {
  title: string;
  description: string;
}

interface KeyInsightsCardProps {
  insights: KeyInsight[];
  isVisible: boolean;
}

export const KeyInsightsCard = ({ insights, isVisible }: KeyInsightsCardProps) => {
  if (!isVisible) return null;

  return (
    <Card className="animate-rise-in mt-6 !p-0">
      <div className="border-b border-hairline px-7 py-4">
        <span className="font-mono text-[11px] tracking-[0.16em] uppercase text-brass">
          Key Findings
        </span>
      </div>
      <ul>
        {insights.map((insight, index) => (
          <li
            key={index}
            className={clsx(
              'flex items-start gap-4 px-7 py-5',
              index !== insights.length - 1 && 'border-b border-hairline'
            )}
          >
            <span className="mt-0.5 font-mono text-[12px] text-slate-soft">
              {String(index + 1).padStart(2, '0')}
            </span>
            <div className="flex flex-col gap-1">
              <span className="font-body text-[15px] font-semibold text-ink">
                {insight.title}
              </span>
              <span className="font-body text-[14px] leading-relaxed text-slate">
                {insight.description}
              </span>
            </div>
          </li>
        ))}
      </ul>
    </Card>
  );
};
