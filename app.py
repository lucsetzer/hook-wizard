# hook_wizard/app.py - HOOK WIZARD
from fastapi import FastAPI, Query, Form
from fastapi.responses import HTMLResponse
import uvicorn
import requests
import re
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates"

# Detect if running locally or deployed
IS_PRODUCTION = os.getenv("RAILWAY_ENVIRONMENT") == "production"
# OR: IS_PRODUCTION = os.getenv("ENVIRONMENT") == "production"app = FastAPI()


app = FastAPI()
DEEPSEEK_KEY = "sk-221a023bf3d245048184283d594e3334"  # Same key

def layout(title: str, content: str) -> str:
    return f'''<!DOCTYPE html>
<html>
<head>
    <title>{title} | Hook Alchemy</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #3b82f6;  /* BLUE theme for hooks */
            --primary-hover: #2563eb;
        }}
        
        [role="button"], button, .btn-primary {{
            background: var(--primary);
            border-color: var(--primary);
        }}
        
        a {{ color: var(--primary); }}
        a:hover {{ color: var(--primary-hover); }}
        
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
            margin: 2rem 0;
        }}
        
        .step-card {{
            padding: 1.5rem;
            border: 2px solid #e5e7eb;
            border-radius: 0.75rem;
            text-align: center;
            text-decoration: none;
            color: inherit;
            transition: all 0.2s;
        }}
        
        .step-card:hover {{
            border-color: var(--primary);
            transform: translateY(-2px);
        }}
        
        .step-card i {{
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 1rem;
        }}
        
        .loading-bar {{
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            margin: 2rem 0;
            overflow: hidden;
        }}
        
        .loading-progress {{
            height: 100%;
            background: linear-gradient(90deg, var(--primary), #60a5fa);
            border-radius: 4px;
            animation: loading 2s infinite;
            width: 60%;
        }}
        
        @keyframes loading {{
            0% {{ transform: translateX(-100%); }}
            100% {{ transform: translateX(350%); }}
        }}
        
        .steps {{
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin: 2rem 0;
        }}
        
        .step {{
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: #e5e7eb;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }}
        
        .step.active {{
            background: var(--primary);
            color: white;
        }}
        
        .result-box {{
            background: #f8fafc;
            border: 2px solid #e5e7eb;
            border-left: 4px solid var(--primary);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin: 1rem 0;
            white-space: pre-wrap;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 1rem;
            line-height: 1.6;
            text-align: left;
            color: #1f2937;
            overflow-x: auto;
        }}
        
        .hook-example {{
            background: #eff6ff;
            border: 1px solid #dbeafe;
            border-radius: 0.5rem;
            padding: 1rem;
            margin: 0.5rem 0;
            font-style: italic;
        }}
    </style>
</head>
<body style="background: white;">
    <!-- ========== COMPLETE NAVBAR ========== -->
    <nav class="main-nav">
        <div class="nav-container">
            <!-- Logo -->
            <a href="/" class="brand">
                <i class="fas fa-flask"></i> Prompts Alchemy
            </a>
            
            <!-- All Links -->
            <div class="nav-links">
                <!-- Home -->
                <a href="/">
                    <i class="fas fa-home"></i> Home
                </a>
                
                <!-- Wizard 1 -->
                <a href="/prompt-wizard/">
                    <i class="fas fa-hat-wizard"></i> Prompt Wizard
                </a>
                
                <!-- Wizard 2 -->
                <a href="/thumbnail-wizard/">
                    <i class="fas fa-image"></i> Thumbnail Wizard
                </a>
                
                <!-- Wizard 3 -->
                <a href="/video-wizard/">
                    <i class="fas fa-video"></i> Video Wizard
                </a>
                
                <!-- Wizard 4 -->
                <a href="/hook-wizard/">
                    <i class="fas fa-fish"></i> Hook Wizard
                </a>
                
                <!-- Wizard 5 -->
                <a href="/document-wizard/">
                    <i class="fas fa-file-contract"></i> Document Wizard
                </a>
                
                <!-- Pricing -->
                <a href="#pricing">
                    <i class="fas fa-tag"></i> Pricing
                </a>
                
                <!-- Get Started Button -->
                <a href="#pricing" class="nav-cta">
                    <i class="fas fa-rocket"></i> Get Started
                </a>
            </div>
        </div>
    </nav>

<main class="container" style="padding: 2rem 0; min-height: 80vh;">
    {content}
</main>

<footer style="text-align: center; padding: 2rem; color: #6b7280; border-top: 1px solid #e5e7eb;">
    <p>Hook Wizard • Create viral openings for any platform</p>
</footer>
</body>
</html>'''

