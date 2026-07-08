"""
Sentinel marketing site — Streamlit Community Cloud wrapper.

The full self-contained marketing page + assets live under ./static/ and are
served by Streamlit's static file server at:

    <app-url>/app/static/Sentinel-Marketing.html

IMPORTANT: the app must be set to PUBLIC in the Streamlit dashboard
("Anyone with the link can view"), otherwise every URL — including the static
files — redirects to a login page.

This app renders a branded splash *inside the embedded frame* (so Streamlit's
own click router can't swallow the link). The Enter button uses an absolute URL
with target="_top", and the tab also auto-redirects best-effort.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sentinel — The 24/7 Camera That Never Sleeps",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all Streamlit chrome and padding; dark full-bleed background.
st.markdown(
    """
    <style>
      #MainMenu, header, footer,
      [data-testid="stToolbar"], [data-testid="stHeader"], [data-testid="stDecoration"] {display:none !important;}
      [data-testid="stAppViewContainer"], [data-testid="stMain"], .stApp {background:#050810 !important;}
      .block-container, [data-testid="stMainBlockContainer"] {padding:0 !important; max-width:100% !important;}
      iframe {display:block; border:0;}
    </style>
    """,
    unsafe_allow_html=True,
)

PATH = "/app/static/Sentinel-Marketing.html"  # absolute path on the app's own origin

components.html(
    f"""
    <!doctype html><html><head><meta charset="utf-8"><style>
      html,body{{margin:0;height:100%;background:#050810;color:#96A3B4;
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;}}
      .wrap{{min-height:96vh;display:flex;align-items:center;justify-content:center;text-align:center;}}
      .dot{{width:14px;height:14px;border-radius:50%;margin:0 auto 20px;
        background:linear-gradient(135deg,#2AF598,#009EFD);box-shadow:0 0 16px #2AF598;animation:p 1.4s ease-in-out infinite;}}
      @keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
      .t{{font-size:2.6rem;font-weight:900;letter-spacing:-.02em;
        background:linear-gradient(120deg,#2AF598,#009EFD);-webkit-background-clip:text;background-clip:text;color:transparent;}}
      .s{{margin-top:.6rem;font-size:1.05rem;}}
      a.btn{{display:inline-block;margin-top:2rem;padding:.95rem 2rem;border-radius:100px;font-weight:800;font-size:1rem;
        color:#04140c;text-decoration:none;background:linear-gradient(120deg,#2AF598,#009EFD);
        box-shadow:0 10px 30px rgba(0,158,253,.3);transition:transform .2s;}}
      a.btn:hover{{transform:translateY(-2px);}}
      .h{{margin-top:1.4rem;font-size:.8rem;color:rgba(150,163,180,.5);}}
    </style></head><body>
      <div class="wrap"><div>
        <div class="dot"></div>
        <div class="t">Sentinel</div>
        <div class="s">The 24/7 camera that never sleeps.</div>
        <div><a id="go" class="btn" target="_top" rel="noopener" href="{PATH}">Enter the site &rarr;</a></div>
        <div class="h">Loading… if nothing happens, click the button above.</div>
      </div></div>
      <script>
        (function() {{
          // Build an ABSOLUTE URL to the static page from the parent (app) origin.
          var origin = "";
          try {{ if (document.referrer) origin = new URL(document.referrer).origin; }} catch (e) {{}}
          if (!origin) {{ try {{ origin = window.top.location.origin; }} catch (e) {{}} }}
          var url = origin ? origin + "{PATH}" : "{PATH}";
          var a = document.getElementById("go");
          if (a) a.href = url;                        // click → target=_top → whole tab navigates (reliable)
          try {{ window.top.location.replace(url); }} catch (e) {{}}   // best-effort auto-redirect
        }})();
      </script>
    </body></html>
    """,
    height=560,
)
