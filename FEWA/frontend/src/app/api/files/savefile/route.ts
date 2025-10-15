import { NextResponse } from 'next/server';
import fs from 'fs/promises';
import path from 'path';

export async function GET() {
  try {
    // Read the savefile.db from the parent directory
    const savefilePath = path.join(process.cwd(), '..', 'SaveFile.db');

    try {
      const content = await fs.readFile(savefilePath);
      return new NextResponse(content, {
        headers: {
          'Content-Type': 'application/octet-stream',
          'Content-Disposition': 'attachment; filename="SaveFile.db"'
        }
      });
    } catch (fileError) {
      return NextResponse.json(
        { error: 'SaveFile.db not found. Please run an analysis first.' },
        { status: 404 }
      );
    }
  } catch (error) {
    console.error('Error serving savefile:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
