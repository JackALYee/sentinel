"""
Sentinel marketing site — Streamlit Community Cloud wrapper.

The full self-contained marketing page (and all of its assets) lives under
./static/ and is served by Streamlit's static file server at
    <app-url>/app/static/Sentinel-Marketing.html
This tiny app just redirects the root URL there so visitors land straight on
the full-bleed site with no Streamlit chrome.
"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sentinel — The 24/7 Camera That Never Sleeps",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's default chrome and padding so the redirect screen is clean.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stHeader"] {display:none !important;}
      [data-testid="stAppViewContainer"], [data-testid="stMain"] {background:#050810 !important;}
      .block-container {padding:0 !important; max-width:100% !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

STATIC_PAGE = "app/static/Sentinel-Marketing.html"

# components.html renders via a same-origin srcdoc iframe, so it can read the
# top window's origin and navigate it to the statically-served marketing page.
components.html(
    f"""
    <!doctype html><html><head><meta charset="utf-8"><style>
      html,body{{margin:0;height:100%;background:#050810;color:#8A99A8;
        font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
        display:flex;align-items:center;justify-content:center;text-align:center;}}
      .dot{{width:12px;height:12px;border-radius:50%;margin:0 auto 14px;
        background:linear-gradient(135deg,#2AF598,#009EFD);box-shadow:0 0 14px #2AF598;
        animation:p 1.4s ease-in-out infinite;}}
      @keyframes p{{0%,100%{{opacity:1}}50%{{opacity:.3}}}}
      a{{color:#2AF598;font-weight:600;}}
    </style></head><body>
      <div>
        <div class="dot"></div>
        <div style="font-size:13px;letter-spacing:.25em">LOADING SENTINEL…</div>
        <div style="margin-top:12px;font-size:13px">
          Not redirected? <a id="lnk" href="{STATIC_PAGE}">Open the site&nbsp;&rarr;</a>
        </div>
      </div>
      <script>
        (function(){{
          var origin;
          try {{ origin = window.top.location.origin; }} catch(e) {{ origin = window.location.origin; }}
          var url = origin.replace(/\\/$/, "") + "/{STATIC_PAGE}";
          var lnk = document.getElementById('lnk'); if (lnk) lnk.href = url;
          try {{ window.top.location.replace(url); }} catch(e) {{ window.location.replace(url); }}
        }})();
      </script>
    </body></html>
    """,
    height=260,
)
