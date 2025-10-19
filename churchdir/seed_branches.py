from core.models import Branch, User

BRANCHES = [
    "Mangere","Manurewa","Onehunga","Grey Lynn","Mt Albert","Mt Wellington",
    "Tauranga","North Shore","Hamilton","Massey","Glen Innes","Oranga",
    "East Tamaki","Pukekohe","Katikati","Rotorua","Manukau","Petani",
    "Dargaville","Papakura","Tuakau","Te Aroha","Buckland","Waihi",
    "Opotiki","Paengaroa"
]

def run():
    for name in BRANCHES:
        Branch.objects.get_or_create(name=name)
    print(f"Seeded {len(BRANCHES)} branches.")

if __name__ == "__main__":
    # Usage: python manage.py shell < seed_branches.py   (or django-extensions runscript)
    pass