# ========== DASHBOARD ==========
@app.get("/")
async def home():
    content = '''
    <div style="text-align: center; padding: 4rem 0;">
        <h1 style="color: var(--primary);">
            <i class="fas fa-fish-hook"></i><br>
            Hook Alchemy
        </h1>
        <p style="font-size: 1.25rem; color: #6b7280; max-width: 500px; margin: 1rem auto;">
            AI-powered hook generator. Stop viewers from scrolling in 3 seconds.
        </p>
        
        <div style="margin: 3rem 0;">
            <a href="/wizard" role="button" style="padding: 1rem 2.5rem; font-size: 1.25rem;">
                <i class="fas fa-magic"></i> Start Hook Wizard
            </a>
        </div>
        
        <div class="card-grid">
            <div class="step-card">
                <i class="fab fa-tiktok"></i>
                <h3>TikTok Hooks</h3>
                <p>Stop the scroll in 1 second</p>
            </div>
            
            <div class="step-card">
                <i class="fab fa-youtube"></i>
                <h3>YouTube Hooks</h3>
                <p>Beat the 30-second skip</p>
            </div>
            
            <div class="step-card">
                <i class="fab fa-instagram"></i>
                <h3>Instagram Hooks</h3>
                <p>Grab attention on Reels</p>
            </div>
            
            <div class="step-card">
                <i class="fab fa-linkedin"></i>
                <h3>LinkedIn Hooks</h3>
                <p>Professional engagement</p>
            </div>
        </div>
        
        <div class="hook-example" style="max-width: 600px; margin: 3rem auto;">
            <h3>Example Hook Generated:</h3>
            <p>"What if I told you your first 3 seconds determine 80% of your video's success? Here's why..."</p>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Home", content))

# ========== STEP 1: PLATFORM ==========
@app.get("/wizard")
async def step1():
    content = '''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step active">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
            <div class="step">5</div>
            <div class="step">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 1: Choose Platform</h1>
        <p style="text-align: center; color: #6b7280;">
            Where will your content be seen?
        </p>
        
        <div class="card-grid">
            <a href="/wizard/step2?platform=tiktok" class="step-card">
                <i class="fab fa-tiktok"></i>
                <h3>TikTok</h3>
                <p>Fast, bold, under 3 seconds</p>
            </a>
            
            <a href="/wizard/step2?platform=youtube" class="step-card">
                <i class="fab fa-youtube"></i>
                <h3>YouTube</h3>
                <p>5-15 second hooks</p>
            </a>
            
            <a href="/wizard/step2?platform=instagram" class="step-card">
                <i class="fab fa-instagram"></i>
                <h3>Instagram</h3>
                <p>Reels & Stories</p>
            </a>
            
            <a href="/wizard/step2?platform=linkedin" class="step-card">
                <i class="fab fa-linkedin"></i>
                <h3>LinkedIn</h3>
                <p>Professional, value-first</p>
            </a>
            
            <a href="/wizard/step2?platform=twitter" class="step-card">
                <i class="fab fa-twitter"></i>
                <h3>Twitter/X</h3>
                <p>Thread starters</p>
            </a>
            
            <a href="/wizard/step2?platform=facebook" class="step-card">
                <i class="fab fa-facebook"></i>
                <h3>Facebook</h3>
                <p>Groups & viral posts</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/" role="button" class="secondary">Cancel</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 1: Platform", content))

# ========== STEP 2: HOOK TYPE ==========
@app.get("/wizard/step2")
async def step2(platform: str = Query("tiktok")):
    content = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step active">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
            <div class="step">5</div>
            <div class="step">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 2: Hook Type</h1>
        <p style="text-align: center; color: #6b7280;">
            What style of hook works best?
        </p>
        
        <p style="text-align: center;"><strong>Platform:</strong> {platform.title()}</p>
        
        <div class="card-grid">
            <a href="/wizard/step3?platform={platform}&type=question" class="step-card">
                <i class="fas fa-question-circle"></i>
                <h3>Question</h3>
                <p>Makes viewer think immediately</p>
            </a>
            
            <a href="/wizard/step3?platform={platform}&type=shocking" class="step-card">
                <i class="fas fa-bolt"></i>
                <h3>Shocking Stat</h3>
                <p>Surprising fact or number</p>
            </a>
            
            <a href="/wizard/step3?platform={platform}&type=story" class="step-card">
                <i class="fas fa-book"></i>
                <h3>Story</h3>
                <p>Personal anecdote or case study</p>
            </a>
            
            <a href="/wizard/step3?platform={platform}&type=controversy" class="step-card">
                <i class="fas fa-fire"></i>
                <h3>Controversy</h3>
                <p>Take a bold stance</p>
            </a>
            
            <a href="/wizard/step3?platform={platform}&type=howto" class="step-card">
                <i class="fas fa-wrench"></i>
                <h3>"How to"</h3>
                <p>Immediate value promise</p>
            </a>
            
            <a href="/wizard/step3?platform={platform}&type=fear" class="step-card">
                <i class="fas fa-exclamation-triangle"></i>
                <h3>Fear/Opportunity</h3>
                <p>What they're missing/avoiding</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 2: Hook Type", content))

