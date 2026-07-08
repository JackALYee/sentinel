# Sentinel — Marketing Site (Streamlit Community Cloud)

Self-contained marketing page for the Streamax **Sentinel** 24/7 AOV camera,
hosted for free on Streamlit Community Cloud.

## How it works
- The entire site (`Sentinel-Marketing.html` + images, video, 3D model, and the
  downloadable spec/manual/install docs) lives under **`static/`**.
- Streamlit serves that folder as static files (`enableStaticServing = true`).
- `streamlit_app.py` redirects the app's root URL to the served page, so
  visitors land directly on the full-screen site.

## Deploy
1. Push this repo to GitHub (branch `main`).
2. Go to https://share.streamlit.io → **Create app** → **Deploy from GitHub**.
3. Repository: `JackALYee/sentinel` · Branch: `main` · Main file: `streamlit_app.py`
4. Click **Deploy**.

Your site will be live at `https://<app-name>.streamlit.app`.
You can also link people straight to `https://<app-name>.streamlit.app/app/static/Sentinel-Marketing.html`.

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
