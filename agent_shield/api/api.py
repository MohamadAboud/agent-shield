# """ Third-party modules """
from typing import Optional
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# """ Local modules """
from logs import BirdLogger
from ..guardian_ai import BotException, GuardianAI, GuardianCategory

logger = BirdLogger("Main")


# Load the environment variables from the .env file
# override=True to override the existing environment variables
load_dotenv(override=True)


# Create a Flask app instance
app = Flask(__name__)

# Instantiate the GuardianAI
guardian = GuardianAI()

################# | ROUTES |#################


@app.route('/', methods=['GET'])
def index():
    """The index route of the Flask server."""
    return jsonify({"message": "Guardian AI server is running 🐍"})


@app.route('/ask', methods=['POST'])
def ask():
    """Guardian AI API route to ask a question."""
    try:
        # Get the json data from the request
        data = request.get_json()
        # Extract the [question] from the data
        question = data.get('question')
        # Run the prediction
        res = guardian.invoke(question)
        # Return the response
        return jsonify({
            "response": res,
            "message": "The request was successfully processed.",
            "status": 200,
        })
    except BotException as e:
        return jsonify({
            "error": str(e),
            "message": "An error occurred while processing the request. Please try again later.",
            "response": None,
            "status": 500,
        }), 500


@app.route('/categories', methods=['GET'])
def categories():
    """Guardian AI API route to get the categories."""
    try:
        # Get the name or id from the query params
        name = request.args.get('name')
        id = request.args.get('id')
        if not name and not id:
            return jsonify({
                "response": [ctg.to_map() for ctg in GuardianCategory],
                "message": "The request was successfully processed.",
                "status": 200,
            })

        # Get the category
        categorie = GuardianCategory.from_type(name or id)
        # Return the response
        return jsonify({
            "response": categorie.to_map(),
            "message": "The request was successfully processed.",
            "status": 200,
        })
    except BotException as e:
        return jsonify({
            "error": str(e),
            "message": "An error occurred while processing the request. Please try again later.",
            "response": None,
            "status": 500,
        }), 500


def run(host: Optional[str] = None, port: Optional[int] = None, debug: bool = False) -> None:
    """
    Main function to run the app server.

    Args:
        host (str, optional): The host to run the server on.
        port (int, optional): The port to run the server on.
        debug (bool): Enable debugging mode.

    Returns:
        None

    Raises:
        If the server could not be started.
    """
    try:
        logger.info(f"[LO] - Starting server on port 7651...")

        # Run the app on all available interfaces on port 7651 (default).
        app.run(
            # Expose the server to the network (Localhost, LAN, etc.)
            host=host or "0.0.0.0",   # Host to run the server on
            port=port or 7651,        # Port to run the server on
            debug=debug,  # Enable debugging mode
        )
    except Exception as e:
        logger.error(f"[ERROR].{e}")
        logger.error("[ERROR] - Server could not be started.")


if __name__ == '__main__':
    # Run the app
    run(host="0.0.0.0", port=7651, debug=True)
