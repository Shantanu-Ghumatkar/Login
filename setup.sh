mkdir -p ~/.streamLit/

echo "\
[server]\n\
Scratches and Consoles
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\

" > ~/.streamlit/config.toml

web: sh setup.sh && streamlit run app.py