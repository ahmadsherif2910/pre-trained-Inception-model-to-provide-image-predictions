from flask import Flask, current_app, request, jsonify
import io
import model
import base64
import logging

app = Flask(__name__)


@app.route("/", methods=["POST"])
def predict():
    data = {}
    try:
        data = request.get_json()["data"]
    except Exception:
        return jsonify(status_code="400", msg="Bad Request"), 400

    data = base64.b64decode(data)
    image = io.BytesIO(data)

    # 1. Get the predictions
    raw_predictions = model.predict(image)

    # 2. Format them and convert numpy float32 to standard float
    formatted_preds = []
    for pred in raw_predictions:
        formatted_preds.append(
            {
                "class_id": pred[0],
                "class_name": pred[1],
                "probability": float(pred[2]),  # <-- This fixes the JSON error!
            }
        )

    current_app.logger.info("Predictions: %s", formatted_preds)

    # 3. Return the formatted predictions
    return jsonify(predictions=formatted_preds)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
