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

  return (
    <div className="w-full mt-8 p-6 bg-white border border-slate-200 rounded-lg shadow-sm">
      <div className="flex justify-between items-center relative">
        {steps.map((step, index) => (
          <React.Fragment key={index}>
            <div className="flex flex-col items-center relative z-10">
              <div
                className={clsx(
                  'w-8 h-8 rounded-full flex items-center justify-center border-2 mb-2 transition-colors duration-300',
                  step.status === 'pending' && 'border-slate-200 bg-white text-slate-400',
                  step.status === 'running' && 'border-blue-600 bg-white text-blue-600 animate-pulse',
                  step.status === 'completed' && 'border-green-600 bg-green-600 text-white'
                )}
              >
                {step.status === 'completed' ? <Check className="w-5 h-5" /> : index + 1}
              </div>
              <span className={clsx('text-sm font-medium', step.status === 'pending' ? 'text-slate-400' : 'text-slate-900')}>{step.label}</span>
            </div>
            {index < steps.length - 1 && (
              <div className="absolute top-4 left-[10%] right-[10%] h-0.5 bg-slate-200 -z-0" />
            )}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
};
