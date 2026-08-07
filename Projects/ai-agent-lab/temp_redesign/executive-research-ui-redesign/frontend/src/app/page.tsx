'use client';

import React from 'react';
import { AlertTriangle, Search } from 'lucide-react';
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
    <main className="flex min-h-screen w-full flex-col items-center">
      <Header />

      <div className="flex w-full max-w-[720px] flex-grow flex-col px-6 pb-20">
        <div className="mt-8">
          <QueryInput onGenerate={generateReport} isProcessing={isProcessing} />
        </div>

        {error && (
          <div className="animate-rise-in mt-8 flex items-start gap-3 rounded-md border border-rust/30 bg-rust-bg px-5 py-4">
            <AlertTriangle className="mt-0.5 h-4 w-4 shrink-0 text-rust" />
            <div>
              <p className="font-body text-[14px] font-medium text-rust">
                The desk couldn&apos;t complete this brief
              </p>
              <p className="mt-0.5 font-body text-[13px] text-rust/80">{error}</p>
            </div>
          </div>
        )}

        {(isProcessing || results) && !error && (
          <ProgressTracker steps={progressSteps} isVisible={true} />
        )}

        {results && !error && (
          <>
            <ExecutiveSummaryCard summary={results.executiveSummary} isVisible={true} />
            <KeyInsightsCard insights={results.keyInsights} isVisible={true} />
            <DownloadButton isVisible={true} reportId={results.reportId} />
          </>
        )}

        {!isProcessing && !results && !error && (
          <div className="mt-16 flex flex-col items-center text-center">
            <div className="flex h-11 w-11 items-center justify-center rounded-full border border-hairline text-slate-soft">
              <Search className="h-4 w-4" strokeWidth={1.75} />
            </div>
            <p className="mt-4 max-w-[38ch] font-body text-[14px] leading-relaxed text-slate-soft">
              Nothing commissioned yet. Ask a real question above and the desk
              will return with a structured briefing.
            </p>
          </div>
        )}
      </div>

      <Footer />
    </main>
  );
}
