#!/usr/bin/env python3
from webapp import app
if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=False, host="127.0.0.1", port=5001)
