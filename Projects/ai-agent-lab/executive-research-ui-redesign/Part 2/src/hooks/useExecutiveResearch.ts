import { useState } from 'react';
import { ResearchResult, ProgressStep } from '../types/research';
import { generateResearchReport } from '../services/api/researchApi';

const INITIAL_STEPS: ProgressStep[] = [
  { label: 'Planning', status: 'pending' },
  { label: 'Research', status: 'pending' },
  { label: 'Summary', status: 'pending' },
  { label: 'Report Generation', status: 'pending' },
];

export const useExecutiveResearch = () => {
  const [isProcessing, setIsProcessing] = useState(false);
  const [results, setResults] = useState<ResearchResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progressSteps, setProgressSteps] = useState<ProgressStep[]>(INITIAL_STEPS);

  const generateReport = async (query: string) => {
    setIsProcessing(true);
    setResults(null);
    setError(null);
    setProgressSteps(INITIAL_STEPS.map((s) => ({ ...s, status: 'pending' })));

    try {
      for (let i = 0; i < INITIAL_STEPS.length; i++) {
        setProgressSteps((prev) =>
          prev.map((step, index) => ({
            ...step,
            status: index === i ? 'running' : index < i ? 'completed' : 'pending',
          }))
        );
        await new Promise((resolve) => setTimeout(resolve, 500));
      }

      const data = await generateResearchReport(query);
      setResults(data);
      setProgressSteps(INITIAL_STEPS.map((s) => ({ ...s, status: 'completed' })));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
      setProgressSteps(INITIAL_STEPS.map((s) => ({ ...s })));
    } finally {
      setIsProcessing(false);
    }
  };

  const reset = () => {
    setResults(null);
    setError(null);
    setProgressSteps(INITIAL_STEPS.map((s) => ({ ...s })));
  };

  return { isProcessing, results, error, progressSteps, generateReport, reset };
};