# ========== STEP 3: CONTENT TYPE ==========
@app.get("/wizard/step3")
async def step3(platform: str = Query("tiktok"), type: str = Query("question")):
    content = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step">2</div>
            <div class="step active">3</div>
            <div class="step">4</div>
            <div class="step">5</div>
            <div class="step">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 3: Content Type</h1>
        <p style="text-align: center; color: #6b7280;">
            What kind of content follows the hook?
        </p>
        
        <p style="text-align: center;">
            <strong>Platform:</strong> {platform.title()} • 
            <strong>Hook Type:</strong> {type.replace("_", " ").title()}
        </p>
        
        <div class="card-grid">
            <a href="/wizard/step4?platform={platform}&type={type}&content=educational" class="step-card">
                <i class="fas fa-graduation-cap"></i>
                <h3>Educational</h3>
                <p>Teach, explain, inform</p>
            </a>
            
            <a href="/wizard/step4?platform={platform}&type={type}&content=entertainment" class="step-card">
                <i class="fas fa-laugh"></i>
                <h3>Entertainment</h3>
                <p>Funny, engaging, fun</p>
            </a>
            
            <a href="/wizard/step4?platform={platform}&type={type}&content=inspirational" class="step-card">
                <i class="fas fa-heart"></i>
                <h3>Inspirational</h3>
                <p>Motivate, uplift, inspire</p>
            </a>
            
            <a href="/wizard/step4?platform={platform}&type={type}&content=review" class="step-card">
                <i class="fas fa-star"></i>
                <h3>Review</h3>
                <p>Product/service analysis</p>
            </a>
            
            <a href="/wizard/step4?platform={platform}&type={type}&content=vlog" class="step-card">
                <i class="fas fa-user"></i>
                <h3>Vlog/Personal</h3>
                <p>Day-in-life, personal stories</p>
            </a>
            
            <a href="/wizard/step4?platform={platform}&type={type}&content=business" class="step-card">
                <i class="fas fa-briefcase"></i>
                <h3>Business</h3>
                <p>Marketing, tips, industry</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard/step2?platform={platform}" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 3: Content Type", content))

# ========== STEP 4: AUDIENCE ==========
@app.get("/wizard/step4")
async def step4(platform: str = Query("tiktok"), type: str = Query("question"), content: str = Query("educational")):
    content_html = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
            <div class="step active">4</div>
            <div class="step">5</div>
            <div class="step">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 4: Target Audience</h1>
        <p style="text-align: center; color: #6b7280;">
            Who are you trying to reach?
        </p>
        
        <p style="text-align: center;">
            <strong>Platform:</strong> {platform.title()} • 
            <strong>Hook:</strong> {type.replace("_", " ").title()} • 
            <strong>Content:</strong> {content.title()}
        </p>
        
        <div class="card-grid">
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=genz" class="step-card">
                <i class="fas fa-mobile-alt"></i>
                <h3>Gen Z</h3>
                <p>18-24, digital natives</p>
            </a>
            
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=millennials" class="step-card">
                <i class="fas fa-home"></i>
                <h3>Millennials</h3>
                <p>25-40, career-focused</p>
            </a>
            
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=professionals" class="step-card">
                <i class="fas fa-suitcase"></i>
                <h3>Professionals</h3>
                <p>Business, B2B, career</p>
            </a>
            
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=creators" class="step-card">
                <i class="fas fa-paint-brush"></i>
                <h3>Creators</h3>
                <p>Content creators, artists</p>
            </a>
            
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=parents" class="step-card">
                <i class="fas fa-baby"></i>
                <h3>Parents</h3>
                <p>Family, parenting, home</p>
            </a>
            
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience=general" class="step-card">
                <i class="fas fa-users"></i>
                <h3>General</h3>
                <p>Broad appeal</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard/step3?platform={platform}&type={type}" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 4: Audience", content_html))

# ========== STEP 5: TONE ==========
@app.get("/wizard/step5")
async def step5(platform: str = Query("tiktok"), type: str = Query("question"), content: str = Query("educational"), audience: str = Query("genz")):
    content_html = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
            <div class="step active">5</div>
            <div class="step">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 5: Choose Tone</h1>
        <p style="text-align: center; color: #6b7280;">
            What's the voice/personality?
        </p>
        
        <p style="text-align: center;">
            <strong>Platform:</strong> {platform.title()} • 
            <strong>Hook:</strong> {type.replace("_", " ").title()} • 
            <strong>Content:</strong> {content.title()} • 
            <strong>Audience:</strong> {audience.title()}
        </p>
        
        <div class="card-grid">
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=urgent" class="step-card">
                <i class="fas fa-clock"></i>
                <h3>Urgent</h3>
                <p>Time-sensitive, must-watch</p>
            </a>
            
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=funny" class="step-card">
                <i class="fas fa-laugh"></i>
                <h3>Funny</h3>
                <p>Humor, wit, entertainment</p>
            </a>
            
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=serious" class="step-card">
                <i class="fas fa-balance-scale"></i>
                <h3>Serious</h3>
                <p>Professional, authoritative</p>
            </a>
            
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=curious" class="step-card">
                <i class="fas fa-search"></i>
                <h3>Curious</h3>
                <p>Questioning, exploratory</p>
            </a>
            
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=excited" class="step-card">
                <i class="fas fa-star"></i>
                <h3>Excited</h3>
                <p>Energetic, enthusiastic</p>
            </a>
            
            <a href="/wizard/step6?platform={platform}&type={type}&content={content}&audience={audience}&tone=relatable" class="step-card">
                <i class="fas fa-handshake"></i>
                <h3>Relatable</h3>
                <p>"I've been there too"</p>
            </a>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard/step4?platform={platform}&type={type}&content={content}" role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 5: Tone", content_html))

