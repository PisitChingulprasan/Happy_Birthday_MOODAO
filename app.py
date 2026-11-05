import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเพจให้แสดงผลเต็มจอและซ่อนเมนูของ Streamlit
st.set_page_config(page_title="Happy Birthday มุดาว ❤️", layout="wide", initial_sidebar_state="collapsed")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# โค้ดเว็บแอปพลิเคชันเวอร์ชันจัดเต็ม ว้าวสุดขีด
html_code = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday มุดาว ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!-- นำเข้า Canvas Confetti สำหรับทำพลุฉลอง -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <style>
        * {
            box-sizing: border-box;
            font-family: 'Prompt', sans-serif;
        }
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #1f1c2c 0%, #928dab 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            position: relative;
        }
        /* เอฟเฟกต์ดาวตกพื้นหลัง */
        .stars {
            position: absolute;
            width: 100%;
            height: 100%;
            background: transparent;
            z-index: 1;
            overflow: hidden;
        }
        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 2s infinite ease-in-out;
        }
        @keyframes twinkle {
            0%, 100% { opacity: 0.2; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1.2); }
        }

        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.92);
            backdrop-filter: blur(10px);
            padding: 35px 25px;
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            width: 90%;
            max-width: 420px;
            position: relative;
            z-index: 10;
            border: 2px solid rgba(255, 255, 255, 0.5);
            animation: popUp 0.5s ease-out;
        }
        @keyframes popUp {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        h2 {
            color: #ff4757;
            margin-bottom: 15px;
            font-size: 24px;
            font-weight: 700;
        }
        p {
            color: #444;
            font-size: 16px;
            margin-bottom: 25px;
            line-height: 1.6;
            word-break: break-word;
        }
        input {
            width: 100%;
            padding: 14px;
            border: 2px solid #ff6b81;
            border-radius: 12px;
            font-size: 16px;
            text-align: center;
            outline: none;
            margin-bottom: 20px;
            color: #333;
            background: #fff;
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.05);
        }
        .btn {
            background: linear-gradient(135deg, #ff4757 0%, #ff6b81 100%);
            color: white;
            border: none;
            padding: 14px 25px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: 0.3s;
            width: 100%;
            box-shadow: 0 5px 15px rgba(255, 71, 87, 0.4);
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 7px 20px rgba(255, 71, 87, 0.6);
        }
        .btn:active {
            transform: scale(0.98);
        }
        .hidden {
            display: none !important;
        }
        
        /* มินิเกมจับหัวใจ */
        #game-area {
            position: relative;
            width: 100%;
            height: 260px;
            background: rgba(255, 240, 243, 0.8);
            border-radius: 18px;
            margin-bottom: 20px;
            overflow: hidden;
            border: 2px dashed #ffb6c1;
        }
        .heart-target {
            position: absolute;
            font-size: 42px;
            cursor: pointer;
            user-select: none;
            transition: transform 0.1s;
            animation: bounceHeart 0.8s infinite alternate;
        }
        @keyframes bounceHeart {
            0% { transform: scale(1); }
            100% { transform: scale(1.15); }
        }

        /* การ์ดฉากจบสุดอลังการ */
        .finale-card {
            background: rgba(20, 15, 35, 0.88);
            border: 2px solid #ff6b81;
            box-shadow: 0 0 30px rgba(255, 107, 129, 0.5);
        }
        .finale-card h2 {
            color: #ff6b81;
            text-shadow: 0 0 10px rgba(255, 107, 129, 0.6);
        }
        .finale-card p {
            color: #f1f1f1;
        }
    </style>
