import { useState } from 'react';
import { ResearchResult, ProgressStep } from '../types/research';
import { generateResearchReport } from '../services/api/researchApi';

export const useExecutiveResearch = () => {
  const [isProcessing, setIsProcessing] = useState(false);
  const [results, setResults] = useState<ResearchResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [progressSteps, setProgressSteps] = useState<ProgressStep[]>([
    { label: 'Planning', status: 'pending' },
    { label: 'Research', status: 'pending' },
    { label: 'Summary', status: 'pending' },
    { label: 'Report Generation', status: 'pending' },
  ]);

  const generateReport = async (query: string) => {
    setIsProcessing(true);
    setResults(null);
    setError(null);
    setProgressSteps((prev) => prev.map((step) => ({ ...step, status: 'pending' })));

    try {
      // Mock progress
      for (let i = 0; i < progressSteps.length; i++) {
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
      setProgressSteps((prev) => prev.map((step) => ({ ...step, status: 'completed' })));
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
      setProgressSteps((prev) => prev.map((step) => ({ ...step, status: 'pending' })));
    } finally {
      setIsProcessing(false);
    }
  };

  return {
    isProcessing,
    results,
    error,
    progressSteps,
    generateReport,
  };
};
