import os
import importlib
from supabase import create_client, Client
from dotenv import load_dotenv

Flask = importlib.import_module("flask").Flask

load_dotenv()

app = Flask(__name__)

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_PUBLISHABLE_KEY")
)

@app.route('/')
def index():
    response = supabase.table('instruments').select("*").execute()
    instruments = response.data

    html = '<h1>Instruments</h1><ul>'
    for instrument in instruments:
        html += f'<li>{instrument["name"]}</li>'
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run(debug=True)