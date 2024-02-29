# Trivia API

Trivia API is a Flask-based RESTful API for managing trivia questions. It allows users to retrieve, suggest, approve, and delete trivia questions through HTTP requests.

## Installation

To set up the Trivia API locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/trivia-api.git
   ```

2. Navigate to the project directory:

   ```
   cd trivia-api
   ```

3. Install dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and provide the necessary environment variables:

   ```plaintext
   ATLAS_URI=mongodb+srv://your_username:your_password@your_cluster_address.your_provider.net/?retryWrites=true&w=majority&appName=Trivia
   DB_NAME=YourDatabaseName
   ```

## Usage

### Running the Server

To start the Flask server, run the following command from the project root directory:

```bash
python -m app.__init__
```

By default, the server will run on `http://localhost:5000`.

### Endpoints

The Trivia API exposes the following endpoints:

- `GET /questions`: Retrieve trivia questions based on specified parameters such as category, difficulty, and amount.

- `POST /questions`: Suggest a new trivia question by providing JSON data in the request body.

- `GET /questions/<question_id>`: Retrieve a specific trivia question by its ID.

- `DELETE /questions/<question_id>`: Delete a trivia question by its ID.

- `PUT /questions/<question_id>/approve`: **[Deprecated]** Approve a suggested trivia question by its ID. *(Note: Direct approval on the database is recommended instead.)*

### Example Usage

Retrieve trivia questions with specific parameters:

```bash
curl -X GET 'http://localhost:5000/questions?category=Sports&amount=5'
```

Suggest a new trivia question:

```bash
curl -X POST 'http://localhost:5000/questions' -H 'Content-Type: application/json' -d '{"question": "What is the capital of France?", "answers": ["Paris", "Berlin", "London", "Tel Aviv"], "correct": 0, "category": "Geography", "difficulty": "Easy", "type": "Multiple Choice"}'
```