# ========== STEP 6: TOPIC INPUT ==========
@app.get("/wizard/step6")
async def step6(
    platform: str = Query("tiktok"),
    type: str = Query("question"),
    content: str = Query("educational"),
    audience: str = Query("genz"),
    tone: str = Query("urgent")
):
    content_html = f'''
    <div style="max-width: 800px; margin: 0 auto;">
        <div class="steps">
            <div class="step">1</div>
            <div class="step">2</div>
            <div class="step">3</div>
            <div class="step">4</div>
            <div class="step">5</div>
            <div class="step active">6</div>
        </div>
        
        <h1 style="text-align: center; color: var(--primary);">Step 6: Enter Your Topic</h1>
        <p style="text-align: center; color: #6b7280;">
            What's your content about?
        </p>
        
        <div style="background: #f9fafb; padding: 1.5rem; border-radius: 0.75rem; margin: 2rem 0;">
            <h3>Your Selections:</h3>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 1rem; margin: 1rem 0;">
                <div><strong>Platform:</strong><br>{platform.title()}</div>
                <div><strong>Hook Type:</strong><br>{type.replace("_", " ").title()}</div>
                <div><strong>Content:</strong><br>{content.title()}</div>
                <div><strong>Audience:</strong><br>{audience.title()}</div>
                <div><strong>Tone:</strong><br>{tone.title()}</div>
            </div>
        </div>
        
        <div style="background: #eff6ff; border: 2px solid var(--primary); border-radius: 0.75rem; padding: 1rem; margin: 1rem 0;">
            <p style="margin: 0; color: #1e40af; display: flex; align-items: center; gap: 0.5rem;">
                <i class="fas fa-lightbulb" style="color: var(--primary);"></i>
                <strong>Pro Tip:</strong> Be specific! "How to lose weight" vs "3 science-backed habits for sustainable weight loss"
            </p>
        </div>
        
        <form action="/process" method="POST">
            <input type="hidden" name="platform" value="{platform}">
            <input type="hidden" name="type" value="{type}">
            <input type="hidden" name="content" value="{content}">
            <input type="hidden" name="audience" value="{audience}">
            <input type="hidden" name="tone" value="{tone}">
            
            <div style="margin: 2rem 0;">
                <label for="topic">
                    <strong>Your Topic/Subject:</strong>
                    <p style="color: #6b7280; margin: 0.5rem 0;">What is your video/post/content about?</p>
                </label>
                <textarea id="topic" name="topic" rows="4" 
                          placeholder="Example: 'Sustainable weight loss without dieting' or 'Review of the new iPhone camera features' or 'Day in the life of a remote software developer'"
                          style="width: 100%; padding: 1rem; border: 2px solid #e5e7eb; border-radius: 0.5rem;" required></textarea>
            </div>
            
            <div style="text-align: center; margin: 2rem 0;">
                <button type="submit" style="padding: 1rem 3rem; font-size: 1.2rem;">
                    <i class="fas fa-magic"></i> Generate Viral Hooks
                </button>
                <p style="margin-top: 1rem; color: #6b7280;">
                    <i class="fas fa-clock"></i> Creating 3 hook options for you...
                </p>
            </div>
        </form>
        
        <div style="text-align: center; margin-top: 2rem;">
            <a href="/wizard/step5?platform={platform}&type={type}&content={content}&audience={audience}" 
               role="button" class="secondary">Back</a>
        </div>
    </div>
    '''
    return HTMLResponse(layout("Step 6: Enter Topic", content_html))

# ========== PROCESS ==========
@app.post("/process")
async def process_hook(
    platform: str = Form(...),
    type: str = Form(...),
    content: str = Form(...),
    audience: str = Form(...),
    tone: str = Form(...),
    topic: str = Form(...)
):
    # Show loading page
    loading_content = f'''
    <div style="max-width: 800px; margin: 0 auto; text-align: center; padding: 4rem 0;">
        <div style="font-size: 4rem; color: var(--primary); margin-bottom: 2rem;">
            <i class="fas fa-fish-hook"></i>
        </div>
        
        <h1 style="color: var(--primary);">Crafting Your Hooks...</h1>
        <p style="font-size: 1.2rem; color: #6b7280; max-width: 500px; margin: 1rem auto;">
            Creating {type} hooks for {platform} targeting {audience}...
        </p>
        
        <div class="loading-bar">
            <div class="loading-progress"></div>
        </div>
        
        <p style="color: #6b7280; margin-top: 2rem;">
            Generating 3 viral hook options...
        </p>
        
        <!-- Auto-refresh to result after 3 seconds -->
        <meta http-equiv="refresh" content="3;url=/result?platform={platform}&type={type}&content={content}&audience={audience}&tone={tone}&topic={topic}">
    </div>
    '''
    
    return HTMLResponse(layout("Creating Hooks...", loading_content))

