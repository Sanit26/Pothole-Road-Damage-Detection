from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        input_video=url_for("static", filename="demo/sample_video.mp4"),
        output_video=url_for("static", filename="demo/detected_video.mp4")
    )

if __name__ == "__main__":
    app.run(debug=True)
