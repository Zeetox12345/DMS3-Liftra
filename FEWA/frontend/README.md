# Liftra ApS - Weld Analysis Suite

A professional Next.js web application for Liftra's Finite Element Analysis on weld joints using ANSYS APDL.

## 🚀 Features

- **Liftra Professional Interface**: Beautiful, clean design with Liftra's brand colors and glass morphism effects
- **Real-time Parameter Input**: Easy-to-use interface for weld geometry parameters with improved visibility
- **File Management**: View ANSYS runfiles and download save files directly from the web interface
- **API Integration**: Seamless integration with Python FEA scripts
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Liftra Branding**: Professional blue color scheme representing Liftra's engineering excellence

## 🛠 Technology Stack

- **Frontend**: Next.js 15 with TypeScript
- **Styling**: Tailwind CSS with custom Liftra-themed gradients
- **Backend**: Next.js API Routes
- **Icons**: Lucide React
- **FEA Engine**: Python with ANSYS APDL integration

## 🎨 Design Features

- **Liftra Brand Colors**: Professional blue gradient scheme representing Liftra's engineering excellence
- **Animated Gradients**: Dynamic color transitions for visual appeal
- **Glass Morphism**: Modern translucent design elements
- **FEA Grid Pattern**: Technical grid overlay for authentic engineering feel
- **Professional Typography**: Clean, readable Inter font
- **Interactive Elements**: Smooth hover effects and loading animations
- **Enhanced Input Visibility**: Dark text on light backgrounds for better readability

## 📁 Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── run-fea/
│   │   │   │   └── route.ts    # API endpoint for FEA analysis
│   │   │   └── files/
│   │   │       ├── runfile/
│   │   │       │   └── route.ts # API endpoint to view runfile.txt
│   │   │       └── savefile/
│   │   │           └── route.ts # API endpoint to download savefile.db
│   │   ├── globals.css          # Custom Liftra-themed styling
│   │   ├── layout.tsx           # Root layout with Liftra metadata
│   │   └── page.tsx             # Main Liftra interface with file management
├── package.json                 # pnpm configuration
└── README.md                    # This file

# Python FEA files (in parent directory)
../
├── MainFEWA.py                  # Main FEA script
├── GeoCreate.py                 # Geometry creation script
├── UsrInput.txt                 # Input parameters file
├── Runfile.txt                  # Generated ANSYS runfile
├── SaveFile.db                  # ANSYS save file
└── [other FEA files]
```

## 🚦 Getting Started

### Prerequisites

- Node.js 18+ and pnpm
- Python 3.x
- ANSYS 251 installed at `C:\Program Files\ANSYS Inc\v251\ansys\bin\winx64\ANSYS251.exe`

### Installation & Setup

1. **Install Frontend Dependencies**
   ```bash
   cd frontend
   pnpm install
   ```

2. **Start Development Server**
   ```bash
   pnpm run dev
   ```

3. **Access the Application**
   Open [http://localhost:3000](http://localhost:3000) in your browser

## 🎯 How to Use

1. **Configure Weld Parameters**:
   - **Weld Length (mm)**: Length of the weld joint
   - **Weld Width (mm)**: Width of the weld joint
   - **Weld Thickness (mm)**: Thickness of the weld material
   - **Weld Throat (mm)**: Throat dimension of the weld

2. **Run Analysis**:
   - Click the "Run Analysis" button
   - Wait for the FEA simulation to complete
   - View results in the application

3. **Access Generated Files**:
   - **View Runfile**: Click "View Runfile" to see the generated ANSYS script
   - **Download SaveFile**: Click "Download SaveFile" to get the ANSYS save file
   - Analysis output files are also available in the project root

## 🔧 API Endpoints

### POST `/api/run-fea`

Runs the finite element analysis with provided weld parameters.

**Request Body**:
```json
{
  "weldLength": 100,
  "weldWidth": 50,
  "weldThick": 4,
  "weldThroat": 4
}
```

**Response**:
```json
{
  "success": true,
  "message": "FEA analysis completed successfully",
  "output": "..."
}
```

### GET `/api/files/runfile`

Serves the generated ANSYS runfile.txt content.

**Response**: Text content of the runfile with proper headers for inline display.

### GET `/api/files/savefile`

Downloads the ANSYS SaveFile.db file.

**Response**: Binary file download with appropriate headers.

## 🎨 Customization

The application features extensive customization options:

- **Color Scheme**: Modify CSS custom properties in `globals.css`
- **Gradients**: Adjust gradient definitions for different visual effects
- **Layout**: Responsive grid layout adapts to different screen sizes
- **Animations**: Smooth transitions and loading states

## 🔧 Development

### Available Scripts

- `pnpm run dev` - Start development server
- `pnpm run build` - Build for production
- `pnpm run start` - Start production server
- `pnpm run lint` - Run ESLint

### Code Quality

- TypeScript for type safety
- ESLint for code quality
- Responsive design principles
- Accessibility considerations

## 📊 FEA Parameters

The application accepts the following weld geometry parameters:

| Parameter | Description | Units | Default |
|-----------|-------------|-------|---------|
| Weld Length | Length of weld joint | mm | 100 |
| Weld Width | Width of weld joint | mm | 50 |
| Weld Thickness | Material thickness | mm | 4 |
| Weld Throat | Weld throat dimension | mm | 4 |

## 🎨 Visual Design Philosophy

The interface is designed with Liftra's engineering excellence in mind:

- **Liftra Brand Identity**: Professional blue color scheme representing trust and precision
- **Technical Aesthetics**: Clean lines and structured layout
- **Liftra Colors**: Deep blue (#1e40af) gradients with professional styling
- **Glass Effects**: Modern transparency for depth
- **Grid Patterns**: Subtle technical grid overlay
- **Smooth Interactions**: Professional hover and click effects

## 🚨 Troubleshooting

### Common Issues

1. **Python Script Not Found**: Ensure `MainFEWA.py` is in the parent directory
2. **ANSYS Path Error**: Verify ANSYS installation path in `MainFEWA.py`
3. **Permission Errors**: Run terminal as administrator if needed

### Support

For technical support or feature requests, please check the project documentation or create an issue in the project repository.

---

**Built with ❤️ for Liftra ApS Engineering Excellence**