def parse_hooks_from_response(ai_response: str) -> list:
    """Parse AI response into structured hook data"""
    hooks = []
    
    # Clean the response
    ai_response = ai_response.strip()
    
    # Split by hook sections (looks for "### **Hook Option X**" or similar)
    import re
    
    # Try multiple patterns
    patterns = [
        r'### \*\*Hook Option \d+\*\*',  # ### **Hook Option 1**
        r'\d+\.\s*\*\*Hook Text\*\*',    # 1. **Hook Text**
        r'Hook Option \d+:',             # Hook Option 1:
    ]
    
    for pattern in patterns:
        sections = re.split(pattern, ai_response, flags=re.IGNORECASE)
        if len(sections) > 1:  # Found matches
            # Skip first part (might be intro text)
            for section in sections[1:4]:  # Take first 3 hooks
                hook = parse_single_hook(section)
                if hook:
                    hooks.append(hook)
            break
    
    # If still no hooks, try a simpler approach
    if not hooks:
        hooks = parse_fallback_hooks(ai_response)
    
    return hooks

def parse_single_hook(section: str) -> dict:
    """Parse a single hook section"""
    import re
    hook = {}
    
    # Clean up the section
    section = section.strip()
    
    # Extract hook text - more specific pattern
    # Look for "Hook Text:" followed by content (might be on next line)
    text_patterns = [
        r'\*\*Hook Text\*\*[:\s]*\n?\s*(.+?)(?=\n\s*\*\*Why It Works\*\*|\n\s*\*\*Visual|\Z)',
        r'Hook Text[:\s]*\n?\s*(.+?)(?=\n\s*Why It Works|\n\s*Visual|\Z)',
        r'1\.\s*\*\*Hook Text\*\*[:\s]*\n?\s*(.+?)(?=\n\s*2\.|\n\s*\*\*Why|$)'
    ]
    
    for pattern in text_patterns:
        text_match = re.search(pattern, section, re.DOTALL | re.IGNORECASE)
        if text_match:
            # Clean up the text - remove extra quotes, trim
            text = text_match.group(1).strip()
            # Remove surrounding quotes if present
            if text.startswith('"') and text.endswith('"'):
                text = text[1:-1]
            elif text.startswith("'") and text.endswith("'"):
                text = text[1:-1]
            hook['text'] = text.strip()
            break
    
    # If we still don't have text, take first non-empty line
    if 'text' not in hook:
        lines = [line.strip() for line in section.split('\n') if line.strip()]
        if lines:
            # Skip lines that look like headers
            for line in lines:
                if not re.match(r'^\*\*.*\*\*$', line) and not re.match(r'^\d+\.', line):
                    hook['text'] = line.strip('"\'')
                    break
    
    # Extract psychology
    psych_patterns = [
        r'\*\*Why It Works\*\*[:\s]*\n?\s*(.+?)(?=\n\s*\*\*Visual/Execution Tip\*\*|\n\s*\*\*Visual Tip\*\*|\n\s*---|\Z)',
        r'Why It Works[:\s]*\n?\s*(.+?)(?=\n\s*Visual/Execution Tip|\n\s*Visual Tip|\n\s*---|\Z)',
        r'2\.\s*\*\*Why It Works\*\*[:\s]*\n?\s*(.+?)(?=\n\s*3\.|\n\s*\*\*Visual|$)'
    ]
    
    for pattern in psych_patterns:
        psych_match = re.search(pattern, section, re.DOTALL | re.IGNORECASE)
        if psych_match:
            hook['psychology'] = psych_match.group(1).strip()
            break
    
    # Extract visual tip
    visual_patterns = [
        r'\*\*Visual/Execution Tip\*\*[:\s]*\n?\s*(.+?)(?=\n\s*---|\n\s*###|\Z)',
        r'\*\*Visual Tip\*\*[:\s]*\n?\s*(.+?)(?=\n\s*---|\n\s*###|\Z)',
        r'Visual/Execution Tip[:\s]*\n?\s*(.+?)(?=\n\s*---|\n\s*###|\Z)',
        r'3\.\s*\*\*Visual/Execution Tip\*\*[:\s]*\n?\s*(.+?)(?=\n\s*---|\n\s*###|\Z)'
    ]
    
    for pattern in visual_patterns:
        visual_match = re.search(pattern, section, re.DOTALL | re.IGNORECASE)
        if visual_match:
            hook['visual'] = visual_match.group(1).strip()
            break
    
    return hook if hook else None

