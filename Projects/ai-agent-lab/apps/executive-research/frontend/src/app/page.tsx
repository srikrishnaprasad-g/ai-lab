'use client';

import React from 'react';
import { Header } from '../components/layout/Header';
import { Footer } from '../components/layout/Footer';
import { QueryInput } from '../components/forms/QueryInput';
import { ProgressTracker } from '../components/progress/ProgressTracker';
import { ExecutiveSummaryCard } from '../components/cards/ExecutiveSummaryCard';
import { KeyInsightsCard } from '../components/cards/KeyInsightsCard';
import { DownloadButton } from '../components/buttons/DownloadButton';
import { useExecutiveResearch } from '../hooks/useExecutiveResearch';

export default function Home() {
  const { isProcessing, results, error, progressSteps, generateReport } = useExecutiveResearch();

  return (
    <main className="min-h-screen bg-slate-50 flex flex-col items-center">
      <div className="w-full max-w-[960px] flex-grow flex flex-col px-4 pb-12">
        <Header />
        <QueryInput onGenerate={generateReport} isProcessing={isProcessing} />
        
        {error && (
          <div className="mt-8 p-4 bg-red-50 border border-red-200 text-red-700 rounded-lg">
            {error}
          </div>
        )}

        {(isProcessing || results) && !error && (
          <ProgressTracker steps={progressSteps} isVisible={true} />
        )}

        {results && !error && (
          <>
            <ExecutiveSummaryCard
              summary={results.executiveSummary}
              isVisible={true}
            />
            <KeyInsightsCard
              insights={results.keyInsights}
              isVisible={true}
            />
            <DownloadButton isVisible={true} reportId={results.reportId} />
          </>
        )}
        
        {!isProcessing && !results && !error && (
          <div className="mt-12 text-center text-slate-500">
            <p>Enter a research question above to generate an executive report.</p>
          </div>
        )}
      </div>
      <Footer />
    </main>
  );
}
