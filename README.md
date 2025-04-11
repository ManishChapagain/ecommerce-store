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

   The backend will be available at `http://localhost:5000`. You can test using Postman as well.

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

   The frontend will be available at `http://localhost:5173`. user with id "1" is hardcoded in frontend.

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

## API Testing with Postman

You can test the backend APIs directly using Postman (userId is hardcoded in frontend as "1", you can include anything here):

### Items API
- **GET** `http://localhost:5000/items/`
  
  - Returns all available items (its static for now)
    ```json
    {
       "items": [
           {
               "id": 1,
               "name": "Apple",
               "price": 10
           },
           {
               "id": 2,
               "name": "Banana",
               "price": 5
           },
           {
               "id": 3,
               "name": "Orange",
               "price": 8
           },
           {
               "id": 4,
               "name": "Grapes",
               "price": 12
           }
       ]
    }
     ```

### Cart API
- **GET** `http://localhost:5000/cart/{user_id}`
  - Returns cart contents for a specific user
   

- **POST** `http://localhost:5000/cart/{user_id}/add`
  - Adds an item to the user's cart
  - Include following in the body(raw):
    ```json
    {
      "name": "Apple",
      "qty": 1
    }
    ```

### Checkout API
- **POST** `http://localhost:5000/checkout/{user_id}`
  
  - Process a checkout for a specific user
  - Body (with discount code):
    ```json
    {
      "discount_code": "ABC123"
    }
    ```
  - Body (no discount, empty json needed, otherwise it'll throw 415):
    ```json
    {}
    ```

### Admin API
- **GET** `http://localhost:5000/admin/get-code`
  - Retrieves discount code (available only after N-1th order)

- **GET** `http://localhost:5000/admin/report`
  - Gets sales report with total items sold, revenue, discounts, etc.
