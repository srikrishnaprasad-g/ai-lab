import React from 'react';
import { clsx } from 'clsx';
import { Card } from '../common/Card';

interface KeyInsight { title: string; description: string; }
interface KeyInsightsCardProps { insights: KeyInsight[]; isVisible: boolean; }

export const KeyInsightsCard = ({ insights, isVisible }: KeyInsightsCardProps) => {
  if (!isVisible) return null;

  return (
    <Card className="animate-rise-in mt-6 !p-0">
      <div className="border-b border-hairline px-7 py-4">
        {/* section label: body 13px semibold brass */}
        <span className="font-body text-[13px] font-semibold tracking-wide text-brass">
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
            {/* index number: body 14px (was mono 12px) */}
            <span className="mt-0.5 font-body text-[14px] font-medium text-slate min-w-[1.5rem]">
              {String(index + 1).padStart(2, '0')}
            </span>
            <div className="flex flex-col gap-1.5">
              <span className="font-body text-[16px] font-semibold text-ink">
                {insight.title}
              </span>
              {/* description bumped to 15px, slate (not slate-soft) */}
              <span className="font-body text-[15px] leading-relaxed text-slate">
                {insight.description}
              </span>
            </div>
          </li>
        ))}
      </ul>
    </Card>
  );
};