</head>
<body>

    <!-- พื้นหลังดวงดาวระยิบระยับ -->
    <div class="stars" id="stars-container"></div>

    <!-- เพลงประกอบ (กล่องดนตรีโลฟายผ่อนคลาย) -->
    <audio id="bgm" loop>
        <source src="https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
    </audio>

    <!-- ด่านที่ 1: ตรวจสอบความปลอดภัย (กวนๆ เล็กน้อย) -->
    <div class="container" id="step-1">
        <h2>✨ ตรวจสอบความปลอดภัย ✨</h2>
        <p>ระบบตรวจพบคนสวยระดับซุปตาร์แถวนี้ กรุณาพิมพ์ชื่อ <b>"มุดาว"</b> เพื่อเข้าสู่ระบบหัวใจ:</p>
        <input type="text" id="name-input" placeholder="พิมพ์ชื่อ มุดาว ตรงนี้..." autocomplete="off">
        <button class="btn" onclick="checkName()">ยืนยันตัวตน 🚀</button>
    </div>

    <!-- ด่านที่ 2: มินิเกมเก็บหัวใจสะสมแต้ม -->
    <div class="container hidden" id="step-2">
        <h2>💖 ภารกิจเก็บใจคนสวย 💖</h2>
        <p style="font-size: 14px; margin-bottom: 10px;">กดเก็บหัวใจให้ครบ 5 ดวงเพื่อเปิดกล่องของขวัญ!</p>
        <div id="game-area">
            <div class="heart-target" id="heart" onclick="catchHeart()">❤️</div>
        </div>
        <p id="score-text" style="font-weight: bold; color: #ff4757; margin: 0; font-size: 16px;">สะสมหัวใจ: 0 / 5</p>
    </div>

    <!-- ด่านที่ 3: ฉากจบเซอร์ไพรส์สุดอลังการ -->
    <div class="container hidden finale-card" id="step-3">
        <h2 style="font-size: 28px;">🎉 Happy Birthday มุดาว ❤️</h2>
        <p style="font-size: 15px; line-height: 1.7;">
            ขอให้คนสวยมีความสุขมากๆ <br>
            ยิ้มเยอะๆ โลกใบนี้ใจดีกับเธอในทุกๆ วันนะ ✨
        </p>
        <div style="font-size: 50px; margin: 15px 0; animation: pulse 1.5s infinite;">🌟 💖 🌟</div>
        <p style="font-weight: bold; color: #ff6b81; font-size: 17px; margin-top: 10px;">
            MooMint แฟนสุดที่รัก ของ มุดาว ❤️
        </p>
    </div>

    <script>
        // สร้างดาวระยิบระยับในพื้นหลังอัตโนมัติ
        const starsContainer = document.getElementById('stars-container');
        for (let i = 0; i < 60; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            const size = Math.random() * 3 + 1;
            star.style.width = size + 'px';
            star.style.height = size + 'px';
            star.style.top = Math.random() * 100 + '%';
            star.style.left = Math.random() * 100 + '%';
            star.style.animationDuration = (Math.random() * 2 + 1) + 's';
            star.style.animationDelay = (Math.random() * 2) + 's';
            starsContainer.appendChild(star);
        }

        // เล่นเพลงอัตโนมัติเมื่อผู้ใช้คลิกหน้าจอครั้งแรก
        document.addEventListener('click', function() {
            var audio = document.getElementById('bgm');
            if (audio.paused) {
                audio.volume = 0.4;
                audio.play().catch(e => console.log(e));
            }
        }, { once: true });

        // ตรวจสอบชื่อด่าน 1
        function checkName() {
            const inputVal = document.getElementById('name-input').value.trim();
            if (inputVal === "มุดาว") {
                document.getElementById('step-1').classList.add('hidden');
                document.getElementById('step-2').classList.remove('hidden');
                moveHeart();
            } else {
                alert("อุ้ย! พิมพ์ชื่อผิดหรือเปล่า ลองพิมพ์คำว่า 'มุดาว' ดูอีกทีนะ ❤️");
            }
        }

        // ระบบมินิเกมเก็บหัวใจ
        let score = 0;
        const heart = document.getElementById('heart');
        const gameArea = document.getElementById('game-area');

        function moveHeart() {
            const maxX = gameArea.clientWidth - 60;
            const maxY = gameArea.clientHeight - 60;
            const randomX = Math.floor(Math.random() * maxX);
            const randomY = Math.floor(Math.random() * maxY);
            
            heart.style.left = randomX + 'px';
            heart.style.top = randomY + 'px';
        }

        // หัวใจวิ่งหนีเองทุกๆ 1.1 วินาที
        let heartTimer = setInterval(() => {
            if(!document.getElementById('step-2').classList.contains('hidden')) {
                moveHeart();
            }
        }, 1100);

        function catchHeart() {
            score++;
            document.getElementById('score-text').innerText = `สะสมหัวใจ: ${score} / 5`;
            
            // เอฟเฟกต์พลุเล็กๆ ทุกครั้งที่กดโดนหัวใจ
            confetti({
                particleCount: 20,
                spread: 50,
                origin: { y: 0.7 }
            });

            if (score >= 5) {
                clearInterval(heartTimer);
                document.getElementById('step-2').classList.add('hidden');
                document.getElementById('step-3').classList.remove('hidden');
                
                // จุดพลุชุดใหญ่ฉลองตอนท้ายแบบอลังการ
                triggerGrandFinaleFireworks();
            } else {
                moveHeart();
            }
        }

        // ฟังก์ชันจุดพลุฉลองตอนจบ
        function triggerGrandFinaleFireworks() {
            var duration = 3 * 1000;
            var end = Date.now() + duration;

            (function frame() {
                confetti({
                    particleCount: 7,
                    angle: 60,
                    spread: 55,
                    origin: { x: 0 }
                });
                confetti({
                    particleCount: 7,
                    angle: 120,
                    spread: 55,
                    origin: { x: 1 }
                });

                if (Date.now() < end) {
                    requestAnimationFrame(frame);
                }
            }());
        }
    </script>
</body>
</html>
"""

# เรนเดอร์ HTML ลงบน Streamlit
components.html(html_code, height=900, scrolling=False)
