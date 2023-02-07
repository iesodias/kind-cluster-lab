from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/validate", methods=["POST"])
def validate():
    request_json = request.get_json()
    deployment = request_json["request"]["object"]
    # verifica se as chaves livenessProbe e readinessProbe existem no deployment falta testar se existir    
    if "livenessProbe" not in deployment["spec"]:
        response = {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": request_json["request"]["uid"],
                "allowed": False,
                "status": {
                    "message": "O Ieso falou que é obrigatorio o uso do livenessProbe."                }
            }
        }
        return jsonify(response)
    if "readinessProbe" not in deployment["spec"]:
        response = {
            "apiVersion": "admission.k8s.io/v1",
            "kind": "AdmissionReview",
            "response": {
                "uid": request_json["request"]["uid"],
                "allowed": False,
                "status": {
                    "message": "O Ieso falou que é obrigatorio o uso do ReadnessProbe"                }
            }
        }
        return jsonify(response)
    response = {
        "apiVersion": "admission.k8s.io/v1",
        "kind": "AdmissionReview",
        "response": {
            "uid": request_json["request"]["uid"],
            "allowed": True,
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)