def parse_fallback_hooks(ai_response: str) -> list:
    """Fallback parsing if regex fails"""
    hooks = []
    lines = ai_response.split('\n')
    
    current_hook = {}
    current_section = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if 'hook text' in line.lower() or line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
            if current_hook and 'text' in current_hook:
                hooks.append(current_hook)
            current_hook = {'text': line.replace('**Hook Text**:', '').replace('**Hook Text**:', '').strip().strip('"')}
        elif 'why it works' in line.lower():
            current_hook['psychology'] = line.replace('**Why It Works**:', '').replace('**Why It Works**:', '').strip()
        elif 'visual' in line.lower():
            current_hook['visual'] = line.replace('**Visual/Execution Tip**:', '').replace('**Visual Tip**:', '').strip()
    
    # Don't forget the last hook
    if current_hook and 'text' in current_hook:
        hooks.append(current_hook)
    
    # Ensure we have 3 hooks
    while len(hooks) < 3:
        hooks.append({
            'text': f'Hook {len(hooks)+1}: Engaging hook about your topic',
            'psychology': 'Creates curiosity and engagement',
            'visual': 'Use text overlay and engaging visuals'
        })
    
    return hooks[:3]  # Return max 3 hooks

def get_hook_type_guidelines(hook_type: str) -> str:
    guidelines = {
        "question": "• Must make viewer answer internally\n• Should be personally relevant\n• Creates immediate engagement\n• Leads naturally to content",
        "shocking": "• Stat/fact must be genuinely surprising\n• Should challenge assumptions\n• Source credibility helps\n• Visual representation powerful",
        "story": "• Personal/relatable anecdote\n• Should have emotional hook\n• Quick setup (2-3 sentences)\n• Clear connection to topic",
        "controversy": "• Bold stance or unpopular opinion\n• Should be defendable\n• Creates discussion/engagement\n• Know your audience limits",
        "howto": "• Clear benefit promised\n• Should seem achievable\n• Specific, not vague\n• Results-oriented language",
        "fear": "• Pain point identification\n• Solution promised\n• Should be legitimate concern\n• Empowering, not paralyzing"
    }
    return guidelines.get(hook_type, "• Grab attention\n• Create curiosity\n• Promise value\n• Lead to content")

def get_topic_guidance(topic: str) -> str:
    topic_lower = topic.lower()
    if any(word in topic_lower for word in ["ai", "artificial", "generated", "machine learning"]):
        return "• Focus on technology, futurism, ethics\n• Highlight uncanny valley, implications\n• Use tech-savvy but accessible language"
    elif any(word in topic_lower for word in ["review", "product", "service", "app"]):
        return "• Focus on value, features, pros/cons\n• Highlight pain points and solutions\n• Use authentic, experience-based language"
    elif any(word in topic_lower for word in ["tutorial", "how to", "guide", "learn"]):
        return "• Focus on transformation, results\n• Highlight before/after, ease of learning\n• Use empowering, step-by-step language"
    elif any(word in topic_lower for word in ["vlog", "personal", "story", "day in life"]):
        return "• Focus on authenticity, connection\n• Highlight relatable moments, emotions\n• Use conversational, intimate language"
    else:
       return "• Tailor hooks specifically to this topic\n• Use topic-relevant language and examples\n• Make hooks feel custom, not generic"


