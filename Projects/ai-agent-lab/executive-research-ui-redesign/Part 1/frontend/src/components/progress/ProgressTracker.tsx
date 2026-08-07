import React from 'react';
import { clsx } from 'clsx';
import { Check } from 'lucide-react';
import { ProgressStep } from '../../types/research';

interface ProgressTrackerProps {
  steps: ProgressStep[];
  isVisible: boolean;
}

export const ProgressTracker = ({ steps, isVisible }: ProgressTrackerProps) => {
  if (!isVisible) return null;

  const completedCount = steps.filter((s) => s.status === 'completed').length;
  const runningIndex = steps.findIndex((s) => s.status === 'running');
  const fillIndex = runningIndex >= 0 ? runningIndex : completedCount;
  const fillPercent = steps.length > 1 ? (fillIndex / (steps.length - 1)) * 100 : 0;

  return (
    <div className="animate-rise-in mt-10 w-full rounded-md border border-hairline bg-paper-raised p-6">
      <p className="mb-6 font-mono text-[11px] tracking-[0.16em] uppercase text-slate-soft">
        Assembling the briefing
      </p>
      <div className="relative pl-1">
        {/* the spine */}
        <div className="absolute left-[15px] top-1 bottom-1 w-px bg-hairline" />
        <div
          className="absolute left-[15px] top-1 w-px bg-brass transition-all duration-700 ease-out"
          style={{ height: `calc(${fillPercent}% )` }}
        />

        <div className="flex flex-col gap-7">
          {steps.map((step, index) => (
            <div key={index} className="relative flex items-start gap-4">
              <div
                className={clsx(
                  'relative z-10 flex h-8 w-8 shrink-0 items-center justify-center rounded-full border font-mono text-[11px] transition-colors duration-300',
                  step.status === 'pending' &&
                    'border-hairline bg-paper-raised text-slate-soft',
                  step.status === 'running' &&
                    'border-brass bg-paper-raised text-brass',
                  step.status === 'completed' &&
                    'border-brass bg-brass text-paper'
                )}
              >
                {step.status === 'completed' ? (
                  <Check className="h-4 w-4" strokeWidth={2.5} />
                ) : (
                  String(index + 1).padStart(2, '0')
                )}
              </div>
              <div className="pt-1.5">
                <span
                  className={clsx(
                    'font-body text-[14px] font-medium',
                    step.status === 'pending' ? 'text-slate-soft' : 'text-ink'
                  )}
                >
                  {step.label}
                </span>
                {step.status === 'running' && (
                  <span className="ml-2 font-mono text-[11px] text-brass">
                    in progress
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
