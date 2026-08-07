import React from 'react';
import { FileText } from 'lucide-react';
import { API_BASE_URL } from '@/config/api';

interface DownloadButtonProps {
  isVisible: boolean;
  reportId: string;
}

export const DownloadButton = ({ isVisible, reportId }: DownloadButtonProps) => {
  if (!isVisible) return null;

  const handleDownload = () => {
    window.location.href = `${API_BASE_URL}/api/v1/download/${reportId}`;
  };

  return (
    <div className="animate-rise-in mt-6 flex w-full items-center justify-between rounded-md border border-hairline bg-paper-raised px-6 py-5">
      <div className="flex items-center gap-3">
        <div className="flex h-9 w-9 items-center justify-center rounded-full bg-moss-bg text-moss">
          <FileText className="h-4 w-4" strokeWidth={2} />
        </div>
        <div>
          <p className="font-body text-[14px] font-medium text-ink">Report ready</p>
          <p className="font-mono text-[11px] text-slate-soft">
            REF {reportId}
          </p>
        </div>
      </div>
      <button
        onClick={handleDownload}
        className="rounded-md bg-ink px-5 py-2.5 font-body text-[13px] font-medium text-paper transition-colors duration-200 hover:bg-ink-soft focus-brass"
      >
        Download PDF
      </button>
    </div>
  );
};
