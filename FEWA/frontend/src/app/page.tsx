'use client';

import { useState } from 'react';
import { Calculator, Zap, Settings, Activity, FileText, Download, Building2 } from 'lucide-react';

interface WeldParams {
  weldLength: string;
  weldWidth: string;
  weldThick: string;
  weldThroat: string;
}

export default function Home() {
  const [params, setParams] = useState<WeldParams>({
    weldLength: '100',
    weldWidth: '50',
    weldThick: '4',
    weldThroat: '4'
  });
  const [isRunning, setIsRunning] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [runfileContent, setRunfileContent] = useState<string | null>(null);

  const handleInputChange = (field: keyof WeldParams, value: string) => {
    setParams(prev => ({ ...prev, [field]: value }));
    setError(null);
  };

  const runAnalysis = async () => {
    setIsRunning(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('/api/run-fea', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          weldLength: parseFloat(params.weldLength),
          weldWidth: parseFloat(params.weldWidth),
          weldThick: parseFloat(params.weldThick),
          weldThroat: parseFloat(params.weldThroat)
        }),
      });

      const data = await response.json();

      if (data.success) {
        setResult(data.message);
      } else {
        setError(data.error || 'Analysis failed');
      }
    } catch (err) {
      setError('Failed to connect to analysis server');
    } finally {
      setIsRunning(false);
    }
  };

  const viewRunfile = async () => {
    try {
      const response = await fetch('/api/files/runfile');
      if (response.ok) {
        const content = await response.text();
        setRunfileContent(content);
      } else {
        setError('Runfile not found. Please run an analysis first.');
      }
    } catch (err) {
      setError('Failed to load runfile');
    }
  };

  const downloadSavefile = () => {
    const link = document.createElement('a');
    link.href = '/api/files/savefile';
    link.download = 'SaveFile.db';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Animated background */}
      <div className="animated-gradient absolute inset-0 opacity-20"></div>

      {/* FEA Grid overlay */}
      <div className="fea-grid absolute inset-0 opacity-10"></div>

      <div className="relative z-10 min-h-screen flex items-center justify-center p-4">
        <div className="glass rounded-3xl p-8 w-full max-w-2xl shadow-2xl">
          {/* Header */}
          <div className="text-center mb-8">
            <div className="flex items-center justify-center gap-3 mb-4">
              <div className="p-3 rounded-full bg-gradient-to-br from-blue-600 to-blue-800 shadow-lg">
                <Building2 className="w-8 h-8 text-white" />
              </div>
              <h1 className="text-4xl font-bold bg-gradient-to-r from-blue-600 via-blue-800 to-blue-400 bg-clip-text text-transparent">
                Liftra ApS - Weld Analysis
              </h1>
            </div>
            <p className="text-gray-700 text-lg">
              Professional Finite Element Analysis for Liftra's welding solutions
            </p>
          </div>

          {/* Parameter Input Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div className="param-card rounded-2xl p-6">
              <div className="flex items-center gap-3 mb-4">
                <Zap className="w-5 h-5 text-blue-600" />
                <label className="text-lg font-semibold text-gray-800">
                  Weld Length (mm)
                </label>
              </div>
              <input
                type="number"
                value={params.weldLength}
                onChange={(e) => handleInputChange('weldLength', e.target.value)}
                className="input-fea w-full px-4 py-3 rounded-xl text-lg font-mono"
                placeholder="100"
                disabled={isRunning}
              />
            </div>

            <div className="param-card rounded-2xl p-6">
              <div className="flex items-center gap-3 mb-4">
                <Settings className="w-5 h-5 text-purple-600" />
                <label className="text-lg font-semibold text-gray-800">
                  Weld Width (mm)
                </label>
              </div>
              <input
                type="number"
                value={params.weldWidth}
                onChange={(e) => handleInputChange('weldWidth', e.target.value)}
                className="input-fea w-full px-4 py-3 rounded-xl text-lg font-mono"
                placeholder="50"
                disabled={isRunning}
              />
            </div>

            <div className="param-card rounded-2xl p-6">
              <div className="flex items-center gap-3 mb-4">
                <Activity className="w-5 h-5 text-cyan-600" />
                <label className="text-lg font-semibold text-gray-800">
                  Weld Thickness (mm)
                </label>
              </div>
              <input
                type="number"
                value={params.weldThick}
                onChange={(e) => handleInputChange('weldThick', e.target.value)}
                className="input-fea w-full px-4 py-3 rounded-xl text-lg font-mono"
                placeholder="4"
                disabled={isRunning}
              />
            </div>

            <div className="param-card rounded-2xl p-6">
              <div className="flex items-center gap-3 mb-4">
                <Calculator className="w-5 h-5 text-green-600" />
                <label className="text-lg font-semibold text-gray-800">
                  Weld Throat (mm)
                </label>
              </div>
              <input
                type="number"
                value={params.weldThroat}
                onChange={(e) => handleInputChange('weldThroat', e.target.value)}
                className="input-fea w-full px-4 py-3 rounded-xl text-lg font-mono"
                placeholder="4"
                disabled={isRunning}
              />
            </div>
          </div>

          {/* Run Analysis Button */}
          <div className="text-center mb-8">
            <button
              onClick={runAnalysis}
              disabled={isRunning}
              className={`btn-fea px-12 py-4 rounded-2xl text-white font-bold text-xl transition-all duration-300 ${
                isRunning ? 'opacity-50 cursor-not-allowed' : 'hover:scale-105'
              }`}
            >
              {isRunning ? (
                <div className="flex items-center gap-3">
                  <div className="loading-pulse w-5 h-5 rounded-full bg-white opacity-70"></div>
                  Running FEA Analysis...
                </div>
              ) : (
                <div className="flex items-center gap-3">
                  <Zap className="w-6 h-6" />
                  Run Analysis
                </div>
              )}
            </button>
          </div>

          {/* Results */}
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-2xl p-6 mb-6">
              <div className="flex items-center gap-3 text-red-800">
                <div className="w-3 h-3 rounded-full bg-red-500"></div>
                <span className="font-semibold">Analysis Error</span>
              </div>
              <p className="text-red-700 mt-2">{error}</p>
            </div>
          )}

          {result && (
            <div className="bg-green-50 border border-green-200 rounded-2xl p-6 mb-6">
              <div className="flex items-center gap-3 text-green-800">
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
                <span className="font-semibold">Analysis Complete</span>
              </div>
              <p className="text-green-700 mt-2">{result}</p>
              <div className="mt-4 text-sm text-green-600">
                Check the output files in your project directory for detailed results.
              </div>
            </div>
          )}

          {/* File Actions */}
          {result && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
              <button
                onClick={viewRunfile}
                className="btn-fea px-6 py-3 rounded-xl text-white font-semibold flex items-center justify-center gap-2"
              >
                <FileText className="w-5 h-5" />
                View Runfile
              </button>
              <button
                onClick={downloadSavefile}
                className="btn-fea px-6 py-3 rounded-xl text-white font-semibold flex items-center justify-center gap-2"
              >
                <Download className="w-5 h-5" />
                Download SaveFile
              </button>
            </div>
          )}

          {/* Runfile Content Modal */}
          {runfileContent && (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
              <div className="glass rounded-2xl p-6 w-full max-w-4xl max-h-[80vh] overflow-auto">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-xl font-bold text-white">Runfile.txt Content</h3>
                  <button
                    onClick={() => setRunfileContent(null)}
                    className="text-white hover:text-gray-300 text-2xl"
                  >
                    ×
                  </button>
                </div>
                <pre className="bg-gray-900 text-green-400 p-4 rounded-lg text-sm overflow-auto max-h-96 whitespace-pre-wrap">
                  {runfileContent}
                </pre>
              </div>
            </div>
          )}

          {/* Technical Info */}
          <div className="text-center text-sm text-gray-600">
            <p>Liftra ApS • Advanced Engineering Solutions</p>
            <p className="mt-2">Powered by ANSYS APDL • Finite Element Analysis Engine</p>
          </div>
        </div>
      </div>
    </div>
  );
}