# ========== RESULT ==========  <-- This comes AFTER the helper functions
@app.get("/result")
async def show_result(
    platform: str = Query(...),
    type: str = Query(...),
    content: str = Query(...),
    audience: str = Query(...),
    tone: str = Query(...),
    topic: str = Query(...)
):
    # TEST MODE - Set to False for real API
    TEST_MODE = True
    
    try:
        if TEST_MODE:
            # Clean mock data with PROPER formatting
            ai_text = f'''HOOK 1 TEXT: "I found a website where two AIs battle to create fake people. The results are terrifyingly real."
WHY IT WORKS: Combines AI intrigue with uncanny valley fascination. The "battle" metaphor makes it dramatic.
VISUAL TIP: Split screen showing AI "painter" vs AI "detective" with facial close-ups.

HOOK 2 TEXT: "What if every face you see online was fake? This website proves it's possible."
WHY IT WORKS: Philosophical question about reality vs AI. Creates immediate "what if" curiosity.
VISUAL TIP: Rapid montage of AI faces with "FAKE" watermark appearing.

HOOK 3 TEXT: "The AI arms race to create perfect humans is happening now. I tested the frontlines."
WHY IT WORKS: "Arms race" framing adds urgency. Positional authority as tester.
VISUAL TIP: War room aesthetic with maps and "AI vs AI" battlefield graphic.'''
        else:
            # BETTER PROMPT for real API
            hook_prompt = f"""Create 3 viral YouTube hooks about this topic: {topic}

IMPORTANT: Do NOT repeat the topic description. Create ORIGINAL, ENGAGING hooks.

For each hook, provide ONLY:
1. HOOK TEXT: [The exact hook wording in quotes]
2. WHY IT WORKS: [Brief psychology explanation]
3. VISUAL TIP: [How to execute visually]

Make hooks URGENT, CURIOUS, and STOPPING.

Topic context: {topic}"""
            
            response = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers={
                    "Authorization": f"Bearer {DEEPSEEK_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": "You are a viral YouTube hook expert. Create ORIGINAL hooks, do not repeat the input."},
                        {"role": "user", "content": hook_prompt}
                    ],
                    "stream": False,
                    "temperature": 0.8  # More creative
                },
                timeout=30
            )
            
            if response.status_code != 200:
                raise Exception(f"API Error {response.status_code}")
            
            ai_text = response.json()["choices"][0]["message"]["content"]
        
        # SIMPLE PARSER
        hooks = []
        current_hook = {}
        
        for line in ai_text.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            line_lower = line.lower()
            
            if 'hook' in line_lower and 'text' in line_lower:
                if current_hook and current_hook.get('text'):
                    hooks.append(current_hook)
                # Extract text
                text = line.split(':', 1)[1].strip() if ':' in line else line
                text = text.strip('"')
                current_hook = {'text': text}
            elif 'why it works' in line_lower and 'psychology' not in current_hook:
                current_hook['psychology'] = line.split(':', 1)[1].strip() if ':' in line else line
            elif 'visual tip' in line_lower and 'visual' not in current_hook:
                current_hook['visual'] = line.split(':', 1)[1].strip() if ':' in line else line
        
        if current_hook and current_hook.get('text'):
            hooks.append(current_hook)
        
        # Fallback if parsing fails
        if not hooks:
            hooks = [
                {'text': 'The AI face generator that\'s too realistic to be comfortable', 'psychology': 'Uncanny valley fascination', 'visual': 'Close-up face montage'},
                {'text': 'Two AIs in an endless battle to create and detect fake humans', 'psychology': 'Dramatic conflict narrative', 'visual': 'Split screen battle animation'},
                {'text': 'What if every person you see online was AI-generated?', 'psychology': 'Reality-questioning curiosity', 'visual': 'Reality vs AI comparison'}
            ]
        
        hooks = hooks[:3]
        
        # YOUR TURQUOISE COLOR: #0d96c1
        TURQUOISE = "#0d96c1"
        TURQUOISE_LIGHT = "#ecfeff"
        TURQUOISE_DARK = "#0c4a6e"
        
        # Build hook cards with YOUR turquoise theme
        hooks_html = ""
        for i, hook in enumerate(hooks):
            hooks_html += f'''
<div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 2rem 0; border: 2px solid {TURQUOISE}; box-shadow: 0 4px 12px rgba(13, 150, 193, 0.1);">
    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
        <div style="background: {TURQUOISE}; color: white; width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">
            {i+1}
        </div>
        <h3 style="margin: 0; color: {TURQUOISE};">Hook {i+1}</h3>
    </div>
    
    <!-- MAIN HOOK TEXT -->
    <div style="margin-bottom: 1.5rem;">
        <div style="font-size: 0.9rem; color: {TURQUOISE}; margin-bottom: 0.5rem; font-weight: 600;">
            <i class="fas fa-quote-left"></i> HOOK TEXT
        </div>
        <div style="font-size: 1.2rem; line-height: 1.5; padding: 1.5rem; background: {TURQUOISE_LIGHT}; border-radius: 8px; border-left: 4px solid {TURQUOISE}; color: {TURQUOISE_DARK}; font-family: 'Georgia', serif;">
            "{hook.get('text', 'No hook text available')}"
        </div>
    </div>
    
    <!-- Tips -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
        <div style="padding: 0.75rem; border-radius: 6px; background: {TURQUOISE_LIGHT}; border: 1px solid #a5f3fc;">
            <div style="font-size: 0.8rem; color: {TURQUOISE}; margin-bottom: 0.25rem; font-weight: 600;">
                <i class="fas fa-brain"></i> Why It Works
            </div>
            <div style="font-size: 0.9rem; color: {TURQUOISE_DARK};">
                {hook.get('psychology', 'Creates engagement')}
            </div>
        </div>
        
        <div style="padding: 0.75rem; border-radius: 6px; background: {TURQUOISE_LIGHT}; border: 1px solid #a5f3fc;">
            <div style="font-size: 0.8rem; color: {TURQUOISE}; margin-bottom: 0.25rem; font-weight: 600;">
                <i class="fas fa-video"></i> Visual Tip
            </div>
            <div style="font-size: 0.9rem; color: {TURQUOISE_DARK};">
                {hook.get('visual', 'Use engaging visuals')}
            </div>
        </div>
    </div>
</div>
'''
        
        result_content = f'''
<div style="max-width: 800px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 3rem; color: {TURQUOISE};">
            <i class="fas fa-fish-hook"></i>
        </div>
        <h1 style="color: {TURQUOISE};">Hook Options Ready!</h1>
        <p style="color: #64748b;">For <strong>{platform.title()}</strong> • <strong>{type.title()}</strong> • <strong>{audience.title()}</strong></p>
        <div style="background: {TURQUOISE_LIGHT}; padding: 0.75rem; border-radius: 8px; margin-top: 1rem; border: 1px solid #a5f3fc;">
            <p style="color: {TURQUOISE_DARK}; margin: 0;"><i class="fas fa-bullseye"></i> <strong>Topic:</strong> {topic[:100]}{'...' if len(topic) > 100 else ''}</p>
        </div>
    </div>
    
    {hooks_html}
    
    <div style="text-align: center; margin-top: 3rem;">
        <a href="/wizard" role="button" style="margin-right: 1rem; background: {TURQUOISE}; border-color: {TURQUOISE};">
            <i class="fas fa-fish-hook"></i> Create More Hooks
        </a>
        <a href="/" role="button" style="background: #64748b; border-color: #64748b;">
            <i class="fas fa-home"></i> Dashboard
        </a>
    </div>
</div>
'''
        
    except Exception as e:
        result_content = f'''
<div style="max-width: 800px; margin: 0 auto; text-align: center;">
    <h1 style="color: #dc2626;"><i class="fas fa-exclamation-triangle"></i> Error</h1>
    <p>{str(e)}</p>
    <a href="/" role="button" style="margin-top: 2rem; background: {TURQUOISE}; border-color: {TURQUOISE};">Start Over</a>
</div>
'''
    
    return HTMLResponse(layout("Hook Options", result_content))

