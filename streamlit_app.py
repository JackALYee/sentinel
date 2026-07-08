"""
Sentinel marketing site — Streamlit Community Cloud wrapper.

The full self-contained marketing page (and all of its assets) lives under
./static/ and is served by Streamlit's static file server at:

    <app-url>/app/static/Sentinel-Marketing.html

This app renders a small branded landing whose "Enter" button links straight
to that page (a plain relative link in the main page DOM — no cross-origin or
sandbox issues), and also best-effort auto-redirects the whole tab there.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sentinel — The 24/7 Camera That Never Sleeps",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Relative to the app root — resolves to https://<app>/app/static/Sentinel-Marketing.html
PAGE = "app/static/Sentinel-Marketing.html"

# Hide Streamlit chrome + padding, dark full-bleed background, and render the
# landing. The <a> lives in the MAIN document, so its relative href resolves
# against the real app URL and clicking it reliably loads the full-screen site.
st.markdown(
    f"""
    <style>
      #MainMenu, header, footer,
      [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stDecoration"] {{display:none !important;}}
      [data-testid="stAppViewContainer"], [data-testid="stMain"], .stApp {{background:#050810 !important;}}
      .block-container, [data-testid="stMainBlockContainer"] {{padding:0 !important; max-width:100% !important;}}
      .snt-wrap{{min-height:92vh;display:flex;align-items:center;justify-content:center;
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#96A3B4;text-align:center;}}
      .snt-dot{{width:14px;height:14px;border-radius:50%;margin:0 auto 20px;
        background:linear-gradient(135deg,#2AF598,#009EFD);box-shadow:0 0 16px #2AF598;animation:sntp 1.4s ease-in-out infinite;}}
      @keyframes sntp{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
      .snt-title{{font-size:2.6rem;font-weight:900;letter-spacing:-.02em;
        background:linear-gradient(120deg,#2AF598,#009EFD);-webkit-background-clip:text;background-clip:text;color:transparent;}}
      .snt-sub{{margin-top:.6rem;font-size:1.05rem;color:#96A3B4;}}
      .snt-btn{{display:inline-block;margin-top:2rem;padding:.95rem 2rem;border-radius:100px;font-weight:800;font-size:1rem;
        color:#04140c !important;text-decoration:none;background:linear-gradient(120deg,#2AF598,#009EFD);
        box-shadow:0 10px 30px rgba(0,158,253,.3);transition:transform .2s;}}
      .snt-btn:hover{{transform:translateY(-2px);}}
      .snt-hint{{margin-top:1.4rem;font-size:.8rem;color:rgba(150,163,180,.55);}}
    </style>
    <div class="snt-wrap">
      <div>
        <div class="snt-dot"></div>
        <div class="snt-title">Sentinel</div>
        <div class="snt-sub">The 24/7 camera that never sleeps.</div>
        <div><a class="snt-btn" href="{PAGE}" target="_top" rel="noopener">Enter the site &rarr;</a></div>
        <div class="snt-hint">Loading automatically… if it doesn't, use the button above.</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Best-effort auto-redirect of the whole tab. Derives the correct app origin from
# document.referrer (the parent page URL — readable even cross-origin), so it
# never builds a broken URL. If the sandbox blocks top navigation, nothing
# happens and the visible button above still works.
components.html(
    f"""
    <script>
      (function() {{
        try {{
          var base = "";
          if (document.referrer) {{ base = new URL(document.referrer).origin; }}
          if (!base) {{ base = window.top.location.origin; }}
          if (base) {{ window.top.location.replace(base + "/{PAGE}"); }}
        }} catch (e) {{ /* top-nav blocked — the Enter button handles it */ }}
      }})();
    </script>
    """,
    height=0,
)
