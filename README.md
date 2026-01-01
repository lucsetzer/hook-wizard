cat > README.md << 'EOF'
# 🎣 Hook Wizard

AI-powered viral hook generator for content creators. Create stopping hooks for any platform in 6 easy steps.

## Features
- **6-Step Wizard** for precise hook customization
- **AI-Powered** with DeepSeek integration
- **Platform-Specific** hooks (YouTube, TikTok, Instagram, etc.)
- **Beautiful UI** with turquoise theme and clean cards
- **Click-to-select** text for easy copying
- **No JavaScript** - Pure Python + FastAPI + Pico.css

## Quick Start
1. Clone the repo
2. Install requirements: `pip install fastapi uvicorn requests python-dotenv`
3. Add your DeepSeek API key to `.env`
4. Run: `python app.py`
5. Visit: `http://localhost:8002`

## Tech Stack
- **Backend**: FastAPI, Python
- **Frontend**: Pico.css, HTML5
- **AI**: DeepSeek API
- **Deployment**: Uvicorn

## Screenshots
[Add screenshots of your wizard steps and results]

## License
MIT
EOF

# Add and commit README
git add README.md
git commit -m "Add README.md with project documentation"
git push
