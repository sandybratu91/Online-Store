import pandas as pd

file_name = 'online_store_data.csv'

# --- Încărcarea datelor ---
try:
    # 1. Încărcarea setului de date în DataFrame
    df = pd.read_csv(file_name)
    print("--- Analiză inițială a datelor magazinului online ---")
    print(f"Setul de date '{file_name}' a fost încărcat cu succes.")
    print("-" * 50)

    # ----------------------------------------------------------------------
    ## 1. Câte produse există în setul de date?
    
    total_products = df.shape[0]
    print(f"1. Numărul total de produse în setul de date este: **{total_products}**")
    print("-" * 50)

    # ----------------------------------------------------------------------
    ## 2. Care este cel mai bine vândut produs din întregul magazin online?
    

    most_sold_product_df = df.sort_values(by='quantity_sold', ascending=False)
    
    # Selectăm primul rând.
    top_product = most_sold_product_df.iloc[0]

    print("2. Cel mai bine vândut produs din întregul magazin online este:")
    print(f"   **Produs**: {top_product['product_name']}")
    print(f"   **Categorie**: {top_product['category']}")
    print(f"   **Unități Vândute**: {int(top_product['quantity_sold'])}")
    print("-" * 50)

    ## 3. Care sunt cele mai bine vândute 5 telefoane mobile?
    
    # a) Filtrare: Selectăm doar produsele din categoria "Smartphones"
    smartphones_df = df[df['category'] == 'Smartphones']
    
    # b) Sortare: Sortăm produsele filtrate după 'sold_quantity' (descrescător)
    top_smartphones_df = smartphones_df.sort_values(by='quantity_sold', ascending=False)
    
    # c) Selectare: Selectăm primele 5 rânduri
    top_5_smartphones = top_smartphones_df.head(5)

    print("3. Top 5 cele mai bine vândute telefoane mobile (Smartphones):")
    # Afișăm coloanele 'product_name' și 'quantity_sold'
    print(top_5_smartphones[['product_name', 'quantity_sold']])
    print("-" * 50)

    ## 4. Care este prețul celui mai scump și al celui mai ieftin laptop?
    
    # a) Filtrare: Selectăm doar produsele din categoria "Laptops"
    laptops_df = df[df['category'] == 'Laptops'].copy()
    
    # b) Curățare: Eliminăm rândurile unde 'price' este lipsă (NaN) și unde prețul este zero sau negativ
    # Metoda dropna pe coloana 'price' și filtrare pentru a ne asigura că prețul este pozitiv.
    laptops_cleaned_df = laptops_df.dropna(subset=['price'])
    laptops_cleaned_df = laptops_cleaned_df[laptops_cleaned_df['price'] > 0]

    if laptops_cleaned_df.empty:
        print("4. Nu s-au găsit laptopuri cu prețuri valide după filtrare.")
    else:
        # c) Găsirea prețului maxim și minim
        max_price = laptops_cleaned_df['price'].max()
        min_price = laptops_cleaned_df['price'].min()

        # Identificăm produsele pentru afișare
        most_expensive_laptop = laptops_cleaned_df[laptops_cleaned_df['price'] == max_price].iloc[0]
        cheapest_laptop = laptops_cleaned_df[laptops_cleaned_df['price'] == min_price].iloc[0]

        print("4. Prețurile celui mai scump și celui mai ieftin laptop:")
        print(f"   - Cel mai scump laptop (Produs: {most_expensive_laptop['product_name']}): **${max_price:.2f}**")
        print(f"   - Cel mai ieftin laptop (Produs: {cheapest_laptop['product_name']}): **${min_price:.2f}**")
    
    print("-" * 50)

except FileNotFoundError:
    print(f"Eroare: Fișierul '{file_name}' nu a fost găsit. Asigură-te că fișierul este în același director cu scriptul Python.")
except KeyError as e:
    print(f"Eroare: Coloana {e} lipsește din setul de date. Verifică numele coloanelor.")
except Exception as e:
    print(f"A apărut o eroare neașteptată: {e}")