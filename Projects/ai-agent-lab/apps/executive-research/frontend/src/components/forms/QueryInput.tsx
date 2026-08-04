'use client';

import React from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  query: z.string().min(20, 'Query must be at least 20 characters').max(5000, 'Query must be at most 5000 characters'),
});

type FormData = z.infer<typeof schema>;

interface QueryInputProps {
  onGenerate: (query: string) => void;
  isProcessing: boolean;
}

export const QueryInput = ({ onGenerate, isProcessing }: QueryInputProps) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  const onSubmit = (data: FormData) => {
    onGenerate(data.query);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="w-full">
      <textarea
        {...register('query')}
        className="w-full h-40 p-4 border border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-600 focus:border-transparent"
        placeholder="Analyze the impact of AI Agents on Enterprise SaaS..."
      />
      {errors.query && <p className="text-red-600 mt-2 text-sm">{errors.query.message}</p>}
      <button
        type="submit"
        disabled={isProcessing}
        className="mt-4 w-full bg-blue-600 text-white font-medium py-3 rounded-lg disabled:bg-slate-400 transition-colors"
      >
        {isProcessing ? 'Generating Executive Report...' : 'Generate Executive Report'}
      </button>
    </form>
  );
};
