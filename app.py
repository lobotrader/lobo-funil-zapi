# app.py — Funil básico Lobo Trader (webhook + respostas)
from flask import Flask, request, jsonify
import requests

# ====== CONFIG ======
INSTANCE_ID = "3E97D4C98D6B113E2FAE3A9184538B5F"
TOKEN = "ADDBFE2D37EED94E55094BA1"
ZAPI_BASE = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}"

COURSE = "https://lobotrader.com.br/treinamento"
GROUP_FREE = "https://chat.whatsapp.com/B95rv2dDV5F75dKi3ne8SZ?mode=wwt"
BROKER = "https://trade.obynexbroker.com/register?aff=757296&aff_model=revenue&afftrack="

app = Flask(__name__)

def send_text(phone, message):
    url = f"{ZAPI_BASE}/send-text"
    body = {"phone": phone, "message": message}
    try:
        requests.post(url, json=body, timeout=20)
    except Exception as e:
        print("Erro send_text:", e)

def send_image(phone, image_url, caption=""):
    url = f"{ZAPI_BASE}/send-image"
    body = {"phone": phone, "image": image_url, "caption": caption}
    try:
        requests.post(url, json=body, timeout=20)
    except Exception as e:
        print("Erro send_image:", e)

@app.route("/")
def health():
    return "OK", 200

# Webhook que você vai colocar no Z-API (“Ao receber”)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True) or {}
    phone = (data.get("phone") or data.get("remoteJid") or "").strip()
    msg = data.get("message") or {}
    text = ""
    if isinstance(msg, dict):
        text = (msg.get("text") or msg.get("body") or "").strip()
    elif isinstance(msg, str):
        text = msg.strip()

    t = (text or "").upper()

    if t in ["QUERO LUCRAR COM O MERCADO FINANCEIRO" in t:
"]:
        send_text(phone, "🔥 Fala, campeão(a)! Aqui é o Lobo Trader 🐺")
        send_text(phone, "Antes da gente continuar, salva meu contato aí pra gente trocar uma ideia 📲")
        send_text(phone, "Depois que salvar, me manda um OK aqui 👇")
        return jsonify({"status":"ok"})

    if t == "OK":
        send_text(phone, "🐺 Show! Agora me diz uma coisa 👇")
        send_text(phone, "Você já opera no mercado ou tá começando do zero?")
        send_text(phone, "Digite apenas:\n1️⃣ Já opero\n2️⃣ Estou começando do zero")
        return jsonify({"status":"ok"})

    if t == "1":
        send_text(phone, "🔥 Perfeito, então você já tem base.")
        send_text(phone, "Quer operar com quem mostra resultado AO VIVO?")
        send_text(phone, "Posso te mostrar o método Falha da Corretora que uso nas lives.")
        send_text(phone, "Quer que eu te mostre como funciona o Grupo VIP?")
        return jsonify({"status":"ok"})

    if t == "2":
        send_text(phone, "🔰 Show! Então vamos do zero.")
        send_text(phone, f"Liberei um mini curso gratuito (5 aulas) pra te ensinar passo a passo.")
        send_text(phone, f"📚 Acesse aqui 👉 {COURSE}")
        send_text(phone, "Depois que terminar, me envia PRONTO que eu te coloco no grupo Free onde mostro resultados e bastidores 🧠")
        return jsonify({"status":"ok"})

    if t == "PRONTO":
        send_text(phone, "🔥 Boa! Isso mostra que você quer aprender de verdade.")
        send_text(phone, f"Aqui está o link do grupo Free 👇\n👉 {GROUP_FREE}")
        send_text(phone, "Lá eu mostro os resultados das lives, feedbacks e aviso das vagas do VIP 🧠")
        return jsonify({"status":"ok"})

    if t == "SIM":
        send_text(phone, "🐺 Top! Então bora pra cima.")
        send_text(phone, f"Pra entrar no Grupo VIP, basta fazer um depósito na corretora 👇\n💸 {BROKER}")
        send_text(phone, "Depois me envia o comprovante aqui que eu libero o acesso ao Zoom e planilha especial 🔥")
        return jsonify({"status":"ok"})

    # Fallback simples
    send_text(phone, "🐺 Desculpa, não entendi 😅")
    send_text(phone, "Digita só:\n1️⃣ Já opero\n2️⃣ Estou começando do zero")
    return jsonify({"status":"ok"})
