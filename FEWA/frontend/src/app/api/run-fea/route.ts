import { NextRequest, NextResponse } from 'next/server';
import { spawn } from 'child_process';
import path from 'path';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { weldLength, weldWidth, weldThick, weldThroat } = body;

    // Validate inputs
    if (!weldLength || !weldWidth || !weldThick || !weldThroat) {
      return NextResponse.json(
        { error: 'All weld parameters are required' },
        { status: 400 }
      );
    }

    // Update UsrInput.txt with new parameters
    const usrInputContent = `# User Input [in mm]
Weldlength = ${weldLength}
Weldwidth = ${weldWidth}
Weldthick = ${weldThick}
Weldthroat = ${weldThroat}`;

    // Write to UsrInput.txt in the parent directory
    const fs = await import('fs/promises');
    await fs.writeFile(
      path.join(process.cwd(), '..', 'UsrInput.txt'),
      usrInputContent
    );

    // Run the Python script
    return new Promise((resolve) => {
      const pythonProcess = spawn('python', ['MainFEWA.py'], {
        cwd: path.join(process.cwd(), '..'),
        stdio: ['pipe', 'pipe', 'pipe']
      });

      let stdout = '';
      let stderr = '';

      pythonProcess.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      pythonProcess.on('close', (code) => {
        if (code === 0) {
          resolve(NextResponse.json({
            success: true,
            message: 'FEA analysis completed successfully',
            output: stdout
          }));
        } else {
          resolve(NextResponse.json({
            success: false,
            error: 'FEA analysis failed',
            details: stderr || stdout
          }, { status: 500 }));
        }
      });

      pythonProcess.on('error', (error) => {
        resolve(NextResponse.json({
          success: false,
          error: 'Failed to start Python script',
          details: error.message
        }, { status: 500 }));
      });
    });

  } catch (error) {
    console.error('API Error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
