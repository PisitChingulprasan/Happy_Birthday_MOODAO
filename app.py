import streamlit as st
import streamlit.components.v1 as components

# ตั้งค่าหน้าเพจให้แสดงผลเต็มจอและซ่อนเมนูของ Streamlit เพื่อความเนียน
st.set_page_config(page_title="Happy Birthday MooDao", layout="wide", initial_sidebar_state="collapsed")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# วางโค้ด HTML ทั้งหมดที่ผมเคยให้ไว้ในกรอบเครื่องหมายคำพูด 3 อัน
html_code = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Happy Birthday MooDao</title>
    <!-- Google Fonts: Prompt for Thai, Playfair Display for premium English text -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,700&family=Prompt:wght@300;400;600&display=swap" rel="stylesheet">
    <!-- Canvas Confetti -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --bg-light: #fff0f5;
            --text-dark: #4a4a4a;
            --accent-pink: #ff6b81;
            
            /* Premium Dark Theme */
            --bg-dark: #0a0e17;
            --text-light: #f1f2f6;
            --gold: #ffd700;
            --card-bg: rgba(255, 255, 255, 0.05);
        }

        * {
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Prompt', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background-color 2s ease-in-out, color 2s ease-in-out;
        }

        /* --- Global Layouts --- */
        .phase {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
            opacity: 0;
            pointer-events: none;
            transition: opacity 1s ease, transform 1s ease;
            transform: scale(0.95);
            z-index: 10;
        }

        .phase.active {
            opacity: 1;
            pointer-events: auto;
            transform: scale(1);
        }

        /* --- Phase 1: Troll Input --- */
        .glass-box {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 2px solid white;
            max-width: 400px;
            width: 90%;
        }

        h2 {
            font-size: 1.5rem;
            margin-bottom: 5px;
            color: var(--accent-pink);
        }

        p.subtitle {
            font-size: 1rem;
            color: #777;
            margin-bottom: 25px;
        }

        .fake-input-container {
            position: relative;
            width: 100%;
        }

        input[type="text"] {
            width: 100%;
            padding: 15px;
            font-size: 1.5rem;
            font-family: 'Prompt', sans-serif;
            text-align: center;
            border: 2px solid #ddd;
            border-radius: 10px;
            outline: none;
            transition: border-color 0.3s, box-shadow 0.3s;
            color: var(--accent-pink);
            font-weight: 600;
        }

        input[type="text"]:focus {
            border-color: var(--accent-pink);
            box-shadow: 0 0 15px rgba(255, 107, 129, 0.3);
        }

        /* --- Phase 2: Dodging Pig --- */
        #pig-btn {
            font-size: 4rem;
            background: none;
            border: none;
            cursor: pointer;
            position: absolute;
            transition: top 0.2s ease-out, left 0.2s ease-out, transform 0.2s;
            filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
            z-index: 50;
        }
        
        #pig-btn:active {
            transform: scale(0.9);
        }

        .instruction {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-dark);
            margin-bottom: 20px;
            position: absolute;
            top: 20%;
            width: 100%;
            pointer-events: none;
        }

        /* --- Phase 3: WOW Finale (Starry Night) --- */
        body.magical-night {
            background-color: var(--bg-dark);
            background-image: radial-gradient(circle at center, #1b2735 0%, #090a0f 100%);
            color: var(--text-light);
        }

        .starry-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none;
            opacity: 0;
            transition: opacity 2s ease;
        }
        
        body.magical-night .starry-bg {
            opacity: 1;
        }

        /* CSS Stars generated by JS */
        .star {
            position: absolute;
            background-color: white;
            border-radius: 50%;
            animation: twinkle infinite ease-in-out;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.2; transform: scale(0.8); }
            50% { opacity: 1; transform: scale(1.2); box-shadow: 0 0 10px #fff, 0 0 20px #fff; }
        }

        .shooting-star {
            position: absolute;
            width: 2px;
            height: 50px;
            background: linear-gradient(to bottom, rgba(255,255,255,1), rgba(255,255,255,0));
            transform: rotate(-45deg);
            animation: shoot 3s linear infinite;
            opacity: 0;
        }

        @keyframes shoot {
            0% { transform: translate(100px, -100px) rotate(-45deg); opacity: 1; }
            20% { transform: translate(-500px, 500px) rotate(-45deg); opacity: 0; }
            100% { transform: translate(-500px, 500px) rotate(-45deg); opacity: 0; }
        }

        /* Premium Text & Card */
        .premium-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            font-weight: 700;
            font-style: italic;
            color: #fff;
            text-shadow: 0 0 20px rgba(255, 215, 0, 0.5),
                         0 0 40px rgba(255, 215, 0, 0.3),
                         0 4px 4px rgba(0,0,0,0.5);
            margin-bottom: 30px;
            z-index: 10;
            opacity: 0;
            transform: translateY(-20px);
            animation: fadeDown 1.5s 1s forwards;
        }

        .premium-card {
            background: var(--card-bg);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 215, 0, 0.2);
            padding: 40px 30px;
            border-radius: 20px;
            max-width: 600px;
            width: 90%;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 0 20px rgba(255,255,255,0.05);
            z-index: 10;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeUp 1.5s 1.5s forwards;
        }

        .premium-message {
            font-size: clamp(1rem, 3vw, 1.2rem);
            line-height: 1.8;
            color: #e2e8f0;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }

        .highlight-date {
            color: var(--gold);
            font-weight: 600;
            font-size: 1.1em;
        }

        .signature {
            margin-top: 20px;
            font-size: 1.1rem;
            color: var(--accent-pink);
            font-weight: 600;
            text-align: right;
        }

        @keyframes fadeDown {
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeUp {
            to { opacity: 1; transform: translateY(0); }
        }

        /* Pig Transformation */
        .pig-to-star {
            position: fixed !important;
            top: 50% !important;
            left: 50% !important;
            transform: translate(-50%, -50%) scale(2) !important;
            transition: all 1.5s cubic-bezier(0.25, 1, 0.5, 1) !important;
            z-index: 100 !important;
            pointer-events: none;
        }

        .star-burst {
            animation: burst 1s forwards;
        }

        @keyframes burst {
            0% { transform: translate(-50%, -50%) scale(2) rotate(0deg); opacity: 1; filter: brightness(1); }
            50% { transform: translate(-50%, -50%) scale(5) rotate(180deg); opacity: 1; filter: brightness(5); }
            100% { transform: translate(-50%, -50%) scale(10) rotate(360deg); opacity: 0; filter: brightness(10); }
        }
    </style>
</head>
<body>

    <!-- Phase 1: Troll Input -->
    <div id="phase1" class="phase active">
        <div class="glass-box">
            <h2>ระบบรักษาความปลอดภัย</h2>
            <p class="subtitle">กรุณายืนยันตัวตน: ใส่ชื่อคนที่น่ารักที่สุดในโลก</p>
            <div class="fake-input-container">
                <input type="text" id="cute-input" placeholder="พิมพ์ชื่อลงไป..." autocomplete="off">
            </div>
        </div>
    </div>

    <!-- Phase 2: Dodging Pig -->
    <div id="phase2" class="phase">
        <div class="instruction">
            ยืนยันตัวตนสำเร็จ! หมูดาวของแท้ 100%<br>
            <span style="font-size: 0.9rem; font-weight: normal; color: #666;">กดที่น้องหมูเพื่อรับของขวัญเลย!</span>
        </div>
        <!-- Button wrapped to handle absolute positioning smoothly -->
        <button id="pig-btn">🐷</button>
    </div>

    <!-- Phase 3: WOW Finale -->
    <div class="starry-bg" id="starry-bg"></div>
    <div id="phase3" class="phase">
        <div class="premium-title">Happy Birthday<br>MooDao &lt;3</div>
        <div class="premium-card">
            <div class="premium-message">
                วันที่ <span class="highlight-date">6 พฤศจิกายน</span> เป็นวันที่ดวงดาวที่สวยที่สุดตกลงมาบนโลก... ✨<br><br>
                สุขสันต์วันเกิดนะคะ "หมูดาว" ขอให้ปีนี้เป็นปีที่ดี มีความสุขมากๆ รอยยิ้มของหนูสว่างไสวและสวยงามเหมือนดวงดาวบนฟ้าเสมอเลยนะ<br><br>
                ขอบคุณที่เกิดมาให้รักนะคะ ขอให้น่ารักแบบนี้ไปนานๆ เลย 💖
            </div>
            <div class="signature">MooMint แฟนสุดที่ยัก ของ มุดาว</div>
        </div>
    </div>

    <script>
        // --- Elements ---
        const phase1 = document.getElementById('phase1');
        const phase2 = document.getElementById('phase2');
        const phase3 = document.getElementById('phase3');
        const input = document.getElementById('cute-input');
        const pigBtn = document.getElementById('pig-btn');
        const starryBg = document.getElementById('starry-bg');

        // --- Phase 1 Logic: Force typing "หมูดาว" ---
        const targetWord = "หมูดาว";
        let typeIndex = 0;

        // Focus input automatically if possible
        window.addEventListener('load', () => {
            setTimeout(() => input.focus(), 500);
        });

        // Use 'input' event for better mobile keyboard compatibility
        input.addEventListener('input', (e) => {
            // Ignore if input is cleared (to allow trying again gracefully) but force word building
            if (typeIndex < targetWord.length) {
                typeIndex++;
                input.value = targetWord.substring(0, typeIndex);
            } else {
                input.value = targetWord;
            }

            if (typeIndex >= targetWord.length) {
                input.disabled = true;
                setTimeout(transitionToPhase2, 1000);
            }
        });

        // Block manual backspacing/deleting to enforce the troll behavior
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace' || e.key === 'Delete') {
                e.preventDefault();
            }
        });

        function transitionToPhase2() {
            phase1.classList.remove('active');
            setTimeout(() => {
                phase2.classList.add('active');
                initPigPosition();
            }, 1000);
        }

        // --- Phase 2 Logic: Dodging Pig ---
        let dodgeCount = 0;
        const maxDodges = 6; // After 6 dodges, it stays still
        
        function initPigPosition() {
            // Center the pig initially
            pigBtn.style.left = `calc(50% - ${pigBtn.offsetWidth/2}px)`;
            pigBtn.style.top = `calc(60% - ${pigBtn.offsetHeight/2}px)`;
        }

        function dodge(e) {
            if (dodgeCount >= maxDodges) return; // Let her catch it
            
            // Prevent default touch to avoid accidental clicks before dodging max limit
            if (e && e.type === 'touchstart') e.preventDefault();

            dodgeCount++;

            const btnWidth = pigBtn.offsetWidth;
            const btnHeight = pigBtn.offsetHeight;
            const padding = 50; // Keep away from edges

            const maxX = window.innerWidth - btnWidth - padding;
            const maxY = window.innerHeight - btnHeight - padding;

            // Generate random position
            const randomX = Math.max(padding, Math.floor(Math.random() * maxX));
            const randomY = Math.max(padding, Math.floor(Math.random() * maxY));

            pigBtn.style.left = `${randomX}px`;
            pigBtn.style.top = `${randomY}px`;

            if (dodgeCount === maxDodges) {
                pigBtn.style.transform = 'scale(1.2)';
                pigBtn.style.filter = 'drop-shadow(0 0 20px rgba(255,107,129,0.8))';
            }
        }

        pigBtn.addEventListener('mouseover', (e) => {
            if (window.matchMedia('(hover: hover)').matches) dodge(e); // Only dodge on hover for non-touch devices
        });
        
        pigBtn.addEventListener('touchstart', (e) => {
            if (dodgeCount < maxDodges) {
                dodge(e);
            } else {
                // If max dodges reached, allow normal click processing
                startWOWFinale();
            }
        }, { passive: false });

        pigBtn.addEventListener('click', () => {
            if (dodgeCount >= maxDodges) {
                startWOWFinale();
            } else {
                // In case of very fast clicks
                dodge();
            }
        });

        // --- Phase 3 Logic: WOW Finale ---
        function startWOWFinale() {
            // 1. Transform Pig
            pigBtn.innerText = '🌟';
            pigBtn.classList.add('pig-to-star');
            
            // Remove Phase 2 text
            document.querySelector('.instruction').style.opacity = '0';

            // 2. Explode the star
            setTimeout(() => {
                pigBtn.classList.add('star-burst');
                
                // 3. Change Background and show Phase 3
                document.body.classList.add('magical-night');
                generateStars();
                
                setTimeout(() => {
                    phase2.classList.remove('active');
                    pigBtn.style.display = 'none'; // hide completely
                    phase3.classList.add('active');
                    
                    // 4. Fire Premium Confetti (Gold/Silver)
                    firePremiumConfetti();
                }, 800);

            }, 1000);
        }

        // Generate CSS background stars
        function generateStars() {
            const numStars = 100;
            for (let i = 0; i < numStars; i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                
                // Random position
                star.style.left = `${Math.random() * 100}%`;
                star.style.top = `${Math.random() * 100}%`;
                
                // Random size
                const size = Math.random() * 3 + 1;
                star.style.width = `${size}px`;
                star.style.height = `${size}px`;
                
                // Random animation delay
                star.style.animationDelay = `${Math.random() * 3}s`;
                star.style.animationDuration = `${Math.random() * 2 + 2}s`;
                
                starryBg.appendChild(star);
            }

            // Generate shooting stars periodically
            setInterval(() => {
                const shootingStar = document.createElement('div');
                shootingStar.classList.add('shooting-star');
                shootingStar.style.left = `${Math.random() * 100}%`;
                shootingStar.style.top = `${Math.random() * 30}%`; // Start near top
                starryBg.appendChild(shootingStar);
                
                setTimeout(() => shootingStar.remove(), 3000);
            }, 2000);
        }

        // Fireworks/Confetti using canvas-confetti
        function firePremiumConfetti() {
            const duration = 5 * 1000;
            const animationEnd = Date.now() + duration;
            const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 0, colors: ['#ffd700', '#ffffff', '#ffb6c1'] };

            function randomInRange(min, max) {
                return Math.random() * (max - min) + min;
            }

            const interval = setInterval(function() {
                const timeLeft = animationEnd - Date.now();

                if (timeLeft <= 0) {
                    return clearInterval(interval);
                }

                const particleCount = 50 * (timeLeft / duration);
                
                // Left fireworks
                confetti(Object.assign({}, defaults, { 
                    particleCount,
                    origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 }
                }));
                // Right fireworks
                confetti(Object.assign({}, defaults, { 
                    particleCount,
                    origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 }
                }));
            }, 250);
            
            // Heart pop in the center
            setTimeout(() => {
                 confetti({
                    particleCount: 100,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#ff0000', '#ff69b4'],
                    shapes: ['circle']
                });
            }, 1000);
        }
    </script>
</body>
</html>
"""

# เรนเดอร์ HTML ลงบนหน้า Streamlit
components.html(html_code, height=900, scrolling=False)
