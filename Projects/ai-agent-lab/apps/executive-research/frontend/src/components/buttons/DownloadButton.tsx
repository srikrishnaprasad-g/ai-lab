import React from 'react';

interface DownloadButtonProps {
  isVisible: boolean;
  reportId: string;
}

export const DownloadButton = ({ isVisible, reportId }: DownloadButtonProps) => {
  if (!isVisible) return null;

  const handleDownload = () => {
    window.location.href = `http://localhost:8000/api/v1/download/${reportId}`;
  };

  return (
    <div className="w-full mt-8">
      <button
        onClick={handleDownload}
        className="w-full bg-slate-900 text-white font-medium py-3 rounded-lg hover:bg-slate-800 transition-colors"
      >
        Download Executive Report (PDF)
      </button>
    </div>
  );
};
