from flask import Flask, render_template, request, redirect
from request_store.service import get_pending_requests, update_request, get_all_requests, mark_unresolved_requests
from agent.knowledge_base import load_knowledge_base

app = Flask(__name__)

@app.route("/")
def index():
    mark_unresolved_requests()
    return render_template("index.html", requests=get_pending_requests())

@app.route("/history")
def history():
    mark_unresolved_requests()
    return render_template("request_detail.html", requests=get_all_requests())

@app.route("/knowledge")
def knowledge():
    kb = load_knowledge_base()
    return render_template("knowledge.html", kb=kb)

@app.route("/respond", methods=["POST"])
def respond():
    request_id = request.form["request_id"]
    answer = request.form["answer"]
    update_request(request_id, answer)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
