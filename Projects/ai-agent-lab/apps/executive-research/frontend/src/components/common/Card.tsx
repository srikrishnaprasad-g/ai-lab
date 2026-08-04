import React from 'react';
import { clsx } from 'clsx';

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

export const Card = ({ children, className }: CardProps) => {
  return (
    <div className={clsx('w-full p-6 bg-white border border-slate-200 rounded-lg shadow-sm', className)}>
      {children}
    </div>
  );
};
