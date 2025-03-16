import requests
import time

# === INPUT USER ===
jumlah_per_hari = int(input("Berapa task (text, image, audio) per hari? "))
jumlah_hari = int(input("Berapa hari AI ingin dijalankan? "))

total_task = jumlah_per_hari * jumlah_hari * 3
print(f"\n🎯 Target: {total_task} total task (text + image + audio) dalam {jumlah_hari} hari\n")

# === API KEY ===
TEXT_GROQ_API = "API-KEY-GROQ-TEXT"
IMAGE_GROQ_API = "API-KEY-GROQ-IMAGE" # SEBENERNYA PAKE 1 API JUGA BISA BIAR GA LIMIT AJA GUA BIKIN 3
AUDIO_GROQ_API = "API-KEY-GROQ-AUDIO" 
HYPERBOLIC_API_KEY = "hyperbolic-API"  # Ganti dengan punyamu hyperbolic

task_counter = 1

for day in range(1, jumlah_hari + 1):
    print(f"\n📅 Hari ke-{day} ===========================\n")

    for i in range(jumlah_per_hari):
        # === TEXT ===
        print(f"\n📌 TASK {task_counter} - TEXT")
        try:
            question = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {TEXT_GROQ_API}"
                },
                json={
                    "messages": [{"role": "user", "content": "Give me a random interesting question about travel or tourism."}],
                    "model": "mixtral-8x7b-32768",
                    "max_tokens": 50,
                    "temperature": 1.2
                }
            ).json()['choices'][0]['message']['content'].strip()

            answer = requests.post(
                "https://api.hyperbolic.xyz/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"
                },
                json={
                    "messages": [{"role": "user", "content": question}],
                    "model": "meta-llama/Llama-3.3-70B-Instruct",
                    "max_tokens": 512,
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            )

            status = "✅ Sukses" if answer.status_code == 200 else f"❌ Gagal ({answer.status_code})"
        except Exception as e:
            status = f"❌ Gagal ({str(e)})"

        with open("HISTORIAI.txt", "a", encoding="utf-8") as log:
            log.write(f"\n=== [Hari {day} - TEXT {i+1}] ===\nStatus: {status}\n{'='*40}\n")

        time.sleep(1)

        # === IMAGE ===
        print(f"\n📌 TASK {task_counter+1} - IMAGE")
        try:
            prompt = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {IMAGE_GROQ_API}"
                },
                json={
                    "messages": [{"role": "user", "content": "Give me a random prompt for a stunning AI-generated image using SDXL."}],
                    "model": "mixtral-8x7b-32768",
                    "max_tokens": 50,
                    "temperature": 1.3
                }
            ).json()['choices'][0]['message']['content'].strip()

            image_status = requests.post(
                "https://api.hyperbolic.xyz/v1/image/generation",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"
                },
                json={
                    "model_name": "SDXL1.0-base",
                    "prompt": prompt,
                    "steps": 30,
                    "cfg_scale": 5,
                    "enable_refiner": False,
                    "height": 1024,
                    "width": 1024,
                    "backend": "auto"
                }
            )

            status = "✅ Sukses" if image_status.status_code == 200 else f"❌ Gagal ({image_status.status_code})"
        except Exception as e:
            status = f"❌ Gagal ({str(e)})"

        with open("HISTORIAI.txt", "a", encoding="utf-8") as log:
            log.write(f"\n=== [Hari {day} - IMAGE {i+1}] ===\nStatus: {status}\n{'='*40}\n")

        time.sleep(1)

        # === AUDIO ===
        print(f"\n📌 TASK {task_counter+2} - AUDIO")
        try:
            audio_text = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {AUDIO_GROQ_API}"
                },
                json={
                    "messages": [{"role": "user", "content": "Give me a short sentence with a maximum of 10 words for AI voice generation."}],
                    "model": "mixtral-8x7b-32768",
                    "max_tokens": 30,
                    "temperature": 1.1
                }
            ).json()['choices'][0]['message']['content'].strip()

            audio_status = requests.post(
                "https://api.hyperbolic.xyz/v1/audio/generation",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"
                },
                json={"text": audio_text, "speed": 1}
            )

            status = "✅ Sukses" if audio_status.status_code == 200 else f"❌ Gagal ({audio_status.status_code})"
        except Exception as e:
            status = f"❌ Gagal ({str(e)})"

        with open("HISTORIAI.txt", "a", encoding="utf-8") as log:
            log.write(f"\n=== [Hari {day} - AUDIO {i+1}] ===\nStatus: {status}\n{'='*40}\n")

        task_counter += 3
        time.sleep(1)

    print(f"\n✅ Selesai hari ke-{day}. Menunggu hari berikutnya...\n")
    if day < jumlah_hari:
        time.sleep(86400)  # Ganti ke 86400 buat 1 hari penuh
