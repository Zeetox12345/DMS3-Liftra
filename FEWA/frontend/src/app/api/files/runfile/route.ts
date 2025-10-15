import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

export async function GET() {
  try {
    // Read the runfile.txt from the parent directory
    const runfilePath = path.join(process.cwd(), '..', 'Runfile.txt');

    try {
      const content = await fs.readFile(runfilePath, 'utf8');
      return new NextResponse(content, {
        headers: {
          'Content-Type': 'text/plain',
          'Content-Disposition': 'inline; filename="Runfile.txt"'
        }
      });
    } catch (fileError) {
      return NextResponse.json(
        { error: 'Runfile.txt not found. Please run an analysis first.' },
        { status: 404 }
      );
    }
  } catch (error) {
    console.error('Error serving runfile:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
