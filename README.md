# Movie Search Web App

A web application that allows users to search for movies using the TMDB (The Movie Database) API. The app displays movie titles, release dates, overviews, and poster images, providing users with an easy way to explore movies.

## Features

- Search for movies by name.
- View movie details including title, release date, overview, and poster image.
- Built using Flask and TMDB API.
- Styled with Bootstrap and Dark Mode for a modern look.

## Technologies Used

- Flask (Python web framework)
- TMDB API (Movie data)
- Bootstrap (Front-end framework)
- HTML/CSS (For styling and structure)
- Jinja2 (Template rendering)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AhrimanXD/movie-search-web-app.git
    ```

2. Navigate to the project folder:

    ```bash
    cd movie-search-web-app
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Create a `.env` file in the root directory and add your TMDB API key:

    ```text
    TMDB_API_KEY=your_tmdb_api_key
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your browser and go to:

    ```
    http://127.0.0.1:5000/
    ```

3. Use the search bar to search for movies!

## Contributing

Feel free to fork this repository and submit pull requests with improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
