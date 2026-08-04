import React from 'react';
import { Card } from '../common/Card';

interface ExecutiveSummaryCardProps {
  summary: string;
  isVisible: boolean;
}

export const ExecutiveSummaryCard = ({ summary, isVisible }: ExecutiveSummaryCardProps) => {
  if (!isVisible) return null;

  return (
    <Card className="mt-8">
      <h2 className="text-xl font-bold text-slate-900 mb-4">Executive Summary</h2>
      <p className="text-slate-600 leading-relaxed">{summary}</p>
    </Card>
  );
};
