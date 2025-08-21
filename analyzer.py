# analyzer.py
import pandas as pd

def get_all_movies_html():
    try:
        df = pd.read_csv('data/movies.csv')
        # Sortiraj filmove po ocjeni, silazno
        df_sorted = df.sort_values(by='Rating', ascending=False)

        html = "<ul>\n"
        for index, row in df_sorted.iterrows():
            html += f"  <li>{row['Title']} (Žanr: {row['Genre']}) - Ocjena: {row['Rating']}</li>\n"
        html += "</ul>"
        return html
    except FileNotFoundError:
        return "<p>Greška: data/movies.csv nije pronađena!</p>"

if __name__ == '__main__':
    print(get_all_movies_html())