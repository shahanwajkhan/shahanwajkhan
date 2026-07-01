/* ==========================================
   SHAHANWAJ_AI CORE INTERFACE LOGIC (app.js)
   ========================================== */

document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================
    // 1. STATE & GLOBAL UTILITIES
    // ==========================================
    const state = {
        audioInitialized: false,
        audioPlaying: false,
        activeProject: null,
        terminalHistory: []
    };

    // Project data dictionary
    const projectsData = {
        skillguard: {
            title: "SKILLGUARD AI",
            classification: "AI Assessment & Proctoring System",
            progress: "90% COMPLETE",
            state: "ACTIVE DEVELOPMENT",
            desc: "An intelligent assessment portal utilizing advanced web algorithms and Gemini AI integrations to evaluate candidate capabilities. Features dynamic code evaluation, real-time proctoring telemetry, and automated feedback loops.",
            tech: ["Python", "JavaScript", "Gemini AI", "WebRTC", "Node.js"],
            repo: "https://github.com/shahanwajkhan/SkillGuard-AI",
            live: "https://shahanwajkhan.github.io/SkillGuard-AI/"
        },
        flashmind: {
            title: "FLASHMIND AI",
            classification: "Neural-Study Platform",
            progress: "100% OPERATIONAL",
            state: "ARCHIVED / DEPLOYED",
            desc: "A smart studying tool that synthesizes lecture files into custom interactive flashcards. Runs on local SQLite caches and incorporates spaced-repetition scheduling for optimized cognitive retention.",
            tech: ["HTML5", "CSS3", "JavaScript", "PHP", "SQLite"],
            repo: "https://github.com/shahanwajkhan/FlashMind",
            live: "https://shahanwajkhan.github.io/FlashMind/"
        },
        traffic: {
            title: "TRAFFIC MANAGEMENT SYSTEM",
            classification: "Computer Vision Optimizer",
            progress: "100% OPERATIONAL",
            state: "STABLE PROTO-BUILD",
            desc: "An intelligent traffic routing model leveraging OpenCV models to analyze vehicle density in real-time. Dynamically adjusts simulated signal durations to optimize flow and reduce gridlock by 28%.",
            tech: ["Python", "OpenCV", "HTML/CSS", "Flask", "MySQL"],
            repo: "https://github.com/shahanwajkhan/Traffic-Management",
            live: "https://github.com/shahanwajkhan/Traffic-Management"
        },
        cycletrack: {
            title: "CYCLETRACK GPS Tracker",
            classification: "IoT & GPS Telemetry Grid",
            progress: "100% OPERATIONAL",
            state: "DECOMMISSIONED / LOGGED",
            desc: "A mobile-responsive bicycle activity and health logging system. Compiles sensor data, maps ride paths using Leaflet coordinates, and reports metrics to a central PHP/MySQL relational hub.",
            tech: ["JavaScript", "Leaflet.js", "PHP", "MySQL", "CSS Grid"],
            repo: "https://github.com/shahanwajkhan/CycleTrack",
            live: "https://github.com/shahanwajkhan/CycleTrack"
        }
    };

    // ==========================================
    // 2. SYNTHESIZED WEB AUDIO ENGINE
    // ==========================================
    let audioCtx = null;
    let ambientHumNode = null;
    let ambientLfoNode = null;
    let masterGainNode = null;

    function initAudio() {
        if (state.audioInitialized) return;
        
        try {
            // Create audio context
            const AudioContextClass = window.AudioContext || window.webkitAudioContext;
            audioCtx = new AudioContextClass();
            masterGainNode = audioCtx.createGain();
            masterGainNode.gain.setValueAtTime(0, audioCtx.currentTime);
            masterGainNode.connect(audioCtx.destination);

            // 1. Ambient spacecraft drone hum
            const oscHum = audioCtx.createOscillator();
            const filterHum = audioCtx.createBiquadFilter();
            const gainHum = audioCtx.createGain();

            oscHum.type = 'triangle';
            oscHum.frequency.setValueAtTime(55, audioCtx.currentTime); // A1 note - very low drone

            // LFO to slowly modulate pitch slightly for warmth
            const lfo = audioCtx.createOscillator();
            const lfoGain = audioCtx.createGain();
            lfo.type = 'sine';
            lfo.frequency.setValueAtTime(0.15, audioCtx.currentTime); // Sweeps every ~6.6 seconds
            lfoGain.gain.setValueAtTime(0.3, audioCtx.currentTime); // Pitch range variation

            // Lowpass filter to muffle high frequencies
            filterHum.type = 'lowpass';
            filterHum.frequency.setValueAtTime(110, audioCtx.currentTime); // cutoff frequency

            gainHum.gain.setValueAtTime(0.35, audioCtx.currentTime); // balance hum volume

            // Route hum elements
            lfo.connect(lfoGain);
            lfoGain.connect(oscHum.frequency);
            oscHum.connect(filterHum);
            filterHum.connect(gainHum);
            gainHum.connect(masterGainNode);

            // Start sound oscillators
            oscHum.start(0);
            lfo.start(0);

            // Store nodes
            ambientHumNode = oscHum;
            ambientLfoNode = lfo;
            state.audioInitialized = true;
        } catch (e) {
            console.error("Web Audio initialization failed: ", e);
        }
    }

    function toggleAudio() {
        const audioBtn = document.getElementById('audio-toggle');
        const audioIcon = document.getElementById('audio-icon');
        const audioText = document.getElementById('audio-text');

        if (!state.audioInitialized) {
            initAudio();
        }

        if (audioCtx && audioCtx.state === 'suspended') {
            audioCtx.resume();
        }

        if (state.audioPlaying) {
            // Fade out
            masterGainNode.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 0.4);
            audioIcon.className = "fa-solid fa-volume-xmark";
            audioText.textContent = "AUDIO: MUTED";
            audioBtn.classList.remove('active');
            state.audioPlaying = false;
        } else {
            // Fade in
            masterGainNode.gain.exponentialRampToValueAtTime(0.12, audioCtx.currentTime + 0.4);
            audioIcon.className = "fa-solid fa-volume-high";
            audioText.textContent = "AUDIO: SYSTEM HUM";
            audioBtn.classList.add('active');
            state.audioPlaying = true;
            // Play a mechanical initialization click
            playClickSound(1000, 0.05, 50);
        }
    }

    // Synthesizer click sound generator (emulating keyboard keys or CRT relays)
    function playClickSound(frequency = 800, gain = 0.03, durationMs = 15) {
        if (!state.audioInitialized || !state.audioPlaying || !audioCtx) return;

        try {
            const osc = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();

            osc.type = 'sine';
            osc.frequency.setValueAtTime(frequency, audioCtx.currentTime);
            // Quick sweep down
            osc.frequency.exponentialRampToValueAtTime(frequency / 4, audioCtx.currentTime + (durationMs / 1000));

            gainNode.gain.setValueAtTime(gain, audioCtx.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + (durationMs / 1000));

            osc.connect(gainNode);
            gainNode.connect(masterGainNode);

            osc.start();
            osc.stop(audioCtx.currentTime + (durationMs / 1000));
        } catch (e) {
            // Quiet fail
        }
    }

    document.getElementById('audio-toggle').addEventListener('click', toggleAudio);

    // ==========================================
    // 3. CANVAS STARFIELD PARTICLE BACKGROUND
    // ==========================================
    const canvasStars = document.getElementById('starfield-canvas');
    const ctxStars = canvasStars.getContext('2d');
    let stars = [];
    const maxStars = 150;
    let w = canvasStars.width = window.innerWidth;
    let h = canvasStars.height = window.innerHeight;

    class Star {
        constructor() {
            this.reset();
        }
        reset() {
            this.x = Math.random() * w;
            this.y = Math.random() * h;
            this.size = Math.random() * 1.5 + 0.25;
            this.speed = Math.random() * 0.35 + 0.05;
            this.color = Math.random() > 0.8 ? 'rgba(0, 243, 255, 0.8)' : 'rgba(255, 255, 255, 0.6)';
        }
        update() {
            this.y -= this.speed;
            if (this.y < 0) {
                this.reset();
                this.y = h;
            }
        }
        draw() {
            ctxStars.fillStyle = this.color;
            ctxStars.shadowBlur = this.size * 2;
            ctxStars.shadowColor = this.color;
            ctxStars.fillRect(this.x, this.y, this.size, this.size);
            ctxStars.shadowBlur = 0; // reset
        }
    }

    function initStars() {
        stars = [];
        for (let i = 0; i < maxStars; i++) {
            stars.push(new Star());
        }
    }

    function animateStars() {
        ctxStars.clearRect(0, 0, w, h);
        for (let i = 0; i < maxStars; i++) {
            stars[i].update();
            stars[i].draw();
        }
        requestAnimationFrame(animateStars);
    }

    window.addEventListener('resize', () => {
        w = canvasStars.width = window.innerWidth;
        h = canvasStars.height = window.innerHeight;
        initStars();
    });

    initStars();
    animateStars();

    // ==========================================
    // 4. RADAR CANVAS SYSTEM
    // ==========================================
    const canvasRadar = document.getElementById('radar-canvas');
    const ctxRadar = canvasRadar.getContext('2d');
    let sweepAngle = 0;
    
    // Skills mapping onto Radar coordinate angles
    // 4 nodes: AI (top: 270deg), Frontend (right: 0deg), Backend (bottom: 90deg), Databases (left: 180deg)
    const skillsData = [
        { label: 'AI Models', val: 0.85, angle: (3 * Math.PI) / 2 },
        { label: 'Frontend', val: 0.95, angle: 0 },
        { label: 'Backend', val: 0.80, angle: Math.PI / 2 },
        { label: 'Databases', val: 0.85, angle: Math.PI }
    ];

    function drawRadar() {
        const cw = canvasRadar.width = canvasRadar.parentElement.clientWidth;
        const ch = canvasRadar.height = 190;
        const cx = cw / 2;
        const cy = ch / 2;
        const radius = Math.min(cw, ch) * 0.42;

        ctxRadar.clearRect(0, 0, cw, ch);

        // 1. Concentric telemetric rings
        ctxRadar.strokeStyle = 'rgba(0, 243, 255, 0.15)';
        ctxRadar.lineWidth = 1;
        for (let r = 0.25; r <= 1.0; r += 0.25) {
            ctxRadar.beginPath();
            ctxRadar.arc(cx, cy, radius * r, 0, 2 * Math.PI);
            ctxRadar.stroke();
        }

        // 2. Crosshairs axes
        ctxRadar.beginPath();
        ctxRadar.moveTo(cx - radius * 1.1, cy);
        ctxRadar.lineTo(cx + radius * 1.1, cy);
        ctxRadar.moveTo(cx, cy - radius * 1.1);
        ctxRadar.lineTo(cx, cy + radius * 1.1);
        ctxRadar.strokeStyle = 'rgba(0, 243, 255, 0.12)';
        ctxRadar.stroke();

        // 3. Draw connecting skill polygonal net
        ctxRadar.beginPath();
        skillsData.forEach((s, idx) => {
            const sx = cx + Math.cos(s.angle) * radius * s.val;
            const sy = cy + Math.sin(s.angle) * radius * s.val;
            if (idx === 0) ctxRadar.moveTo(sx, sy);
            else ctxRadar.lineTo(sx, sy);
        });
        ctxRadar.closePath();
        ctxRadar.fillStyle = 'rgba(0, 243, 255, 0.1)';
        ctxRadar.fill();
        ctxRadar.strokeStyle = 'rgba(0, 243, 255, 0.7)';
        ctxRadar.lineWidth = 1.5;
        ctxRadar.stroke();

        // 4. Radar sweep line
        sweepAngle += 0.015;
        const sx = cx + Math.cos(sweepAngle) * radius;
        const sy = cy + Math.sin(sweepAngle) * radius;

        // Gradient sweep effect
        const sweepGrad = ctxRadar.createRadialGradient(cx, cy, 0, cx, cy, radius);
        sweepGrad.addColorStop(0, 'rgba(0, 243, 255, 0.05)');
        sweepGrad.addColorStop(1, 'rgba(0, 243, 255, 0)');
        
        ctxRadar.beginPath();
        ctxRadar.moveTo(cx, cy);
        ctxRadar.arc(cx, cy, radius, sweepAngle - 0.25, sweepAngle);
        ctxRadar.closePath();
        ctxRadar.fillStyle = 'rgba(0, 243, 255, 0.12)';
        ctxRadar.fill();

        ctxRadar.beginPath();
        ctxRadar.moveTo(cx, cy);
        ctxRadar.lineTo(sx, sy);
        ctxRadar.strokeStyle = 'rgba(0, 243, 255, 0.6)';
        ctxRadar.lineWidth = 2;
        ctxRadar.stroke();

        // 5. Draw interactive node labels and glowing markers
        skillsData.forEach(s => {
            const nx = cx + Math.cos(s.angle) * radius * s.val;
            const ny = cy + Math.sin(s.angle) * radius * s.val;

            // Check if sweep line is close to this node's angle
            const angleDiff = Math.abs((sweepAngle % (2 * Math.PI)) - (s.angle < 0 ? s.angle + 2 * Math.PI : s.angle) % (2 * Math.PI));
            const isColliding = angleDiff < 0.15 || angleDiff > (2 * Math.PI - 0.15);

            ctxRadar.beginPath();
            ctxRadar.arc(nx, ny, isColliding ? 5 : 3.5, 0, 2 * Math.PI);
            ctxRadar.fillStyle = isColliding ? '#d300ff' : '#00f3ff';
            ctxRadar.shadowColor = isColliding ? '#d300ff' : '#00f3ff';
            ctxRadar.shadowBlur = isColliding ? 8 : 4;
            ctxRadar.fill();
            ctxRadar.shadowBlur = 0; // reset

            // Print Label texts near nodes
            ctxRadar.font = '10px "Share Tech Mono"';
            ctxRadar.fillStyle = 'rgba(196, 217, 252, 0.75)';
            const offsetDist = 18;
            const lx = cx + Math.cos(s.angle) * (radius * s.val + offsetDist);
            const ly = cy + Math.sin(s.angle) * (radius * s.val + offsetDist) + 3;
            ctxRadar.textAlign = Math.cos(s.angle) > 0.1 ? 'left' : (Math.cos(s.angle) < -0.1 ? 'right' : 'center');
            ctxRadar.fillText(s.label, lx, ly);
        });

        requestAnimationFrame(drawRadar);
    }
    
    // Start radar
    drawRadar();

    // ==========================================
    // 5. JARVIS AI ASSISTANT CHAT ENGINE
    // ==========================================
    const assistantText = document.getElementById('assistant-text');
    let typewriterTimeout = null;

    const jarvisResponses = {
        mission: "Scanning objective metrics: Shahanwaj is actively building 'SkillGuard AI' (AI-proctored code assessment hub), targeted at 90% completion. Highly available for Internship contracts starting immediately. Focus: intelligent full-stack applications.",
        skills: "Analyzing capabilities grid: HTML/CSS architectures (95%), Core ES6 JavaScript logic (90%), Python and Deep Learning integrations (85%), and PHP/MySQL data storage layers (80%). Code robustness index: OPTIMAL.",
        experience: "Retrieving developmental logs. System achievements unlocked: constructions of real-time Traffic Optimizers, Flashcard Synthesizers, GPS Activity trackers, and hackathon prototypes. All bosses: DEFEATED.",
        contact: "Opening secure ports. E-mail route: shahanwajkhan@example.com. Active signals established on GitHub and LinkedIn. Initiate communications at your convenience.",
        greeting: "System loaded. I am Shahanwaj's JARVIS assistant. Select a query button below or command the terminal.",
        unknown: "Query syntax invalid. Re-check prompt or click a telemetry shortcut to analyze Shahanwaj's profile."
    };

    function triggerJarvisReply(type) {
        // Clear active typewriter processes
        if (typewriterTimeout) {
            clearTimeout(typewriterTimeout);
        }

        const msg = jarvisResponses[type] || jarvisResponses.unknown;
        assistantText.innerHTML = '';
        let index = 0;
        
        // Pulse animation on the avatar
        const pulseRing = document.querySelector('.pulse-ring');
        if (pulseRing) {
            pulseRing.style.animation = 'flash-pulse 0.3s infinite';
            setTimeout(() => {
                pulseRing.style.animation = '';
            }, 1000);
        }

        // Typewriter loop
        function typeWriter() {
            if (index < msg.length) {
                assistantText.innerHTML += msg.charAt(index);
                
                // Play typing hum click sound
                if (index % 3 === 0) {
                    playClickSound(1200 + Math.random() * 400, 0.015, 8);
                }
                
                index++;
                typewriterTimeout = setTimeout(typeWriter, 15);
            }
        }
        
        typeWriter();
    }

    // Attach suggested query event listeners
    document.querySelectorAll('.query-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const queryType = e.target.getAttribute('data-query');
            triggerJarvisReply(queryType);
            playClickSound(700, 0.03, 20);
        });
    });

    // ==========================================
    // 6. INTERACTIVE PROJECT PLANETARY EXPLORER
    // ==========================================
    const detailOverlay = document.getElementById('project-details-overlay');
    const closeOverlay = document.getElementById('close-overlay');
    
    const holoTitle = document.getElementById('holo-title');
    const holoClass = document.getElementById('holo-class');
    const holoProgress = document.getElementById('holo-progress');
    const holoState = document.getElementById('holo-state');
    const holoDesc = document.getElementById('holo-desc');
    const holoTech = document.getElementById('holo-tech');
    const holoGitLink = document.getElementById('holo-github-link');
    const holoLiveLink = document.getElementById('holo-live-link');

    // Click project planetary nodes
    document.querySelectorAll('.planet-wrapper').forEach(planetWrap => {
        planetWrap.addEventListener('click', (e) => {
            // Find planet key
            const projKey = planetWrap.getAttribute('data-project');
            const data = projectsData[projKey];
            
            if (data) {
                playClickSound(400, 0.05, 40);
                
                // Populate Hologram details
                holoTitle.textContent = data.title;
                holoClass.textContent = data.classification;
                holoProgress.textContent = data.progress;
                holoState.textContent = data.state;
                holoDesc.textContent = data.desc;
                
                // Tech badges
                holoTech.innerHTML = '';
                data.tech.forEach(t => {
                    const badge = document.createElement('span');
                    badge.className = 'tech-badge';
                    badge.textContent = t;
                    holoTech.appendChild(badge);
                });
                
                // Links
                holoGitLink.href = data.repo;
                holoLiveLink.href = data.live;

                // Adjust color classes on overlay border to match planet
                detailOverlay.className = 'project-details-overlay active';
                if (projKey === 'skillguard') {
                    detailOverlay.style.borderColor = 'var(--neon-cyan)';
                    detailOverlay.style.boxShadow = '0 0 25px rgba(0, 243, 255, 0.4)';
                } else if (projKey === 'flashmind') {
                    detailOverlay.style.borderColor = 'var(--neon-purple)';
                    detailOverlay.style.boxShadow = '0 0 25px rgba(211, 0, 255, 0.4)';
                } else if (projKey === 'traffic') {
                    detailOverlay.style.borderColor = 'var(--neon-green)';
                    detailOverlay.style.boxShadow = '0 0 25px rgba(57, 255, 20, 0.4)';
                } else if (projKey === 'cycletrack') {
                    detailOverlay.style.borderColor = 'var(--neon-orange)';
                    detailOverlay.style.boxShadow = '0 0 25px rgba(255, 108, 0, 0.4)';
                }

                // JARVIS comments on this project
                const jarvisComment = `Accessing diagnostics for project ${data.title}... Status: ${data.progress}. Stack incorporates ${data.tech.slice(0, 3).join(', ')}.`;
                assistantText.innerHTML = '';
                let index = 0;
                
                if (typewriterTimeout) clearTimeout(typewriterTimeout);
                function commentWriter() {
                    if (index < jarvisComment.length) {
                        assistantText.innerHTML += jarvisComment.charAt(index);
                        if (index % 3 === 0) playClickSound(1400, 0.015, 6);
                        index++;
                        typewriterTimeout = setTimeout(commentWriter, 15);
                    }
                }
                commentWriter();
            }
        });
    });

    closeOverlay.addEventListener('click', () => {
        detailOverlay.classList.remove('active');
        playClickSound(600, 0.03, 15);
    });

    // Close on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            detailOverlay.classList.remove('active');
        }
    });

    // Sun core trigger jarvis greeting
    document.getElementById('sun-core').addEventListener('click', () => {
        triggerJarvisReply('greeting');
        playClickSound(500, 0.05, 30);
    });

    // ==========================================
    // 7. INTERACTIVE WEB TERMINAL EMULATOR
    // ==========================================
    const termInput = document.getElementById('terminal-input');
    const termOutput = document.getElementById('terminal-output');

    // Make typing play a keyboard click
    termInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const val = termInput.value.trim();
            termInput.value = '';
            
            if (val.length > 0) {
                handleTerminalCommand(val);
            }
        } else if (e.key.length === 1 || e.key === 'Backspace') {
            // Typing key click feedback
            playClickSound(900 + Math.random() * 200, 0.012, 10);
        }
    });

    // Focus input when clicking terminal card body
    document.getElementById('card-terminal').addEventListener('click', () => {
        termInput.focus();
    });

    function printTerm(text, className = '') {
        const p = document.createElement('p');
        p.className = className;
        p.innerHTML = text;
        termOutput.appendChild(p);
        termOutput.scrollTop = termOutput.scrollHeight;
    }

    function handleTerminalCommand(cmdString) {
        const args = cmdString.toLowerCase().split(' ');
        const primary = args[0];

        // Print input echoed back
        printTerm(`<span class="terminal-prompt">guest@shahanwaj_ai:~$</span> ${cmdString}`);

        switch (primary) {
            case 'help':
                printTerm("--- COGNITIVE SHELL COMMANDS ---", "text-glow-blue");
                printTerm("about       - Diagnostics summary for Shahanwaj");
                printTerm("skills      - List experience points & coding arsenals");
                printTerm("projects    - List orbiting code repository systems");
                printTerm("radar       - Print detailed frequency mapping");
                printTerm("jarvis      - Ask JARVIS assistant for voice files [usage: jarvis &lt;query&gt;]");
                printTerm("contact     - Open transmission lines");
                printTerm("clear       - Flush output history");
                printTerm("matrix      - Boot terminal visual sub-module");
                break;
            case 'about':
                printTerm("SYSTEM USER SUMMARY:", "text-glow-purple");
                printTerm("• Name: Shahanwaj Khan");
                printTerm("• Level: 22 (Full Stack Node)");
                printTerm("• Class: Full Stack Developer / AI Integration Specialist");
                printTerm("• Special Ability: AI Web Architecture & Automation");
                printTerm("• Status: Open for Internship contracts");
                break;
            case 'skills':
                printTerm("SKILL COMPILATION DATA:", "text-glow-green");
                printTerm("HTML/CSS   [███████████████████░] 95%");
                printTerm("JavaScript [██████████████████░░] 90%");
                printTerm("Python/AI  [█████████████████░░░] 85%");
                printTerm("PHP        [████████████████░░░░] 80%");
                printTerm("MySQL      [█████████████████░░░] 85%");
                break;
            case 'projects':
                if (args[1]) {
                    const searchProj = args[1];
                    let foundKey = null;
                    if (searchProj.includes('guard') || searchProj === '1') foundKey = 'skillguard';
                    else if (searchProj.includes('mind') || searchProj === '2') foundKey = 'flashmind';
                    else if (searchProj.includes('traffic') || searchProj === '3') foundKey = 'traffic';
                    else if (searchProj.includes('cycle') || searchProj === '4') foundKey = 'cycletrack';

                    if (foundKey) {
                        printTerm(`Opening planet diagnostics overlay for: ${foundKey.toUpperCase()}...`);
                        document.getElementById(`planet-${foundKey === 'skillguard' ? 1 : foundKey === 'flashmind' ? 2 : foundKey === 'traffic' ? 3 : 4}`).click();
                    } else {
                        printTerm(`System error: project '${args[1]}' not registered in solar system map.`, "text-glow-red");
                    }
                } else {
                    printTerm("--- REGISTERED ORBITAL PLANETS ---");
                    printTerm("[1] SkillGuard AI         - AI Assessments & Proctoring (90%)");
                    printTerm("[2] FlashMind             - Neural Flashcard generator (100%)");
                    printTerm("[3] Traffic Management    - CV Intelligent Signal Grid (100%)");
                    printTerm("[4] CycleTrack            - GPS ride activity logs (100%)");
                    printTerm("Type 'projects <number>' to deploy holographic analyzer panel.");
                }
                break;
            case 'radar':
                printTerm("RADAR SCANNING REPORT:", "text-glow-blue");
                skillsData.forEach(s => {
                    printTerm(`• frequency sweep - ${s.label}: ${s.val * 100}% signal integrity`);
                });
                break;
            case 'jarvis':
                const queryVal = args.slice(1).join(' ');
                if (!queryVal) {
                    printTerm("Usage: jarvis &lt;mission|skills|experience|contact&gt;");
                } else {
                    printTerm(`Querying JARVIS core: "${queryVal}"...`);
                    if (queryVal.includes('mission') || queryVal.includes('goal')) {
                        triggerJarvisReply('mission');
                    } else if (queryVal.includes('skill') || queryVal.includes('tech')) {
                        triggerJarvisReply('skills');
                    } else if (queryVal.includes('exp') || queryVal.includes('achieve') || queryVal.includes('work')) {
                        triggerJarvisReply('experience');
                    } else if (queryVal.includes('contact') || queryVal.includes('email') || queryVal.includes('phone')) {
                        triggerJarvisReply('contact');
                    } else {
                        triggerJarvisReply('unknown');
                    }
                }
                break;
            case 'contact':
                printTerm("SECURE TRANSMISSION FREQUENCIES:", "text-glow-purple");
                printTerm("• Mail routing: shahanwajkhan@example.com");
                printTerm("• GitHub node: github.com/shahanwajkhan");
                printTerm("• LinkedIn link: linkedin.com/in/shahanwajkhan");
                break;
            case 'clear':
                termOutput.innerHTML = '';
                break;
            case 'matrix':
                printTerm("BOOTING VIRTUAL MATRIX SECTIONS...");
                let linesCount = 0;
                const matrixInterval = setInterval(() => {
                    let matrixLine = "";
                    for (let x = 0; x < 28; x++) {
                        matrixLine += String.fromCharCode(33 + Math.floor(Math.random() * 93));
                    }
                    printTerm(matrixLine, "text-glow-green");
                    linesCount++;
                    if (linesCount > 15) {
                        clearInterval(matrixInterval);
                        printTerm("MATRIX EMULATION STREAM TERMINATED.");
                    }
                }, 100);
                break;
            default:
                printTerm(`Command not recognized: '${primary}'. Type 'help' for support.`, "text-glow-red");
                break;
        }
        
        playClickSound(600, 0.05, 30);
    }

    // ==========================================
    // 8. TELEMETRY FLUCTUATOR (Ticking status)
    // ==========================================
    const coordsEl = document.getElementById('sys-coords');
    const tempEl = document.getElementById('sys-temp');
    const tickerEl = document.getElementById('log-ticker');

    const logMessages = [
        "INITIALIZING PORTFOLIO TELEMETRY DATA STREAMS...",
        "CONNECTING SECURE DATABASE NODES...",
        "DECRYPTING EXPERIMENTAL AI INTERVIEWS...",
        "OPTIMIZING SIGNAL PROCESSING GRID...",
        "TRAFFIC CV ALGORITHMS RETURNING 99.4% HIT RATE...",
        "UPDATING STARFIELD PARTICLE VELOCITIES...",
        "AI INTERVIEW ANALYZER INITIATING STANDBY STATE...",
        "FLASHMIND COGNITIVE MAP LOADED SUCCESSFUL...",
        "COMPILING PORTFOLIO VERSION 3.2 SUCCESS..."
    ];

    setInterval(() => {
        // Temperature fluctuations
        const currentTemp = (36.2 + Math.random() * 2.2).toFixed(1);
        tempEl.textContent = `${currentTemp}°C`;
        if (currentTemp > 38.0) {
            tempEl.className = "value text-glow-red";
        } else {
            tempEl.className = "value text-glow-green";
        }

        // Coordinate adjustments
        const decMinutes = Math.floor(Math.random() * 60);
        const decSeconds = Math.floor(Math.random() * 60);
        coordsEl.textContent = `RA 18h 36m / DEC +38° ${decMinutes}′ ${decSeconds}″`;

        // Update footer log ticker occasionally
        if (Math.random() > 0.6) {
            const randomMsg = logMessages[Math.floor(Math.random() * logMessages.length)];
            tickerEl.textContent = `${randomMsg} // ${tickerEl.textContent.slice(0, 160)}`;
        }
    }, 4000);

});