# ========== HELPER FUNCTIONS ==========
# PUT THESE RIGHT HERE, AFTER /process BUT BEFORE /result

def get_platform_requirements(platform: str) -> str:
    requirements = {
        "tiktok": "• MUST grab attention in FIRST 1-2 seconds\n• Use trending sounds/text-on-screen\n• Fast cuts, high energy\n• Clear value proposition immediately",
        "youtube": "• Beat the 5-second skip\n• State value within 10 seconds\n• Use curiosity gap\n• Preview what's coming",
        "instagram": "• Visual-first hooks\n• Text overlay crucial\n• Reels format (9:16)\n• Quick setup, fast payoff",
        "linkedin": "• Professional/value-first\n• Problem/solution framing\n• Credibility indicators\n• Clear target audience",
        "twitter": "• Thread starter hooks\n• Controversy/curiosity\n• Short, punchy\n• Retweetable",
        "facebook": "• Storytelling hooks\n• Emotional connection\n• Shareable content\n• Community-focused"
    }
    return requirements.get(platform, "• Grab attention immediately\n• Clear value proposition\n• Platform-appropriate tone")

def get_hook_type_guidelines(hook_type: str) -> str:
    guidelines = {
        "question": "• Must make viewer answer internally\n• Should be personally relevant\n• Creates immediate engagement\n• Leads naturally to content",
        "shocking": "• Stat/fact must be genuinely surprising\n• Should challenge assumptions\n• Source credibility helps\n• Visual representation powerful",
        "story": "• Personal/relatable anecdote\n• Should have emotional hook\n• Quick setup (2-3 sentences)\n• Clear connection to topic",
        "controversy": "• Bold stance or unpopular opinion\n• Should be defendable\n• Creates discussion/engagement\n• Know your audience limits",
        "howto": "• Clear benefit promised\n• Should seem achievable\n• Specific, not vague\n• Results-oriented language",
        "fear": "• Pain point identification\n• Solution promised\n• Should be legitimate concern\n• Empowering, not paralyzing"
    }
    return guidelines.get(hook_type, "• Grab attention\n• Create curiosity\n• Promise value\n• Lead to content")

def get_topic_guidance(topic: str) -> str:
    topic_lower = topic.lower()
    if any(word in topic_lower for word in ["ai", "artificial", "generated", "machine learning"]):
        return "• Focus on technology, futurism, ethics\n• Highlight uncanny valley, implications\n• Use tech-savvy but accessible language"
    elif any(word in topic_lower for word in ["review", "product", "service", "app"]):
        return "• Focus on value, features, pros/cons\n• Highlight pain points and solutions\n• Use authentic, experience-based language"
    elif any(word in topic_lower for word in ["tutorial", "how to", "guide", "learn"]):
        return "• Focus on transformation, results\n• Highlight before/after, ease of learning\n• Use empowering, step-by-step language"
    elif any(word in topic_lower for word in ["vlog", "personal", "story", "day in life"]):
        return "• Focus on authenticity, connection\n• Highlight relatable moments, emotions\n• Use conversational, intimate language"
    else:
        return "• Tailor hooks specifically to this topic\n• Use topic-relevant language and examples\n• Make hooks feel custom, not generic"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)

          
           
            
           
           
            



     
 
