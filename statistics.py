import statistics


def veri_analizi(veriler):
    # Aritmetik Ortalama
    ortalama = statistics.mean(veriler)

    # Medyan
    medyan = statistics.median(veriler)

    # Mod (Eğer birden fazla mod varsa, hepsini döndürür)
    try:
        mod = statistics.mode(veriler)
    except statistics.StatisticsError:
        mod = "Veri setinde mod bulunamadı (benzersiz bir mod yok)."

    return ortalama, medyan, mod


# Kullanıcıdan veri girişi alalım
veriler = input("Lütfen verileri boşlukla ayırarak girin (örneğin: 1 2 3 4 5): ")
veriler = list(map(float, veriler.split()))  # Girdiyi float listesine dönüştür

# Veri analizini yapalım
ortalama, medyan, mod = veri_analizi(veriler)

# Sonuçları ekrana yazdıralım
print(f"Aritmetik Ortalama: {ortalama}")
print(f"Medyan: {medyan}")
print(f"Mod: {mod}")
