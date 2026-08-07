import React from 'react';
import { clsx } from 'clsx';

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

export const Card = ({ children, className }: CardProps) => {
  return (
    <div
      className={clsx(
        'w-full rounded-md border border-hairline bg-paper-raised p-7',
        className
      )}
    >
      {children}
    </div>
  );
};
