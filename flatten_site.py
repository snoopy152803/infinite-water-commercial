import os

# 1. Configuration Map of our Flat HTML Pages
nav_menu = """    <!-- Shared Header Navigation -->
    <header>
        <div class="logo">AethelFlow</div>
        <nav>
            <a href="/">Home</a>
            <a href="/features">Features</a>
            <a href="/pricing">Pricing</a>
            <a href="/testimonials">Reviews</a>
            <a href="/about">Our Alchemists</a>
        </nav>
    </header>"""

footer_menu = """    <!-- Final Clean Legal Footer -->
    <footer style="text-align: center; padding: 45px 20px; color: #4b5563; border-top: 1px solid #1f2937; font-size: 0.85rem; background-color: #0b0f19;">
        <p style="margin-bottom: 10px;">&copy; 2026 AethelFlow Inc. All Rights Reserved.</p>
        <div class="footer-legal-links">
            <a href="/terms" class="legal-link">Terms of Sorcery</a> | 
            <a href="/privacy" class="legal-link">Privacy Policy</a>
        </div>
    </footer>"""

html_pages = {
    "index.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AethelFlow | Infinite Hydration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
{nav_menu}
    <section class="hero">
        <div class="hero-content">
            <h1>The Last Drop You Will Ever Need.</h1>
            <p>Say goodbye to drought, plumbing, and logic. AethelFlow is a hand-carved obsidian chalice that manifests pure, ice-cold glacial water out of the ethereal plane. Constantly.</p>
            <div class="hero-buttons">
                <a href="/pricing" class="btn-primary">Claim Yours</a>
                <a href="/features" class="btn-secondary">Explore The Lore</a>
            </div>
        </div>
    </section>

    <section class="video-section">
        <h2>Leaked Laptop Footage</h2>
        <p class="subtitle">A customer tried unboxing the chalice next to their computer. Things got out of hand.</p>
        <div class="video-container">
            <video controls><source src="your-commercial.mp4" type="video/mp4"></video>
        </div>
    </section>

    <section class="faq-section">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-container">
            <div class="faq-item">
                <button class="faq-question">Will the infinite water flood my house?</button>
                <div class="faq-answer"><p>Only if you misplace it! The chalice is enchanted with spill-proof containment runes.</p></div>
            </div>
            <div class="faq-item">
                <button class="faq-question">Does this water require an incantation?</button>
                <div class="faq-answer"><p>No mana required. The cosmic link is permanently anchored during the forging process.</p></div>
            </div>
        </div>
    </section>
{footer_menu}
    <script>
        document.querySelectorAll('.faq-question').forEach(q => {{
            q.addEventListener('click', () => q.parentElement.classList.toggle('active'));
        }});
    </script>
</body>
</html>""",

    "features.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Features</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container">
        <h1>Magical Architecture</h1>
        <div class="features">
            <div class="feature-card"><h3>🌀 Infinite Supply</h3><p>Renders up to 5 litres per minute indefinitely.</p></div>
            <div class="feature-card"><h3>✨ Magic-Filtered</h3><p>Sourced straight from the pristine Elemental Plane.</p></div>
        </div>
    </section>
{footer_menu}
</body>
</html>""",

    "pricing.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Pricing</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container">
        <h1>Choose Your Vessel</h1>
        <div class="features">
            <div class="feature-card"><h3>Apprentice Flask</h3><p class="price-tag">150 Gold Pieces</p><button class="btn-primary">Order Flask</button></div>
            <div class="feature-card"><h3>Archmage Chalice</h3><p class="price-tag">450 Gold Pieces</p><button class="btn-primary">Order Chalice</button></div>
        </div>
    </section>
{footer_menu}
</body>
</html>""",

    "testimonials.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Reviews</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container">
        <h1>Endorsed Across Realms</h1>
        <div class="features">
            <div class="feature-card"><p>"I haven't paid a copper coin to the local water grid since the Second Age."</p><h3>— Elrond M.</h3></div>
        </div>
    </section>
{footer_menu}
</body>
</html>""",

    "about.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | About Us</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container" style="max-width: 800px; margin: 0 auto;">
        <h1>Our Alchemical Mission</h1>
        <p>We construct micro-bridges across time and space to tap into high-pressure elemental zones.</p>
    </section>
{footer_menu}
</body>
</html>""",

    "privacy.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Privacy Policy</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container" style="max-width: 800px; margin: 0 auto; text-align: left;">
        <h1>Privacy Policy</h1>
        <h3>1. Information We Collect</h3>
        <p>We collect basic mortal data required to ship your physical vessel. We do not harvest your personal aura.</p>
    </section>
{footer_menu}
</body>
</html>""",

    "terms.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Terms of Sorcery</title>
</head>
<body>
{nav_menu}
    <section class="sub-page-container" style="max-width: 800px; margin: 0 auto; text-align: left;">
        <h1>Terms of Sorcery</h1>
        <h3>1. License to Hydrate</h3>
        <p>Users strictly agree NOT to attempt to modify the internal wormhole geometry to draw liquid magma.</p>
    </section>
{footer_menu}
</body>
</html>""",

    "404.html": f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>AethelFlow | Spatial Tear</title>
</head>
<body>
{nav_menu}
    <div style="text-align:center; padding: 150px 20px;">
        <h1 style="font-size: 5rem; color: #ff3366;">ERROR 404</h1>
        <h2>Runic Pathway Broken</h2>
        <p style="margin: 20px 0 40px; color:#9ca3af;">The portal collapsed. Other known server anomalies include 301 (Permanent Redirection) and 500 (Alchemical Meltdown).</p>
        <a href="/" class="btn-primary">Return Home</a>
    </div>
{footer_menu}
</body>
</html>"""
}

# 2. Cleanup Legacy Runic Folders
legacy_dirs = ["features", "pricing", "testimonials", "about", "privacy", "terms"]
for folder in legacy_dirs:
    if os.path.exists(folder):
        nested_file = os.path.join(folder, "index.html")
        if os.path.exists(nested_file):
            os.remove(nested_file)
        try:
            os.rmdir(folder)
            print(f"🗑️ Cleaned out directory: /{folder}")
        except:
            pass

# 3. Write Flat HTML Files
for filename, content in html_pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"📄 Created: {filename}")

# 4. Generate vercel.json Route Config
with open("vercel.json", "w", encoding="utf-8") as f:
    f.write('{\n  "cleanUrls": true\n}')
print("⚙️ Created vercel.json routing rule configuration.")

print("\n✨ Success! Your website files are fully flattened. Everything is now managed from one main directory.")
