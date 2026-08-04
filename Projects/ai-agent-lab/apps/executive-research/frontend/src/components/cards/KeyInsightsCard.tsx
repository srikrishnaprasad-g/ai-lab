import React from 'react';
import { Check } from 'lucide-react';
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
    <Card className="mt-8">
      <h2 className="text-xl font-bold text-slate-900 mb-4">Key Insights</h2>
      <ul className="space-y-3">
        {insights.map((insight, index) => (
          <li key={index} className="flex items-start">
            <Check className="w-5 h-5 text-green-600 mr-2 mt-0.5" />
            <div className="flex flex-col">
                <span className="font-semibold text-slate-900">{insight.title}</span>
                <span className="text-slate-600">{insight.description}</span>
            </div>
          </li>
        ))}
      </ul>
    </Card>
  );
};
