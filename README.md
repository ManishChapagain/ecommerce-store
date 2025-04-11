# ecommerce-store
minimal ecommerce store for demo

## Project Structure

```
ecommerce-store/
├── frontend/     # React.js (Vite) frontend
├── backend/      # Flask backend
└── README.md
```

## Tested on following configs

- Node.js (v20.10.0)
- npm (v10.4.0)
- Python (v3.12.5)
- pip 

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```
   flask run
   ```

   The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## Running Tests

### Backend Tests (pytest)

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Ensure your virtual environment is activated and inside backend dir

3. Run tests:
   ```
   pytest
   ```

### Frontend Tests (Vitest)

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Run tests:
   ```
   npm test
   ```
